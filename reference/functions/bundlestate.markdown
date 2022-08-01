---
layout: default
title: bundlestate
published: true
tags: [reference, data functions, functions, json, bundlestate, evaluation, vars, classes, container]
---

[%CFEngine_function_prototype(bundlename)%]

**Description:** Returns the current evaluation data state for bundle `bundlename`.

The returned data container will have keys corresponding to the
variables in bundle `bundlename`. The value is converted to a data
container (JSON format) if necessary. So for example the variable `x`
holding the CFEngine slist `{ "1", "a", "foo" }` will be converted to
the equivalent JSON array under the key `x`: `"x": [ "1", "a", "foo" ]`.

**Note:** unlike `datastate()` classes are **not** collected.

The namespace of the bundle should **not** be included if it's in the
`default:` namespace (all CFEngine bundles are, unless you override
that). But if the bundle is in another namespace, you must prefix the
name with the namespace in the normal `mynamespace:mybundle` fashion.

[%CFEngine_function_attributes(bundlename)%]

**Example:**

[%CFEngine_include_snippet(bundlestate.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(bundlestate.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** `getindices()`, `classesmatching()`, `variablesmatching()`, `mergedata()`, [template_method][files#template_method], `mustache`, `inline_mustache`, `datastate()`

**History:**

* Introduced in CFEngine 3.7.0
