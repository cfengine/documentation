---
layout: default
title: meta
aliases:
  - "/reference-promise-types-meta.html"
---

Meta-data promises have no internal function. They are intended to be used to
represent arbitrary information about promise bundles. Formally, meta promises
are implemented as variables, and the values map to a variable context called
`bundlename_meta`. The values can be used as variables and will appear in
CFEngine Enterprise variable reports.

```cf3
bundle agent example
{
meta:

  "bundle_version" string => "1.2.3";
  "works_with_cfengine" slist => { "3.4.0", "3.5.0" };

reports:

  "Not a local variable: $(bundle_version)";
  "Meta data (variable): $(example_meta.bundle_version)";

}
```

The value of meta data can be of the types `string` or `slist` or `data`.

## Attributes

{{< CFEngine_include_markdown(common-attributes.include.markdown) >}}

### data

**Description:** A data container structure

**Type:** `data`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
vars:

 "loaded1" data => readjson("/tmp/myfile.json", 40000);
 "loaded2" data => parsejson('{"key":"value"}');
 "loaded3" data => readyaml("/tmp/myfile.yaml", 40000);
 "loaded4" data => parseyaml('- key2: value2');
 "merged1" data => mergedata(loaded1, loaded2, loaded3, loaded4);

 # JSON or YAML can be inlined since CFEngine 3.7
 "inline1" data => '{"key":"value"}'; # JSON
 "inline2" data => '---$(const.n)- key2: value2'; # YAML requires "---$(const.n)" header
```

### slist

**Description:** A list of scalar strings

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
vars:

 "xxx"    slist  => {  "literal1",  "literal2" };
 "xxx1"   slist  => {  "1", @(xxx) }; # interpolated in order
 "yyy"    slist  => {
                    readstringlist(
                                  "/home/mark/tmp/testlist",
                                  "#[a-zA-Z0-9 ]*",
                                  "[^a-zA-Z0-9]",
                                  15,
                                  4000
                                  )
                    };

 "zzz"    slist  => { readstringlist(
    "/home/mark/tmp/testlist2",
    "#[^\n]*",
    ",",
    5,
    4000)
    };
```

**Notes:**

Some [functions][Functions] return `slist`s, and an `slist`
may contain the values copied from another `slist`, `rlist`, or `ilist`. See
[`policy`](#policy).

### string

**Description:** A scalar string

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
vars:

 "xxx"    string => "Some literal string...";
 "yyy"    string => readfile( "/home/mark/tmp/testfile" , "33" );
```
