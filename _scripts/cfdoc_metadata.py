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
import json
import cfdoc_qa as qa
from os import listdir
from os.path import isfile, join
from string import ascii_letters, digits

def run(config):
	config["syntax_path"] = config["project_directory"] + "/_generated/syntax_map.json"
	config["syntax_map"] = json.load(open(config["syntax_path"], 'r'))
	
	markdown_files =  config["markdown_files"]
	for file in markdown_files:
		processMetaData(file, config)

	# validate that the category tree is consistent, ie that there is an
	# index page for every subdirectory. Otherwise, Jekyll bails out
	category_tree = config["category_tree"]
	for node in category_tree:
		branch = category_tree.get(node)
		if branch == None: # orphan
			print "Orphan in the category tree! Check path to '%s / %s'" % (branch, node)
			exit(1)
		last_branch = branch.split("/")[-1]
		if last_branch == "":
			continue
		parent_branch = category_tree.get(last_branch)
		if parent_branch == None: # gaps
			print "ERROR: Missing index file '%s.markdown'" % (branch)
			exit(2)

# parse meta data lines, remove existing header for later reconstruction
def parseHeader(lines):
	header = {}
	
	new_lines = []
	in_header = False
	for line in lines:
		if line.find("---") == 0:
			in_header = not in_header
			if in_header:	# start of header - nothing to see here
				continue
			else: 			# end of header - done
				return header
		if not in_header:
			continue
		token_list = line.split(":")
		if len(token_list) != 2:
			print "parseHeader: ERROR in %s - wrong number of tokens" % line
			continue
		tag = token_list[0].lstrip().rstrip()
		value = token_list[1].lstrip().lstrip('\"').rstrip().rstrip('\"')
		header[tag] = value

	return header;

def processMetaData(file_path, config):
	category_tree = config.get("category_tree")
	if category_tree == None:
		category_tree = {}

	in_file = open(file_path,"r")
	lines = in_file.readlines()
	in_file.close()
	
	rel_file_path = file_path[len(config["markdown_directory"]) + 1:file_path.rfind('/')]
	file_name = os.path.basename(file_path)
	file_name = file_name[:file_name.rfind('.')]
	
	header = parseHeader(lines)
	if (not "published" in header) or (header["published"] == "false"):  # ignore unpublished content
		return
	if header.get("layout") != "default": # ignore special pages
		return
	if not "title" in header: # ignore pages without title, but that's an error at this point
		print "ERROR! Page without title: %s" % file_name
		return

	categories = []
	if len(rel_file_path):
		categories = rel_file_path.split("/")
	categories.append(file_name)
	if len(categories) > 1:
		category_tree[categories[-1]] = rel_file_path # store each leaf with its path
	else:
		category_tree[file_name] = ""
	categories = ["\"%s\"" % c for c in categories] # quote all entires to avoid ruby keywords
	if len(categories) == 1:
		category = categories[0]
	else:
		category = ", ".join(categories)

	if len(rel_file_path):
		alias = "%s-%s" % (rel_file_path, file_name)
	else:
		alias = file_name
	
	alias = alias.replace("/", "-").lower()

	out_file = open(file_path, "w")
	in_header = False
	for line in lines:
		if line.find("---") == 0:
			in_header = not in_header
			if not in_header: # write new tags before header is terminated
				out_file.write("categories: [%s]\n" % category)
				out_file.write("alias: %s.html\n" % alias)
		if in_header: # skip hard-coded duplicates
			if line.find("categories:") == 0:
				continue
			if line.find("alias:") == 0:
				continue
			
		out_file.write(line)

	out_file.close()
	config["category_tree"] = category_tree

