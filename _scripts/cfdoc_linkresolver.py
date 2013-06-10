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
from os import listdir
from os.path import isfile, join
from string import ascii_letters, digits

def createLinkFile(cur_name,output_file,cur_dir):
	if os.path.isdir(cur_name) == True:
		markdownfiles = os.listdir(cur_name)	
		for file_name in markdownfiles:
			if os.path.isdir(cur_name+"/"+file_name) == True:
				createLinkFile(cur_name+"/"+file_name,output_file,cur_dir+"/"+file_name)
			elif os.path.isdir(file_name) == False and ".markdown" in file_name:
				addToLinkFile(cur_name+"/"+file_name,output_file,cur_dir)

def addToLinkFile(file_name,output_file,cur_dir):
	
	in_file = open(file_name,"r")
	lines = in_file.readlines()
	in_file.close()

	out_file = open(output_file, "a")
	current_file_name = ""
	current_file_label = ""
	current_title = ""
	header_list = []
	
	for line in lines:
		if line.find("title:") == 0:
			current_title = line.split('title: ')					
			current_title = current_title[1].rstrip()
			current_title = current_title.lstrip()
		elif line.find("alias:") == 0:
			current_file_name = line.split('alias: ')
			current_file_name = current_file_name[1].rstrip()
		elif line.find("#") == 0:
			current_header = line.lstrip('#').rstrip().lstrip()
			header_list.append(current_header)

	current_file_label = current_title

	if current_file_label != "" and current_file_name != "":
		output_string = '['+current_file_label+']: '+current_file_name+' \"'+current_title+'\"'
		out_file.write(output_string+"\n")
		for header in header_list:
			if header == "":
				continue
			anchor = header.lower()
			anchor = anchor.replace(" ", "-")
			anchor = anchor.replace(":", "-")
			anchor = anchor.replace("`", "-")
			anchor = anchor.replace("/", "-")
			anchor = anchor.replace("$", "-")
			anchor = anchor.replace("(", "-")
			anchor = anchor.replace(")", "-")
			anchor = anchor.replace("--", "-")
			anchor = anchor.lstrip("-").rstrip("-")
			output_string = '['+current_file_label+ '#' + header + ']: '
			output_string += current_file_name + '#' + anchor + ' '
			output_string += '\"'+current_title + ' - ' + header + '\"'
			out_file.write(output_string+"\n")
