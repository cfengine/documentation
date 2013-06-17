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

def run(config):
	markdown_files = config["markdown_files"]
	for file in markdown_files:
		config["context_current_file"] = file
		processFile(file, config)

def processFile(markdown, config):
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
		markdown_line_number += 1
		config["context_current_line"] = markdown_line
		config["context_current_line_number"] = markdown_line_number
		# skip markdown codeblocks
		if markdown_line[:3] == '```':
			in_pre = not in_pre
		if in_pre or markdown_line[:4] == "    ":
			new_markdown_lines.append(markdown_line)
			continue
			
		marker = "[%CFEngine_"
		marker_index = markdown_line.find(marker)
		if marker_index == -1:
			new_markdown_lines.append(markdown_line)
			continue
			
		new_lines = []
		call = markdown_line[marker_index + len(marker):markdown_line.find("%]")]
		function = call[:call.find('(')]
		parameters = call[len(function) + 1:call.find(')')]
		parameters = parameters.replace(" ", "")
		parameters = parameters.split(",")
		if len(parameters) == 1 and parameters[0] == "":
			parameters = None
		
		try:
			functor = getattr(sys.modules[__name__], function)
		except:
			functor = None
		if (functor):
			try:
				new_lines = functor(parameters, config)
			except:
				sys.stdout.write("cfdoc_syntaxmap: Exception calling ")
				print functor
				sys.stdout.write("                 in " + config["context_current_file"])
				sys.stdout.write("(%d): " % config["context_current_line_number"])
				sys.stdout.write('`%s`' % config["context_current_line"])
				sys.stdout.write("     Exception : ")
				print sys.exc_info()
		else:
			print "cfdoc_syntaxmap: Unknown function `" + function + "`"
			print "                 in " + markdown + "(%d)" % markdown_line_number
			print "                 " + markdown_line
			new_lines += "<!-- " + markdown_line + "-->"
			
		if len(new_lines) > 0:
			write_changes = True
			for new_line in new_lines:
				new_markdown_lines += new_line
		else:
			new_markdown_lines += markdown_line
			
	if write_changes == True:
		new_markdown_filename = markdown_dir + "/new_" + markdown_name
		new_markdown_file = open(new_markdown_filename, 'w')
		for line in new_markdown_lines:
			new_markdown_file.write(line)
		new_markdown_file.close()
		os.rename(new_markdown_filename,markdown)

def addToDict(dictionary, key, function):
	values = dictionary.get(key)
	if values == None: values = list()
	values.append(function)
	dictionary [key] = values

def functionLink(function):
	link = "[`" + function + "`][" + function + "]"
	return link

def dictToTable(dictionary):
	lines = list()
	row = 0
	index = 0
	while True:
		columns = 0
		line = "| "
		for key in dictionary.keys():
			if row == 0:
				line += "`" + key + "`"
				columns =- 1
			elif row == 1:
				line += "------------"
				columns =- 1
			else:
				functionlist = dictionary[key]
				if index < len(functionlist):
					line += functionLink(functionlist[index])
					columns += 1
			line += " | "
		line += "\n"
		row += 1
		if columns == 0:
			break
		elif columns > 0:
			index += 1
		lines.append(line)
	lines.append("\n")
	return lines

def function_table(parameters, config):
	syntax_map = config["syntax_map"]
	lines = []
	functions = syntax_map["functions"]
	ordered_functions = sorted(functions)
	
	categoryDict = dict()
	returnTypeDict = dict()
	functionlist = list()
	
	for function in ordered_functions:
		category = functions[function]["category"]
		addToDict(categoryDict, category, function)
		
		returnType = functions[function]["returnType"]
		if returnType == "context": returnType = "class"
		elif returnType in ["ilist","slist","rlist"]: returnType = "(i,r,s)list"
		elif returnType in ["irange","rrange"]: returnType = "(i,r)range"
		addToDict(returnTypeDict, returnType, function)
		
	lines.append("### Functions by Category\n\n")
	lines += dictToTable(categoryDict)
	
	lines.append("### Functions by Return Type\n\n")
	lines += dictToTable(returnTypeDict)
	
	for function in ordered_functions:
		returnType = functions[function]["returnType"]
		if returnType == "context": returnType = "class"
		line = "* `" + returnType + "` "
		line += functionLink(function)
		line += '\n'
		lines.append(line)
	return lines

def function_prototype(parameters, config):
	syntax_map = config["syntax_map"]
	# assume that basename of file = function
	function = config["context_current_file"]
	function = function[function.rfind("/")+1:function.rfind('.')+1]
	function = function[:function.find('(')]

	prototype = function + "("
	for parameter in parameters:
		prototype += parameter + ", "
	if prototype[-2:] == ", ":
		prototype = prototype[:len(prototype)-2]
	prototype += ")"
	
	lines = []
	lines = "**Prototype:** `" + prototype + "`\n"
	return lines

def function_attributes(parameters, config):
	syntax_map = config["syntax_map"]
	# assume that basename of file = function
	function = config["context_current_file"]
	function = function[function.rfind("/")+1:function.rfind('.')+1]

	parameter_names = parameters
	function = function[:function.find('(')]

	returnType = syntax_map["functions"][function]["returnType"]
	parameters = syntax_map["functions"][function]["parameters"]
	arguments = []
	arg_idx = 0
	for parameter in parameters:
		arguments += "* `" + parameter_names[arg_idx] + "`: `"
		arguments += parameter["type"] + "`, in the range: `"
		arguments += parameter["range"] + "`\n"
		arg_idx += 1
	
	lines = []
	lines += "**Return type:** `" + returnType + "`\n\n"
	lines += "**Arguments:** \n\n"
	for argument in arguments:
		lines += argument
	return lines
	return lines
