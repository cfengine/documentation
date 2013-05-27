---
layout: default
title: meta in common promises
<<<<<<< HEAD:reference/common/meta-in-common-promises.markdown
categories: [Reference, Bundles for Common,meta in common promises]
=======
categories: [Bundles for common,meta in common promises]
>>>>>>> 702a8ca0231da6ae5e2672b6298561254d98aa29:bundles-logs-functions-variables/Bundles-for-common/Bundles-for-common-0-meta-in-common-promises.markdown
published: true
alias: reference-bundles-for-common-meta-in-common-promises.html
tags: [reference, bundles, common, meta, promises]
---

### `meta` promises in \*

  

Meta-data promises have no internal function. They are intended to be
used to represent arbitrary information about promise bundles. Formally,
meta promises are implemented as variables, and the values map to a
variable context called bundlename\_meta, and therefore the values can
be used as variables and will appear in Enterprise variable reports.

  

```cf3
bundle agent example

{     
meta:

  "bundle_version" string => "1.2.3";
  "works_with_cfengine" string => "3.4.0";

reports:

 cfengine_3::

  "Not a local variable: $(bundle_version)";
  "Meta data (variable): $(example_meta.bundle_version)";

}
```

  

-   [string in meta](#string-in-meta)
-   [slist in meta](#slist-in-meta)

#### `string`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: A scalar string

In previous versions of CFEngine lists were represented (as in the
shell) using separated scalars; similar to the PATH variable. In
CFEngine 3 lists are kept as an independent type.

**Example**:  
   

```cf3
vars:

 "xxx"    string => "Some literal string...";

 "yyy"    string => readfile( "/home/mark/tmp/testfile" , "33" );
```

#### `slist`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: A list of scalar strings

Some functions return `slist`s (see [Introduction to
functions](#Introduction-to-functions)), and an `slist` may contain the
values copied from another `slist`, `rlist`, or `ilist` (see [List
variable substitution and
expansion](#List-variable-substitution-and-expansion), and [policy in
vars](#policy-in-vars)).

**Example**:  
   

```cf3
vars:

 "xxx"    slist  => {  "literal1",  "literal2" };

 "yyy"    slist  => { 
                    readstringlist(
                                  "/home/mark/tmp/testlist",
                                  "#[a-zA-Z0-9 ]*",
                                  "[^a-zA-Z0-9]",
                                  15,
                                  4000
                                  ) 
                    };

 "zzz"    slist  => { readstringlist("/home/mark/tmp/testlist2","#[^\n]*",",",5,4000) };

```
