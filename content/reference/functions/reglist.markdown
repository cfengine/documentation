---
layout: default
title: reglist
aliases:
  - "/reference-functions-reglist.html"
---

{{< CFEngine_function_prototype(list, regex) >}}

**Description:** Returns whether the [anchored][anchored] regular expression
`regex` matches any item in `list`.

[This function can accept many types of data parameters.][Functions#collecting functions]

{{< CFEngine_function_attributes(list, regex) >}}

`reglist()` will return as soon as any item matches.

**Example:**

{{< CFEngine_include_snippet(reglist.cf, #\+begin_src cfengine3, .*end_src) >}}

Output:

{{< CFEngine_include_snippet(reglist.cf, #\+begin_src\s+example_output\s*, .*end_src) >}}

In the example above, the IP address in `$(sys.ipv4[eth0])` must be `escape`d,
so that the (.) characters in the IP address are not interpreted as the
regular expression "match any" characters.

**History:**

- The [collecting function][Functions#collecting functions] behavior was added in 3.9.
- Returns as soon as an item matches in 3.29.0 (CFE-4272).

**See also:** [short-circuit evaluation][Functions#short-circuit evaluation], `getindices()`, `getvalues()`, [about collecting functions][Functions#collecting functions], and `data` documentation.
