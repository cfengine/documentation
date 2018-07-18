---
layout: default
title: regex_replace
published: true
tags: [reference, data functions, functions, regex_replace, pcre]
---

[%CFEngine_function_prototype(string, regex, replacement, options)%]

**Description:** In a given string, replaces a regular expression with something else.

[%CFEngine_function_attributes(string, regex, replacement, options)%]

The supported options are single letters you place in the `options`
string in any order. Consult http://pcre.org/pcre.txt for the exact
meaning of the uppercase options, and note that some can be turned on
inside the regular expression, e.g. `(?s)`.

* `i`: case-insensitive
* `m`: multiline (`PCRE_MULTILINE`)
* `s`: dot matches newlines too (`PCRE_DOTALL`)
* `x`: extended regular expressions (`PCRE_EXTENDED`, very nice for readability)
* `U`: ungreedy (`PCRE_UNGREEDY`)
* `T`: disables special characters and backreferences in the replacement string

In the replacement, `$1` and `\1` refer to the first capture group.
`$2` and `\2` refer to the second, and so on, except there is no `\10`
or higher, you have to use `$10` etc.

In addition, `$+` is replaced with the capture count. `$'` (dollar
sign + single quote) is the part of the string after the regex match.
$\` (dollar sign + backtick) is the part of the string before the
regex match. `$&` holds the entire regex match.

**Example:**

[%CFEngine_include_snippet(regex_replace.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(regex_replace.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Was introduced in version 3.8.0 (2015)

**See also:** `data_regextract()` `regextract()`
