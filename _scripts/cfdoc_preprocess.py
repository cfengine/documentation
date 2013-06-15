#!/usr/bin/python

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

import cfdoc_environment as environment
import cfdoc_linkresolver as linkresolver
import cfdoc_extractexamples as extractexamples
import cfdoc_syntaxmap as syntaxmap
import cfdoc_git as git

config = environment.validate()
try:
	git.createData(config)
except:
	print "cfdoc_preprocess: Fatal error generating git tags"
	exit(1)

try:
	linkresolver.processDirectory(config["markdown_directory"],config["reference_path"],"")
except:
	print "cfdoc_preprocess: Fatal error generating link map"
	exit(2)

try:
	if (config["example_directory"] != ""):
		extractexamples.run(config)
except:
	print "cfdoc_preprocess: Fatal error extracting example code"
	exit(3)

#try:
syntaxmap.run(config)
#except:
#print "cfdoc_syntaxmap: Fatal error generating syntax maps"
#exit(4)

exit(0)
