---
layout: default
title: splitstring
categories: [Reference, Functions, splitstring]
published: true
alias: reference-functions-splitstring.html
tags: [reference, data functions, functions, splitstring]
---

[%CFEngine_function_prototype(string, regex, maxent)%]

**Description:** Splits `string` into at most `maxent` substrings wherever 
`regex` occurs, and  returns the list with those strings.

The regular expression is [unanchored][unanchored].
If the maximum number of substrings is insufficient to accommodate all 
entries,then the final entry in the `slist` that is generated will contain the 
rest of the un-split string.

[%CFEngine_function_attributes(string, regex, maxent)%]

**Example:**

```cf3
bundle agent test
{
vars:

  "split1" slist => splitstring("one:two:three",":","10");
  "split2" slist => splitstring("one:two:three",":","1");
  "split3" slist => splitstring("alpha:xyz:beta","xyz","10");

reports:

  "split1: $(split1)";  # will list "one", "two", and "three"
  "split2: $(split2)";  # will list "one" and "two:three"
  "split3: $(split3)";  # will list "alpha:" and ":beta"

}
```
