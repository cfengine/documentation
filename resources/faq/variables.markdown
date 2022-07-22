---
layout: default
title: How do I pass a data type variable?
published: true
sorting: 90
tags: [getting started, vars, faq]
---

Data type variables also known as "data containers" are passed using the same
syntax as passing a list.

```cf3
bundle agent example
{
  vars:
    # First you must have a data type variable, define it inline or read from a
    # file using `readjson()`.
    "data" data => parsejson('[ { "x": 1 }, { "y": 2 } ]');

  methods:
    "use data"
      usebundle => use_data(@(data));
}

bundle agent use_data(dc)
{
  vars:
    # Use the data
    # Get its keys, or its index
    "dc_index" slist => getindices(dc);

  classes:
    "have_x" expression => isvariable("dc[$(dc_index)][x]");
    "have_z" expression => isvariable("dc[$(dc_index)][z]");

  reports:
    "CFEngine version '$(sys.cf_version)'";
    have_x::
      "Index '$(dc_index)' has key for x";

    have_z::
      "Index '$(dc_index)' has key for z";
}
```

```console
$ cf-agent -Kf ./example.cf -b example
R: CFEngine version '3.6.4'
R: Index '0' has key for x
R: Index '1' has key for x
```
