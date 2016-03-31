---
layout: default
title: "read[int|real|string]array"
published: true
tags: [reference, io functions, functions, readintarray, readrealarray, readstringarray]
---

**Prototype:** `readintarray(array, filename, comment, split, maxentries, maxbytes)`<br>
**Prototype:** `readrealarray(array, filename, comment, split, maxentries, maxbytes)`<br>
**Prototype:** `readstringarray(array, filename, comment, split, maxentries, maxbytes)`

**Return type:** `int`

**Description:** Populates `array` with up to `maxentries` values, parsed from
the first `maxbytes` bytes in file `filename`.

Reads a two dimensional array from a file. One dimension is separated by the
regex `split`, the other by the lines in the file. The first field of the
lines names the first array argument.

The `comment` field is a multiline regular expression and will strip out
unwanted patterns from the file being read, leaving unstripped characters to be
split into fields. Using the empty string (`""`) indicates no comments.

Returns the number of keys in the array, i.e., the number of
lines matched.

**Arguments**:

* `array` : Array identifier to populate, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`
* `filename` : File name to read, in the range `"?(/.*)`
* `comment` : [Unanchored][unanchored] regex matching comments, in the range `.*`
* `split` : [Unanchored][unanchored] regex to split lines into fields, in the range `.*`
* `maxentries` : Maximum number of entries to read, in the range
`0,99999999999`
* `maxbytes` : Maximum bytes to read, in the range `0,99999999999`

**Example:**

```cf3
    readintarray("array_name","/tmp/array","#[^\n]*",":",10,4000);
```

Input:

```cf3
     1: 5:7:21:13
     2:19:8:14:14
     3:45:1:78:22
     4:64:2:98:99
```

Results in:

```cf3
     array_name[1][0]   1
     array_name[1][1]   5
     array_name[1][2]   7
     array_name[1][3]   21
     array_name[1][4]   13
     array_name[2][0]   2
     array_name[2][1]   19
     array_name[2][2]   8
     array_name[2][3]   14
     array_name[2][4]   14
     array_name[3][0]   3
     array_name[3][1]   45
     array_name[3][2]   1
     array_name[3][3]   78
     array_name[3][4]   22
     array_name[4][0]   4
     array_name[4][1]   64
     array_name[4][2]   2
     array_name[4][3]   98
     array_name[4][4]   99
```

```cf3
    readstringarray("array_name","/tmp/array","\s*#[^\n]*",":",10,4000);
```

Input:

```cf3
     at:x:25:25:Batch jobs daemon:/var/spool/atjobs:/bin/bash
     avahi:x:103:105:User for Avahi:/var/run/avahi-daemon:/bin/false    # Disallow login
     beagleindex:x:104:106:User for Beagle indexing:/var/cache/beagle:/bin/bash
     bin:x:1:1:bin:/bin:/bin/bash
     # Daemon has the default shell
     daemon:x:2:2:Daemon:/sbin:
```

Results in a systematically indexed map of the file:

```cf3
     ...
     array_name[daemon][0]   daemon
     array_name[daemon][1]   x
     array_name[daemon][2]   2
     array_name[daemon][3]   2
     array_name[daemon][4]   Daemon
     array_name[daemon][5]   /sbin
     array_name[daemon][6]   /bin/bash
     ...
     array_name[at][3]       25
     array_name[at][4]       Batch jobs daemon
     array_name[at][5]       /var/spool/atjobs
     array_name[at][6]       /bin/bash
     ...
     array_name[games][3]    100
     array_name[games][4]    Games account
     array_name[games][5]    /var/games
     array_name[games][6]    /bin/bash
     ...
```
