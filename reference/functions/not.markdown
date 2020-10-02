---
layout: default
title: not
published: true
tags: [reference, data functions, functions, not]
---

[%CFEngine_function_prototype(expression)%]

**Description:** Returns `any` if all arguments evaluate to false and `!any` if
any argument evaluates to true.

[%CFEngine_function_attributes(expression)%]

**Argument Descriptions:**

* `expression` - Class, class expression, or function that returns a class

**Example:**

```cf3
commands:
  "/usr/bin/generate_config $(config)"
    ifvarclass => not( fileexists("/etc/config/$(config)") );
```

**Notes:** Introduced primarily for use with `ifvarclass`, `if`, and `unless`
promise attributes.

**See also:** `and`, `or`, `not`

**History:** Was introduced in 3.2.0, Nova 2.1.0 (2011)
