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

def validate(branch):
	config = {}
	config["WORKDIR"] = os.environ.get('WRKDIR')
	if config["WORKDIR"] == None:
		print 'Environment variable WRKDIR is not set, setting it to current working directory'
		config["WORKDIR"] = os.getcwd()
		os.environ["WRKDIR"] = os.getcwd()

	if not os.path.exists(config["WORKDIR"]):
		print "Directory WORKDIR not found: " + config["WORKDIR"]
		exit(2)
		
	config["project_directory"] = config["WORKDIR"] + "/documentation-generator"
	if not os.path.exists(config["project_directory"]):
		print "Directory 'documentation-generator' not found in WORKDIR"
	
	config["markdown_directory"] = config["WORKDIR"] + "/documentation"
	if not os.path.exists(config["markdown_directory"]):
		print "Directory 'documentation' not found in WORKDIR"

	if (branch == "master"):
		all_versions = [ent for ent in os.listdir(config["WORKDIR"] + "/masterfiles/lib") if (re.match("^[0-9].*", ent))]
		version = sorted(all_versions)[-1]
	else:
		version = branch

	config["include_directories"] = []
	config["include_directories"].append(config["WORKDIR"])
	config["include_directories"].append(config["WORKDIR"] + "/core/examples")
	config["include_directories"].append(config["WORKDIR"] + "/documentation/examples/example-snippets")
	config["include_directories"].append(config["WORKDIR"] + "/documentation-generator/_generated")
	config["include_directories"].append(config["WORKDIR"] + "/masterfiles/_generated")
	config["include_directories"].append(config["WORKDIR"] + "/masterfiles")
	config["include_directories"].append(config["WORKDIR"] + "/masterfiles/lib/" + version)
	config["include_directories"].append(config["WORKDIR"] + "/core/tests")

	config["reference_path"] = config["project_directory"] + "/_references.md"
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
