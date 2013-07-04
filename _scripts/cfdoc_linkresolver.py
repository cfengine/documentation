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
from os import listdir
from os.path import isfile, join
from string import ascii_letters, digits

def run(config):
	markdown_files =  config["markdown_files"]
	readLinkFile(config)
	for file in markdown_files:
		parseMarkdownForAnchors(file, config)

def apply(config):
	markdown_files =  config["markdown_files"]
	for file in markdown_files:
		applyLinkMap(file, config)

def readLinkFile(config):
	output_file = config["reference_path"]
	link_map = config.get("link_map", dict())
	
	link_file = open(output_file, 'r')
	link_lines = link_file.readlines()
	for line in link_lines:
		label = line[line.find('[') + 1:line.find(']')]
		link_map["`" + label + "`"] = "[" + label + "]"
	config["link_map"] = link_map

def addLinkToMap(keyword, anchor, html, config):
	link_map = config.get("link_map", dict())

	# don't overwrite
	if keyword in link_map:
		return
		
	link_map[keyword] = "[" + anchor + "]"
	
	output_file = config["reference_path"]
	out_file = open(output_file, "a")
	output_string = '[' + anchor + ']: ' + html
	out_file.write(output_string+"\n")
	out_file.close()
	
	config["link_map"] = link_map

def parseMarkdownForAnchors(file_name, config):
	in_file = open(file_name,"r")
	lines = in_file.readlines()
	in_file.close()
	
	current_file_name = ""
	current_file_label = ""
	current_title = ""
	header_list = []
	
	in_pre = False
	for line in lines:
		# ignore code blocks
		if line.find("    ") == 0:
			continue
		elif line.find("```") == 0:
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
		elif line.find("#") == 0:
			current_header = line.lstrip('#').rstrip().lstrip()
			header_list.append(current_header)

	current_file_label = current_title

	if current_file_label != "" and current_file_name != "":
		keyword = current_file_label
		# generate auto-link to functions via `function()`
		if current_file_name.find("reference-functions-") == 0:
			keyword += "()"
		addLinkToMap("`" + keyword + "`", current_file_label, current_file_name + ' \"' + current_title + '\"', config)
		# keep dictionary reasonably short by including at most three-word headers
		for header in header_list:
			if header == "":
				continue
			anchor = header.lower()
			anchor = anchor.replace(" ", "-")
			anchor = anchor.replace(":", "-")
			anchor = anchor.replace(".", "-")
			anchor = anchor.replace("`", "-")
			anchor = anchor.replace("/", "-")
			anchor = anchor.replace("$", "-")
			anchor = anchor.replace("(", "-")
			anchor = anchor.replace(")", "-")
			anchor = anchor.replace("\"", "")
			anchor = anchor.replace("--", "-")
			anchor = anchor.lstrip("-").rstrip("-")
			label = current_file_label+ '#' + header
			# prefer top-level anchors
			addLinkToMap("`" + header + "`", label, current_file_name + '#' + anchor + ' \"' + current_title + ' - ' + header + '\"', config)
	
def applyLinkMap(file_name, config):
	markdown_file = open(file_name,"r")
	markdown_lines = markdown_file.readlines()
	markdown_file.close()
	
	link_map = config["link_map"]
	
	new_lines = []
	write_changes = False
	in_pre = False
	previous_empty = True
	current_section = ""
	for markdown_line in markdown_lines:
		# we ignore everything in code blocks
		if previous_empty or in_pre:
			if markdown_line.lstrip()[:3] == '```':
				in_pre = not in_pre
			if markdown_line[:4] == "    ":
				new_lines.append(markdown_line)
				continue
			
		# don't link to the current section
		if markdown_line.find("title:") == 0:
			current_section = markdown_line.split('title: ')
			current_section = current_section[1].rstrip().rstrip('\"')
			current_section = current_section.lstrip().lstrip('\"')
			current_section = "`" + current_section + "`"
		elif markdown_line.find("#") == 0:
			current_section = "`" + markdown_line.lstrip('#').rstrip().lstrip() + "`"
					
		new_line = ""
		if not in_pre:
			while True:
				value = ""
				bracket_depth = 0
				index = -1
				candidate_start = -1
				i = 0
				# ignore existing links, ie everything in brackets
				while i < len(markdown_line):
					if markdown_line[i] == '[': bracket_depth += 1
					elif markdown_line[i] == ']': bracket_depth -= 1
					elif bracket_depth == 0:
						if markdown_line[i] == '`':
							if candidate_start == -1:
								candidate_start = i
							else:
								candidate = markdown_line[candidate_start:i+1]
								value = link_map.get(candidate)
								if not value == None and candidate != current_section:
									index = candidate_start
									break
								candidate_start = -1
					i += 1
				if index != -1:
					write_changes = True
					new_line += markdown_line[:index]
					new_line += "[" + candidate + "]" + value
					markdown_line = markdown_line[index + len(candidate):]
				else:
					break
		new_line += markdown_line
		new_lines.append(new_line)
		previous_empty = markdown_line.lstrip() == "\n"
		
	if write_changes:
		markdown_file = open(file_name + ".new", "w")
		for new_line in new_lines:
			markdown_file.write(new_line)
		markdown_file.close()
		os.rename(file_name + ".new", file_name)
