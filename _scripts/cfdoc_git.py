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

def createData(config):
	configpath = config["config_path"]
	if not os.path.exists(configpath):
		print "cfdoc_git: \"_config.yml\" not found in " + configpath
		return

	cwd = os.getcwd()
	os.chdir(config["markdown_directory"])
	config["branch"] = "master"
	try:
		git = os.popen("git rev-list -1 HEAD")
		while True:
			line = git.readline().rstrip()
			if line == '': break
			config["revision"] = line
		git.close()
	except:
		print "cfdoc_git: Exception when reading revision"
		print "cfdoc_git: cwd = " + os.getcwd()
	
	branch = "master"
	try:
		git = os.popen("git branch --no-color")
		while True:
			line = git.readline().rstrip()
			if line == '': break
			if line.find('*') == 0 and line.find('(') == -1:
				branch = line.split(' ')[1].rstrip()
	except:
		print "cfdoc_git: Exception when reading current branch"

	config["branch"] = branch
	print "cfdoc_git: Updating " + configpath
	print "           branch   = \'" + config["branch"] + "\'"
	print "           revision = \'" + config.get("revision", "NOT FOUND!") + "\'"
	try:
		config_file = open(configpath, "a")
		config_file.write("git-branch: \"" + config.get("branch", "master") + "\"\n")
		if "revision" in config:
			config_file.write("git-revision: \"" + config["revision"] + "\"\n")
		config_file.close()
	except:
		print "cfdoc_git: Exception when updating " + configpath

	os.chdir(cwd)

