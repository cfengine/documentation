---
layout: default
title: registryvalue
categories: [Reference, Functions, registryvalue]
published: true
alias: reference-functions-registryvalue.html
tags: [reference, functions, registryvalue]
---

**Prototype**: `registryvalue(key, valueid)`

**Return type**: `string`

**Description**: Returns the value of `valueid` in the Windows registry key 
`key`.

This function applies only to Windows-based systems. The value is parsed as a 
string.

**Arguments**:

* `key` : Windows registry key, *in the range* .\*
* `value-id` : Windows registry value-id, *in the range* .\*

**Example**:

```cf3
    bundle agent reg
    {
    vars:

      "value" string => registryvalue("HKEY_LOCAL_MACHINE\SOFTWARE\CFEngine AS\CFEngine","value3");

    reports:

      windows::

       "Value extracted: $(value)";

    }
```

**Notes**: Currently values of type `REG_SZ` (string), `REG_EXPAND_SZ` 
(expandable string) and `REG_DWORD` (double word) are supported.
