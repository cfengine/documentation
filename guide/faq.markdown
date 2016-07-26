---
layout: default
title: FAQ
published: true
sorting: 90
tags: [getting started, installation, enterprise, faq]
---

# Mustache Templating

## How can I pass a data variable to template_data?

Just use `template_data => @(mycontainer)`.

If you need to extract a portion of the container or merge it with another, use
`template_data => mergedata("mycontainer[piece]", "othercontainer")`.

## Can I render a Mustache template into a string?

Yes, see `string_mustache()`.

## How do I render a section only if a given class is defined?

In this Mustache example the word 'Enterprise' will only be rendered if the
class 'enterprise' is defined.

This template should not be passed a data container; it uses the `datastate()`
of the CFEngine system. That's where `classes.enterprise` and
`vars.sys.cf_version` came from.

```
Version: CFEngine {{#classes.enterprise}}Enterprise{{/classes.enterprise}} {{vars.sys.cf_version}}
```

## How do I iterate over a list?

This template should not be passed a data container; it uses the `datastate()`
of the CFEngine system. That's where `vars.mon.listening_tcp4_ports` came from.

{% raw %}
```
{{#vars.mon.listening_tcp4_ports}}
  * {{.}}
{{/vars.mon.listening_tcp4_ports}}
```
{% endraw %}

## Policy Writing ##

Common questions asked about policy writing.

# How do I ensure that a local user is locked?

To ensure that a local user exists but is locked (for example a service
account) simply specify `policy => "locked"`.

[%CFEngine_include_snippet(users_type.cf, ### Locked User BEGIN ###, ### Locked User END ###)%]

# How do I pass a data type variable?

Data type variables also known as "data containers" are passed using the same
syntax as passing a list.

```cf3
bundle agent example
{
  vars:
    # First you must have a data type variable, define it inline or read from a
    # file using `readjson()`.
    "data" data => parsejson('[ { "x": 1 }, { "y": 2 } ]');

  methods:
    "use data"
      usebundle => use_data(@(data));
}

bundle agent use_data(dc)
{
  vars:
    # Use the data
    # Get its keys, or its index
    "dc_index" slist => getindices(dc);

  classes:
    "have_x" expression => isvariable("dc[$(dc_index)][x]");
    "have_z" expression => isvariable("dc[$(dc_index)][z]");

  reports:
    "CFEngine version '$(sys.cf_version)'";
    have_x::
      "Index '$(dc_index)' has key for x";

    have_z::
      "Index '$(dc_index)' has key for z";
}
```

```console
$ cf-agent -Kf ./example.cf -b example
R: CFEngine version '3.6.4'
R: Index '0' has key for x
R: Index '1' has key for x
```
