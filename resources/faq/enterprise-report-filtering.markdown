---
layout: default
title: Enterprise Report Filtering
published: true
sorting: 90
tags: [getting started, faq, enterprise]
---

## Filtering Inventoried Lists

When filtering an inventoried list item filtering can be based on one or more
elements of the specific inventoried item. Note that when filtering for multiple
elements of a list AND logic is used.

For example, this simple policy will inventory "My Inventory" with "common" and
either "one" and "four" or "two" and "three".

```cf3
bundle agent example
{
  meta:
    "tags" slist => { "autorun" };

  vars:

  !host_001::
    "slist" slist => { "common", "one", "four" },
      meta => { "inventory", "attribute_name=My Inventory" };

  host_001::
    "slist" slist => { "common", "two", "three" },
      meta => { "inventory", "attribute_name=My Inventory" };

}
```

The above policy can produce inventory that looks like this:

![inventoried list items](inventoried-list-items.png)

Adding a filter where "My Inventory" *matches* or *contains* ```common``` AND ```one```:

![inventoried list items](filter-inventoried-list-items.png)


