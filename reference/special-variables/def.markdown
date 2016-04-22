---
layout: default
title: def
published: true
tags: [reference, variables, def, augments]
---

The context `def` is populated by the
[Masterfiles Policy Framework][The Policy Framework] and can also be populated
by the [augments file][Augments].

**Note:** Variables defined from policy in a bundle named `def` **will
override** the variables defined by the augments file unless the policy
explicitly guards against it.

For example `mailto` is only defined from policy if it is not yet defined by the
augments file.:

```cf3
bundle common def
{

  vars:

  # ...

      "mailto"
        string => "root@$(def.domain)",
        ifvarclass => not(isvariable("mailto"));

  # ...
}
```

### def.jq

This variable gives a convenient way to invoke
[jq](https://stedolan.github.io/jq/) for the `mapdata()` function in `json_pipe`
mode and elsewhere. Note the below is the **default** value defined in the C
code that you can override in the `vars` section of the
[augments file][Augments] or in policy as described above.

```cf3
    # def.jq = jq --compact-output --monochrome-output --ascii-output --unbuffered --sort-keys
```
