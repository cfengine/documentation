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
	
	f = open(file_name,"r")
	lines = f.readlines()
	f.close()
	
	current_file_name = ""
	current_file_label = ""
	current_title = ""
	
	for line in lines:
		if line.find("title:") == 0:
			current_title = line.split('title: ')					
			current_title = current_title[1].rstrip()	
		elif line.find("alias:") == 0:
	
			current_file_name = line.split('alias: ')					
			current_file_name = current_file_name[1].rstrip()		
			current_file_label = current_file_name.replace(".html","")				
			current_file_label = "".join([ch for ch in current_file_label if ch in (ascii_letters) or ch == "-"])
			current_file_label = current_file_label.lstrip('-')

	current_file_label = current_title.replace(" ","-")	
	current_file_label = current_file_label.lstrip('-')
	output_string = '['+current_file_label+']: '+cur_dir+"/"+current_file_name+' \"'+current_title+'\"'

	open(output_file, "a").write(output_string+"\n")

