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
body common control
{
      bundlesequence => { "example" };
}

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

Output:

```
R: canonified component == _var_cfengine_bin_cf_serverd
R: component exists in /var/cfengine/bin/cf-serverd
```

**See also:** [classify()][classify], `canonifyuniquely`.
