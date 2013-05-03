---
layout: default
title: Function-registryvalue
categories: [Special-functions,Function-registryvalue]
published: true
alias: Special-functions-Function-registryvalue.html
tags: [Special-functions,Function-registryvalue]
---

### Function registryvalue

**Synopsis**: registryvalue(arg1,arg2) returns type **string**

\
 *arg1* : Windows registry key, *in the range* .\* \
 *arg2* : Windows registry value-id, *in the range* .\* \

Returns a value for an MS-Win registry key,value pair

**Example**:\
 \

~~~~ {.verbatim}
bundle agent reg
{
vars:

  "value" string => registryvalue("HKEY_LOCAL_MACHINE\SOFTWARE\CFEngine AS\CFEngine","value3");

reports:

  windows::

   "Value extracted: $(value)";

}
~~~~

**Notes**:\
 \

This function applies only to Windows-based systems. It reads a data
field for the value named in the second argument, which lies within the
registry key given by the first argument.

The value is parsed as a string. Currently values of type `REG_SZ`
(string), `REG_EXPAND_SZ` (expandable string) and `REG_DWORD` (double
word) are supported.
