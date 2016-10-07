---
layout: default
title: services
published: true
tags: [reference, bundle agent, services, processes, services promises, promise types]
---

`services` type promises in their simplest *generic* form are an abstraction on
**bundles**. `services` type promises are implemented by mapping a bundle to
`service_bundle` in a `service_method` body. Reference the
[services bodies and bundles in the standard library][Services Bodies and Bundles].

Most commonly services type promises are use to manage standard operating system
services using the platforms standard service management tools via the
`standard_services` bundle in the standard library. However, services type
promises can be leveraged to build standard abstractions around custom services
as well.

Services are registered in the operating system in some way, and get a unique name.
Service promises abstracts the mechanism for interacting with services
on the given operating system, making it as uniform and easy as possible
to work with services cross-platform. The exact mechanism CFEngine uses
vary depending on availability at the OS, but it could be System V scripts,
systemd units, tools such as `chkconfig`, or the Windows API.

Some operating systems are bundled with a lot of unused services that
are running as default. At the same time, faulty or inherently insecure
services are often the cause of security issues. With CFEngine, one can
create promises stating the services that should be stopped and disabled.

The operating system may start a service at boot time, or it can be
started by CFEngine. Either way, CFEngine will ensure that the service
maintains the correct state (started, stopped, or disabled).

CFEngine supports the concept of dependencies between services,
and can automatically start or stop these, if desired. Parameters can be
passed to services that are started by CFEngine.

```cf3
    bundle agent example
    {
    services:

      "Dhcp"
        service_policy => "start",
        service_dependencies => { "Alerter", "W32Time" },
        service_method => winmethod;
    }

    body service_method winmethod
    {
      service_type => "windows";
      service_args => "--netmask=255.255.0.0";
      service_autostart_policy => "none";
      service_dependence_chain => "start_parent_services";
    }
```

**Note:** Services promises for Windows are only available in CFEngine
Enterprise. Windows Vista/Server 2008 and later introduced new complications
to the service security policy. Therefore, when testing `services`
promises from the command line, CFEngine may not be given proper access
rights, which gives errors like "Access is denied". However, when
running through the CFEngine Enterprise Executor service, typical for on
production machines, CFEngine has sufficient rights.

Services of type generic promises are implemented for all operating
systems and are merely as a convenient front-end to `processes` and
`commands`. If nothing else is specified, CFEngine looks for an special
reserved agent bundle called

```cf3
    bundle agent standard_services(service,state)
    {
    ...
    }
```

This bundle is called with two parameters: the name of the service and a
start/stop state variable. The CFEngine standard library defines many
common services for standard operating systems for convenience. If no
`service_bundle` is defined in a `service_method` body, then CFEngine
assumes the `standard_services` bundle to be the default source of action
for the services. This is executed just like a `methods` promise on the
service bundle, so this is merely a front-end.

The standard bundle can be replaced with another, as follows:

```cf3
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

    body service_method service_test
    {
      service_bundle => non_standard_services("$(this.promiser)","$(this.service_policy)");
    }

    bundle agent non_standard_services(service,state)
    {
    reports:

      !done::

        "Test service promise for \"$(service)\" -> $(state)";
    }
```

Note that the special variables [`$(this.promiser)`][this#this.promiser] and
[`$(this.service_policy)`][this#this.service_policy] may be used to fill in
the service and state parameters from the promise definition. The
[`$(this.service_policy)`][this#this.service_policy] variable is only defined
for services promises.

**History:** This promise type was introduced in CFEngine 3.3.0 (2012).

****

## Attributes ##

[%CFEngine_include_markdown(common-attributes-include.markdown)%]

### service_policy

**Description:** Policy for service status.

The `service_policy` is expected to be passed to the service bundle in order to
manage it's state. It is up to the mapped `service_bundle` to determine which
promises should be actuated in order to converge to the specified
`service_policy`.

Reference the policy for detailed information about the semantics of a given
`service_method` or `service_bundle`, for example the `standard_services` in the
standard library.

**Type:** `string`

**Allowed input range:** (arbitrary string)|(menu_option) depending on `service_type`

* When `service_type` is `windows` allowed values are limited to `start`,
  `stop`, `enable`, or `disable`.

   * **start|enable** :: Will start the service if it is not running. ```Startup
     Type``` will be set to ```Manual``` if it is not ```Automatic``` or
     ```Automatic (Delayed Start)```. For a service to be configured to start
     automatically on boot a `service_method` must be declared and
     `service_autostart_policy` must be set to ```boot_time```.

   * **stop** :: Will stop the service if it is running. ```Startup Type``` will
     not be modified unless a `service_method` is declared and
     `service_autostart_policy` is set.

   * **disable** :: Will stop the service if it is running, and ```Startup Type```
     will be set to ```Disabled```.


* When `service_type` is ```generic``` any string is allowed and
  `service_bundle` is responsible for interpreting and implementing the desired
  state based on the `service_policy` value.

  Historically `service_type` ```generic``` has supported ```start```,
  ```stop```, ```enable```, ```disable```, ```restart``` and ```reload```.


**Example:**

```cf3
bundle agent example
{
  services:

    redhat|centos::

      # Manage a service using the standard_services implementation from the
      # standard library.

      "httpd"
        service_policy => "disable";

    any::

      # Manage a custom service using custom service_method

      "myservice"
        service_policy => "my_custom_state",
        service_method => "my_custom_service_method";


    windows::

        "AdobeARMservice"
          service_policy => "stop",
          comment => "Ensure the Adobe Acrobat Update Service is not running. It
                      may or may not be automatically started on the next boot
                      depending on the configuration.";

        "CfengineNovaExec"
          service_policy => "enable",
          service_method => bootstart, # Ref stdlib
          comment => "Ensure cf-execd is running and configured to start on
                      boot.";

        "VBoxService"
          service_policy => "start",
          service_method => bootstart, # Ref stdlib
          comment => "Ensure VirtualBox Guest Additions Service is running and
                      configured to start on boot.";

        "Spooler"
          service_policy => "disable",
          comment => "Ensure the Print Spooler is not running and will not start
                      automatically on boot. We do not want to kill any trees.";

        "tzautoupdate"
          service_policy => "start",
          comment => "Ensure that the Auto Time Zone Updated is running, and set
                      Startup Type to Manual.";


}

body service_method my_custom_service_method
{

  windows::
    service_bundle => my_custom_service_method_windows( $(this.promiser), $(this.service_policy) );

  redhat|centos::
    service_bundle => my_custom_service_method_EL( $(this.promiser), $(this.service_policy) );

  debian|ubuntu::
    service_bundle => my_custom_service_method_DEB( $(this.promiser), $(this.service_policy) );
}

bundle agent my_custom_service_method_windows( service_identifier, desired_service_state )
{
  # Specific windows implementation
}

bundle agent my_custom_service_method_EL( service_identifier, desired_service_state )
{
  # Specific Redhat|Centos implementation
}

bundle agent my_custom_service_method_DEB( service_identifier, desired_service_state )
{
  # Specific Debian|Ubuntu implementation
}
```

**See Also:** [generic standard_services][Services Bodies and Bundles#standard_services]

**History:**

* Type changed from `menu_option` to `string` and allowed input range changed to
  arbitrary string from start|stop|enable|disable|restart|reload in CFEngine
  3.10. Previously enable was mapped to start, disable was mapped to stop and
  reload was mapped to restart.

### service_dependencies

**Description:** A list of services on which the named service abstraction
depends

A list of services that must be running before the service can be started.
These dependencies can be started automatically by CFEngine if they
are not running see `service_dependence_chain`. However, the dependencies will
never be implicitly stopped by CFEngine. Specifying dependencies is optional.

Note that the operating system may keep an additional list of dependencies for
a given service, defined during installation of the service. CFEngine
requires these dependencies to be running as well before starting
the service. The complete list of dependencies is thus the union of
`service_dependencies` and the internal operating system list.

**Type:** `slist`

**Allowed input range:** `[a-zA-Z0-9_$(){}\[\].:]+`

**Example:**

```cf3
services:

  "ftp"
    service_policy => "start",
    service_dependencies => { "network", "logging" };
```

### service_method

**Type:** `body service_method`

[%CFEngine_include_markdown(common-body-attributes-include.markdown)%]

`service_method` bodies have access to `$(this.promiser)` (the promised service)
and `$(this.service_policy)` (the policy state the service should have).

**Notes:** `service_bundle` is not used when `service_type` is ```windows```.

#### service_args

**Description:** Parameters for starting the service as command

These arguments will only be passed if CFEngine starts the service.
Thus, set `service_autostart_policy` to `none` to ensure that the
arguments are always passed.

Escaped quotes can be used to pass an argument containing spaces as a
single argument, e.g. `-f \"file name.conf\"`. Passing arguments is
optional.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body service_method example
     {
       service_args => "-f filename.conf --some-argument";
     }
```

#### service_autostart_policy

**Description:** Should the service be started automatically by the OS

Defaults to `none`, which means that the service is not registered for
automatic startup by the operating system in any way. It must be `none`
if `service_policy` is not `start`. `boot_time` means the service is
started at boot time, while `on_demand` means that the service is
dispatched once it is being used.

**Type:** (menu option)

**Allowed input range:**

```
    none
    boot_time
    on_demand
```

**Example:**

```cf3
     body service_method example
     {
       service_autostart_policy => "boot_time";
     }
```

**Notes:** `on_demand` is not supported by Windows, and is implemented through
inetd or xinetd on Unix.


#### service_bundle

**Type:** `bundle agent`

#### service_dependence_chain

**Description:** How to handle dependencies and dependent services

The service dependencies include both the dependencies defined by the
operating system and in `service_dependencies`, as described there.

Defaults to `ignore`, which means that CFEngine will never start or
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
will start A, if it is not running. On the other hand, if we want
to stop B, C needs to be stopped first. `stop_child_services` or
`all_related` means that CFEngine will stop C, if it is running.

**Type:** (menu option)

**Allowed input range:**

```
    ignore
    start_parent_services
    stop_child_services
    all_related
```

**Example:**

```cf3
     body service_method example
     {
       service_dependence_chain => "start_parent_services";
     }
```

#### service_type

**Description:** Service abstraction type

**Type:** (menu option)

**Allowed input range:**

```
    windows
    generic
```

**Example:**

```cf3
     body service_method example
     {
       service_type => "windows";
     }
```

**Notes:** On Windows this defaults to, and must be `windows`. Unix systems can
however have multiple means of registering services, but the choice must be
available on the given system. `service_bundle` is not used when `service_type`
is ```windows```.
