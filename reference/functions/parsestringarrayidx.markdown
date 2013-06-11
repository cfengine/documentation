---
layout: default
title: parsestringarrayidx
categories: [Reference, Functions, parsestringarrayidx]
published: true
alias: reference-functions-parsestringarrayidx.html
tags: [reference, io functions, functions, parsestringarrayidx]
---

**Prototype:** `parsestringarrayidx(array, input, comment, split, maxentries, maxbytes)`

**Return type:** `int`

**Description:** Populates the two-dimensional array `array` with up to 
`maxentries` fields from the first `maxbytes` bytes of the string `input`.

This function mirrors the exact behavior of `readstringarrayidx()`, but
reads data from a variable instead of a file. By making data readable from a variable, data driven policies can be kept inline.

**Arguments**:

* `array` : Array identifier to populate, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`
* `input` : A string to parse for input data, in the range `"?(/.*)`
* `comment` : Regex matching comments, in the range `.*`
* `split` : Regex to split data, in the range `.*`
* `maxentries` : Maximum number of entries to read, in the range
`0,99999999999`
* `maxbytes` : Maximum bytes to read, in the range `0,99999999999`   

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
      cfengine_3::
        "$(keys)";
    }
```

**History:** Was introduced in version 3.1.5, Nova 2.1.0 (2011)
