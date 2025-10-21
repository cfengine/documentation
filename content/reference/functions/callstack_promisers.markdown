---
layout: default
title: callstack_promisers
aliases:
  - "/reference-functions-callstack_promisers.html"
---

{{< CFEngine_function_prototype() >}}

**Description:** Return the promisers along the call stack for the current promise.

{{< CFEngine_function_attributes() >}}

This is a call stack inspection function and the specific content may be tied
to a specific CFEngine version. Using it requires writing code that takes the
specific CFEngine version into account.

The returned data container is a `slist` of promiser names. It's a much simpler
version of `callstack_callers()` intended for quick debugging.

**Example:**

```cf3 {skip TODO}
vars:
  "my_promisers" slist => callstack_promisers();
```

Output:

```
{ "my_promisers" }
```

**History:** Introduced in CFEngine 3.9

**See also:** `callstack_callers()`
