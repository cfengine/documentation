---
layout: default
title: classesmatching
categories: [Reference, Functions, classesmatching]
published: true
alias: reference-functions-classesmatching.html
tags: [reference, utility functions, functions, classesmatching]
---

[%CFEngine_function_prototype(regex, tag1, tag2, ...)%]

**Description:** Return the list of set classes matching `regex` and any tags given.

This function searches for the [unanchored][unanchored] regular expression in 
the list of currently set classes (in order hard, then soft, then local to the 
current bundle).

When any tags are given, only the classes with those tags are returned.

[%CFEngine_function_attributes(regex, tag1, tag2, ...)%]

**Example:**  


```cf3
body common control
{
      bundlesequence => { run };
}

bundle agent run
{
  vars:
      "all" slist => classesmatching(".*");
      "c" slist => classesmatching("cfengine");
      "c_plus_plus" slist => classesmatching("cfengine", "plus");
  reports:
      "All classes = $(all)";
      "Classes matching 'cfengine' = $(c)";
      "Classes matching 'cfengine' with the 'plus' tag = $(c_plus_plus)";
}

```

Output:

```
R: All classes = Sunday
R: All classes = GMT_Yr2013
R: All classes = compiled_on_linux_gnu
R: All classes = ipv4_10_132_51
R: All classes = GMT_Hr01_Q1
R: All classes = ipv4_10_132
R: All classes = GMT_Min01
R: All classes = localhost
R: All classes = GMT_Night
R: All classes = GMT_Q1
R: All classes = Hr03
R: All classes = Lcycle_0
R: All classes = ipv4_127_0_0_1
R: All classes = x86_64
R: All classes = debian_7_0
R: All classes = cfengine_3_6
R: All classes = Day15
R: All classes = GMT_December
R: All classes = cfengine_3_6_0a1
R: All classes = Hr03_Q1
R: All classes = ipv4_127_0_0
R: All classes = cfengine_3
.
.
.
R: All classes = have_aptitude
R: Classes matching 'cfengine' = cfengine
```


**Note**: This function replaces the `allclasses.txt` static file available
in older versions of CFEngine.

**History:** Introduced in CFEngine 3.6
