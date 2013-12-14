---
layout: default
title: canonify
categories: [Reference, Functions, canonify]
published: true
alias: reference-functions-canonify.html
tags: [reference, data functions, functions, canonify]
---

[%CFEngine_function_prototype(text)%]

**Description:** Convert an arbitrary string `text` into a legal class name.

This function turns arbitrary text into class data.

[%CFEngine_function_attributes(text)%]

**Example:**  


```cf3
bundle agent example
{
    vars:
     "component" string => "/var/cfengine/bin/cf-serverd";
     "canon" string => canonify("$(component)");

    classes:
     "$(component)_exists" expression => fileexists("$(component)");

    reports:
     "canonified component == $(canon)";
     "component exists in $(component)"
       ifvarclass => canonify("$(component)_exists");
}

```

**See also:** [classify()][classify], `canonifyuniquely`.
