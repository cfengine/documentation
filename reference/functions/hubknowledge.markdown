---
layout: default
title: hubknowledge
published: true
tags: [reference, communication functions, functions, hubknowledge, cached function]
---

**This function is only available in CFEngine Enterprise.**

[%CFEngine_function_prototype(id)%]

**Description:** Read global knowledge from the CFEngine Database host by
`id`.

This function allows for is intended for use in distributed orchestration.
If the identifier matches a persistent scalar variable (such as is used to
count distributed processes in CFEngine Enterprise) then this will be returned
preferentially. If no such variable is found, then the server will look for a
literal string in a server bundle with a handle that matches the requested object.

It is recommended that you use this function sparingly, using classes as guards,
as it contributes to network traffic and depends on the network for its function.
Unlike `remotescalar()`, the result of `hubknowledge()` is not stored locally.

This function behaves similarly to the `remotescalar()` function, except that it
always gets its information from the CFEngine Enterprise Database by an encrypted
connection. It is designed for spreading globally calibrated information about
a CFEngine system back to the client machines. The data available through this
channel are generated automatically by discovery, unlike `remotescalar` which
accesses user defined data.


[%CFEngine_function_attributes(id)%]

**Example:**

```cf3
    vars:

      guard::

       "global_number" string => hubknowledge("number_variable");
```

**See also:** `remotescalar()`, `remoteclassesmatching()`, `hostswithclass()`
