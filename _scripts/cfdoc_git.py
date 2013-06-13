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

REVISION = ""
BRANCH = "master"

def createData(docdir, linkfile):
	cwd = os.getcwd()

	try:
		os.chdir(docdir)
		configpath = os.path.dirname(linkfile) + "/_config.yml"
		if os.path.exists(configpath):
			git = os.popen("git rev-list -1 HEAD")
			while True:
				line = git.readline().rstrip()
				if line == '': break
				REVISION = line
			git.close()

			git = os.popen("git branch --no-color")
			while True:
				line = git.readline().rstrip()
				if line == '': break
				if line.find('*') == 0 and line.find('(') == -1:
					BRANCH = line.split(' ')[1].rstrip()

			print "cfdoc_git: Updating " + configpath + " with " + BRANCH + " at " + REVISION
			config = open(configpath, "a")
			if BRANCH != '':
				config.write("git-branch: \"" + BRANCH + "\"\n")
			if REVISION != '':
				config.write("git-revision: \"" + REVISION + "\"\n")
			config.close()
	except:
		print "cfdoc_git: Exception when setting revision"
		print "cfdoc_git: cwd = " + os.getcwd()

	os.chdir(cwd)

