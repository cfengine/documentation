---
layout: default
title: eval
published: true
tags: [reference, data functions, functions, eval, context, class, equality, numbers]
---

[%CFEngine_function_prototype(expression, mode, options)%]

**Description:** Returns `expression` evaluated according to `mode`
and `options`. Currently only the `math` and `class` modes with
`infix` option are supported for evaluating traditional math
expressions.

All the math is done with the C `double` type internally.  The results are returned as a string.  When the `mode` is `math` the returned value is a floating-point value formatted to 6 decimal places as a string.

`mode` and `options` are optional and default to `math` and `infix`,
respectively.

**Example:**

```
  vars:
    # returns 20.000000
    "result" string => eval("200/10", "math", "infix");
```

When the `mode` is `class`, the returned string is either false for 0 (`!any`) or true for anything else (`any`) so it can be used in a class expression under `classes`.  The `==` operator (see below) is very convenient for this purpose.  The actual accepted values for false allow a tiny margin around 0, just like `==`.

**Example:**

```
  classes:
    # the class will be set
    "they_are_equal" expression => eval("20 == (200/10)", "class", "infix");
```

The supported infix mathematical syntax, in order of precedence, is:

- `(` and `)` parentheses for grouping expressions
- `^` operator for exponentiation
- `*` and `/` operators for multiplication and division
- `%` operators for modulo operation
- `+` and `-` operators for addition and subtraction
- `==` "close enough" operator to tell if two expressions evaluate to the same number, with a tiny margin to tolerate floating point errors.  It returns 1 or 0.
- `>=` "greater or close enough" operator with a tiny margin to tolerate floating point errors.  It returns 1 or 0.
- `>` "greater than" operator.  It returns 1 or 0.
- `<=` "less than or close enough" operator with a tiny margin to tolerate floating point errors.  It returns 1 or 0.
- `<` "less than" operator.  It returns 1 or 0.

The numbers can be in any format acceptable to the C `scanf` function with the `%lf` format specifier, followed by the `k`, `m`, `g`, `t`, or `p` SI units.  So e.g. `-100` and `2.34m` are valid numbers.

In addition, the following constants are recognized:

- `e`: 2.7182818284590452354
- `log2e`: 1.4426950408889634074
- `log10e`: 0.43429448190325182765
- `ln2`: 0.69314718055994530942
- `ln10`: 2.30258509299404568402
- `pi`: 3.14159265358979323846
- `pi_2`: 1.57079632679489661923 (pi over 2)
- `pi_4`: 0.78539816339744830962 (pi over 4)
- `1_pi`: 0.31830988618379067154 (1 over pi)
- `2_pi`: 0.63661977236758134308 (2 over pi)
- `2_sqrtpi`: 1.12837916709551257390 (2 over square root of pi)
- `sqrt2`: 1.41421356237309504880 (square root of 2)
- `sqrt1_2`: 0.70710678118654752440 (square root of 1/2)

The following functions can be used, with parentheses:

- `ceil` and `floor`: the next highest or the previous highest integer
- `log10`, `log2`, `log`
- `sqrt`
- `sin`, `cos`, `tan`, `asin`, `acos`, `atan`
- `abs`: absolute value
- `step`: 0 if the argument is negative, 1 otherwise

[%CFEngine_function_attributes(expression, mode, options)%]

**Example:**

[%CFEngine_include_example(eval.cf)%]

**History:**

* Function added in 3.6.0.
* `mode` and `options` optional and default to `math` and `infix`, respectively in 3.9.0.
* comparison `<`, `<=`, `>`, `>=` operators added in 3.10.0
