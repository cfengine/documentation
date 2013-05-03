---
layout: default
title: Function-escape
categories: [Special-functions,Function-escape]
published: true
alias: Special-functions-Function-escape.html
tags: [Special-functions,Function-escape]
---

### Function escape

**Synopsis**: escape(arg1) returns type **string**

\
 *arg1* : IP address or string to escape, *in the range* .\* \

Escape regular expression characters in a string

**Example**:\
 \

~~~~ {.verbatim}
bundle server control
{
allowconnects         => { "127\.0\.0\.1", escape("192.168.2.1") };
}
~~~~

**Notes**:\
 \

This function is useful for making inputs readable when a regular
expression is required, but the literal string contains special
characters. The function simply 'escapes' all the regular expression
characters, so that you do not have to.

This in the example above, the string "192.168.2.1" is "escaped" to be
equivalent to "192\\.168\\.2\\.1", because without the backslashes, the
regular expression "192.168.2.1" will also match the IP ranges
"192.168.201", "192.168.231", etc (since the dot character means "match
any character" when used in a regular expression).

**History**: This function was introduced in CFEngine version 3.0.4
(2010)
