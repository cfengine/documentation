---
layout: default
title: read[int|real|string]list
categories: [Reference, Functions, read*list]
published: true
alias: reference-functions-readintrealstringlist.html
tags: [reference, functions, readintlist, readreallist, readstringlist]
---

**Prototype**: `readintlist(filename, comment, split, maxentries, maxbytes)`<br>
**Prototype**: `readreallist(filename, comment, split, maxentries, maxbytes)`<br>
**Prototype**: `readstringlist(filename, comment, split, maxentries, maxbytes)`

**Return type**: `ilist`, `rlist` or `slist`

**Description**: Splits the file `filename` into separated 
values and returns the list.

The `comment` regex will strip out unwanted patterns from the file being read, 
leaving unstripped characters to be split into fields. Using the empty string 
(`""`) indicates no comments.

**Arguments**:

* `filename` : File name to read, *in the range* "?(/.\*)
* `comment` : [Unanchored][unanchored] regex matching comments, *in the range* .\*
* `split` : [Unanchored][unanchored] regex to split data, *in the range* .\*
* `maxentries` : Maximum number of entries to read, *in the range*
0,99999999999   
* `maxbytes` : Maximum bytes to read, *in the range* 0,99999999999   

**Example**:

```cf3
    bundle agent example
    {     
    vars:

      "integers" ilist => readintlist("/tmp/listofint","#.*","[\n]",10,400);
      "strings" slist => readstringlist("/tmp/listofstring", "#.*", "\s", 10, 400);
      "reals" rlist => readreallist("/tmp/listofreal","#.*","[\n]",10,400);

    reports:

        "List entry: $(mylist)";

    }
```
