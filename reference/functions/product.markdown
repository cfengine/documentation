---
layout: default
title: product
categories: [Reference, Functions, product]
published: true
alias: reference-functions-product.html
tags: [reference, data functions, functions, product]
---

[%CFEngine_function_prototype(list)%]

**Description:** Returns the product of the reals in `list`.

This function might be used for simple ring computation. Of course, you could 
easily combine `product` with `readstringarray` or `readreallist` etc., to 
collect summary information from a source external to CFEngine.

[%CFEngine_function_attributes(list)%]

**Example:**

```cf3
    bundle agent test
    {
    vars:

      "series" rlist => { "1.1", "2.2", "3.3", "5.5", "7.7" };

      "prod" real => product("series");
      "sum"  real => sum("series");

    reports:
        "Product result: $(prod) > $(sum)";
    }
```

**History:** Was introduced in version 3.1.0b1,Nova 2.0.0b1 (2010)
