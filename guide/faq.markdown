---
layout: default
title: FAQ
published: true
sorting: 90
tags: [getting started, installation, enterprise, faq]
---

{:toc}

* [Enterprise Installation][#Enterprise Installation and Configuration]
	* [What steps should I take after installing CFEngine Enterprise?][#What steps should I take after installing CFEngine Enterprise]
	* [Can I use an existing PostgreSQL installation?][#Can I use an existing PostgreSQL installation]
	* [What is the system user for the CFEngine dedicated PostgreSQL database?][#What is the system user for the CFEngine dedicated PostgreSQL database and Apache server]
	* [Do I need experience with PostgreSQL?][#Do I need experience with PostgreSQL]
	* [What are the requirements for installing CFEngine Enterprise?][#What are the requirements for installing CFEngine Enterprise]
* [Enterprise Scalability][#Enterprise Scalability]
    * [ Is it normal to have many cf-hub processes running?][#Is it normal to have many cf-hub processes running]
* [Agent Email Reports][#Agent Email Reports]
	* [How do I set the email where agent reports are sent?][#How do I set the email where agent reports are sent]
	* [How do I disable agent email output?][#How do I disable agent email output]
* [Policy Writing][#Policy Writing]
  * [How do I pass a data type variable?][#How do I pass a data type variable]

### Enterprise Installation and Configuration ###

#### What steps should I take after installing CFEngine Enterprise ####

There are general steps to be taken outlined in [Post-Installation Configuration][General Installation#Post-Installation Configuration].

In addition to this, Enterprise 3.6 uses the local mail relay, and it is assumed that the server where CFEngine Enterprise is installed on has proper mail setup.

The default FROM email for all emails sent from the Mission Portal is currently admin@organization.com. This can be changed on the CFEngine Hub in `/var/cfengine/httpd/htdocs/application/config/appsettings.php:$config['appemail']`.

#### Can I use an existing PostgreSQL installation ####

No.  Although CFEngine keeps its assumptions about Postgres to a bare minimum,
CFEngine should use a dedicated PostgreSQL database instance to ensure there is
no conflict with an existing installation.

#### Do I need experience with PostgreSQL ####

PostgreSQL is highly configurable and you should have some in-house
expertise to properly configure your database installation. The
defaults are well tuned for common cases but you may find
optimizations depending on your hardware and OS.

#### What is the system user for the CFEngine dedicated PostgreSQL database and Apache server ####

Starting with CFEngine 3.6 there will be a system user called ```cfpostgres``` for running the dedicated CFEngine PostgreSQL database
installation.

Similarly there will be a ```cfapache``` system user for the Apache web server.

#### What are the requirements for installing CFEngine Enterprise ####

##### General Information #####

* [Pre-Installation Checklist][Pre-Installation Checklist]
* [Supported Platforms and Versions][Supported Platforms and Versions]

##### Users and Permissions #####

* CFEngine Enterprise makes an attempt to create the local users ```cfapache``` and ```cfpostgres```, as well as group ```cfapache``` when installing 3.6. The server must allow creation of these users and groups.


### Enterprise Scalability ###

See: [Enterprise Scalability][Best Practices#Scalability]

#### Is it normal to have many cf-hub processes running

* Yes, it is expected to have ~ 50 cf-hub processes running on your hub

### Agent Email Reports ###

#### How do I set the email where agent reports are sent ####

The agent report email functionality is configured in `body executor control`
https://github.com/cfengine/masterfiles/blob/master/controls/cf_execd.cf. It
defaults to `root@$(def.domain)` which is configured in `bundle common def`
https://github.com/cfengine/masterfiles/blob/master/def.cf.

For details see [domain][The Policy Framework#domain (variable)].

#### How do I disable agent email output ####

You can simply remove or comment out the settings.

In 3.6.x there is a convenience class `cfengine_internal_agent_email` avaiable
in `bundle common def` to switch on/off agent email.

For details see [cfengine_internal_agent_email][The Policy Framework#cfengine_internal_agent_email (class)].

### Mustache Templating ###

#### How can I pass a data variable to template_data? ####

Just use `template_data => @(mycontainer)`.

If you need to extract a portion of the container or merge it with another, use
`template_data => mergedata("mycontainer[piece]", "othercontainer")`.

#### Can I render a Mustache template into a string? ####

Yes, see `string_mustache()`.

#### How do I render a section only if a given class is defined? ####

In this Mustache example the word 'Enterprise' will only be rendered if the class 'enterprise' is defined.

This template should not be passed a data container; it uses the `datastate()` of the CFEngine system.  That's where `classes.enterprise` and `vars.sys.cf_version` came from.

```
Version: CFEngine {{#classes.enterprise}}Enterprise{{/classes.enterprise}} {{vars.sys.cf_version}}
```

#### How do I iterate over a list? ####

This template should not be passed a data container; it uses the `datastate()` of the CFEngine system.  That's where `vars.mon.listening_tcp4_ports` came from.

{% raw %}
```
{{#vars.mon.listening_tcp4_ports}}
  * {{.}}
{{/vars.mon.listening_tcp4_ports}}
```
{% endraw %}

### How do I ensure that a local user is locked? ###

To ensure that a local user exists but is locked (for example a service
account) simply specify `policy => "locked"`.

[%CFEngine_include_snippet(users_type.cf, ### Locked User BEGIN ###, ### Locked User END ###)%]

## Policy Writing ##

Common questions asked about policy writing.

### How do I pass a data type variable ###

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
