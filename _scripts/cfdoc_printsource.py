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

class Page:
	def __init__(self):
		self.title = str()
		self.parent = None
		self.childtrees = dict()
		self.childlist = list()
		self.sorting = None
		self.source_filename = None

def run(config):
	markdown_files = config["markdown_files"]
	pagetree = Page()
	for markdown_file in markdown_files:
		in_file = open(markdown_file, 'r')
		lines = in_file.readlines()
		in_file.close()
		
		in_header = False
		publish = False
		sorting = -1
		title = str()
		alias = str()
		categories = list()
		for line in lines:
			if line[:3] == '---':
				if in_header:
					break;
				in_header = True
			if in_header:
				line = line.lstrip().rstrip()
				if line.find('categories: [') == 0:
					categories = line[line.find('[') + 1:line.find(']')].split(",")
				elif line.find('title: ') == 0:
					title = line[line.find(':') + 1:].lstrip().rstrip()
				elif line.find('alias: ') == 0:
					alias = line[line.find(':') + 1:].lstrip().rstrip()
				elif line.find('published: true') == 0:
					publish = True
				elif line.find('sorting: ') == 0:
					sortstring = line[9:]
					if sortstring.isdigit(): sorting = int(sortstring)
		
		if publish and len(categories) > 0:
			child = pagetree
			count = len(categories)
			for category in categories:
				category = category.lstrip().rstrip()
				parent = child
				child = parent.childtrees.get(category)
				if child == None: # new branch
					child = Page()
					child.parent = parent
					parent.childtrees[category] = child
					parent.childlist.append(child)
				if count == 1: # node
					child.title = title
					child.alias = alias
					child.source_filename = markdown_file
					child.sorting = sorting
				count -= 1
	
	print_pages(pagetree, 1, None)

def print_pages(pages, level, out_file):
	sorted_pages = sorted(pages.childlist, key=lambda page: page.sorting)
	for page in sorted_pages:
		if page == None:
			continue
		if level == 1:
			out_filename = page.source_filename
			out_filename = out_filename.replace(".markdown", "-printsource.markdown")
			out_file = open(out_filename, "w")
			out_file.write("---\n")
			out_file.write("layout: default\n")
			out_file.write("title: \"The Complete " + page.title + "\"\n")
			out_file.write("categories: [Printable, " + page.title + "]\n") 
			out_file.write("published: true\n")
			out_file.write("alias: printable-" + page.alias + "\n")
			out_file.write("---\n")
			out_file.write("\n")
		else:
			title = "#" * level
			title += " " + page.title
			out_file.write(title + "\n")
		
		print_page(page.source_filename, out_file, level)
		
		if len(page.childlist) > 0:
			print_pages(page, level +1, out_file)

def print_page(page_file, out_file, level):
	in_file = open(page_file, 'r')
	lines = in_file.readlines()
	
	out_file.write("<!--- Begin include: `" + page_file + "` -->\n")
	
	in_body = True
	for line in lines:
		if line[:3] == '---':
			in_body = not in_body
			continue
		if in_body:
			if line[0] == '#': # increase indent level for header in page
				line = '#' * (level - 1) + line
			out_file.write(line)

	out_file.write("\n")
	out_file.write("<!--- End include: `" + page_file + "` -->\n")	
	out_file.write("\n")
