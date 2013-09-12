---
layout: default
title: eval
categories: [Reference, Functions, eval]
published: true
alias: reference-functions-eval.html
tags: [reference, data functions, functions, eval]
---

[%CFEngine_function_prototype(mode, options, expression)%]

**Description:** Returns `expression` evaluated according to `mode`
and `options`.  Currently only the `math` mode with `infix` option
is supported for evaluating traditional math expressions.

All the math is done with the C `double` type internally.  The results are returned as a string 

The supported infix mathematical syntax, in order of precedence, is:

- `(` and `)` parentheses for grouping expressions
- `^` operator for exponentiation
- `*` and `/` operators for multiplication and division
- `%` operators for modulo operation
- `+` and `-` operators for addition and subtraction
- `==` "close enough" operator to tell if two expressions evaluate to the same number, with a tiny margin to tolerate floating point errors.  It returns 1 or 0.

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

[%CFEngine_function_attributes(mode, options, expression)%]

**Example:**

[%CFEngine_include_snippet(eval.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

```
2013-09-14T08:34:16-0400     info: eval error: expression could not be parsed (input 'x')
2013-09-14T08:34:16-0400     info: eval error: expression could not be parsed (input '+ 200')
2013-09-14T08:34:16-0400     info: eval error: expression could not be parsed (input '- - -')
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('x') = ''
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('+ 200') = ''
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('floor(3.4)') = '3.000000'
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('sqrt(0.2)') = '0.447214'
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('2 + 3 - 1') = '4.000000'
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('sin(20)') = '0.912945'
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('200 - 100') = '100.000000'
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('20 % 3') = '2.000000'
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('ceil(3.5)') = '4.000000'
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('200 + 100') = '300.000000'
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('pi') = '3.141593'
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('- - -') = ''
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('-3.400000 == -3.400001') = '0.000000'
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('3 / 0') = 'inf'
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('e') = '2.718282'
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('cos(20)') = '0.408082'
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('') = '0.000000'
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('-1^2.1') = '-nan'
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('abs(-3.4)') = '3.400000'
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('-3.4 == -3.4') = '1.000000'
2013-09-14T08:34:16-0400   notice: R: math/prefix eval('3^3') = '27.000000'
```

