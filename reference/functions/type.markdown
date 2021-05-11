---
layout: default
title: type
published: true
tags: [reference, utility functions, functions, type]
---

[%CFEngine_function_prototype(var, detail)%]

**Description:** Returns a variables type decription.

**Return type:** `string`

**Arguments:**

* `var`: `string`, in the range `.*`
* `detail`: `boolean`, in the range: `true,false,yes,no,on,off`

This function returns a variables type description as a string. The function
expects a variable identifier as the first argument `var`. An optional second
argument `detail` may be used to enable detailed description. When set to
`"true"` the returned string comes in a two word format including type and
subtype. This lets us to easily
differentiate between policy- and data primitives. Argument `detail` defaults
to `"false"` when not specified.

If argument `var` is not a valid variable identifier, the function returns
`"none"` or `"policy none"` based on whether the `detail` argument is
set to `"false"` or `"true"` respectively.

The following table demonstrates the strings you can expect to be returned
with different combinations of the arguments `type` and `detail`.

| type         | detail | return        |
|--------------|--------|---------------|
| string       | false  | string        |
| string       | true   | policy string |
| int          | false  | int           |
| int          | true   | policy int    |
| real         | false  | real          |
| real         | true   | policy real   |
| slist        | false  | slist         |
| slist        | true   | policy slist  |
| ilist        | false  | ilist         |
| ilist        | true   | policy ilist  |
| rlist        | false  | rlist         |
| rlist        | true   | policy rlist  |
| data object  | false  | data          |
| data object  | true   | data object   |
| data array   | false  | data          |
| data array   | true   | data array    |
| data string  | false  | data          |
| data string  | true   | data string   |
| data int     | false  | data          |
| data int     | true   | data int      |
| data real    | false  | data          |
| data real    | true   | data real     |
| data boolean | false  | data          |
| data boolean | true   | data boolean  |
| data null    | false  | data          |
| data null    | true   | data null     |
| undefined    | false  | none          |
| undefined    | true   | policy none   |

**Example:**

[%CFEngine_include_snippet(type.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(type.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:**

* Introduced in 3.18.0
