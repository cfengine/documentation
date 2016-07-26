---
layout: default
title: Mustache templating
published: true
sorting: 90
tags: [getting started, mustache, faq]
---

## How can I pass a data variable to template_data?

Just use `template_data => @(mycontainer)`.

If you need to extract a portion of the container or merge it with another, use
`template_data => mergedata("mycontainer[piece]", "othercontainer")`.

# Can I render a Mustache template into a string?

Yes, see `string_mustache()`.

# How do I render a section only if a given class is defined?

In this Mustache example the word 'Enterprise' will only be rendered if the
class 'enterprise' is defined.

This template should not be passed a data container; it uses the `datastate()`
of the CFEngine system. That's where `classes.enterprise` and
`vars.sys.cf_version` came from.

```
Version: CFEngine {{#classes.enterprise}}Enterprise{{/classes.enterprise}} {{vars.sys.cf_version}}
```

# How do I iterate over a list?

This template should not be passed a data container; it uses the `datastate()`
of the CFEngine system. That's where `vars.mon.listening_tcp4_ports` came from.

{% raw %}
```
{{#vars.mon.listening_tcp4_ports}}
  * {{.}}
{{/vars.mon.listening_tcp4_ports}}
```
{% endraw %}
