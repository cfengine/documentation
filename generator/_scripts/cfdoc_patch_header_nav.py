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

import urllib.request, urllib.parse, urllib.error
import json
import sys


def patch(current_branch):
    url = "https://docs.cfengine.com/docs/branches.json"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    with open("_includes/header_nav_options.html", "w") as f:
        for branch in data["docs"]:
            if (
                "(LTS)" not in branch["Title"]
                and branch["Version"] != "master"
                and branch["Version"] != current_branch
            ):
                continue
            selected = ""
            link = branch["Link"]
            if branch["Version"] == current_branch:
                selected = ' selected="selected"'
                link = "javascript:void(0);"
            print(
                '<a onclick="selectVersion(\'%s\')" href="#"%s>%s</a>'
                % (link, selected, branch["Title"].replace("Version ", "")),
                file=f,
            )
        print('<a href="/versions/">view all versions</a>', file=f)

    with open("_includes/versions_list.html", "w") as f:
        for branch in data["docs"]:
            print(
                '<li><a href="%s">%s</a></li>'
                % ("../../.." + branch["Link"], branch["Title"].replace("Version ", "")),
                file=f,
            )
    with open("_includes/lts_versions_list.html", "w") as f:
        for branch in data["docs"]:
            if "(LTS)" in branch["Title"]:
                print(
                    '<li><a href="%s">%s</a></li>'
                    % (
                        "../.." + branch["Link"],
                        branch["Title"].replace("Version ", "CFEngine "),
                    ),
                    file=f,
                )
