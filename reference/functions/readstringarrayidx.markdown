---
layout: default
title: readstringarrayidx
categories: [Reference, Functions, readstringarrayidx]
published: true
alias: reference-functions-readstringarrayidx.html
tags: [reference, io functions, functions, readstringarrayidx]
---

[%CFEngine_function_prototype(array, filename, comment, split, maxentries, maxbytes)%]

**Description:** Populates the two-dimensional array `array` with up to 
`maxentries` fields from the first `maxbytes` bytes of file `filename`.

One dimension is separated by the regex `split`, the other by the the lines in
the file. The array arguments are both integer indexes, allowing for 
non-identifiers at first field (e.g. duplicates or names with spaces), unlike 
`readstringarray`.

The `comment` field will strip out unwanted patterns from the file being read, leaving unstripped characters to be split into fields. Using the empty string (`""`) indicates no comments.

Returns an integer number of keys in the array (i.e., the number of lines 
matched). If you only want the fields in the first matching line (e.g., to 
mimic the behavior of the *getpwnam(3)* on the file `/etc/passwd`), use 
`getfields()`, instead.

[%CFEngine_function_attributes(array, filename, comment, split, maxentries, maxbytes)%]

**Example:**

```cf3
    vars:

      "dim_array" 

         int =>  readstringarrayidx("array_name","/tmp/array","\s*#[^\n]*",":",10,4000);
```

Input example:

```
     
     at spaced:x:25:25:Batch jobs daemon:/var/spool/atjobs:/bin/bash
     duplicate:x:103:105:User for Avahi:/var/run/avahi-daemon:/bin/false    # Disallow login
     beagleindex:x:104:106:User for Beagle indexing:/var/cache/beagle:/bin/bash
     duplicate:x:1:1:bin:/bin:/bin/bash
     # Daemon has the default shell
     daemon:x:2:2:Daemon:/sbin:
```

Results in a systematically indexed map of the file:

```
     array_name[0][0]       at spaced
     array_name[0][1]       x
     array_name[0][2]       25
     array_name[0][3]       25
     array_name[0][4]       Batch jobs daemon
     array_name[0][5]       /var/spool/atjobs
     array_name[0][6]       /bin/bash
     array_name[1][0]       duplicate
     array_name[1][1]       x
     array_name[1][2]       103
     array_name[1][3]       105
     array_name[1][4]       User for Avahi
     array_name[1][5]       /var/run/avahi-daemon
     array_name[1][6]       /bin/false
     ...
```
