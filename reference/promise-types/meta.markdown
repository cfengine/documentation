---
layout: default
title: meta
categories: [Reference, Promise Types,meta]
published: true
alias: reference-promise-types-meta.html
tags: [reference, bundles, common, meta, promises]
---

Meta-data promises have no internal function. They are intended to be used to 
represent arbitrary information about promise bundles. Formally, meta promises 
are implemented as variables, and the values map to a variable context called 
`bundlename\_meta`, and therefore the values can be used as variables and will 
appear in Enterprise variable reports.

```cf3
    bundle agent example

    {     
    meta:

      "bundle_version" string => "1.2.3";
      "works_with_cfengine" slist => "{ 3.4.0, 3.5.0 }";

    reports:

     cfengine_3::

      "Not a local variable: $(bundle_version)";
      "Meta data (variable): $(example_meta.bundle_version)";

    }
```

The value of meta data can be of the types `string` or `slist`.

