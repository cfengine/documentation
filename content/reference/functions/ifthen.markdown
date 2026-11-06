---
layout: default
title: ifthen
aliases:
  - "/reference-functions-ifthen.html"
---

{{< CFEngine_function_prototype(...) >}}

**Description:** Evaluate each pair of arguments as a (`class`, `value`) tuple, returning the `value` of the first pair whose `class` is set.

If none are set, the variable is not defined.

**Arguments**:

The `ifthen` function is like `ifelse()` without the default (`else`)
value. It must have an even number of arguments (at least 2). Any other
number is a fatal error. The first argument of each pair is a class
expression, like the `expression` attribute of a classes promise, so it
can be more than a class name, for example `Tuesday.linux.!verbose`.

Generally, if `ifthen` were called with arguments `(a1, a2, b1, b2)`,
the behavior expressed as pseudo-code is:

```
if a1 then return a2
else-if b1 then return b2
else return nothing
```

When no class expression is true, the function returns nothing, so the
variable is not defined by that promise. This is useful when there is
no sensible default value, for example to leave a variable to be
defined by another promise or to be checked with `isvariable()`. With
`ifelse()`, you have to provide a placeholder default value and check
for it.

**Example:**

```cf3
bundle agent __main__
{
  classes:
    "webserver" expression => "any";

  vars:
    # The value of the first true class expression is used.
    "port" string => ifthen("dbserver", "5432", "webserver", "80");

    # No class expression is true, so the variable is not defined.
    "unset" string => ifthen("dbserver", "5432", "mailserver", "25");

  reports:
    "port is $(port)";
    "unset is not defined" if => not(isvariable("unset"));
}
```

Output:

```
R: port is 80
R: unset is not defined
```

**Notes:**

- Unlike `ifelse()` with exactly three arguments, `ifthen()` follows the
  general rule for functions: it is not evaluated while any of its
  arguments contain unresolved variables.

**See also:** `ifelse()`, `isvariable()`

**History:**

- Introduced in 3.29.0
