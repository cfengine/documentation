---
layout: default
title: usemodule
published: true
tags: [reference, utility functions, functions, usemodule]
---

[%CFEngine_function_prototype(module, args)%]

**Description:** Execute CFEngine module script `module` with `args`, and 
return whether successful.

The module script is expected to be located in the registered modules 
directory, `WORKDIR/modules`.

[%CFEngine_function_attributes(module, args)%]

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
**See Also:** [Module Protocol][commands#module]
