---
layout: default
title: product
categories: [Reference, Functions, product]
published: true
alias: reference-functions-product.html
tags: [reference, functions, product]
---

**Prototype**: `product(list)`

**Return type**: `real`

**Description**: Returns the product of the reals in `list`.

This function might be used for simple ring computation. Of course, you could 
easily combine `product` with `readstringarray` or `readreallist` etc., to 
collect summary information from a source external to CFEngine.

**Arguments**:

* `list` : A list of arbitrary real values, *in the range* 
[a-zA-Z0-9\_\$(){}\\[\\].:]+

**Example**:

```cf3
    bundle agent test
    {
    vars:

      "series" rlist => { "1.1", "2.2", "3.3", "5.5", "7.7" };

      "prod" real => product("series");
      "sum"  real => sum("series");

    reports:

      cfengine_3::

        "Product result: $(prod) > $(sum)";
    }
```

**History**: Was introduced in version 3.1.0b1,Nova 2.0.0b1 (2010)
