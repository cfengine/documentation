---
layout: default
title: variablesmatching
published: true
tags: [reference, utility functions, functions, variablesmatching]
---

[%CFEngine_function_prototype(name, tag1, tag2, ...)%]

**Description:** Return the list of variables matching `name` and any tags
given. Both `name` and tags are regular expressions.

This function searches for the given [anchored][anchored] `name` and
`tag1`, `tag2`, ... regular expressions in the list of currently defined
variables.

When one or more tags are given, the variables with tags matching any
of the given [anchored][anchored] regular expressions are returned (logical OR semantics).
For example, if one variable has tag `inventory`, a second variable has tag `time_based`
but not `inventory`, *both* are returned by variablesmatching(".*", "inventory", "time_based").
If you want logical AND semantics instead, you can make two calls to the function
with one tag in each call and use the `intersection` function on the return values.

Variable tags are set using the [`meta`][Promise Types and Attributes#meta] attribute.

[%CFEngine_function_attributes(regex, tag1, tag2, ...)%]

**Example:**


[%CFEngine_include_snippet(variablesmatching.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(variablesmatching.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** [classesmatching()][classesmatching], [bundlesmatching()][bundlesmatching]

**History:** Introduced in CFEngine 3.6
