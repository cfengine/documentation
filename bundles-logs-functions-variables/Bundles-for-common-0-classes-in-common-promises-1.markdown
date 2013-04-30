---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Bundles-for-common-0-classes-in-common-promises-1.markdown.html
tags: [xx]
---

### `classes` promises in \*

\
 Classes promises refer to the classification of different run-contexts.
These are not related to object oriented classes, but are more like tag
labels representing different properties of the environment.

Note: The words class and context are sometimes used interchangeably.

\

    bundle common g
    {
    classes:

      "one" expression => "any";

      "client_network" expression => iprange("128.39.89.0/24");
    }

\

Classes promises may be made in any bundle. In other words, bundles that
pertain to any agent.

Classes that are defined in common bundles are global in scope, while
classes in all other bundles are local.

-   and in classes
-   dist in classes
-   expression in classes
-   or in classes
-   persistence in classes
-   not in classes
-   select\_class in classes
-   xor in classes

#### `and`

**Type**: clist

**Allowed input range**: `[a-zA-Z0-9_!@@$|.()\[\]{}:]+`

**Synopsis**: Combine class sources with AND

**Example**:\
 \

    classes:

      "compound_class" and => { classmatch("host[0-9].*"), "Monday", "Hr02" };

**Notes**:\
 \

If an expression contains a mixture of different object types that need
to be ANDed together, this list form is more convenient than providing
an expression. If all of the class expressions listed on the right-hand
side match, then the class on the left-hand side is defined.

#### `dist`

**Type**: rlist

**Allowed input range**: `-9.99999E100,9.99999E100`

**Synopsis**: Generate a probabilistic class distribution (from
strategies in CFEngine 2)

**Example**:\
 \

    classes:

      "my_dist"  

        dist => { "10", "20", "40", "50" };

**Notes**:\
 \

Assign one generic class (always) and one additional class, randomly
weighted on a probability distribution. The sum of `10+20+40+50 = 120`
in the example above, so in generating a distribution, CFEngine picks a
number between `1-120`. This will generate the following classes:

         my_dist    (always)
         my_dist_10 (10/120 of the time)
         my_dist_20 (20/120 of the time)
         my_dist_40 (40/120 of the time)
         my_dist_50 (50/120 of the time)

This was previous called a strategy in CFEngine 2.

#### `expression`

**Type**: class

**Allowed input range**: `[a-zA-Z0-9_!@@$|.()\[\]{}:]+`

**Synopsis**: Evaluate string expression of classes in normal form

**Example**:\
 \

    classes:

      "class_name" expression => "solaris|(linux.specialclass)";
      "has_toor"   expression => userexists("toor");

**Notes**:\
 \

A way of aliasing class combinations.

#### `or`

**Type**: clist

**Allowed input range**: `[a-zA-Z0-9_!@@$|.()\[\]{}:]+`

**Synopsis**: Combine class sources with inclusive OR

**Example**:\
 \

    classes:

        "compound_test" 

          or => { classmatch("linux_x86_64_2_6_22.*"), "suse_10_3" };

**Notes**:\
 \

The class on the left-hand side will be defined if any one (or more) of
the class expressions on the right-hand side are true. This is useful
construction for writing expressions that contain special functions.

#### `persistence`

**Type**: int

**Allowed input range**: `0,99999999999`

**Synopsis**: Make the class persistent (cached) to avoid reevaluation,
time in minutes

**Example**:\
 \

    bundle common setclasses
    {
    classes:

      "cached_classes" 
                    or => { "any" },
           persistence => "1";

      "cached_class" 
           expression => "any",
           persistence => "1";

    }

**Notes**:\
 \

This feature can be used to avoid recomputing expensive classes
calculations on each invocation, if a class discovered is essentially
constant or only slowly varying. For example, a hostname or alias from a
non-standard naming facility)

For example, to create a conditional inclusion of costly class
definitions, put them into a separate bundle in a file classes.cf.

    # promises.cf

    body common control 
    {
    cached_classes::
      bundlesequence => { "test" };

    !cached_classes::
      bundlesequence => {  "setclasses", "test" };

    !cached_classes::
      inputs => { "classes.cf" };
    }
     

    bundle agent test
    {
    reports:

      !my_cached_class::
       "no cached class";

      my_cached_class::
        "cached class defined";
    }
     

Then create classes.cf

    # classes.cf

    bundle common setclasses
    {
    classes:

      "cached_classes"            # timer flag 
             expression => "any",
            persistence => "480";

      "my_cached_class" 
                    or => { ...long list or heavy function... } ,
           persistence => "480";

    }

#### `not`

**Type**: class

**Allowed input range**: `[a-zA-Z0-9_!@@$|.()\[\]{}:]+`

**Synopsis**: Evaluate the negation of string expression in normal form

**Example**:\
 \

    classes:

       "others"  not => "linux|solaris";
       "no_toor" not => userexists("toor");

**Notes**:\
 \

This negates the effect of the promiser-pattern regular expression. The
class on the left-hand side will only be defined if the class expression
on the right-hand side is false.

#### `select_class`

**Type**: clist

**Allowed input range**: `[a-zA-Z0-9_!@@$|.()\[\]{}:]+`

**Default value:** random\_selection

**Synopsis**: Select one of the named list of classes to define based on
host identity

**Example**:\
 \

    bundle common g
    {
    classes:
      "selection" select_class => { "one", "two" };

    reports:
      one::
        "One was selected";
      two::
        "Two was selected";
      selection::
         "A selection was made";
    }

**Notes**:\
 \

This feature is similar to the `splayclass` function. However, instead
of selecting a class for a moment in time, it always chooses one class
in the list; the same class each time for a given host. This allows
hosts to be distributed across a controlled list of classes (e.g for
load balancing purposes).

The class is chosen deterministically (not randomly) but it is not
possible to say which host will end up in which class in advance. Only
that hosts will always end up in the same class every time.

#### `xor`

**Type**: clist

**Allowed input range**: `[a-zA-Z0-9_!@@$|.()\[\]{}:]+`

**Synopsis**: Combine class sources with XOR

**Example**:\
 \

    classes:

     "another_global" xor => { "any", "linux", "solaris"};

**Notes**:\
 \

This behaves as the XOR operation on class expressions. It can be used
to define a class if exactly one of the class expressions on the
right-hand side matches.
