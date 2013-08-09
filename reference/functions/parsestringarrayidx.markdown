---
layout: default
title: parsestringarrayidx
categories: [Reference, Functions, parsestringarrayidx]
published: true
alias: reference-functions-parsestringarrayidx.html
tags: [reference, io functions, functions, parsestringarrayidx]
---

[%CFEngine_function_prototype(array, input, comment, split, maxentries, maxbytes)%]

**Description:** Populates the two-dimensional array `array` with up to 
`maxentries` fields from the first `maxbytes` bytes of the string `input`.

This function mirrors the exact behavior of `readstringarrayidx()`, but
reads data from a variable instead of a file. By making data readable from a variable, data driven policies can be kept inline.

[%CFEngine_function_attributes(array, input, comment, split, maxentries, maxbytes)%]

**Example:**

```cf3
    bundle agent test(f) 
    {
    vars:
      # Define data inline for convenience
      "table"   string => "one: a
                           two: b
                         three: c";

    #######################################

     "dim" int => parsestringarrayidx(
                      "items",
                      "$(table)",
                      "\s*#[^\n]*",
                      ":",
                      "1000",
                      "200000"
                      );

     "keys" slist => getindices("items");

    reports:
        "$(keys)";
    }
```

**History:** Was introduced in version 3.1.5, Nova 2.1.0 (2011)
