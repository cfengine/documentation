---
layout: default
title: product
published: true
tags: [reference, data functions, functions, product]
---

[%CFEngine_function_prototype(list)%]

**Description:** Returns the product of the reals in `list`.

This function might be used for simple ring computation. Of course, you could 
easily combine `product` with `readstringarray` or `readreallist` etc., to 
collect summary information from a source external to CFEngine.

[%CFEngine_function_attributes(list)%]

**Example:**

[%CFEngine_include_snippet(product.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(product.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Was introduced in version 3.1.0b1,Nova 2.0.0b1 (2010)
