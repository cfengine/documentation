---
layout: default
title: Function-product
categories: [Special-functions,Function-product]
published: true
alias: Special-functions-Function-product.html
tags: [Special-functions,Function-product]
---

### Function product

**Synopsis**: product(arg1) returns type **real**

\
 *arg1* : A list of arbitrary real values, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+ \

Return the product of a list of reals

**Example**:\
 \

~~~~ {.verbatim}
bundle agent test
{
vars:

  "series" rlist => { "1.1", "2.2", "3.3", "5.5", "7.7" };

  "prod" real => product("series");
  "sum"  real => sum("series");

reports:

  cfengine_3::

    "Product result: $(prod) > $(sum)";
}
~~~~

**Notes**:\
 \
 Of course, you could easily combine `product` with `readstringarray` or
`readreallist` etc., to collect summary information from a source
external to CFEngine.

**History**: Was introduced in version 3.1.0b1,Nova 2.0.0b1 (2010)

This function might be used for simple ring computation.
