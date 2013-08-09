---
layout: default
title: hubknowledge
categories: [Reference, Functions, hubknowledge]
published: true
alias: reference-functions-hubknowledge.html
tags: [reference, communication functions, functions, hubknowledge]
---

**This function is only available in CFEngine Enterprise.**

[%CFEngine_function_prototype(id)%]

**Description:** Read global knowledge from the CFEngine Database host by 
`id`.

This function is only available in CFEngine Enterprise. It is intended for use 
in distributed orchestration. It is recommended that you use this function 
sparingly with *guards*, as it contributes to network traffic and depends on 
the network for its function. Unlike `remotescalar()`, the value of 
`hubknowledge` is not cached.

This function behaves similarly to the `remotescalar` function, except that it 
always gets its information from the CFEngine Database by an encrypted 
connection. It is designed for spreading globally calibrated information about 
a CFEngine system back to the client machines. The data available through this 
channel are generated automatically by discovery, unlike `remotescalar` which 
accesses user defined data.

This function asks for an identifier. It is up to the server to interpret what 
this means and to return a value of its choosing. If the identifier matches a 
persistent scalar variable (such as is used to count distributed processes in 
CFEngine Enterprise) then this will be returned preferentially. If no such 
variable is found, then the server will look for a literal string in a server 
bundle with a handle that matches the requested object.

[%CFEngine_function_attributes(id)%]

**Example:**

```cf3
    vars:

      guard::

       "global_number" string => hubknowledge("number_variable");
```

