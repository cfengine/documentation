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
import cfdoc_linkresolver as linkresolver
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
		if markdown_line.find("title:") == 0:
			current_title = markdown_line.split('title: ')
			current_title = current_title[1].rstrip().rstrip('\"')
			current_title = current_title.lstrip().lstrip('\"')
			config["context_current_title"] = current_title
		elif markdown_line.find("alias:") == 0:
			current_html = markdown_line.split('alias: ')
			current_html = current_html[1].rstrip()
			config["context_current_html"] = current_html
			
		config["context_current_line"] = markdown_line
		config["context_current_line_number"] = markdown_line_number
		# skip markdown codeblocks
		if markdown_line.lstrip()[:3] == '```':
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
					line += "`" + functionlist[index] + "()`"
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

def generateTreeLine(keyword, depth):
	line = " " * depth * 4
	line += "* `" + keyword + "`\n"
	return line

def generateTree(tree, excludes, depth, config):
	skip_leaves = ["attributes"]
	lines = []
	try:
		keys = tree.keys()
		for key in keys:
			if key in excludes:
				continue
			subtree = tree.get(key)
			# skip some branches, but not the tree
			if not key in skip_leaves:
				lines.append(generateTreeLine(key, depth))
			else:
				depth -= 1
			if subtree:
				lines += generateTree(subtree, excludes, depth + 1, config)
				type = subtree.get("type")
				try:
					if type and (type == "body"):
						syntax_map = config["syntax_map"]
						bodyTree = syntax_map["bodyTypes"]
						bodyTree = bodyTree.get(key)
						lines += generateTree(bodyTree, excludes, depth + 1, config)
				except:
					continue
		return lines
	except:
		lines.append(generateTreeLine(tree, depth))
		return lines

def syntax_map(parameters, config):
	syntax_map = config["syntax_map"]
	if parameters != None:
		syntax_map = syntax_map[parameters[0]]
		parameters = parameters[1:]
	
	lines = generateTree(syntax_map, parameters, 0, config)
	return lines

def resolveAttribute(attributes, argument):
	attribute_line = ""
	
	for attribute in attributes:
		rval = attribute["rval"]
		lval = attribute["lval"]
		lval_link = "`" + lval + "`"
		attribute_type = rval["type"]
		
		if attribute_type == "string":
			value = rval.get("value")
			if value == None:
				continue
			if value.find("(" + argument + ")") != -1:
				attribute_line += ": " + attribute_type
				attribute_line += ", used as rval of attribute " + lval_link
		elif attribute_type == "functionCall":
			function_name = rval["name"]
			function_name_link = "`" + function_name + "()`"
			for function_argument in rval["arguments"]:
				function_argument_type = function_argument.get("type")
				function_argument_value = function_argument.get("value")
				if function_argument_value == None:
					continue
				if function_argument_value.find("(" + argument + ")") != -1:
					attribute_line += ": " + function_argument_type
					attribute_line += ", used as a parameter to function " + function_name_link
					attribute_line += " setting promise attribute " + lval_link
				
	return attribute_line

def library_include(parameters, config):
	markdown_lines = []
	
	policy_filename = parameters[0] + ".json"
	policy_json = config.get(policy_filename)
	html_name = config.get("context_current_html")
	if policy_json == None:
		policy_path = config["project_directory"] + "/_site/" + policy_filename
		if not os.path.exists(policy_path):
			print "cfdoc_syntaxmap:library_include: File does not exist: " + policy_path
			return markdown_lines
		
		policy_json = json.load(open(policy_path, 'r'))
		config[policy_filename] = policy_json
		
	# for all bundles and bodies...
	for key in policy_json.keys():
		markdown_lines += "## " + key + "\n\n"
		element_list = policy_json[key]
		
		current_type = None
		for element in element_list:
			namespace = element["namespace"]
			if namespace == "default":
				namespace = None
			name = element["name"]
			element_type = element.get("bundleType")
			if element_type == None:
				element_type = element.get("bodyType")
			if element_type == None:
				print "cfdoc_syntaxmap:library_include: element without type: " + name
				continue
				
			# start a new block for changed types
			# Assumes that bundles and bodies are grouped by type in library.cf
			if element_type != current_type:
				current_type = element_type
				markdown_lines.append("### " + current_type + " " + key + "\n")
				markdown_lines.append("\n")
		
			prototype = name
			if namespace:
				prototype = namespace + ":" + prototype
				
			markdown_lines.append("#### " + prototype + "\n")
			link_target = prototype + "()"
			if not namespace:
				link_target = parameters[0] + ":" + link_target
			linkresolver.addLinkToMap("`" + prototype + "()`", link_target, html_name + "#" + prototype, config)
			markdown_lines.append("\n")
			
			arguments = element["arguments"]
			argument_idx = 0
			argument_lines = []
			while argument_idx < len(arguments):
				if argument_idx == 0:
					prototype += "("
					argument_lines.append("**Arguments:**\n\n")
				argument = arguments[argument_idx]
				prototype += argument
				argument_line = "* `" + argument + "`"
				# find out where the argument is being used
				if key == "bundles":
					for promise_type in element["promiseTypes"]:
						for context in promise_type["contexts"]:
							for promise in context["promises"]:
								if promise["promiser"].find("(" + argument + ")") != -1:
									promise_type_link = "`" + promise_type["name"] + "`"
									argument_line += ", used as promiser of type " + promise_type_link
								else:
									argument_line += resolveAttribute(promise["attributes"], argument)
				elif key == "bodies":
					for context in element["contexts"]:
						argument_line += resolveAttribute(context["attributes"], argument)
				argument_line += "\n"
					
				argument_lines.append(argument_line)
				argument_idx += 1
				if argument_idx == len(arguments):
					prototype += ")"
				else:
					prototype += ", "
					
			markdown_lines.append("**Prototype:** `" + prototype + "`\n")
			markdown_lines.append("\n")
			markdown_lines.append(argument_lines)
			markdown_lines.append("\n")
			
			try:
				source_path = config["project_directory"] + "/" + element["sourcePath"]
				source_file = open(source_path, 'r')
				source_code = source_file.read()
				offset = element["offset"]
				offsetEnd = element["offsetEnd"]
				
				markdown_lines.append("\n```cf3\n")
				markdown_lines.append(source_code[offset:offsetEnd])
				markdown_lines.append("\n```\n")
				markdown_lines.append("\n")
			except:
				print "cfdoc_syntaxmap:library_include: could not include code from " + name
		
	if len(markdown_lines) == 0:
		print "cfdoc_syntaxmap:library_include: Failure to include " + parameters[0]
		
	return 	markdown_lines
