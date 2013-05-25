---
layout: default
title: Classes - Making Decisions
categories: [Manuals, Language Concepts, Classes]
published: true
alias: manuals-language-concepts-classes.html
tags: [manuals, language, syntax, concepts, classes, decisions]
---

When you write promises in CFEngine, you don't write a series of control statements and loops. You don't write if/else statements CFEngine to control when and how a promise is fulfilled. Instead you use +classes+ to apply promise bodies to particular environments depending on context. +classes+ are simply variables, Boolean variables, which evaluate to true or false depending on context.

Let's make it more concrete than that with a few examples.  Consider one of the previous examples in this chapter that manipulated file permissions. You could decide that this promise is only applicable to machines that are running Max OSX, or you could decide that you only want to implement this promise on the third day of every month.    Classes are simply facts that represent the current state or context of a system and they can be used for much more than just applying specific recipes to different operating systems.  For example, you can use CFEngine classes to increase capacity for a system during business hours and decrease capacity at night.

### How Classes Work

How does it work?  How are classes made available to CFEngine promises?  CFEngine runs on every computer individually and each time it wakes up the underlying generic agent platform discovers and reads properties of the environment or context in which it runs. It turns these properties of the environment into classes.  This information is effectively cached and may be used to make decisions about configuration.

You can see all of the classes defined on a particular host by running the following command as a privileged user.

    host# cf-promises -v

Do this a few times over the course of a day and you will see that time-varying classes make up an important component of available classes as well as classes that describe the operating system and other attributes of your system.   

### Hard Classes (Built-in Classes)

There are two categories of classes.  Hard classes which are discovered by CFEngine.   These are classes that describe your operating system, the time of day, the week of the year, etc.   Soft classes are user-defined classes which you can use to implement your own classifications.

The following is a sample of some of the Hard classes available to CFEngine administrators:

* The name of an operating system architecture
    * `linux`, `solaris`, etc.
* Network Classes
    * Unqualified Name of Host. CFEngine truncates it at the first dot. 
      Note: `www.sales.company.com` and `www.research.company.com` have the
      same unqualified name – `www`
    * The IP address octets of any active interface (in the form
    `ipv4_192_0_0_1`, `ipv4_192_0_0`, `ipv4_192_0`, `ipv4_192`)
    * User-defined Group of Hosts
* Time Classes
    * Day of the Week - `Monday, Tuesday, Wednesday,...`
    * Hour of the Day in Current Time Zone - `Hr00, Hr01,... Hr23`
    * Hour of the Day in GMT - `GMT_Hr00, GMT_Hr01, ...GMT_Hr23`
    * Minutes of the Hour - `Min00, Min17,... Min45`
    * Five Minute Interval of the Hour - `Min00_05, Min05_10,... Min55_00`
    * Quarter of the Hour - `Q1, Q2, Q3, Q4`
    * Day of the Month - `Day1, Day2,... Day31`
    * Month - `January, February,... December`
    * Year - `Yr1997, Yr2004`
    * Period of the Day - `Night, Morning, Afternoon, Evening` (six hour
      blocks starting at 00:00 hours).

### Soft Classes (User-defined Classes)

User-defined or soft classes are defined in bundles. Bundles of type common yield classes that are global in scope.  Classes defined in all other bundle types are local in scope. 

Soft classes are evaluated when the bundle is evaluated. They can be based on test functions or simply
from other classes.  The following example defines a few soft classes local to the myclasses bundle.

* The "solinux" soft class is defined as a combination of the "linux" or the "solaris" hard classes.   This class will evaluate to true if the operating system family is either of these values.

* The "atl_class" soft class is defined as a combination of "linux", "solaris", or the presence of a file named /etc/fstab.   If one of the two hard classes ("linux" or "solaris") evaluate to true or if there is a file named "/etc/fstab" the "alt_class" class will also evaluate to true.

* The "oth_class" soft class is defined as the combination of two fileexists functions - "/etc/shadow" and "/etc/passwd".  If both of these files are present the "oth_class" class evaluates to true.

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

There are a few ways to define a class.  The first form shown for the "solinus" express uses a syntax that combines classes using the "||" or "&&" operators.  This convenient form is useful when you are basing a soft class on a combination of several hard classes.

The list form used for "alt_class" and "oth_class" is used when you need to combine hard classes and functions.  In these two sample classes, the fileexists functions are combined with hard classes "linux" and "solaris" using either and or or combinations.   In an or combination only one of the classes or functions needs to evaluate as true, and in an and combination all of the classes or functions included need to evaluate as true.

### Class combination operators and precedence

Classes may be combined with the operators listed here in order from highest to lowest precedence:

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

These operators can be combined to form complex expressions.  For example, the following expression would be only true on Mondays or Wednesdays from 2:00pm to 2:59pm on Windows XP systems:

    (Monday|Wednesday).Hr14.WinXP::

### Variables in class expressions

The class predicate `ifvarclass` is `AND`ed with the normal class expression, and is evaluated together with the promise. It may contain variables as long as the resulting expansion is a legal class expression.

### Global and local classes

User defined classes are mostly defined in bundles, but they are
used as a signaling mechanism between promises.

Classes promises define new classes based on combinations of old
ones. This is how to make complex decisions in CFEngine, with
readable results. It is like defining aliases for class
combinations. Such class 'aliases' may be specified in any kind of
bundle. Bundles of type `common` yield classes that are global in
scope, whereas in all other bundle types classes are local. Classes
are evaluated when the bundle is evaluated (and the bundles are
evaluated in the order specified in the `bundlesequence`). Consider
the following example.

```cf3
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
```

Here we see that class 'one' is global (because it is defined
inside the `common` bundle), while classes 'two' and 'three' are
local (to their respective bundles). The report result 'Success'
is therefore true because only 'one' and 'three' are in scope (and
'two' is *not* in scope) inside of the third bundle.

Note that any class promise must have one - and only one - value
constraint. That is, you might not leave 'expression' in the
example above or add both 'and' and 'xor' constraints to the single
promise.

Another type of class definition happens when you define classes
based on the outcome of a promise, e.g. to set a class if a promise
is repaired, one might write:

```cf3
     "promiser..."
    
        ...
    
        classes => if_repaired("signal_class");
```

These classes are global in scope. Finally `restart_class` classes
in `processes` are global.


#### Class Scopes: A More Complex Example

In a more advanced example, let's consider how common classes with a global scope can be combined with bundle-level classes with a local scope. Promises in bundles of type ‘common’ are global in scope – all other promises are local to the scope of their bundle.

In this example, there are three bundles.  One common bundle named "global" with a global scope.  Classes defined in common bundles can be used throughout your CFEngine configuration.   Two other bundles define classes which are local to those bundles.   Three classes are defined:

* "zero" from the common bundle with a global scope
* "one" from the local_one bundle with a local scope
* "two" from the local_two bundle with a local scope

In the body of the local_two bundle we define a report "Success" which evaluates if "zero.!one.two" is true.   Withing the local_two scope this evaluates to true because the "one" class is not defined.

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