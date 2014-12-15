---
layout: default
title: randomint
published: true
tags: [reference, data functions, functions, randomint]
---

[%CFEngine_function_prototype(lower, upper)%]

**Description:** Returns a random integer between `lower` and *up to but not including* `upper`.

The limits must be integer values and the resulting numbers are based on
the entropy of the md5 algorithm.

The `upper` limit is excluded from the range.  Thus `randomint(0, 100)`
will return 100 possible values, not 101.

The function will be re-evaluated on each pass if it is not restricted with a
context class expression as shown in the example.

**NOTE:** The randomness produced by randomint is not safe for cryptographic usage.

[%CFEngine_function_attributes(lower, upper)%]

**Example:**

[%CFEngine_include_snippet(randomint.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(randomint.cf, #\+begin_src\s+example_output\s*, .*end_src)%]
