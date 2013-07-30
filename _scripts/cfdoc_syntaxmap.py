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
	previous_empty = True
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
		if previous_empty or in_pre:
			if markdown_line.lstrip()[:3] == '```':
				in_pre = not in_pre
			if in_pre or markdown_line[:4] == "    ":
				new_markdown_lines.append(markdown_line)
				continue
			
		marker = "[%CFEngine_"
		marker_index = markdown_line.find(marker)
		if marker_index == -1:
			new_markdown_lines.append(markdown_line)
			previous_empty = markdown_line.lstrip() == '\n'
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
	if parameters != None:
		for parameter in parameters:
			prototype += parameter + ", "
		if prototype[-2:] == ", ":
			prototype = prototype[:len(prototype)-2]
	prototype += ")"

	returnType = syntax_map["functions"][function]["returnType"]
	if returnType == "context":
		returnType = "boolean"

	lines = []
	lines = "**Prototype:** `" + prototype + "`\n\n"
	lines += "**Return type:** `" + returnType + "`\n\n"

	return lines

def function_attributes(parameters, config):
	syntax_map = config["syntax_map"]
	# assume that basename of file = function
	function = config["context_current_file"]
	function = function[function.rfind("/")+1:function.rfind('.')+1]

	parameter_names = parameters
	function = function[:function.find('(')]

	parameters = syntax_map["functions"][function]["parameters"]
	arguments = []
	arg_idx = 0
	for parameter in parameters:
		parameter_name = parameter_names[arg_idx]
		parameter_type = parameter["type"]
		option_arg = parameter_type == "option"
		if parameter_name == "regex":
			parameter_type = "regular expression"
		else:
			parameter_type = "`" + parameter_type + "`"

		arguments += "* `" + parameter_name  + "`: "
		if option_arg:
			arguments += "one of\n"
			options = parameter["range"].split(',')
			for option in options:
				arguments += "    * `" + option + "`\n"
		else:
			arguments += parameter_type + ", in the range: `"
			arguments += parameter["range"] + "`\n"
		arg_idx += 1
	
	lines = []
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
				attribute_line += ", used in the value of attribute " + lval_link
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
					attribute_line += ", used to set promise attribute " + lval_link
		if attribute_line != "":
			break

	return attribute_line

def library_include(parameters, config):
	markdown_lines = []
	
	policy_filename = parameters[0] + ".json"
	policy_json = config.get(policy_filename)
	html_name = config.get("context_current_html")
	if policy_json == None:
		policy_path = config["project_directory"] + "/_json/" + policy_filename
		if not os.path.exists(policy_path):
			print "cfdoc_syntaxmap:library_include: File does not exist: " + policy_path
			return markdown_lines
		
		policy_json = json.load(open(policy_path, 'r'))
		config[policy_filename] = policy_json
		
	# for all bundles and bodies...
	for key in policy_json.keys():
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
			
			code_lines = []
			documentation_lines = []
			documentation_dict = dict()
			
			try:
				source_path = config["project_directory"] + "/" + element["sourcePath"]
				source_file = open(source_path, 'r')
				sourceLine = element["line"]
				sourceLines = source_file.readlines()
			except:
				print "cfdoc_syntaxmap:library_include: could not include code from " + name
			
			if len(sourceLines):
				# search up to include bundle/body declaration and comments in between
				headerLines = list()
				header_line = sourceLine - 1
				while header_line:
					line = sourceLines[header_line].lstrip()
					header_line -= 1
					headerLines.insert(0, line) # aka prepend
					if key == "bundles" and line.find("bundle ") == 0:
						break
					if key == "bodies" and line.find("body ") == 0:
						break
				
				# scan comments for doxygen-style documentation
				if len(headerLines):
					current_tag = None
					current_param = None
					current_line = ""
					for headerLine in headerLines:
						if headerLine.find("#") != 0:
							continue
							
						headerLine = headerLine[1:].lstrip().rstrip()
						if headerLine.find("@") == 0:
							current_param = None
							headerLine = headerLine[1:]
							current_tag = headerLine[:headerLine.find(" ")]
							headerLine = headerLine[len(current_tag) + 1:]
							documentation_dict[current_tag] = ""
							
						if current_tag == None:
							continue
						
						if current_tag == "param":
							if current_param == None:
								current_param = headerLine[:headerLine.find(" ")]
								headerLine = headerLine[len(current_param) + 1:]
								documentation_dict["param_" + current_param] = headerLine + "\n"
							else:
								documentation_dict["param_" + current_param] += headerLine + "\n"
						else:
							documentation_dict[current_tag] += headerLine + "\n"
							
					brief = documentation_dict.get("brief", "")
					if len(brief):
						documentation_lines.append("**Description:** ")
						documentation_lines.append(brief)
						documentation_lines.append("\n")
					return_doc = documentation_dict.get("return", "")
					if len(return_doc):
						documentation_lines.append("**Return value:** ")
						documentation_lines.append(return_doc)
						documentation_lines.append("\n")
				
				code_lines.append("\n```cf3\n")
				if len(headerLines):
					code_lines.append(headerLines[0])
					code_lines.append("{\n")
				while sourceLine < len(sourceLines):
					line = sourceLines[sourceLine]
					code_lines.append(line)
					# super-naive parser...
					if line.find("}") == 0:
						break
					sourceLine += 1
				code_lines.append("\n```\n")

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
				
				# if we have already found documentation for this, use it
				param_line = documentation_dict.get("param_" + argument)
				if param_line != None:
					argument_line += ": " + param_line
				# find out where the argument is being used
				elif key == "bundles":
					for promise_type in element["promiseTypes"]:
						promise_type_link = "`" + promise_type["name"] + "`"
						for context in promise_type["contexts"]:
							for promise in context["promises"]:
								promiser = promise["promiser"]
								if promiser.find("(" + argument + ")") != -1:
									argument_line += ", used as promiser of type " + promise_type_link
								else:
									argument_line += resolveAttribute(promise["attributes"], argument)
									if len(argument_line):
										argument_line += " of " + promise_type_link + " promiser *" + promiser + "*"
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
			if len(documentation_lines):
				markdown_lines.append(documentation_lines)
				markdown_lines.append("\n")
			if len(argument_lines):
				markdown_lines.append(argument_lines)
				markdown_lines.append("\n")
			if len(code_lines):
				markdown_lines.append(code_lines)
				markdown_lines.append("\n")
			markdown_lines.append("\n")
		
	if len(markdown_lines) == 0:
		print "cfdoc_syntaxmap:library_include: Failure to include " + parameters[0]
		
	return 	markdown_lines
