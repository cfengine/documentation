---
layout: default
title: usemodule
aliases:
  - "/reference-functions-usemodule.html"
---

{{< CFEngine_function_prototype(module, args) >}}

**Description:** Execute CFEngine module script `module` with `args`, and
return whether successful.

The module script is expected to be located in the registered modules
directory, `WORKDIR/modules`.

{{< CFEngine_function_attributes(module, args) >}}

**Example:**

```cf3
bundle agent test
{
  classes:

      # returns $(user)

      "done" expression => usemodule("getusers","");

  commands:

      "/bin/echo" args => "test $(user)";
}
```

**Simulate mode:** This function is [_unsafe_][cf-agent#Safe and unsafe functions]
and is skipped in `--simulate` mode unless the promise has `simulate_safe` in
its [`meta`][Promise types#meta] attribute.

**See also:** [read_module_protocol()][read_module_protocol], [Module Protocol][commands#module]
