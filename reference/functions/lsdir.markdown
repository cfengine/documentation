---
layout: default
title: lsdir
categories: [Reference, Functions, lsdir]
published: true
alias: reference-functions-lsdir.html
tags: [reference, files functions, functions, lsdir]
---

[%CFEngine_function_prototype(path, regex, include_base)%]

**Description:** Returns a list of files in the directory `path` matching the regular expression `regex`.

If `include_base` is true, full paths are returned, otherwise only names 
relative to the the directory are returned.

[%CFEngine_function_attributes(path, regex, include_base)%]

**Example:**

```cf3
    vars:
      "listfiles" slist => lsdir("/etc", "(passwd|shadow).*", "true");
```

**Notes:**  
   
 **History:** Was introduced in 3.3.0, Nova 2.2.0 (2011)

