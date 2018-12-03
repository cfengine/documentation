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
import cfdoc_metadata as metadata
import cfdoc_linkresolver as linkresolver
import cfdoc_macros as macros
import cfdoc_printsource as printsource
import cfdoc_git as git
import cfdoc_qa as qa
import cfdoc_patch_header_nav as patch_header_nav
import sys
import os

config = environment.validate(sys.argv[1])
qa.initialize(config)

try:
	metadata.run(config)
except:
	print "cfdoc_preprocess: Fatal error setting meta data"
	sys.stdout.write("       Exception: ")
	print sys.exc_info()
	exit(2)

try:
	linkresolver.run(config)
except:
	print "cfdoc_preprocess: Fatal error generating link map"
	sys.stdout.write("       Exception: ")
	print sys.exc_info()
	exit(3)

try:
	macros.run(config)
except:
	print "cfdoc_macros: Error generating documentation from syntax maps"
	sys.stdout.write("      Exception: ")
	print sys.exc_info()

try: # update the link map with content added by macros
	linkresolver.run(config)
except:
	print "cfdoc_preprocess: Fatal error updating link map"
	sys.stdout.write("       Exception: ")
	print sys.exc_info()
	exit(4)

# generate links to known targets
linkresolver.apply(config)

# create printable sources from completely pre-processed markdown

try:
	printsource.run(config)
except:
	print "cfdoc_printsource: Error generating print-pages"
	sys.stdout.write("      Exception: ")
	print sys.exc_info()

try:
	patch_header_nav.patch(sys.argv[1])
except:
	print "cfdoc_patch_header_nav: Error patching header navigation"
	sys.stdout.write("      Exception: ")
	print sys.exc_info()

exit(0)
