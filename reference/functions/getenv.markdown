---
layout: default
title: getenv
categories: [Reference, Functions, getenv]
published: true
alias: reference-functions-getenv.html
tags: [reference, system functions, functions, getenv]
---

[%CFEngine_function_prototype(variable, maxlength)%]

**Description:** Return the environment variable `variable`, truncated at 
`maxlength` characters

Returns an empty string if the environment variable is not defined. 
`maxlength` is used to avoid unexpectedly large return values, which could 
lead to security issues. Choose a reasonable value based on the environment 
variable you are querying.

[%CFEngine_function_attributes(variable, maxlength)%]

**Example:**

```cf3
bundle agent example
{
vars:

   "myvar" string => getenv("PATH","20");

classes:

  "isdefined" not => strcmp("$(myvar)","");

reports:

  isdefined::

   "The path is $(myvar)";

  !isdefined::

   "The named variable PATH does not exist";

}
```

**Notes:**  

**History:** This function was introduced in CFEngine version 3.0.4
(2010)
