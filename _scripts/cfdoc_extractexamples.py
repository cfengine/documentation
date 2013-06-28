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

# Usage:
# - Put [%examplefile%] as a placeholder into a markdown source
# - point environment variable CFDOC_EXAMPLEPATH to the location of the file
# - put [%+] and [%-] markers into the example file to include/exclude blocks
#   default is exclude so that license headers are automatically skipped
# - for each occurance of [%examplefile%], the next code block is injected

import os

def run(config):
	markdown_files = config["markdown_files"]
	for file in markdown_files:
		processFile(file, config)

def terminateBlock(lines):
	if lines[-1] != '\n': lines += '\n'
	lines += '```\n'
	
def processFile(markdown, config):
	markdown_file = open(markdown, 'r')
	markdown_lines = markdown_file.readlines()
	markdown_file.close()

	markdown_dir = os.path.dirname(markdown)
	markdown_name = os.path.basename(markdown)

	write_changes = False
	new_markdown_lines = []
	example_lines = []
	example_idx = 0
	in_pre = False
	terminate_block = False
	begin_block = True
	for line in markdown_lines:
		keepline = True
		# skip markdown codeblocks
		if line.lstrip()[:3] == '```':
			in_pre = not in_pre
		if not in_pre and line.find("[%CFEngine_include(") == 0:
			# out of previous example source, read next
			if (example_idx == len(example_lines)):
				parameters = line[line.find("(")+1:line.find(")%]")]
				parameters = parameters.replace(" ", "")
				parameters = parameters.split(",")
				example = parameters[0]
				example_lines = include(parameters, config)
				example_idx = 0
			
			# write example until next stop marker [%-]
			if len(example_lines) > example_idx:
				keepline = False
				write_changes = True
				if begin_block:
					new_markdown_lines += '```cf3\n'
				while len(example_lines) > example_idx:
					example_line = example_lines[example_idx]
					example_idx += 1
					if example_line.find("#[%-]") == 0:
						example_idx += 1
						terminate_block = True
						begin_block = False
						break
					new_markdown_lines += "    " + example_line
				
				# end of example or rest is skipped?
				if (len(example_lines[example_idx:]) == 0):
					terminateBlock(new_markdown_lines)
					terminate_block = False
					new_markdown_lines.append("\n")
					new_markdown_lines.append("This policy can be found in ")
					new_markdown_lines.append("`/var/cfengine/share/doc/examples/" + example + "`")
					new_markdown_lines.append("\n")
					example_idx = len(example_lines)
					
		if keepline == True:
			# terminate code block
			if terminate_block:
				terminateBlock(new_markdown_lines)
				terminate_block = False
				begin_block = True
			new_markdown_lines += line
			
	if write_changes == True:
		new_markdown_filename = markdown_dir + "/new_" + markdown_name
		new_markdown_file = open(new_markdown_filename, 'w')
		for line in new_markdown_lines:
			new_markdown_file.write(line)
		new_markdown_file.close()
		os.rename(new_markdown_filename,markdown)
			
def include(parameters, config):
	lines = []
	example_directories = config["example_directories"]
	for example_directory in example_directories:
		example = example_directory + "/" + parameters[0]
		if os.path.exists(example):
			example_file = open(example, 'r')
			lines = example_file.readlines()
		
	if len(lines) == 0:
		print "cfdoc_extractexamples: File not found or can't open: " + parameters[0]
		print "                       searching :"
		for dir in example_directories:
			print "                                  " + dir
		return lines
	
		
	markdown_lines = []
	skip_block = True
	for line in lines:
		if skip_block == False:
			markdown_lines.append(line)
		if line.find("#[%+]") == 0:
			skip_block = False
		elif line.find("#[%-]") == 0:
			skip_block = True
			
	return markdown_lines
