---
layout: default
title: Mustache templating
sorting: 90
---

## CFEngine specific extensions

CFEngine has several extensions to the mustache standard.

* `-top-` special key representing the complete data given.
* `%` variable prefix causing data to be rendered as multi-line json representation.
* `$` variable prefix causing data to be rendered as compact json representation.
* `@` expands the current key being iterated.

**See also:** [`template_method` `mustache` extensions][files#template_method mustache extensions]

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


## How do I render a section only if a given class is not defined?

In the mustache documentation this is referred to as an *inverted section*.

In this mustache example the word ```Enterprise``` will only be rendered if the
class ```cfengine_enterprise``` is defined and the word ```Community``` will
only be rendered if the class ```cfengine_enterprise``` is not defined.

This template should not be passed a data container; it uses the `datastate()`
of the CFEngine system. That's where `classes.cfengine_enterprise` and
`vars.sys.cf_version` came from.


```
Version: CFEngine {{#classes.cfengine_enterprise}}Enterprise{{/classes.cfengine_enterprise}}{{^classes.cfengine_enterprise}}Community{{/classes.cfengine_enterprise}} {{vars.sys.cf_version}}
```


## How do I use class expressions?

Mustache does not understand CFEngine's class expression logic and it is not
possible to use full class expressions in mustache templates. Instead, use class
expressions inside CFEngine policy to define a singular class which can be used
to conditionally render a block.


[%CFEngine_include_example(mustache_classes.cf)%]


## How do I iterate over a list?

This template should not be passed a data container; it uses the `datastate()`
of the CFEngine system. That's where `vars.mon.listening_tcp4_ports` came from.


```
{{#vars.mon.listening_tcp4_ports}}
  * {{.}}
{{/vars.mon.listening_tcp4_ports}}
```


## How can I access keys when iterating over a dict?

In CFEngine, the `@` symbol expands to the current key  when iterating over a dict.


[%CFEngine_include_example(mustache_extension_expand_key.cf)%]


## Can you use nested classes?

You can. This is handy when options slightly differ for different operating systems.
In this example for ssh daemon the authorized key configuration will only be added if
class `SSH_LDAP_PUBKEY_BUNDLE` is true and for the class debian/centos diffenrent
keywords are added.


```
{{#classes.SSH_LDAP_PUBKEY_BUNDLE}}
    {{#classes.debian}}
AuthorizedKeysCommand {{vars.sara_data.ssh.authorized_keys_command}}
AuthorizedKeysCommandUser {{vars.sara_data.ssh.authorized_keys_commanduser}}
    {{/classes.debian}}
    {{#classes.centos}}
AuthorizedKeysCommand {{vars.sara_data.ssh.authorized_keys_command}}
AuthorizedKeysCommandRunAs {{vars.sara_data.ssh.authorized_keys_commanduser}}
    {{/classes.centos}}
{{/classes.SSH_LDAP_PUBKEY_BUNDLE}}
```
