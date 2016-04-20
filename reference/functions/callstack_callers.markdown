---
layout: default
title: callstack_callers
published: true
tags: [reference, internal functions, functions, callstack_callers, call, stack, debugging]
---

[%CFEngine_function_prototype()%]

**Description:** Return the call stack for the current promise.

[%CFEngine_function_attributes()%]

This is a call stack inspection function and the specific content may be tied
to a specific CFEngine version. Using it requires writing code that takes the
specific CFEngine version into account.

The returned data container is a list of key-value maps.

The maps all have a `type` key and a `frame` key with a counter. For different
frames along the stack frame path, the maps have additional keys:

* whenever possible,
* bodies: under key `body` the entry has a full dump of the body policy as JSON, same as what `cf-promises -p json` would produce, using the internal C function `BodyToJson()`. This may include the `line` and `sourcePath` to locate the exact code line.
* bundles: under key `bundle` the entry has a full dump of the bundle policy as JSON, same as what `cf-promises -p json` would produce, using the internal C function `BundleToJson()`. This may include the `line` and `sourcePath` to locate the exact code line.
* promise iteration: the `iteration_index` is recorded
* promises: the `promise_type`, `promiser`, `promise_classes`, and `promise_comment` are recorded
* promise sections (types): the `promise_type` is recorded

**Example:**

```cf3
    vars:
      "stack" data => callstack_callers();
```

Output:

```
    [ ... call stack information ... ,
      {
        "depth": 2,
        "frame": 9,
        "promise_classes": "any",
        "promise_comment": "",
        "promise_type": "methods",
        "promiser": "",
        "type": "promise"
      }, ... more call stack information ... ]
```

**History:** Introduced in CFEngine 3.9

**See also:** `callstack_promisers()`
