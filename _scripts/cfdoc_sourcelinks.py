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
import re

from os import listdir
from os.path import isfile, join
from string import ascii_letters, digits

def run(config):
	markdown_files = config["markdown_files"]
	error_count = 0
	for file in markdown_files:
		error_count += addLinkToSource(file, config)
	if error_count:
		raise Exception("%d errors while processing HTML files" % error_count)

def addLinkToSource(file_name,config):
	in_file = open(file_name,"r")
	lines = in_file.readlines()
	in_file.close()
	source_file = file_name[config["markdown_directory"].__len__():]
	html_file = ""

	for line in lines:
		if line.find("alias:") == 0:
			html_file = line.split('alias: ')
			html_file = html_file[1].rstrip()
			break
		if line.find("layout: printable") == 0:
			return 0
	
	if not html_file:
		return 0
	
	error_count = 0
	html_file = config['CFE_DIR'] + "/" + html_file
	try:
		in_file = open(html_file, "r")
		lines = in_file.readlines()
		in_file.close()
		unresolved_link = re.compile("(^|\\s+|>)\\[.+?\\]\\[.*?\\](\\s|[\\,\\.\\;])")
		unexpanded_macro = re.compile("\\[%CFEngine_.*%\\]")

		new_html_file = html_file + ".new"
		out_file = open(new_html_file, "w")
		for line in lines:
			line = line.replace("\">markdown source</a>]", source_file + "\">markdown source</a>]")
			if unresolved_link.search(line) != None:
				print "Unresolved link in '%s', html-line '%s'\n" % (file_name, line)
				error_count += 1
			if unexpanded_macro.search(line) != None:
				print "Unexpanded macro in '%s', html-line '%s'\n" % (file_name, line)
				error_count += 1
			out_file.write(line)
		out_file.close()
		
		os.rename(new_html_file,html_file)
		return error_count
	except:
		print "cfdoc_sourcelinks: Error processing " + html_file
		return 1
