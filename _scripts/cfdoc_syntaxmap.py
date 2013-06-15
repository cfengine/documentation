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
import cfdoc_environment as environment
import collections

def processDirectory(cur_name,cur_dir, config):
	if os.path.isdir(cur_name) == True:
		markdownfiles = os.listdir(cur_name)	
		for file_name in markdownfiles:
			if os.path.isdir(cur_name+"/"+file_name) == True:
				processDirectory(cur_name+"/"+file_name,cur_dir+"/"+file_name, config)
			elif os.path.isdir(file_name) == False and ".markdown" in file_name:
				processFile(cur_name+"/"+file_name, config)

def processFile(markdown, config):
	syntax_map = config["syntax_map"]
	markdown_dir = os.path.dirname(markdown)
	markdown_name = os.path.basename(markdown)

	markdown_file = open(markdown, 'r')
	markdown_lines = markdown_file.readlines()
	markdown_file.close()
	
	write_changes = False
	new_markdown_lines = []
	in_pre = False
	markdown_line_number = 0
	for markdown_line in markdown_lines:
		keepline = True
		markdown_line_number += 1
		# skip markdown codeblocks
		if markdown_line[:3] == '```':
			in_pre = not in_pre
		
		new_lines = []
		if not in_pre:
			try:
				if markdown_line.find("[%CFENGINE_FUNCTION_TABLE%]") == 0:
					new_lines = generateFunctionTable(syntax_map)
				elif markdown_line.find('[%CFENGINE_FUNCTION_PROTOTYPE(') == 0:
					function = markdown_name[:markdown_name.find('.')]
					function += markdown_line[markdown_line.find('('):markdown_line.find('%]')]
					new_lines = generateFunctionPrototype(function, syntax_map)
			except:
				print "cfdoc_syntaxmap.py: Exception in " + markdown + ", line %d" % markdown_line_number 
				sys.stdout.write("         Exception : ")
				print sys.exc_info()
				print syntax_map.keys()

		if len(new_lines) > 0:
			keepline = False
			write_changes = True
			for new_line in new_lines:
				new_markdown_lines += new_line
		
		if keepline == True:
			new_markdown_lines += markdown_line
			
	if write_changes == True:
		new_markdown_filename = markdown_dir + "/new_" + markdown_name
		new_markdown_file = open(new_markdown_filename, 'w')
		for line in new_markdown_lines:
			new_markdown_file.write(line)
		new_markdown_file.close()
		os.rename(new_markdown_filename,markdown)

def generateFunctionTable(syntax_map):
	lines = []
	functions = syntax_map["functions"]
	ordered_functions = collections.OrderedDict(sorted(functions.items()))
	for function in ordered_functions:
		returnType = ordered_functions[function]["returnType"]
		if returnType == "context": returnType = "class"
		line = "* `" + returnType + "` "
		line += "[`" + function + "`][" + function + "]"
		line += '\n'
		lines.append(line)
	return lines

def generateFunctionPrototype(function, syntax_map):
	parameter_names = function[function.find('(')+1:-1].split(',')
	function = function[:function.find('(')]

	returnType = syntax_map["functions"][function]["returnType"]
	parameters = syntax_map["functions"][function]["parameters"]
	prototype = function + "("
	arguments = []
	arg_idx = 0
	for parameter in parameters:
		arguments += "* `" + parameter_names[arg_idx] + "`: `"
		arguments += parameter["type"] + "`, in the range: `"
		arguments += parameter["range"] + "`\n"
		prototype += parameter_names[arg_idx] + ", "
		arg_idx += 1
	if prototype[-2:] == ", ":
		prototype = prototype[:len(prototype)-2]
	prototype += ")"
	
	lines = []
	lines = "**Prototype:** `" + prototype + "`\n\n"
	lines += "**Return type:** `" + returnType + "`\n\n"
	lines += "**Arguments:** \n\n"
	for argument in arguments:
		lines += argument
	lines += "\n"
	return lines

def run(config):
	processDirectory(config["markdown_directory"], "", config)
