# The MIT License (MIT)
#
# Copyright (c) 2013 CFEngine AS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os
import sys
import re
import cfdoc_qa as qa

def run(config):
	markdown_files =  config["markdown_files"]
	readLinkFile(config)
	for file in markdown_files:
		parseMarkdownForAnchors(file, config)

def apply(config):
	qa.LogProcessStart(config, "Applying Link Map")
	markdown_files =  config["markdown_files"]
	for file in markdown_files:
		applyLinkMap(file, config)

def readLinkFile(config):
	output_file = config["reference_path"]
	link_map = config.get("link_map", dict())
	html_map = config.get("html_map", dict())
	
	link_file = open(output_file, 'r')
	link_lines = link_file.readlines()
	for line in link_lines:
		label = line[line.find('[') + 1:line.find(']')]
		html = line[line.find("]: ") + 3:].lstrip()
		html = html[:html.find("\"")].rstrip() # cut off alias
		keyword = label
		if line.find("]: reference-functions-") != -1:
			keyword += "()"
		link_map["`" + keyword + "`"] = ["[" + label + "]"]
		html_map[label] = html
	config["link_map"] = link_map
	config["html_map"] = html_map

def addLinkToMap(keyword, anchor, html, config):
	link_map = config.get("link_map", dict())
	html_map = config.get("html_map", dict())

	autolink = keyword[-1] != "#"
	if not autolink:
		keyword = keyword.rstrip("#").rstrip()
		anchor = anchor.rstrip("#").rstrip()
		html = html.rstrip("#").rstrip()

	html_map[anchor] = html[:html.find(" \"")]
	anchor = "[%s]" % anchor
	anchor_list = link_map.get("`%s`" % keyword, list())
	if anchor in anchor_list:
		return

	if autolink:
		# prioritize titles over sub-headers
		if anchor.find("#") != -1:
			anchor_list.append(anchor)
		else:
			anchor_list.insert(0, anchor)
		
		link_map["`%s`" % keyword] = anchor_list
	
	output_file = config["reference_path"]
	out_file = open(output_file, "a")
	out_file.write("%s: %s\n" % (anchor, html))
	out_file.close()
	
	config["link_map"] = link_map
	config["html_map"] = html_map

def headerToAnchor(header):
	# remove trailing hashes, allowed in markdown and
	# interpreted by us to not include the header in the link map
	anchor = header.lower()
	anchor = anchor.rstrip("#").rstrip()
	anchor = anchor.replace(" ", "-")
	anchor = anchor.replace(":", "-")
	anchor = anchor.replace(".", "-")
	anchor = anchor.replace(",", "-")
	anchor = anchor.replace("`", "-")
	anchor = anchor.replace("/", "-")
	anchor = anchor.replace("$", "-")
	anchor = anchor.replace("(", "-")
	anchor = anchor.replace(")", "-")
	anchor = anchor.replace("\"", "")
	anchor = anchor.replace("--", "-")
	anchor = anchor.lstrip("-").rstrip("-")
	return anchor

def parseMarkdownForAnchors(file_name, config):
	in_file = open(file_name,"r")
	lines = in_file.readlines()
	in_file.close()
	
	current_file_name = ""
	current_file_label = ""
	current_title = ""
	header_list = []
	keywords = []
	
	in_pre = False
	for line in lines:
		# ignore code blocks
		if line.find("    ") == 0:
			continue
		elif line.find("```") == 0 and line.find("```", 3) == -1:
            # line which starts with triple backticks denotes start/end of codeblock,
            # _unless_ it contains triple backticks somewhere else
			in_pre = not in_pre
		if in_pre:
			continue

		if line.find("title:") == 0:
			current_title = line.split('title: ')
			current_title = current_title[1].rstrip().rstrip('\"')
			current_title = current_title.lstrip().lstrip('\"')
		elif line.find("alias:") == 0:
			current_file_name = line.split('alias: ')
			current_file_name = current_file_name[1].rstrip()
		elif line.startswith("published:"):
			published = line[len("published:"):].rstrip().lstrip().lower()
			if published == "false":
				return
		elif line.find("#") == 0:
			current_header = line.lstrip('#').rstrip().lstrip()
			header_list.append(current_header)
		elif line.find("layout:") == 0:
			layout = line.split('layout:')[1].lstrip().rstrip()
			if layout == "printable":
				return
		elif line.find("keywords:") == 0:
			keywords = line.split('keywords: ')[1].rstrip().lstrip('[').rstrip(']')
			keywords = keywords.split(",")

	current_file_label = current_title

	if current_file_label != "" and current_file_name != "":
		for keyword in keywords:
			keyword = keyword.lstrip().rstrip()
			addLinkToMap(keyword, current_file_label, current_file_name + ' \"' + current_title + '\"', config)

		keyword = current_file_label
		# generate auto-link to functions via `function()`
		if current_file_name.find("reference-functions-") == 0:
			keyword += "()"
		addLinkToMap(keyword, current_file_label, current_file_name + ' \"' + current_title + '\"', config)
		for header in header_list:
			if header == "":
				continue
			anchor = headerToAnchor(header)
			label = current_file_label+ '#' + header
			# prefer top-level anchors
			addLinkToMap(header, label, current_file_name + '#' + anchor + ' \"' + current_title + ' - ' + header.rstrip("#") + '\"', config)
	
def applyLinkMap(file_name, config):
	# print("applyLinkMap() filename = %s" % file_name)
	markdown_file = open(file_name,"r")
	markdown_lines = markdown_file.readlines()
	markdown_file.close()
	
	config["context_current_file"] = file_name
	config["context_current_line_number"] = 0
	link_map = config["link_map"]
	
	inside_anchor = re.compile("\\[(.*?)\\]\\[#(.+?)\\]")
	
	new_lines = []
	write_changes = False
	in_pre = False
	previous_empty = True
	current_section = ""
	current_title = ""
	for markdown_line in markdown_lines:
		config["context_current_line_number"] += 1
		# we ignore everything in code blocks
		if previous_empty or in_pre:
			if markdown_line.lstrip()[:3] == '```':
				in_pre = not in_pre
			if markdown_line[:4] == "    ":
				new_lines.append(markdown_line)
				continue
			
		# don't link to the current section
		if markdown_line.find("title:") == 0:
			current_title = markdown_line.split('title: ')[1]
			current_title = current_title.rstrip().rstrip('\"')
			current_title = current_title.lstrip().lstrip('\"')
			current_section = current_title
		elif markdown_line.find("#") == 0:
			current_section = markdown_line.rstrip().rstrip('#').lstrip('#').rstrip().lstrip()
					
		new_line = ""
		if not in_pre:
			match = inside_anchor.search(markdown_line)
			if match != None:
				markdown_line = inside_anchor.sub("[\\1][%s#\\2]" % current_title, markdown_line)
			while True:
				anchor = ""
				bracket_depth = 0
				index = -1
				candidate_start = -1
				i = 0
				# ignore existing links, ie everything in brackets
				while i < len(markdown_line):
					if markdown_line[i] == '[': bracket_depth += 1
					elif markdown_line[i] == ']': bracket_depth -= 1
					elif bracket_depth == 0:
						# single backtick creates link; triple backticks don't
						if markdown_line[i] == '`':
							if markdown_line[i:i+3] == '```':
								i += 2
							elif candidate_start == -1:
								candidate_start = i
							else:
								candidate = markdown_line[candidate_start:i+1]
								values = link_map.get(candidate)
								if not values == None and candidate != "`%s`" % current_section:
									anchor = values[0]
									if len(values) > 1:
										errors = ["Multiple link targets in section [%s#%s][%s#%s]" % (current_title, current_section, current_title, current_section)]
										for value in values:
											errors.append("Option: %s" % value)
										qa.LogMissingDocumentation(config, candidate, errors, file_name)
									index = candidate_start
									break
								candidate_start = -1
					i += 1
				if index != -1:
					# print("applyLinkMap() candidate = %s" % candidate)
					# print("applyLinkMap() markdownline = %s" % markdown_line)
					write_changes = True
					new_line += markdown_line[:index]
					new_line += "[" + candidate + "]" + anchor
					markdown_line = markdown_line[index + len(candidate):]
				else:
					break
		new_line += markdown_line
		new_lines.append(new_line)
		previous_empty = markdown_line.lstrip() == ""
		
	if write_changes:
		markdown_file = open(file_name + ".new", "w")
		for new_line in new_lines:
			markdown_file.write(new_line)
		markdown_file.close()
		os.rename(file_name + ".new", file_name)
