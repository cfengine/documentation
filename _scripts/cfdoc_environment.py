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
import json

def validate():
	config = {}
	config["reference_path"] = os.environ.get('CFDOC_LINKFILE')
	if not os.path.exists(config["reference_path"]):
		print "Path in 'CFDOC_LINKFILE' not found: " + config["reference_path"]
	
	config["markdown_directory"] = os.environ.get('CFDOC_DIRNAME')
	if not os.path.exists(config["markdown_directory"]):
		print "Path in 'CFDOC_DIRNAME' not found: " + config["markdown_directory"]

	config["example_directory"] = os.environ.get('CFDOC_EXAMPLEPATH')
	if not os.path.exists(config["example_directory"]):
		print "Path in 'CFDOC_EXAMPLEPATH' not found: " + config["example_directory"]

	if config["reference_path"] == None or config["markdown_directory"] == None:
	
		print 'Please set environment variables and retry. Example:'
		print '> CFDOC_LINKFILE="/path/to/link/file"'
		print '> export CFDOC_LINKFILE'
		print '> CFDOC_DIRNAME="/path/to/doc/dir"'
		print '> export CFDOC_DIRNAME'
		print '> /path/to/this/script/cfdoc_createlinks.py'
		exit(1)
	
	config["project_directory"] = os.path.dirname(config["reference_path"])
	config["config_path"] = config["project_directory"] + "/_config.yml"

	with open(config["config_path"], 'r') as config_file:
		lines = config_file.readlines()
		for line in lines:
			comment = line.find('#')
			if comment != -1:
				line = line[:comment]
			assign = line.split(':')
			if assign.__len__() != 2:
				continue
			if assign[1] == '' or assign[1] == '\n':
				continue
			key = assign[0].lstrip().rstrip()
			value = assign[1].lstrip().rstrip()
			
			config[key] = value
			
	print 'cfdoc_environment: cwd              = ' + os.getcwd()
	print '                   config           = '
	print config
		
	config["syntax_path"] = config["project_directory"] + "/_site/syntax_map.json"
	config["syntax_map"] = json.load(open(config["syntax_path"], 'r'))
	
	markdown_files = []
	scanDirectory(config["markdown_directory"], "", ".markdown", markdown_files)
	config["markdown_files"] = markdown_files
	
	return config

def scanDirectory(cur_name, cur_dir, ext, file_list):
	if os.path.isdir(cur_name) == True:
		markdownfiles = os.listdir(cur_name)
		for file_name in markdownfiles:
			if os.path.isdir(cur_name+"/"+file_name) == True and file_name[0] != '.':
				scanDirectory(cur_name+"/"+file_name,cur_dir+"/"+file_name, ext, file_list)
			elif os.path.isdir(file_name) == False and file_name[-len(ext):] == ext:
				file_list.append(cur_name + "/" + file_name)
