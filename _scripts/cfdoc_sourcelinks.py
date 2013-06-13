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
import cfdoc_environment as environment

from os import listdir
from os.path import isfile, join
from string import ascii_letters, digits

def processDirectory(cur_name,cur_dir):
	if os.path.isdir(cur_name) == True:
		markdownfiles = os.listdir(cur_name)
		for file_name in markdownfiles:
			if os.path.isdir(cur_name+"/"+file_name) == True:
				processDirectory(cur_name+"/"+file_name,cur_dir+"/"+file_name)
			elif os.path.isdir(file_name) == False and ".markdown" in file_name:
				addLinkToSource(cur_name+"/"+file_name,cur_dir)

def addLinkToSource(file_name,cur_dir):
	in_file = open(file_name,"r")
	lines = in_file.readlines()
	in_file.close()
	
	source_file = file_name[environment.CFDOC_DIRNAME.__len__():]
	html_file = ""
	
	for line in lines:
		if line.find("alias:") == 0:
			html_file = line.split('alias: ')
			html_file = html_file[1].rstrip()
			break
	
	if not html_file:
		return
	
	html_file = environment.CFDOC_CONFIG['CFE_DIR'] + "/" + html_file
	print html_file
	try:
		out_file = open(html_file, "r")
		lines = out_file.readlines()
		out_file.close()
	
		out_file = open(html_file, "w")
		for line in lines:
			line = line.replace("\">markdown source</a>]", source_file + "\">markdown source</a>]")
			out_file.write(line)
		out_file.close()
	except:
		print "cfdoc_sourcelinks: Error processing " + html_file
