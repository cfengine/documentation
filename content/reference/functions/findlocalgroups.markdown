---
layout: default
title: findlocalgroups
aliases:
  - "/reference-functions-findlocalgroups.html"
---

{{< CFEngine_function_prototype(filter) >}}

**Description:** Returns a data container of all local groups with their attributes that are matching a filter. If no filter is specified, it will return all the local groups.

{{< CFEngine_function_attributes(filter) >}}

The `filter` argument can be used to look up groups with specific attributes that match values. The filter is a `"data"` container array or `"slist"` comprised of pairs of attribute and value/regex pattern `{ "attribute1=value1", "attribute2=value2", ... }`.

The possible attributes are:

- `name`: name
- `gid`: group id
- `member` members: a list of users separated by commas

**Example:**

```cfengine3
bundle agent main
{
  vars:
    "filter" slist => { "name=root" };
    "groups" data => findlocalgroups("@(filter)");

  reports:
    "$(with)" with => storejson("@(groups)");
}
```

Output:

```
R: {
  "root": {
    "gid": 0,
    "members": []
  }
}
```

**Notes:**

- This function is currently only available on Unix-like systems.

**History:**

- Function added in 3.27.0.
