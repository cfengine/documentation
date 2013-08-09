---
layout: default
title: registryvalue
categories: [Reference, Functions, registryvalue]
published: true
alias: reference-functions-registryvalue.html
tags: [reference, system functions, functions, registryvalue]
---

[%CFEngine_function_prototype(key, valueid)%]

**Description:** Returns the value of `valueid` in the Windows registry key 
`key`.

This function applies only to Windows-based systems. The value is parsed as a 
string.

[%CFEngine_function_attributes(key, valueid)%]

**Example:**

```cf3
    bundle agent reg
    {
    vars:
      windows::
        "value" string => registryvalue("HKEY_LOCAL_MACHINE\SOFTWARE\CFEngine AS\CFEngine","value3");

    reports:
       "Value extracted: $(value)";

    }
```

**Notes:** Currently values of type `REG_SZ` (string), `REG_EXPAND_SZ` 
(expandable string) and `REG_DWORD` (double word) are supported.
