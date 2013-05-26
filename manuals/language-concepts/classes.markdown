---
layout: default
title: Classes
categories: [Manuals, Language Concepts, Classes]
published: true
alias: manuals-language-concepts-classes.html
tags: [manuals, language, syntax, concepts, classes, decisions]
---

Classes are used to apply promises only to particular environments, depending 
on context. A promise might only apply to Linux systems, or should only be 
applied on Sundays, or only when a 
[variable](manuals-language-concepts-variables.html) has a certain value.

Classes are simply facts that represent that current state or context of a 
system. They are either `set` or `not set`, depending on context. The list of 
classes set classifies the current environment.

In CFEngine Enterprise, the list of set classes is reported to the CFEngine 
Database Server, and can be used there for reporting and inventory management.

## Making Decisions based on classes

**TODO:Example**

The class predicate `ifvarclass` is `AND`ed with the normal class expression, 
and is evaluated together with the promise. It may contain variables as long 
as the resulting expansion is a legal class expression.

## Hard Classes

Hard classes are discovered by CFEngine. Each time it wakes up, it discovers 
and reads properties of the environment or context in which it runs.It turns 
these properties of the environment into classes. This information is 
effectively cached and may be used to make decisions about configuration.

You can see all of the classes defined on a particular host by running the following command as a privileged user.

    host# cf-promises -v

These are classes that describe your operating system, the time of day, the 
week of the year, etc. Time-varying classes will change if you do this a few 
times over the course of a week.

## Soft Classes

Soft classes are user-defined classes which you can use to implement your own 
classifications. These classes are defined in bundles, and are evaluated when 
the bundle is evaluated. They can be based on test functions or on other 
classes.

### Negative Knowledge

If a class is set, then it is certain that the corresponding fact is true.
However, that a class is not set could mean that something is not the case, or 
that something is simply not known. This is only a problem with soft classes,
where the state of a class can change during the execution of a policy, 
depending on the [order](manuals-language-concepts-normal-ordering.html) in 
which bundles and promises are evaluated.

## Operators and Precedence

Classes promises define new classes based on combinations of old ones. This is 
how to make complex decisions in CFEngine, with readable results. It is like 
defining aliases for class combinations. Such class 'aliases' may be specified 
in any kind of bundle.

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

### An Example

```cf3
    bundle agent myclasses
    {
    classes:
      "solinus" expression => "linux||solaris";
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

* The `solinux` soft class is defined as a combination of the `linux` or the 
  `solaris` hard classes. This class will be set if the operating 
  system family is either of these values.

* The `atl_class` soft class is defined as a combination of `linux`, 
  `solaris`, or the presence of a file named `/etc/fstab`. If one of the two 
  hard classes evaluate to true or if there is a file named `/etc/fstab`, the 
  `alt_class` class will also be set.

* The `oth_class` soft class is defined as the combination of two `fileexists`
  functions - `/etc/shadow` and `/etc/passwd`.  If both of these files are 
  present the `oth_class` class will also be set.


## Global and Local classes

Classes defined in bundles of type `common` are global in scope, whereas 
classes defined in all other bundle types are local. Classes are evaluated 
when the bundle is evaluated (and the bundles are evaluated in the order 
specified in the `bundlesequence`).

Note that any class promise must have one - and only one - value constraint. 
That is, you might not leave 'expression' in the example above or add both 
'and' and 'xor' constraints to the single promise. **TODO: rephrase this**

Another type of class definition happens when you define classes based on the 
outcome of a promise, e.g. to set a class if a promise is repaired, one might 
write:

```cf3
     "promiser..."
        ...
        classes => if_repaired("signal_class");
```

These classes are global in scope. Finally `restart_class` classes
in `processes` are global.
**TODO: document scope-attribute of classes bodies**


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
