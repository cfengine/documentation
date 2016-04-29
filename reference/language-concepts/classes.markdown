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
user-defined. Refer to [Hard and Soft Classes][Hard and Soft Classes] in the **Reference**
section for more information.

In [CFEngine Enterprise][], the list of set classes is
reported to the CFEngine Database Server and can be used there for reporting,
grouping of hosts and inventory management.

## Hard Classes

Hard classes are discovered by CFEngine. Each time it wakes up, it discovers
and reads properties of the environment or context in which it runs.It turns
these properties of the environment into classes. This information is
effectively cached and may be used to make decisions about configuration.

You can see all of the classes defined on a particular host by running the following command as a privileged user.

    $ cf-promises --show-classes|grep hardclass

These are classes that describe your operating system, the time of
day, the week of the year, etc. Time-varying classes (tagged with
`time_based`) will change if you do this a few times over the course
of a week.

## Soft Classes

Soft classes are user-defined classes which you can use to implement your own
classifications. These classes are defined in bundles and are evaluated when
the bundle is evaluated. They can be based on test functions or on other
classes.

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

This example defines a few soft classes local to the `myclasses` bundle.

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

The easiest way to limit the application of a promise to certain conditions is to use the following notation:

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
         "Good evening too!" ifvarclass => "$(myclassname)";
    }
```



As you saw above, the class predicate `ifvarclass` (aliased to `if`;
`unless` is also available) can be used if variable class expressions
are required. It is `AND`ed with the normal class expression, and is
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
            ifvarclass => "$(all_cities)";

        Afternoon.germany::
          "Good afternoon from Germany",
            ifvarclass => "$(all_cities)";

        france::
          "Hello from France",
            ifvarclass => "$(all_cities)";

        france::
          "IMPOSSSIBLE!  THIS WILL NOT PRINT!!!",
            unless => "france";

        "$(all_cities)"::
          "Hello from $(all_cities)";

        "Hello from $(all_cities), ifvarclass edition",
          ifvarclass => "$(all_cities)";
    }
```

Example Output:

```
    cf-agent -Kf example.cf -D lawrence -b example
    R: It's Tue May 28 16:47:33 2013 here
    R: Hello from lawrence
    R: Hello from lawrence, ifvarclass edition

    cf-agent -Kf example.cf -D paris -b example
    R: It's Tue May 28 16:48:18 2013 here
    R: Hello from France
    R: Hello from paris
    R: Hello from paris, ifvarclass edition

    cf-agent -Kf example.cf -D milan -b example
    R: It's Tue May 28 16:48:40 2013 here
    R: Hello from milan
    R: Hello from milan, ifvarclass edition

    cf-agent -Kf example.cf -D germany -b example
    R: It's Tue May 28 16:49:01 2013 here

    cf-agent -Kf example.cf -D berlin -b example
    R: It's Tue May 28 16:51:53 2013 here
    R: Good afternoon from Germany
    R: Hello from berlin
    R: Hello from berlin, ifvarclass edition
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

## Global and Local classes

Classes defined in bundles of type `common` are global in scope, whereas
classes defined in all other bundle types are local. Classes are evaluated
when the bundle is evaluated (and the bundles are evaluated in the order
specified in the `bundlesequence`).

Note that any class promise must have one - and only one - value constraint.
That is, you might not leave 'expression' in the example above or add both
'and' and 'xor' constraints to the single promise.

Another type of class definition uses the
[`body classes`][Promise Types and Attributes#classes]. This allows setting of
classes based on the outcome of a promise. To set a class if a promise is
repaired, one might write:

```cf3
     "promiser..."
        ...
        classes => if_repaired("signal_class");
```

These classes are global in scope, but the
[`scope`][Promise Types and Attributes#scope] attribute can be used to make
them local to the bundle.

Finally, `restart_class` classes in `processes` are global.

## Canceling classes

You can cancel a class with a [`classes`][Promise Types and Attributes#classes] body.
See the `cancel_kept`, `cancel_notkept`, and `cancel_repaired` attributes.

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
