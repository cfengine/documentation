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
import sys
import json
import copy
import cfdoc_environment as environment
import cfdoc_linkresolver as linkresolver
import cfdoc_qa as qa
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
		parameters = parameters.split(",")
		parameters = [p.lstrip().rstrip() for p in parameters]
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
				sys.stdout.write("cfdoc_macros: Exception calling ")
				print functor
				sys.stdout.write("                 in " + config["context_current_file"])
				sys.stdout.write("(%d): " % config["context_current_line_number"])
				sys.stdout.write('`%s`' % config["context_current_line"])
				sys.stdout.write("     Exception : ")
				print sys.exc_info()
		else:
			print "cfdoc_macros: Unknown function `" + function + "`"
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
	qa.LogProcessStart(config, "function_table")
	link_map = config["link_map"]
	
	syntax_map = config["syntax_map"]
	lines = []
	functions = syntax_map["functions"]
	ordered_functions = sorted(functions)
	
	categoryDict = dict()
	returnTypeDict = dict()
	functionlist = list()
	
	for function in ordered_functions:
		link = function + "()"
		if not "`" + link + "`" in link_map:
			qa.LogMissingDocumentation(config, link, ["No documentation"], "")
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

def document_type(type, type_definition, excludes, config):
	link_map = config["link_map"]

	lines = []

	type_status = type_definition.get("status", "normal")
	type_attributes = type_definition.get("attributes")
	
	attributes = sorted(type_attributes.keys())
	for attribute in attributes:
		if attribute in excludes:
			continue
		attribute_definition = type_attributes.get(attribute)
		if attribute_definition == None:
			print "cfdoc_macros: syntax_map - no definition for attribute %s in type %s" % (attribute, type)
			continue
		
		attribute_status = attribute_definition.get("status", "normal")
		attribute_type = attribute_definition.get("type")
		attribute_range = attribute_definition.get("range")

		if attribute_status == "normal" and (not "`" + attribute + "`" in link_map):
			qa.LogMissingDocumentation(config, type + "/" + attribute, ["No documentation for attribute"], "")

		if attribute_type == "body":
			if "`body " + attribute + "`" in link_map:
				attribute_type = "body [`%s`][body %s]" % (attribute, attribute)
			elif "`" + attribute + "`" in link_map:
				attribute_type = "body `%s`" % attribute
			else:
				attribute_type = "body `%s`" % attribute
				qa.LogMissingDocumentation(config, type + "/" + attribute, ["No documentation for body type"], "")
		elif attribute_type == "option":
			attribute_type = "one of `%s`" % attribute_range.replace(",", "`, `")
			attribute_range = None
		elif attribute_type == "context":
			attribute_type = "class expression"
		else:
			attribute_type = "`%s`" % attribute_type
		
		if attribute_status == "normal":
			attribute_status = ""
		else:
			attribute_status = "<sup>**%s**</sup>" % attribute_status
		
		line = "* `%s`%s: %s" % (attribute, attribute_status, attribute_type)
		if attribute_range:
			 line += " in range `%s`" % attribute_range
		lines.append(line + "\n")
	lines.append("\n")

	return lines

def document_syntax_map(tree, config):
	lines = []

	# JSON structure in `tree` is:
	# * type -> dict
	#     * status: normal|deprecated
	#     * attributes -> dict
	#         * attr_name -> dict
	#             * attribute: attr_name
	#             * status: normal|deprecated
	#             * type: int, string, slist...
	#             * range: regex
	#             * visibility: (ignored)
	
	# first, collect everything that all types have and call it "common"
	types = sorted(tree.keys())
	common_attributes = dict()
	if not "common" in types:
		try:
			common_attributes = copy.deepcopy(tree.get("classes").get("attributes"))
		except:
			print "cfdoc_macros: syntax_map - no promise type classes?!"
		for common_attribute in common_attributes.keys():
			type_count = 0
			for type in types:
				if tree.get(type).get("attributes").get(common_attribute):
					type_count += 1
			if type_count != len(types):
				del common_attributes[common_attribute]
	
		if len(common_attributes):
			common_definition = dict()
			common_definition["status"] = "normal"
			common_definition["attributes"] = common_attributes
			lines.append("### [Common Attributes][Promise Types and Attributes#Common Attributes]\n\n")
			lines.append(document_type("common", common_definition, [], config))
			
	excludes = common_attributes.keys()
	
	link_map = config["link_map"]
	for type in types:
		link = None
		if "`body " + type + "`" in link_map:
			# hack for classes, common and file bodies - see _reference.md
			link = "body " + type
		elif "`" + type + "`" in link_map:
			link = type
			
		if link:
			lines.append("### [%s][%s]\n\n" % (type, link))
		else:
			lines.append("### %s\n\n" % type)
			qa.LogMissingDocumentation(config, type, ["No documentation for type"], "")
		type_definition = tree.get(type)
		if type_definition == None:
			print "cfdoc_macros: syntax_map - no definition for type %s" % type
			continue
		lines.append(document_type(type, type_definition, excludes, config))
	
	return lines

def syntax_map(parameters, config):
	qa.LogProcessStart(config, "syntax_map for %s" % parameters[0])
	syntax_map = config["syntax_map"]
	if parameters != None:
		syntax_map = syntax_map[parameters[0]]
	
	lines = document_syntax_map(syntax_map, config)
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

def find_include_file(searchfile, searchpaths):
	for searchpath in searchpaths:
		filename = searchpath + "/" + searchfile
		if os.path.exists(filename):
			return filename
	return None

def load_include_file(filename):
	lines = list()
	in_file = open(filename, 'r')
	lines = in_file.readlines()
	if len(lines) == 0:
		print "load_include_file: File not found or can't open: " + searchfile
		print "       searching :"
		print "                  " + searchpaths
		return None
	return lines

def prune_include_lines(markdown_lines):
	# remove leading and trailing empty lines
	while markdown_lines[0].lstrip() == "":
		del markdown_lines[0]
	while markdown_lines[-1].lstrip() == "":
		del markdown_lines[-1]

	if len(markdown_lines):
		markdown_lines.insert(0, "\n```cf3\n")
		# if example ended with documentation, prune trailing code, else terminate block
		if markdown_lines[-1] != "\n```cf3\n":
			markdown_lines.append("```")
		else:
			del markdown_lines[-1]
	return markdown_lines

def include_example(parameters, config):
	filename = find_include_file(parameters[0], config["example_directories"])
	lines = load_include_file(filename)
	if lines == None:
		return ""
	
	markdown_lines = []
	skip_block = False
	in_documentation = False
	for line in lines:
		if skip_block == False:
			if line.find("#[%-%]") == 0:
				skip_block = True
				continue
			if line.find("#@ ") == 0:
				line = line[3:]
				if not in_documentation:
					markdown_lines.append("```\n\n")
					in_documentation = True
			elif in_documentation:
				markdown_lines.append("\n```cf3\n")
				in_documentation = False
			elif line[0] == '#':
				continue
			markdown_lines.append(line)
		if line.find("#[%+%]") == 0:
			skip_block = False

	prune_include_lines(markdown_lines)
	
	markdown_lines.append("\n")
	markdown_lines.append("This policy can be found in " )
	markdown_lines.append("`/var/cfengine/share/doc/examples/" + parameters[0] + "`")
	markdown_lines.append("\n")
	
	return markdown_lines

def include_snippet(parameters, config):
	filename = find_include_file(parameters[0], config["example_directories"])
	lines = load_include_file(filename)
	if lines == None:
		return ""
	
	begin = re.compile(parameters[1])
	end = re.compile(parameters[2])

	markdown_lines = []
	skip_block = True
	for line in lines:
		if skip_block == False:
			markdown_lines.append(line)
			if end.match(line) != None:
				 # if last line a comment, assume end-marker and skip
				if line[0] == "#":
					del markdown_lines[-1]
				break
		elif begin.match(line) != None:
			skip_block = False
			if line[0] != '#':
				markdown_lines.append(line)

	if not len(markdown_lines):
		print "Snippet not found: "
		print begin.pattern
		return list()
		
	return prune_include_lines(markdown_lines)

def library_include(parameters, config):
	markdown_lines = []
	policy_filename = parameters[0] + ".json"
	policy_json = config.get(policy_filename)
	html_name = config.get("context_current_html")
	if policy_json == None:
		policy_path = config["project_directory"] + "/_json/" + policy_filename
		if not os.path.exists(policy_path):
			print "cfdoc_macros:library_include: File does not exist: " + policy_path
			return markdown_lines
		
		policy_json = json.load(open(policy_path, 'r'))
		config[policy_filename] = policy_json
		
	qa.LogProcessStart(config, "library_include: %s" % policy_filename)
	
	# for all bundles and bodies...
	for key in policy_json.keys():
		element_list = policy_json[key]
		errorString = []
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
				print "cfdoc_macros:library_include: element without type: " + name
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
			sourceLines = []
			sourceLine = -1
			
			try:
				source_path = config["project_directory"] + "/" + element["sourcePath"]
				source_path = os.path.normpath(source_path)
				source_file = open(source_path, 'r')
				sourceLine = element["line"] - 1 # zero-based indexing
				sourceLines = source_file.readlines()[sourceLine:]
			except:
				print "cfdoc_macros:library_include: could not include code from " + name
			
			if len(sourceLines):
				headerLines = list()
				code_lines.append("\n```cf3\n")
				code_lines.append(sourceLines[0])
				del sourceLines[0]
				in_code = False
				
				for line in sourceLines:
					if not in_code:
						line = line.lstrip()
						if line.find("{") == 0:
							in_code = True
						else:
							headerLines.append(line)
					if in_code:
						code_lines.append(line)
						# super-naive parser...
						if line.find("}") == 0:
							break
				code_lines.append("\n```\n")
				
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
					else:
						errorString.append("Missing description")
					return_doc = documentation_dict.get("return", "")
					if len(return_doc):
						documentation_lines.append("**Return value:** ")
						documentation_lines.append(return_doc)
						documentation_lines.append("\n")
				else: # no header lines
					errorString.append("No documentation")
			else: # no source lines
				errorString.append("No source code or unable to read source code")

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
				if param_line == None:
					errorString.append("No documentation for parameter %s" % argument)
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
			if len(errorString):
				locationString = "in library `" + os.path.relpath(source_path) + "` (%d)" % sourceLine
				qa.LogMissingDocumentation(config, prototype, errorString, locationString)
				errorString = []

	if len(markdown_lines) == 0:
		print "cfdoc_macros:library_include: Failure to include " + parameters[0]
		
	return 	markdown_lines
