---
layout: default
title: services-in-agent-promises
categories: [Bundles-for-agent,services-in-agent-promises]
published: true
alias: Bundles-for-agent-services-in-agent-promises.html
tags: [Bundles-for-agent,services-in-agent-promises]
---

### `services` promises in agent

\
 A service is a set of zero or more processes. It can be zero if the
service is not currently running. Services run in the background, and do
not require user intervention.

Service promises may be viewed as an abstraction of process and commands
promises. An important distinguisher is however that a single service
may consist of multiple processes. Additionally, services are registered
in the operating system in some way, and get a unique name. Unlike
processes and commands promises, this makes it possible to use the same
name both when it is running and not.

Some operating systems are bundled with a lot of unused services that
are running as default. At the same time, faulty or inherently insecure
services are often the cause of security issues. With CFEngine, one can
create promises stating the services that should be stopped and
disabled.

The operating system may start a service at boot time, or it can be
started by CFEngine. Either way, CFEngine will ensure that the service
maintains the correct state (started, stopped, or disabled). On some
operating systems, CFEngine also allows services to be started on
demand, when they are needed. This is implemented though the `inetd` or
`xinetd` daemon on Unix. Windows does not support this.

CFEngine also allows for the concept of dependencies between services,
and can automatically start or stop these, if desired. Parameters can be
passed to services that are started by CFEngine.

\

~~~~ {.verbatim}
bundle agent example
{
services:

  "Dhcp"
    service_policy => "start",
    service_dependencies => { "Alerter", "W32Time" },
    service_method => winmethod;
}
 
########################################################

body service_method winmethod
{
  service_type => "windows";
  service_args => "--netmask=255.255.0.0";
  service_autostart_policy => "none";
  service_dependence_chain => "start_parent_services";
}
~~~~

\

Services promises for Windows are only available in CFEngine Nova and
above. Windows Vista/Server 2008 and later introduced new complications
to the service security policy. Therefore, when testing `services`
promises from the command line, CFEngine may not be given proper access
rights, which gives errors like "Access is denied". However, when
running through the CFEngine Nova Executor service, typical for on
production machines, CFEngine has sufficient rights.

Services of type generic promises are implemented for all operating
systems and are merely as a convenient front-end to `processes` and
`commands`. If nothing else is specified, CFEngine looks for an special
reserved agent bundle called

~~~~ {.verbatim}
bundle agent standard_services(service,state)
{
...
}
~~~~

This bundle is called with two parameters: the name of the service and a
start/stop state variable. The CFEngine standard library defines many
common services for standard operating systems for convenience. If no
`service_bundle` is defined in a `service_method` body, then CFEngine
assumes the standard\_services bundle to be the default source of action
for the services. This is executed just like a `methods` promise on the
service bundle, so this is merely a front-end.

The standard bundle can be replaced with another, as follows:

~~~~ {.verbatim}
body common control
{
bundlesequence => { "test" };
}

#

bundle agent test
{
vars:

 "mail" slist => { "spamassassin", "postfix" };


services:

  "www" service_policy => "start",
        service_method => service_test;


  "$(mail)" service_policy => "stop",
        service_method => service_test;
}

#

body service_method service_test
{
service_bundle => non_standard_services("$(this.promiser)","$(this.service_policy)");
}

#

bundle agent non_standard_services(service,state)
{
reports:

  !done::

    "Test service promise for \"$(service)\" -> $(state)";
}
~~~~

Note that the special variables `$(this.promiser)` and
`$(this.service_policy)` may be used to fill in the service and state
parameters from the promise definition. The `$(this.service_policy)`
variable is only defined for services promises.

-   [service\_policy in services](#service_005fpolicy-in-services)
-   [service\_dependencies in
    services](#service_005fdependencies-in-services)
-   [service\_method in services](#service_005fmethod-in-services)

#### `service_policy`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               start
               stop
               disable
               restart
               reload
~~~~

**Synopsis**: Policy for cfengine service status

**Example**:\
 \

~~~~ {.verbatim}
services:
  
  "Telnet"
     service_policy => "disable";
~~~~

**Notes**:\
 \

If set to `start`, CFEngine Nova will keep the service in a running
state, while `stop` means that the service is kept in a stopped state.
`disable` implies `stop`, and ensures that the service can not be
started directly, but needs to be enabled somehow first (e.g. by
changing file permissions).

#### `service_dependencies`

**Type**: slist

**Allowed input range**: `[a-zA-Z0-9_$(){}\[\].:]+`

**Synopsis**: A list of services on which the named service abstraction
depends

**Example**:\
 \

~~~~ {.verbatim}
services:
  
  "ftp"
    service_policy => "start",
    service_dependencies => { "network", "logging" };
~~~~

**Notes**:\
 \

A list of services that must be running before the service can be
started. These dependencies can be started automatically by CFEngine
Nova if they are not running see `service_dependence_chain`. However,
the dependencies will never be implicitly stopped by CFEngine Nova.
Specifying dependencies is optional.

Note that the operating system may keep an additional list of
dependencies for a given service, defined during installation of the
service. CFEngine Nova requires these dependencies to be running as well
before starting the service. The complete list of dependencies is thus
the union of `service_dependencies` and the internal operating system
list.

#### `service_method` (body template)

**Type**: (ext body)

`service_args`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Parameters for starting the service as command

**Example**:\
 \

~~~~ {.verbatim}
     
     body service_method example
     {
       service_args => "-f filename.conf --some-argument";
     }
     
~~~~

**Notes**:\
 \

These arguments will only be passed if CFEngine Nova starts the service.
Thus, set `service_autostart_policy` to `none` to ensure that the
arguments are always passed.

Escaped quotes can be used to pass an argument containing spaces as a
single argument, e.g. "-f \\"file name.conf\\"". Passing arguments is
optional. \

`service_autostart_policy`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    none
                    boot_time
                    on_demand
~~~~

**Synopsis**: Should the service be started automatically by the OS

**Example**:\
 \

~~~~ {.verbatim}
     
     body service_method example
     {
       service_autostart_policy => "boot_time";
     }
     
~~~~

**Notes**:\
 \

Defaults to `none`, which means that the service is not registered for
automatic startup by the operating system in any way. It must be `none`
if `service_policy` is not `start`. `boot_time` means the service is
started at boot time, while `on_demand` means that the service is
dispatched once it is being used.

`on_demand` is not supported by Windows, and is implemented through
inetd or xinetd on Unix. \

`service_bundle`

**Type**: (ext bundle) (Separate Bundle) \

`service_dependence_chain`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    ignore
                    start_parent_services
                    stop_child_services
                    all_related
~~~~

**Synopsis**: How to handle dependencies and dependent services

**Example**:\
 \

~~~~ {.verbatim}
     
     body service_method example
     {
       service_dependence_chain => "start_parent_services";
     }
     
~~~~

**Notes**:\
 \

The service dependencies include both the dependencies defined by the
operating system and in `service_dependencies`, as described there.

Defaults to `ignore`, which means that CFEngine Nova will never start or
stop dependencies or dependent services, but fail if dependencies are
not satisfied. `start_parent_services` means that all dependencies of
the service will be started if they are not already running. When
stopping a service, `stop_child_services` means that other services that
depend on this service will be stopped also. `all_related` means both
`start_parent_services` and `stop_child_services`.

Note that this setting also affects dependencies of dependencies and so
on.

For example, consider the case where service A depends on B, which
depends on C. If we want to start B, we must first make sure A is
running. If `start_parent_services` or `all_related` is set, CFEngine
Nova will start A, if it is not running. On the other hand, if we want
to stop B, C needs to be stopped first. `stop_child_services` or
`all_related` means that CFEngine Nova will stop C, if it is running. \

`service_type`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    windows
                    generic
~~~~

**Synopsis**: Service abstraction type

**Example**:\
 \

~~~~ {.verbatim}
     
     body service_method example
     {
       type => "windows";
     }
     
~~~~

**Notes**:\
 \

On Windows this defaults to, and must be `windows`. Unix systems can
however have multiple means of registering services, but the choice must
be available on the given system.
