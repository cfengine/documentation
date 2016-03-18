---
layout: default
title: product
published: true
tags: [reference, data functions, functions, product, inline_json]
---

[%CFEngine_function_prototype(list)%]

**Description:** Returns the product of the reals in `list`.

This function might be used for simple ring computation. Of course, you could 
easily combine `product` with `readstringarray` or `readreallist` etc., to 
collect summary information from a source external to CFEngine.

This is a [collecting function][Functions#collecting functions] so it can accept many types of data parameters.

[%CFEngine_function_attributes(list)%]

**Example:**

[%CFEngine_include_snippet(product.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(product.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Was introduced in version 3.1.0b1,Nova 2.0.0b1 (2010). The [collecting function][Functions#collecting functions] behavior was added in 3.9.

**See also:** `sort()`, `variance()`, `sum()`, `max()`, `min()`, [about collecting functions][Functions#collecting functions], and `data` documentation.
