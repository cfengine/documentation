---
layout: default
title: splitstring
categories: [Reference, Functions, splitstring]
published: true
alias: reference-functions-splitstring.html
tags: [reference, functions, splitstring]
---

**Prototype**: `splitstring(string, regex, maxent)`

**Return type**: `slist`

**Description**: Splits `string` into substrings wherever `regex` occurs, and 
returns the list with at most `maxent` those strings.

If the maximum number of splits is insufficient to accommodate all entries, 
then the final entry in the `slist` that is generated will contain the rest of 
the un-split string.

**Arguments**:

* `string` : A data string, *in the range* .\*
* `regex` : Unanchored regular expression to split on, *in the range* .\*
* `maxent` : Maximum number of pieces, *in the range* 0,99999999999   

**Example**:

```cf3
bundle agent test
{
vars:

  "split1" slist => splitstring("one:two:three",":","10");
  "split2" slist => splitstring("one:two:three",":","1");
  "split3" slist => splitstring("alpha:xyz:beta","xyz","10");

reports:

 linux::

  "split1: $(split1)";  # will list "one", "two", and "three"
  "split2: $(split2)";  # will list "one" and "two:three"
  "split3: $(split3)";  # will list "alpha:" and ":beta"

}
```
