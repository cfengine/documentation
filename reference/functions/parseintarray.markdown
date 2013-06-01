---
layout: default
title: parseintarray
categories: [Reference, Functions, parseintarray]
published: true
alias: reference-functions-parseintarray.html
tags: [reference, functions, parseintarray]
---

**Prototype**: `parseintarray(array, input, regex, split, maxentires, maxbytes)`

**Return type**: `int`

**Description**: Reads up to `maxentries` integers from the first `maxbytes` 
bytes in string `input` into `array` and returns the dimension.

This function mirrors the exact behavior of `readintarray()`, but reads
data from a variable instead of a file. By making data readable from a
variable, data driven policies can be kept inline.

**Arguments**:

* `array` : Array identifier to populate, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+
* `input` : A string to parse for input data, *in the range* "?(/.\*)
* `regex` : Regex matching comments, *in the range* .\*
* `split` : Regex to split data, *in the range* .\*
* `maxentries` : Maximum number of entries to read, *in the range*
0,99999999999
* `maxbyes` : Maximum bytes to read, *in the range* 0,99999999999

**Example**:

```cf3
    bundle agent test(f) 
    {
      vars:
         # Define data inline for convenience
        "table"   string => 
          "1:2
          3:4
          5:6";

       "dim" int => parseintarray(
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

**History**: Was introduced in version 3.1.5a1, Nova 2.1.0 (2011)
