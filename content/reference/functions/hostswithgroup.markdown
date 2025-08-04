---
layout: default
title: hostswithgroup
---

**This function is only available in CFEngine Enterprise.**

{{< CFEngine_function_prototype(group_name, field) >}}

**Description:** Returns a list from the CFEngine Database with the information `field` of all hosts sharing the group `group_name`.

On CFEngine Enterprise, this hub function can be used to return a list of hostnames, ip-addresses or public key SHAs of hosts that are from the same group. It works very similarly as its twin `hostswithclass()`.

{{< CFEngine_function_attributes(group_name, field) >}}

**Example:**

```cf3
bundle agent debian_hosts
{
  vars:
    am_policy_hub::
      "host_list"
        slist => hostswithgroup( "Linux", "name" );

  files:
    am_policy_hub::
      "/tmp/master_config.cfg"
        edit_line => insert_lines("host=$(host_list)"),
        create => "true";
}
```

**History:** Was introduced in 3.26.0

**See also:** `hostswithclass()`
