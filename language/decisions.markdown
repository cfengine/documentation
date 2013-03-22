### 1.7 Decisions

CFEngine decisions are made behind the scenes and the results of
certain true/false propositions are cached in Booleans referred to
as \`classes'. There are no if-then-else statements in CFEngine;
all decisions are made with classes.

Classes fall into hard (discovered) and soft (user-defined) types.
A single hard class can be one of several things:

-   [Hard classes](/manuals/cf3-Reference#Hard-classes)
-   [Class combination operators and precedence](/manuals/cf3-Reference#Class-combination-operators-and-precedence)
-   [Global and local classes](/manuals/cf3-Reference#Global-and-local-classes)




#### 1.7.1 CFEngine hard classes

CFEngine runs on every computer individually and each time it wakes
up the underlying generic agent platform discovers and classifies
properties of the environment or context in which it runs. This
information is cached and may be used to make decisions about
configuration[^1^](/manuals/cf3-Reference#fn-1).

Classes fall into hard (discovered) and soft (defined) types. A
single class can be one of several things:

-   The name of an operating system architecture e.g. `ultrix`,
    `sun4`, etc.
-   The unqualified name of a particular host (e.g., `www`). If
    your system returns a fully qualified domain name for your host
    (e.g., `www.iu.hio.no`), CFEngine will also define a hard class for
    the fully qualified name, as well as the partially-qualified
    component names `iu.hio.no`, `hio.no`, and `no`.
-   The name of a user-defined group of hosts.
-   A day of the week (in the form
    `Monday, Tuesday, Wednesday, ..`).
-   An hour of the day, in the current time zone (in the form
    `Hr00, Hr01 ... Hr23`).
-   An hour of the day GMT (in the form
    `GMT_Hr00, GMT_Hr01 ... GMT_Hr23`). This is consistent the world
    over, in case you need virtual simulteneity of change coordination.
-   Minutes in the hour (in the form `Min00, Min17 ... Min45`).
-   A five minute interval in the hour (in the form
    `Min00_05, Min05_10 ... Min55_00`).
-   A fifteen minute (quarter-hour) interval (in the form
    `Q1, Q2, Q3, Q4`).
-   An expression of the current quarter hour (in the form
    `Hr12_Q3`).
-   A day of the month (in the form `Day1, Day2, ... Day31`).
-   A month (in the form `January, February, ... December`).
-   A year (in the form `Yr1997, Yr2004`).
-   A shift in `Night,Morning,Afternoon,Evening`, which fall into
    six hour blocks starting at 00:00 hours.
-   A \`lifecycle index', which is the year number modulo 3 (in the
    form `Lcycle_0, Lcycle_1, Lcycle_2`, used in long term resource
    memory).
-   An arbitrary user-defined string (as specified in the `-D`
    command line option, or defined in a `classes` promise or body,
    `restart_class` in a `processes` promise, etc).
-   The IP address octets of any active interface (in the form
    `ipv4_192_0_0_1<!-- /@w -->`, `ipv4_192_0_0<!-- /@w -->`,
    `ipv4_192_0<!-- /@w -->`, `ipv4_192<!-- /@w -->`), provided they
    are not excluded by a regular expression in the file
    WORKDIR/inputs/ignore\_interfaces.rx.
-   The names of the active interfaces (in the form
    `net_iface_xl0`, `net_iface_vr0`).
-   System status and entropy information reported by
    `cf-monitord`.
-   On Solaris-10 systems, the zone name (in the form
    `zone_global, zone_foo, zone_baz`).

To see all of the classes defined on a particular host, run

         host# cf-promises -v

as a privileged user. Note that some of the classes are set only if
a trusted link can be established with cf-monitord, i.e. if both
are running with privilege, and the /var/cfengine/state/env\_data
file is secure. More information about classes can be found in
connection with `allclasses`.




#### 1.7.2 Class combination operators and precedence

Classes may be combined with the usual boolean operators, in the
usual precedence (AND binds stronger than OR). On addition the dot
may be used for AND to improve readability, or imply the
interpretation \`subset' or \`subclass'. In order of precedence:

‘()’
  ~ The parenthesis group operator.
‘!’
  ~ The NOT operator.
‘.’
  ~ The AND operator.
‘&’
  ~ The AND operator (alternative).
‘|’
  ~ The OR operator.
‘||’
  ~ The OR operator (alternative).

So the following expression would be only true on Mondays or
Wednesdays from 2:00pm to 2:59pm on Windows XP systems:

         
         (Monday|Wednesday).Hr14.WinXP::
         




#### 1.7.3 Global and local classes

User defined classes are mostly defined in bundles, but they are
used as a signalling mechanism between promises. We'll return to
those in a moment.

Classes promises define new classes based on combinations of old
ones. This is how to make complex decisions in CFEngine, with
readable results. It is like defining aliases for class
combinations. Such class \`aliases' may be specified in any kind of
bundle. Bundles of type `common` yield classes that are global in
scope, whereas in all other bundle types classes are local. Classes
are evaluated when the bundle is evaluated (and the bundles are
evaluated in the order specified in the `bundlesequence`). Consider
the following example.

    body common control
    {
    bundlesequence => { "g","tryclasses_1", "tryclasses_2" };
    }
    
    #################################
    
    
    bundle common g
    {
    classes:
    
      "one" expression => "any";
    
    }
    
    #################################
    
    
    bundle agent tryclasses_1
    {
    classes:
    
      "two" expression => "any";
    }
    
    #################################
    
    
    bundle agent tryclasses_2
    {
    classes:
    
      "three" expression => "any";
    
    reports:
    
      one.three.!two::
    
        "Success";
    }

Here we see that class ‘one’ is global (because it is defined
inside the `common` bundle), while classes ‘two’ and ‘three’ are
local (to their respective bundles). The report result \`Success'
is therefore true because only ‘one’ and ‘three’ are in scope (and
‘two’ is *not* in scope) inside of the third bundle.

Note that any class promise must have one - and only one - value
constraint. That is, you might not leave ‘expression’ in the
example above or add both ‘and’ and ‘xor’ constraints to the single
promise.

Another type of class definition happens when you define classes
based on the outcome of a promise, e.g. to set a class if a promise
is repaired, one might write:

     "promiser..."
    
        ...
    
        classes => if_repaired("signal_class");

These classes are global in scope. Finally `restart_class` classes
in `processes` are global.
