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
import cfdoc_linkresolver as linkresolver

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
	
	new_pages = dict()
	print_pages(pagetree, 1, None, new_pages)
	for new_page in new_pages.keys():
		headers = new_pages[new_page]
		in_file = open(new_page, 'r')
		lines = in_file.readlines()
		in_file.close()
		
		out_file = open(new_page, 'w')
		for line in lines:
			if line.find("alias:") == 0:
				alias = line[line.find(':') + 1:].lstrip().rstrip()
				out_file.write(line)
			elif line.find("[%CFEngine_TOC%]") == 0:
				out_file.write("# Table of Content\n")
				out_file.write("\n")
				first = True
				for header in headers:
					level = header.find(' ') - 1
					if level > 3 or level < 1:
						continue
					header = header[level + 2:]
					
					 # make sure we start with a proper list
					if first and level > 1:
						level = 1
					if alias != None:
						entry = " " * ((level - 1) * 4) + "* [" + header + "]"
						entry += "("+ alias + "#" + linkresolver.headerToAnchor(header) + ")"
					else:
						entry = header
					out_file.write(entry + "\n")
					first = False
			else:
				out_file.write(line)
		out_file.close()

def print_pages(pages, level, out_file, new_pages):
	sorted_pages = sorted(pages.childlist, key=lambda page: page.sorting)
	for page in sorted_pages:
		if page == None:
			continue
		if level == 1:
			out_filename = page.source_filename
			out_filename = out_filename.replace(".markdown", "-printable.markdown")
			new_pages[out_filename] = list()
			out_file = open(out_filename, "w")
			out_file.write("---\n")
			out_file.write("layout: printable\n")
			out_file.write("title: \"The Complete " + page.title + "\"\n")
			out_file.write("published: true\n")
			out_file.write("alias: %s-printable.html\n" % page.alias[:page.alias.rfind('.')])
			out_file.write("---\n")
			out_file.write("\n")
			out_file.write("[%CFEngine_TOC%]\n")
			out_file.write("\n")
		else:
			title = "#" * level
			title += " " + page.title
			out_file.write(title + "\n\n")
			new_pages[out_file.name].append(title)
		
		new_pages[out_file.name] += print_page(page.source_filename, out_file, level)
		
		print_pages(page, level +1, out_file, new_pages)

def print_page(page_file, out_file, level):
	in_file = open(page_file, 'r')
	lines = in_file.readlines()
	
	out_file.write("<!--- Begin include: `" + page_file + "` -->\n")
	
	headers = list()
	in_body = True
	in_code = False
	for line in lines:
		if line[:3] == '---':
			in_body = not in_body
			continue
		if line[:3] == '```':
			in_code = not in_code
			out_file.write(line)
			continue
		if in_body:
			if not in_code:
				if line[0] == '#': # increase indent level for header in page, up to 4 more levels
					line = '#' * max(level - 1, 4) + line
					if (line.find("exclude-from-toc") == -1 and line.rstrip()[-1] != '#'):
						headers.append(line.lstrip().rstrip())
			out_file.write(line)

	out_file.write("\n")
	out_file.write("<!--- End include: `" + page_file + "` -->\n")	
	out_file.write("\n")
	return headers
