---
layout: default
title: data_regextract
published: true
tags: [reference, data functions, functions, json, container, regextract, pcre]
---

[%CFEngine_function_prototype(regex, string)%]

**Description:** Returns a data container filled with backreferences
and named captures if the *multiline* [anchored][anchored] `regex` matches the
`string`.

This function is significantly better than `regextract()` because it
doesn't create classic CFEngine array variables and supports named
captures.

If there are any back reference matches from the regular expression,
then the data container will be populated with the values, in the
manner:

```
    $(container[0]) = entire string
    $(container[1]) = back reference 1, etc
```

Note `0` and `1` are string keys in a map, not offsets.

If named captures are used, e.g. `(?<name1>...)` to capture three
characters under `name1`, then that will be the key instead of the
numeric position of the backreference.

PCRE named captures are described in http://pcre.org/pcre.txt and several syntaxes are supported:

         (?<name>...)    named capturing group (Perl)
         (?'name'...)    named capturing group (Perl)
         (?P<name>...)   named capturing group (Python)

Since the regular expression is run with /dotall/ and /multiline/ modes, to match the end of a line, use ```[^\n]*``` instead of ```$```.

[%CFEngine_function_attributes(regex, string)%]

**Example:**

[%CFEngine_include_snippet(data_regextract.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(data_regextract.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**

**History:** Was introduced in version 3.7.0 (2015)

**See also:** `regextract()`, `regex_replace()`, [pcre2 regular expression syntax summary](http://www.pcre.org/current/doc/html/pcre2syntax.html#SEC10)
