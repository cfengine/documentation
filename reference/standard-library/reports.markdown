---
layout: default
title: Reports Bundles and Bodies
categories: [Reference, Standard Library, reports]
published: true
sorting: 100
alias: reference-standard-library-reports.html
tags: [reference, standard library]
---

See the [`report_data_select` body][access#report_data_select] documentation for a
comprehensive reference on the body type used here.

To use these bodies, add the following to your policy:

```cf3
body file control
{
	inputs => { "reports.cf" }
}
```



[%CFEngine_library_include(lib/3.6/reports)%]
