---
layout: default
title: getindices
published: true
tags: [reference, data functions, functions, getindices, inline_json]
---

[%CFEngine_function_prototype(varref)%]

**Description:** Returns the list of keys in `varref` which can be
the name of an array or container.

[This function can accept many types of data parameters.][Functions#collecting functions]

Make sure you specify the correct scope when supplying the name of the
variable.

**Note:**

- The function **always** returns a list. If called on something that has no
  index (for example, an undefined variable) an empty list is returned.

- The list which getindices returns is not guaranteed to be in any specific
  order.

- In the case of a doubly-indexed array (such as `parsestringarrayidx()` and
  friends produce), the primary keys are returned; i.e. if `varref[i][j]` exist
  for various `i`, `j` and you ask for the keys of `varref`, you get the `i`
  values. For each such `i` you can then ask for `getindices("varref[i]")` to
  get a list of the `j` values (and so on, for higher levels of indexing).

[%CFEngine_function_attributes(varref)%]

**Example:**

[%CFEngine_include_snippet(getindices.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(getindices.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:**

- [Collecting function][Functions#collecting functions] behavior as of 3.9.0
- Always returns list as of 3.9.0

**See also:** `getvalues()`, [about collecting functions][Functions#collecting functions], and `data` documentation.
