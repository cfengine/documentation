---
layout: default
title: Classes and Decisions
published: true
sorting: 50
tags: [manuals, language, syntax, concepts, classes, decisions]
---

Classes are used to apply promises only to particular environments, depending
on context. A promise might only apply to Linux systems, or should only be
applied on Sundays, or only when a
[variable][variables] has a certain value.

Classes are simply facts that represent the current state or context of a
system. The list of set classes classifies the environment at time of
execution.

Classes are either `set` or `not set`, depending on context. Classes fall into
**hard** classes that are discovered by CFEngine, and **soft** classes that are
user-defined.

Classes have either a `namespace` or `bundle` scoped. namespace scoped classes
are visible from any bundle. `bundle` scoped classes can only be checked within
that bundle or from a bundle called with inheritance. Hard classes always have a
namespace scope.

In [CFEngine Enterprise](https://cfengine.com/product-overview/), classes that are defined can be reported to the
CFEngine Database Server and can be used there for reporting, grouping of hosts
and inventory management. For more information about how this is configured please read the documentation on [Enterprise Reporting][].

## Listing Classes

To see the first order of `hard classes` and `soft classes` run `cf-promises
--show-classes` as a privileged user. Alternatively run `cf-agent
--show-evaluated-classes` to get the listing of classes at the end of the agent
execution. This will show additional namespace scoped classes that were defined
over the course of the agent execution. This output can be convenient for policy
testing.

Example:

```console
[root@hub masterfiles]# cf-promises --show-classes
Class name                                                   Meta tags
10_0_2_15                                                    inventory,attribute_name=none,source=agent,hardclass
127_0_0_1                                                    inventory,attribute_name=none,source=agent,hardclass
192.168.56_2                                                 inventory,attribute_name=none,source=agent,hardclass
1_cpu                                                        source=agent,derived-from=sys.cpus,hardclass
64_bit                                                       source=agent,hardclass
Afternoon                                                    time_based,source=agent,hardclass
Day22                                                        time_based,source=agent,hardclass
...
```

Note that some of the classes are set only if a trusted link can be established
with [`cf-monitord`][cf-monitord], i.e. if both are running with privilege, and
the `/var/cfengine/state/env_data` file is secure.

The `classesmatching()` function searches using a regular expression for classes
matching a given name and or tag.

**See also:** The ```--show-vars``` option for `cf-promises` and the
```--show-evaluated-vars``` option for `cf-agent`.

## Tags

Classes and variables have tags that describe their provenance (who
created them) and purpose (why were they created).

While you can provide your own tags for soft classes in policy with
the [`meta`][Promise Types#meta] attribute, there are some tags applied to hard classes and
other special cases.  This list may change in future versions of
CFEngine.

* `source=agent`: this hard class or variable was created by the agent in the C code.  This tag is useful when you need to find classes or variables that don't match the other sources below.  e.g. `linux`.
* `source=environment`: this hard class or variable was created by the agent in the C code.  It reflects something about the environment like a command-line option, e.g. `-d` sets `debug_mode`, `-v` sets `verbose_mode`, and `-I` sets `inform_mode`.  Another useful option, `-n`, sets `opt_dry_run`.
* `source=bootstrap`: this hard class or variable was created by the agent in the C code based on bootstrap parameters.  e.g. `policy_server` is set based on the IP address or host name you provided when you ran `cf-agent -B host-or-ip`.
* `source=module`: this class or variable was created through the module protocol.
* `source=persistent`: this persistent class was loaded from storage.
* `source=body`: this variable was created by a body with side effects.
* `source=function`: this class or variable was created by a function as a side effect, e.g. see the classes that `selectservers()` sets or the variables that `regextract()` sets.  These classes or variables will also have a `function=FUNCTIONNAME` tag.
* `source=promise`: this soft class was created from policy.
* `inventory`: related to the system inventory, e.g. the network interfaces
  * `attribute_name=none`: has no visual attribute name (ignored by Mission Portal)
  * `attribute_name=X`: has visual attribute name `X` (used by Mission Portal)
* `monitoring`: related to the monitoring (`cf-monitord` usually).
* `time_based`: based on the system date, e.g. `Afternoon`
* `derived-from=varname`: for a class, this tells you it was derived from a variable name, e.g. if the special variable `sys.fqhost` is `xyz`, the resulting class `xyz` will have the tag `derived-from=sys.fqhost`.
* `cfe_internal`: internal utility classes and variables

Enterprise only:

* `source=ldap`: this soft class or variable was created from an LDAP lookup.
* `source=observation`: this class or variable came from a `measurements` system observation and will also have the `monitoring` tag.

## Hard Classes

Hard classes are discovered by CFEngine. Each time it wakes up, it discovers
and reads properties of the environment or context in which it runs.It turns
these properties of the environment into classes. This information is
effectively cached and may be used to make decisions about configuration.

You can see all of the hard classes defined on a particular host by running the
following command as a privileged user.

```console
    $ cf-promises --show-classes|grep hardclass
```

These are classes that describe your operating system, the time of
day, the week of the year, etc. Time-varying classes (tagged with
`time_based`) will change if you do this a few times over the course
of a week.

* CFEngine-specific classes
    * `any`: this class is always set
    * `am_policy_hub`, `policy_server`: set when the file
      `$(workdir)/state/am_policy_hub` exists. When a host is [bootstrapped][cf-agent], if
      the agent detects that it is bootstrapping to itself the file is created.
    * `bootstrap_mode`: set when bootstrapping a host
    * `inform_mode`, `verbose_mode`, `debug_mode`: log verbosity levels in order of noisiness
    * `opt_dry_run`: set when the `--dry-run` option is given
    * `failsafe_fallback`: set when the base policy is invalid and the built-in `failsafe.cf` (see `bootstrap.c`) is invoked
    * (`community`, `community_edition`) and (`enterprise`, `enterprise_edition`): the two different CFEngine products, Community and Enterprise, can be distinguished by these mutually exclusive sets of hard classes
    * Component Specific Classes (each component has a class that is always considered defined by that component):
        * `cf-agent` :: ```agent```
        * `cf-serverd` :: ```server```
        * `cf-monitord` :: ```monitor```
        * `cf-execd` :: ```executor```
        * `cf-runagent` :: ```runagent```
        * `cf-key` :: ```keygenerator```
        * `cf-hub` :: ```hub```
        * `cf-promises` :: ```common```
* Operating System Classes (note that the presence of these classes doesn't imply platform support)
    * Operating System Architecture -  `arista`, `big_ip`, `debian`, `eos`, `fedora`, `Mandrake`, `Mandriva`, `oracle`, `redhat`, `slackware`, `smartmachine`, `smartos`, `solarisx86`, `sun4`, `SuSE`, `ubuntu`, `ultrix`, the always-favorite `unknown_ostype`, etc.
    * VM or hypervisor specific: `VMware`, `virt_guest_vz`, `virt_host_vz`, `virt_host_vz_vzps`, `xen`, `xen_dom0`, `xen_domu_hv`, `xen_domu_pv`, `oraclevmserver`, etc.
    * On Solaris-10 systems, the zone name (in the form `zone_global, zone_foo, zone_baz`).
    * Windows-specific: `DomainController`, `Win2000`, `WinServer`, `WinServer2003`, `WinServer2008`, `WinVista`, `WinWorkstation`, `WinXP`
    * `have_aptitude`, `powershell`, `systemd`: based on the detected capabilities of the platform or the compiled-in options
    * **See also:** `sys.arch`, `sys.class`, `sys.flavor`, `sys.os`, `sys.ostype`.
* Network Classes
    * Unqualified Name of Host. CFEngine truncates it at the first dot.
      Note: `www.sales.company.com` and `www.research.company.com` have the
      same unqualified name – `www`
    * The IPv4 address octets of any active interface (in the form
      `ipv4_192_0_0_1`, `ipv4_192_0_0`, `ipv4_192_0`, `ipv4_192`)
    * The IPv6 addresses of all active interfaces (with dots replaced by
      underscores, e.g. `ipv6_fe80__a410_6072_21eb_d3fa`) added in 3.7.8, 3.10.3, 3.12.0
    * User-defined Group of Hosts
    * `mac_unknown`: set when the MAC address can't be found
    * **See also:** `sys.domain`, `sys.hardware_addresses`, `sys.sys.host`, `sys.interface`, `sys.interfaces`, `sys.interface_flags`, `sys.ipv4`, `sys.ip_addresses`, `sys.fqhost`, `sys.uqhost`.
* Time Classes
    * note ALL of these have a local and a GMT version.  The GMT classes are consistent the world over, in case you need global change coordination.
    * Day of the Week - `Monday, Tuesday, Wednesday,...GMT_Monday, GMT_Tuesday, GMT_Wednesday,...`
    * Hour of the Day in Current Time Zone - `Hr00, Hr01,... Hr23` and `Hr0, Hr1,... Hr23`
    * Hour of the Day in GMT - `GMT_Hr00, GMT_Hr01, ...GMT_Hr23` and `GMT_Hr0, GMT_Hr1, ...GMT_Hr23`.
    * Minutes of the Hour - `Min00, Min17,... Min45,...` and `GMT_Min00, GMT_Min17,... GMT_Min45,...`
    * Five Minute Interval of the Hour - `Min00_05, Min05_10,... Min55_00` and `GMT_Min00_05, GMT_Min05_10,... GMT_Min55_00`.  Note the second number indicates *up to* what minute the interval extends and does not include that minute.
    * Quarter of the Hour - `Q1, Q2, Q3, Q4` and `GMT_Q1, GMT_Q2, GMT_Q3, GMT_Q4`
    * An expression of the current quarter hour - `Hr12_Q3` and `GMT_Hr12_Q3`
    * Day of the Month - `Day1, Day2,... Day31` and `GMT_Day1, GMT_Day2,... GMT_Day31`
    * Month - `January, February,... December` and `GMT_January, GMT_February,... GMT_December`
    * Year - `Yr1997, Yr2004` and `GMT_Yr1997, GMT_Yr2004`
    * Period of the Day - `Night, Morning, Afternoon, Evening` and `GMT_Night, GMT_Morning, GMT_Afternoon, GMT_Evening` (six hour blocks starting at 00:00 hours).
    * Lifecycle Index - `Lcycle_0, Lcycle_1, Lcycle_2` and `GMT_Lcycle_0, GMT_Lcycle_1, GMT_Lcycle_2` (the year number modulo 3, used in long term resource memory).
    * **See also:** `sys.cdate`, `sys.date`.

-   The unqualified name of a particular host (e.g., `www`). If
    your system returns a fully qualified domain name for your host
    (e.g., `www.iu.hio.no`), CFEngine will also define a hard class for
    the fully qualified name, as well as the partially-qualified
    component names `iu.hio.no`, `hio.no`, and `no`.
    * **See also:** `sys.fqhost`, `sys.uqhost`.
-   An arbitrary user-defined string (as specified in the `-D`
    command line option, or defined in a [`classes` promise][classes] promise or
    [`classes` body][Promise Types#classes],
    `restart_class` in a `processes` promise, etc).
-   The IP address octets of any active interface (in the form
    `ipv4_192_0_0_1<!-- /@w -->`, `ipv4_192_0_0<!-- /@w -->`,
    `ipv4_192_0<!-- /@w -->`, `ipv4_192<!-- /@w -->`), provided they
    are not excluded by a regular expression in the file
    `WORKDIR/inputs/ignore_interfaces.rx`.
-   The names of the active interfaces (in the form
    `net_iface_xl0`, `net_iface_vr0`).
-   System status and entropy information reported by
    `cf-monitord`.

## Soft Classes

Soft classes are user-defined classes which you can use to implement your own
classifications.

Soft classes can be set by using the `-D` or `--define` options wihtout having
to edit the policy. Multiple classes can be defined by separating them with
commas (no spaces).

```console
$ cf-agent -Dclass
```

or

```console
$ cf-agent --define class1,class2,class3
```

This can be especially useful when requesting a remote host to run its policy
by using `cf-runagent` to activate policy that is normally dormant.

```console
$ cf-runagent -Demergency_evacuation -H remoteclient
```

If you're using dynamic inputs this can be useful in combination with
`cf-promises` to ensure that various input combinations syntax is validated
correctly. Many people will have this run by pre-commit hooks or as part of a
continuous build system like [Jenkins](http://jenkins-ci.org/) or
[Bamboo](https://www.atlassian.com/software/bamboo).

```console
$ cf-promises -f ./promises.cf -D prod
$ cf-promises -f ./promises.cf -D dev
./promises.cf:10:12: error: syntax error
   "global1" expression => "any";
           ^
./promises.cf:10:12: error: Check previous line, Expected ';', got '"global1"'
   "global1" expression => "any";
           ^
./promises.cf:10:23: error: Expected promiser string, got 'expression'
   "global1" expression => "any";
                      ^
./promises.cf:10:26: error: Expected ';', got '=>'
   "global1" expression => "any";
                         ^
2014-05-22T13:46:05+0000    error: There are syntax errors in policy files
```

*Note*: Classes, once defined, will stay defined either for as long as the
bundle is evaluated (for classes with a `bundle` scope) or until the agent
exits (for classes with a `namespace` scope). See `cancel_kept`,
`cancel_repaired`, and `cancel_notkept` in classes body.


This example defines a few soft classes local to the `myclasses` bundle.

```cf3
bundle agent myclasses
{
classes:
  "always";
  "always2" expression => "any";
  "solinux" expression => "linux||solaris";
  "alt_class" or => { "linux", "solaris", fileexists("/etc/fstab") };
  "oth_class" and => { fileexists("/etc/shadow"), fileexists("/etc/passwd") };

reports:
  alt_class::
    # This will only report "Boo!" on linux, solaris, or any system
    # on which the file /etc/fstab exists
    "Boo!";
}
```

* The `always` and `always2` soft classes are always defined.

* The `solinux` soft class is defined as a combination of the `linux` or the
  `solaris` hard classes. This class will be set if the operating
  system family is either of these values.

* The `alt_class` soft class is defined as a combination of `linux`,
  `solaris`, or the presence of a file named `/etc/fstab`. If one of the two
  hard classes evaluate to true, or if there is a file named `/etc/fstab`, the
  `alt_class` class will also be set.

* The `oth_class` soft class is defined as the combination of two `fileexists`
  functions - `/etc/shadow` and `/etc/passwd`.  If both of these files are
  present the `oth_class` class will also be set.



### Negative Knowledge

If a class is set, then it is certain that the corresponding fact is true.
However, that a class is not set could mean that something is not the case, or
that something is simply not known. This is only a problem with soft classes,
where the state of a class can change during the execution of a policy,
depending on the [order][normal ordering] in which bundles and promises are
evaluated.

## Making Decisions based on classes

Class guards are the most common way to restrict a promise to a specific context. Once stated the restriction applies until a new context is specified. A new promise type automatically resets to an unrestricted context (the unrestricted context is typically referred to as `any`). 

This example illustrates how a class guard applies (to multiple promises) until a new context is specified.

[%CFEngine_include_example(classes_context_applies_multiple_promises.cf)%]

Another Example:

```cf3
bundle agent greetings
{
  reports:
    Morning::
      "Good morning!";

    Evening::
      "Good evening!";

      "! any"::
      "This report won't ever be seen.";

      # whitespace allowed only in 3.8 and later
      Friday . Evening::
      "It's Friday evening, TGIF!";

      "Monday . Evening"::
      "It's Monday evening.";
}
```

In this example, the report "Good morning!" is only printed if the class
`Morning` is set, while the report "Good evening!" is only printed when the
class `Evening` is set.

The `"! any"` context will never be evaluated. Note that since
CFEngine 3.8 context expressions can contain spaces for legibility.

The `"Monday . Evening"` context will only be true on Monday evenings.
The `Friday . Evening` context will only be true on Friday evenings.
See below for more on context operators.

Sometimes it's convenient to put class names in variables. This
example shows two ways to execute code conditionally based on such
variables:

```cf3
    bundle agent greetings
    {
     vars:
      "myclassname" string => "Evening";

      reports:
       "$(myclassname)"::
         "Good evening!";

       "any"::
         "Good evening too!" if => "$(myclassname)";
    }
```



As you saw above, the class predicate `if` (`unless` is also available)
can be used if variable class expressions are required.
It is `AND`ed with the normal class expression, and is
evaluated together with the promise. Both may contain variables as long
as the resulting expansion is a legal class expression.

```cf3
    bundle agent example
    {
      vars:
              "french_cities"  slist => { "toulouse", "paris" };
              "german_cities"  slist => { "berlin" };
              "italian_cities" slist => { "milan" };
              "usa_cities"     slist => { "lawrence" };

              "all_cities" slist => { @(french_cities), @(german_cities), @(italian_cities), @(usa_cities) };

      classes:
          "italy"   or => { @(italian_cities) };
          "germany" or => { @(german_cities) };
          "france"  or => { @(french_cities) };

      reports:
        "It's $(sys.date) here";

        Morning.italy::
          "Good morning from Italy",
            if => "$(all_cities)";

        Afternoon.germany::
          "Good afternoon from Germany",
            if => "$(all_cities)";

        france::
          "Hello from France",
            if => "$(all_cities)";

        france::
          "IMPOSSSIBLE!  THIS WILL NOT PRINT!!!",
            unless => "france";

        "$(all_cities)"::
          "Hello from $(all_cities)";

        "Hello from $(all_cities), if edition",
          if => "$(all_cities)";
    }
```

Example Output:

```
    cf-agent -Kf example.cf -D lawrence -b example
    R: It's Tue May 28 16:47:33 2013 here
    R: Hello from lawrence
    R: Hello from lawrence, if edition

    cf-agent -Kf example.cf -D paris -b example
    R: It's Tue May 28 16:48:18 2013 here
    R: Hello from France
    R: Hello from paris
    R: Hello from paris, if edition

    cf-agent -Kf example.cf -D milan -b example
    R: It's Tue May 28 16:48:40 2013 here
    R: Hello from milan
    R: Hello from milan, if edition

    cf-agent -Kf example.cf -D germany -b example
    R: It's Tue May 28 16:49:01 2013 here

    cf-agent -Kf example.cf -D berlin -b example
    R: It's Tue May 28 16:51:53 2013 here
    R: Good afternoon from Germany
    R: Hello from berlin
    R: Hello from berlin, if edition
```


In this example, lists of cities are defined in the `vars` section and these
lists are combined into a list of all cities. These variable lists are used to
qualify the greetings and to make the policy more concise. In the [`classes`][classes]
section a country class is defined if a class described on the right hand side
evaluates to true. In the reports section the current time is always reported
but only agents found to have the `Morning` and `italy` classes defined will
report "Good morning from Italy", this is further qualified by ensuring that
the report is only generated if one of the known cities also has a class
defined.

**Note:** Classes are automatically canonified when they are defined. Classes
are not automatically canonified when they are checked.


This example shows how classes are automatically canonified when they are
defined and that you must explicitly canonify when verifying classes.

[%CFEngine_include_example(class-automatic-canonificiation.cf)%]


## Operators and Precedence

Classes promises define new classes based on combinations of old ones. This is
how to make complex decisions in CFEngine, with readable results. It is like
defining aliases for class combinations. Such class 'aliases' may be specified
in any kind of bundle.

Since CFEngine 3.8, whitespace is **allowed** between operators. It
was not allowed up to 3.7.

For example `a . b` is equivalent to `a.b` and perhaps more readable.

Classes may be combined with the operators listed here in order from highest
to lowest precedence:

* ‘()'::
    ~ The parenthesis group operator.

* ‘!’::
    ~ The NOT operator.

* ‘.’::
    ~ The AND operator.

* ‘&’::
    ~ The AND operator (alternative).

* ‘|’::
    ~ The OR operator.

* ‘||’::
    ~ The OR operator (alternative).

These operators can be combined to form complex expressions.  For example, the
following expression would be only true on Mondays or Wednesdays from 2:00pm
to 2:59pm on Windows XP systems:

    (Monday|Wednesday).Hr14.WinXP::

### Operands that are functions

If an operand is another function and the return value of the function is
undefined, the result of the logical operation will also be undefined.
For this reason, when using functions as operators, it is safer to collapse
the functions down to scalar values and to test if the values are either
true or false before using them as operands in a logical expression.

e.g.

```cf3
    ...
    classes:
            "variable_1"
            expression => fileexists("/etc/aliases.db");
    ...

    "result"
    or => { isnewerthan("/etc/aliases", "/etc/aliases.db"),
    "!variable_1" };
```

The function, `isnewerthan` can return "undefined" if one or other of the files
does not exist. In that case, result would also be undefined. By checking the
validity of the return value before using it as an operand in a logical expression,
unpredictable results are avoided. i.e negative knowledge does not necessarily
imply that something is not the case, it could simply be unknown. Checking if
each file exists before calling `isnewerthan` would avoid this problem.

### Operands that are JSON booleans

If an operand is `true` it will succeed, **even though there doesn't have to be
a class named** `true`. If an operand is `false` it will fail, **even though
there may be a class named** `false`. This allows JSON booleans from data
containers to be used in context expressions:

```cf3
bundle agent main
{
    vars:
      "checks" data => '[true, false]';
      # find all classes named
      "classes_named_true" slist => classesmatching('true');

  classes:
      # always defined
      "first_check" expression => "$(checks[0])";
      # never defined
      "second_check" expression => "$(checks[1])";

  reports:
      # prints nothing, there are no classes named 'true'
      "Classes named 'true': $(classes_named_true)";

    first_check::
      "The class was defined from '$(checks[0])'";
    !first_check::
      "The class was NOT defined from '$(checks[0])'";
    second_check::
      "The class was defined from '$(checks[1])'";
    !second_check::
      "The class was NOT defined from '$(checks[1])'";
}
```

Output:

```
R: The class was defined from 'true'
R: The class was NOT defined from 'false'
```

## Class scope

Classes defined by classes type promises in bundles of type `common` are
`namespace` scoped by default (globally available, can be seen from any bundle),
whereas classes defined in all other bundle types are local aka `bundle` scoped
(they can not be seen from other bundles). Classes are evaluated when the bundle
is evaluated (and the bundles are evaluated in the order specified in the
`bundlesequence`).

Note that any class promise must have one - and only one - value constraint.
That is, you may not leave [`expression`][classes#expression] in the example
above and add [`and`][classes#and] or [`xor`][classes#xor] constraints to the
single promise.

Additionally classes can be defined or undefined as the result of a promise by
using a [classes body][Promise Types#classes]. To set a class if
a promise is repaired, one might write:

```cf3
     "promiser..."
        ...
        classes => if_repaired("signal_class");
```

These classes are `namespace` scoped by default. The
[`scope`][Promise Types#scope] attribute can be used to make them
local to the bundle.

It is recommended to use bundle scoped classes whenever possible. This example
will define ```signal_class``` prefixed classes with a suffix matching the
promise outcome (```_kept```, ```_repaired```, ```_notkept```).

```cf3
     "promiser..."
        ...
        classes => results("bundle", "signal_class");

    reports:

      signal_class_repaired::
        "Some aspect of the promise was repaired.";
        "The agent made a change to take us closer to the desired state";

      signal_class_kept::
        "Some aspect of the promise was kept";

      signal_class_notkept::
        "Some aspect of the promsie was unable to be repaired";

      signal_class_kept.signal_class_notkept::
        "All promise aspects were as desired";
```

Classes defined by the [module protocol][commands#module] are `namespace`
scoped.

Finally, `restart_class` classes in `processes` are global.

### Class Scopes: A More Complex Example

```cf3
    body common control
    {
        bundlesequence => { "global","local_one", "local_two" };
    }

    #################################

    bundle common global
    {
        classes:
            # The soft class "zero" is always satisfied,
            # and is global in scope
            "zero" expression => "any";
    }

    #################################

    bundle agent local_one
    {
        classes:
            # The soft class "one" is always satisfied,
            # and is local in scope to local_one
            "one" expression => "any";
    }

    #################################

    bundle agent local_two
    {
        classes:
            # The soft class "two" is always satisfied,
            # and is local in scope to ls_2
            "two" expression => "any";

        reports:
            zero.!one.two::
                # This report will be generated
                "Success";
    }
```

In this example, there are three bundles. One common bundle named `global`
with a global scope. Two agent bundles define classes `one` and `two` which
are local to those bundles.

The `local_two` bundle promises a report "Success" which applies only if
`zero.!one.two` evaluates to true. Within the `local_two` scope this evaluates
to `true` because the `one` class is not set.

## Persistence

By default classes are re-computed on each agent execution. Once a class has
been defined, it persists until the end of that agent execution. Persistent classes
are always global and can not be set to local by **scope** directive. Classes can
persist for a period of time. This can be useful to avoid the expense of
re-evaluation, communicate states across multiple agent runs on the same host.

The standard library in the Masterfiles Policy Framework contains
the [`feature`][lib/feature.cf] bundle which implements a useful model for
defining classes for a period of time as well as canceling them on demand.

**See also:** [`persistance` classes attribute][classes#persistence], [`persist_time` in classes body][Promise Types#persist_time], [`lib/event.cf`][lib/event.cf] in the MPF, [`lib/feature.cf`][lib/feature.cf] in the MPF

## Canceling classes

You can cancel a class with a [`classes`][Promise Types#classes] body.
See the `cancel_kept`, `cancel_notkept`, and `cancel_repaired` attributes.

