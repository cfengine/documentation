---
layout: default
title: randomint
categories: [Reference, Functions, randomint]
published: true
alias: reference-functions-randomint.html
tags: [reference, data functions, functions, randomint]
---

[%CFEngine_function_prototype(lower, upper)%]

**Description:** Returns a random integer between `lower` and `upper`.

The limits must be integer values and the resulting numbers are based on
the entropy of the md5 algorithm.

The function will be re-evaluated on each pass if it is not restricted with a
context class expression as shown in the example.

[%CFEngine_function_attributes(lower, upper)%]

**Example:**

```cf3
    bundle agent randomint_example
    {
      vars:
          "low"    string => "4";
          "high"   string => "60";

          "random"    int => randomint("$(low)", "$(high)"),
                   policy => "free";

        !classes1::
          "random1" 
            string  => "$(random)",
            handle  => "var_random1",
            comment => "this should only be set on the first pass";

        classes1.!classes2::

          "random2" 
            string     => "$(random)",
            handle     => "var_random2",
            comment    => "this should only be set on the second pass";

        classes2::

          "random3" 
            string     => "$(random)",
            handle     => "var_random3",
            comment    => "this should only be set on the third pass";

      classes:
          "classes3" expression => "classes2";
          "classes2" expression => "classes1";
          "classes1" expression => "any";

      reports:
        classes3::
          "Random Numbers: $(random1), $(random2), $(random3)";
    }
```

Example output:

    R: Random Numbers: 32, 56, 37
