---
layout: default
title: getenv
categories: [Reference, Functions, getenv]
published: true
alias: reference-functions-getenv.html
tags: [reference, functions, getenv]
---

**Prototype**: `getenv(variable, maxlength)`

**Return type**: `string`

**Description:** Return the environment variable `variable`, truncated at 
`maxlength` characters

Returns an empty string if the environment variable is not defined. 
`maxlength` is used to avoid unexpectedly large return values, which could 
lead to security issues. Choose a reasonable value based on the environment 
variable you are querying.


**Arguments**

* `variable` : Name of environment variable, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`
* `maxlength` : Maximum number of characters to read , in the range
`0,99999999999`

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

**History**: This function was introduced in CFEngine version 3.0.4
(2010)
