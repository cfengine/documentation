---
layout: default
title: not
aliases:
  - "/reference-functions-not.html"
---

{{< CFEngine_function_prototype(expression) >}}

**Description:** Returns `any` if all arguments evaluate to false and `!any` if
any argument evaluates to true.

{{< CFEngine_function_attributes(expression) >}}

**Argument Descriptions:**

- `expression` - Class, class expression, or function that returns a class

**Example:**

```cf3 {skip TODO}
commands:
  "/usr/bin/generate_config $(config)"
    if => not( fileexists("/etc/config/$(config)") );
```

**Notes:** Introduced primarily for use with `if` and `unless` promise attributes.

**See also:** `and()`, `or()`

**History:**

- Introduced in 3.2.0, Nova 2.1.0 (2011)
- Return type changed from `string` to `boolean` in 3.17.0 (2020) (CFE-3470)
