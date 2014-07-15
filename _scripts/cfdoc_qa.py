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
import sys
from time import gmtime, strftime

def initialize(config):
	config["log_file"] = config["markdown_directory"] + "/cfdoc_log.markdown"
	if os.path.exists(config["log_file"]):
		os.remove(config["log_file"])
	logfile = open(config["log_file"], "w")
	logfile.write("---\n")
	logfile.write("layout: printable\n")
	logfile.write("title: \"Documentation Issues\"\n")
	logfile.write("published: true\n")
	logfile.write("alias: cfdoc_log.html\n")
	logfile.write("---\n")
	logfile.write("\n")
	logfile.write("Documentation generated at %s GMT\n" % strftime("%Y-%m-%d %H:%M:%S", gmtime()))
	logfile.write("\n")
	logfile.write("# Logging\n")
	logfile.write("\n")
	logfile.close()


def OpenLogFile(config):
	logfile = open(config["log_file"], "a")
	return logfile

def LogProcessStart(config, string):
	logfile = OpenLogFile(config)
	logfile.write("\n")
	logfile.write("### %s\n" % string)
	logfile.write("\n")
	logfile.close()

def LogMissingDocumentation(config, element, strings, location):
	logfile = OpenLogFile(config)
	if not element.startswith("`"):
		element = "`%s`" % element
	logfile.write("* %s:\n" % element)
	if len(strings):
		logfile.write("    * Errors:\n")
	for string in strings:
		logfile.write("        * **%s**\n" % string)
	if len(location):
		logfile.write("    * Source location: `%s`\n" % location)
	logfile.write("    * Triggered by: `%s` (%d)\n" % (os.path.relpath(config["context_current_file"]), config["context_current_line_number"]))
	logfile.close()

def Log(config, string):
	# Prepend the error string as a general error without context of current process
	logfile = open(config["log_file"], 'r')
	original = logfile.readlines()
	logfile.close()

	logfile = open(config["log_file"], 'w')
	line_offset = 0
	for line in original:
		logfile.write(line)
		line_offset += 1
		if line == "# Logging\n":
			break

	logfile.write("\n* %s\n" % string)
	logfile.write("    * Triggered by: `%s` (%d)\n" % (os.path.relpath(config["context_current_file"]), config["context_current_line_number"]))
	print "%s (%d): %s" % (os.path.relpath(config["context_current_file"]), config["context_current_line_number"], string)

	logfile.writelines(original[line_offset:])
	logfile.close()
