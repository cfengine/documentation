---
layout: default
title: File Template Examples
published: true
sorting: 7
tags: [Examples]
---

* [Templating][File Template Examples#Templating]

## Templating

With CFEngine you have a choice between editing `deltas' into files or distributing more-or-less finished templates. Which method you should choose depends should be made by whatever is easiest.

    If you are managing only part of the file, and something else (e.g. a package manager) is managing most of it, then it makes sense to use CFEngine file editing.
    If you are managing everything in the file, then it makes sense to make the edits by hand and install them using CFEngine. You can use variables within source text files and let CFEngine expand them locally in situ, so that you can make generic templates that apply netwide.

Example template:


[%CFEngine_include_snippet(templating.cf, .* )%]


To copy and expand this template, you can use a pattern like this:


[%CFEngine_include_snippet(templating_1.cf, .* )%]

The the following driving code (based on `copy then edit') can be placed in a library, after configuring to your environmental locations:

[%CFEngine_include_snippet(templating_1.cf, .* )%]
