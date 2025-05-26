#!/usr/bin/python3

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
import cfdoc_codeblock_resolver as codeblock_resolver
import cfdoc_macros as macros
import cfdoc_git as git
import cfdoc_qa as qa
import cfdoc_patch_header_nav as patch_header_nav
import cfdoc_references_resolver as references_resolver
import cfdoc_shortcodes_resolver as shortcodes_resolver
import cfdoc_images_path_resolver as images_path_resolver
import sys
import os
import traceback

config = environment.validate(sys.argv[1])
qa.initialize(config)

try:
    metadata.run(config)
except:
    print("cfdoc_preprocess: Fatal error setting meta data")
    sys.stdout.write("       Exception: ")
    print(sys.exc_info())
    exit(2)

try:
    linkresolver.run(config)
except:
    print("cfdoc_preprocess: Fatal error generating link map")
    sys.stdout.write("       Exception: ")
    print(sys.exc_info())
    exit(3)

try:
    codeblock_resolver.run(config)
except:
    print("cfdoc_preprocess: Fatal error processing codeblocks")
    sys.stdout.write("       Exception: ")
    print(sys.exc_info())
    exit(3)

try:
    macros.run(config)
except:
    print("cfdoc_macros: Error generating documentation from syntax maps")
    sys.stdout.write("      Exception: ")
    print(sys.exc_info())

try:  # update the link map with content added by macros
    linkresolver.run(config)
except:
    print("cfdoc_preprocess: Fatal error updating link map")
    sys.stdout.write("       Exception: ")
    print(sys.exc_info())
    exit(4)

# generate links to known targets
linkresolver.apply(config)

try:
    patch_header_nav.patch(sys.argv[1])
except:
    print("cfdoc_patch_header_nav: Error patching header navigation")
    sys.stdout.write("      Exception: ")
    print(sys.exc_info())
    
try:
    references_resolver.run(config)
except:
    print("cfdoc_references_resolver: Fatal error resolving references")
    sys.stdout.write("       Exception: ")
    traceback.print_exc()
    exit(3)

try:
    shortcodes_resolver.run(config)
except:
    print("cfdoc_shortcodes_resolver: Fatal error resolving shortcodes replacement")
    sys.stdout.write("       Exception: ")
    print(sys.exc_info())
    exit(3)

try:
    images_path_resolver.run(config)
except:
    print("images_path_resolver: Fatal error resolving images paths")
    sys.stdout.write("       Exception: ")
    print(sys.exc_info())
    exit(3)

exit(0)
