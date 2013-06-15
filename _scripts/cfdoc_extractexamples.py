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
	processDirectory(config["markdown_directory"], "", config)

def processDirectory(cur_name,cur_dir, config):
	if os.path.isdir(cur_name) == True:
		markdownfiles = os.listdir(cur_name)	
		for file_name in markdownfiles:
			if os.path.isdir(cur_name+"/"+file_name) == True:
				processDirectory(cur_name+"/"+file_name,cur_dir+"/"+file_name, config)
			elif os.path.isdir(file_name) == False and ".markdown" in file_name:
				processFile(cur_name+"/"+file_name, config)

def terminateBlock(lines):
	if lines[-1] != '\n': lines += '\n'
	lines += '```\n'
	

def processFile(markdown, config):
	example_dir = config["example_directory"]

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
		if line[:3] == '```':
			in_pre = not in_pre
		if not in_pre and line.find("[%") == 0:
			# out of previous example source, read next
			if (example_idx == len(example_lines)):
				example = line[2:line.find("%]")]
				example_lines = readExample(example_dir + "/" + example)
			
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
			
def readExample(example):
	markdown_lines = []
	
	try:
		example_file = open(example, 'r')
	except:
		print "cfdoc_extractexamples: File not found or can't open " + example
		return markdown_lines
		
	lines = example_file.readlines()	
	print "Injecting " + example
	skip_block = True
	for line in lines:
		if skip_block == False:
			markdown_lines.append(line)
		if line.find("#[%+]") == 0:
			skip_block = False
		elif line.find("#[%-]") == 0:
			skip_block = True
			
	return markdown_lines
