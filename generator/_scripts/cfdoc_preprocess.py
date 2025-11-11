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
import cfdoc_macros as macros
import cfdoc_git as git
import cfdoc_qa as qa
import cfdoc_patch_header_nav as patch_header_nav
import cfdoc_references_resolver as references_resolver
import cfdoc_shortcodes_resolver as shortcodes_resolver
import cfdoc_images_path_resolver as images_path_resolver
import cfdoc_codeblock_resolver as codeblock_resolver
import sys
import os

config = environment.validate(sys.argv[1])
qa.initialize(config)

metadata.run(config)
linkresolver.run(config)
macros.run(config)
linkresolver.run(config)
# generate links to known targets
linkresolver.apply(config)
patch_header_nav.patch(sys.argv[1], sys.argv[2])
references_resolver.run(config)
shortcodes_resolver.run(config)
images_path_resolver.run(config)
codeblock_resolver.run(config)
