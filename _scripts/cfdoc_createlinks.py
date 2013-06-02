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


import cfdoc_linkresolver as linkresolver
import os

#####################################################################
# BASIC USAGE INSTRUCTIONS                                          #
#####################################################################
#                                                                   #
# To use this script you will need to set two environment variables.#
#                                                                   #
# 1. CFDOC_DIRNAME, which represents the directory where the script #
#    can find markdown files.                                       #
#                                                                   #
# 2. CFDOC_LINKFILE, which is the output file that will contain the #
#    link information for all the files under CFDOC_DIRNAME.        #
#                                                                   #
#####################################################################
#                                                                   #
# To set the variables manually, do the following:                  #
#                                                                   #
# > CFDOC_DIRNAME="/path/to/doc/dir"                                #
# > export CFDOC_DIRNAME'                                           #
# > CFDOC_LINKFILE="/path/to/link/file/_references.md"              #
# > export CFDOC_LINKFILE'                                          #
#                                                                   #
# Running the script is then as easy as entering the following on   #
# the command line:                                                 #
#                                                                   #
# > /path/to/this/script/cfdoc_createlinks.py'                      #
#                                                                   #
#####################################################################
#                                                                   #
# *** IMPORTANT NOTE ***                                            #
#                                                                   #
# For usage with the Jekyll plugin                                  #
# https://github.com/olov/jekyll-references, CFDOC_LINKFILE should  # 
# be defined as follows:                                            #
#                                                                   #
#                                                                   #
# > CFDOC_LINKFILE=$CFDOC_DIRNAME"/_references.md"	                 #
#                                                                   #
#####################################################################

CFDOC_LINKFILE=os.environ.get('CFDOC_LINKFILE')
CFDOC_DIRNAME=os.environ.get('CFDOC_DIRNAME')

if CFDOC_LINKFILE == None or CFDOC_DIRNAME == None:
	
	print 'Please set environment variables and retry. Example:'
	print '> CFDOC_LINKFILE="/path/to/link/file"'
	print '> export CFDOC_LINKFILE'
	print '> CFDOC_DIRNAME="/path/to/doc/dir"'
	print '> export CFDOC_DIRNAME'
	print '> /path/to/this/script/cfdoc_createlinks.py'
	exit(1)
else:	

	os.system("rm "+CFDOC_LINKFILE)
	linkresolver.createLinkFile(CFDOC_DIRNAME,CFDOC_LINKFILE,"")
	exit(0)
