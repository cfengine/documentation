---
layout: default
title: getgroups
aliases:
  - "/reference-functions-getgroups.html"
---

{{< CFEngine_function_prototype(exclude_names, exclude_ids) >}}

**Description:** Returns a list of all groups defined, except those names in the comma separated string of `exclude_names` and the comma separated string of uids in `exclude_ids`

{{< CFEngine_function_attributes(exclude_names, exclude_ids) >}}

**Example:**

```cf3
bundle agent main
{
  vars:
    "groups"
      slist => getgroups("root", "");

    "first_three_groups"
      slist => sublist("@(groups)", head, 3);

  reports:
    "$(first_three_groups)";

}
```

**Output:**

```
R: daemon
R: bin
R: sys
```

**Notes:**

- This function is currently only available on Unix-like systems.
- This function will return both local and remote (for example, groups defined in an external directory like LDAP) groups on a system.

**History:**

- Introduced in CFEngine 3.27.

**See also:** [`getgroupinfo()`][getgroupinfo].
