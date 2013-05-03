---
layout: default
title: classes-in-common-promises
categories: [Bundles-for-common,classes-in-common-promises]
published: true
alias: Bundles-for-common-classes-in-common-promises.html
tags: [Bundles-for-common,classes-in-common-promises]
---

### `classes` promises in \*

\
 Classes promises refer to the classification of different run-contexts.
These are not related to object oriented classes, but are more like tag
labels representing different properties of the environment.

Classes promises may be made in any bundle. In other words, bundles that
pertain to any agent.

Classes that are defined in common bundles are global in scope, while
classes in all other bundles are local.

Note: The words class and context are sometimes used interchangeably.

\

~~~~ {.verbatim}
bundle common g
{
classes:

  "one" expression => "any";

  "client_network" expression => iprange("128.39.89.0/24");
}
~~~~

-   [and in classes](#and-in-classes)
-   [dist in classes](#dist-in-classes)
-   [expression in classes](#expression-in-classes)
-   [or in classes](#or-in-classes)
-   [persistence in classes](#persistence-in-classes)
-   [not in classes](#not-in-classes)
-   [select\_class in classes](#select_005fclass-in-classes)
-   [xor in classes](#xor-in-classes)

#### `and`

**Type**: clist

**Allowed input range**: `[a-zA-Z0-9_!@@$|.()\[\]{}:]+`

**Synopsis**: Combine class sources with AND

If an expression contains a mixture of different object types that need
to be ANDed together, this list form is more convenient than providing
an expression. If all of the class expressions listed on the right-hand
side match, then the class on the left-hand side is defined.

**Example**:\
 \

~~~~ {.verbatim}
classes:

  "compound_class" and => { classmatch("host[0-9].*"), "Monday", "Hr02" };
~~~~

#### `dist`

**Type**: rlist

**Allowed input range**: `-9.99999E100,9.99999E100`

**Synopsis**: Generate a probabilistic class distribution

Assign one generic class ('always') and one additional class, randomly
weighted on a probability distribution. This was previous called a
strategy in CFEngine 2.

**Example**:\
 \

~~~~ {.verbatim}
classes:

  "my_dist"  

    dist => { "10", "20", "40", "50" };
~~~~

Referring to the the sum of `10+20+40+50 = 120` in the example above,
when generating the distribution, CFEngine picks a number between
`1-120`. This will generate the following classes:

~~~~ {.smallexample}
     my_dist    (always)
     my_dist_10 (10/120 of the time)
     my_dist_20 (20/120 of the time)
     my_dist_40 (40/120 of the time)
     my_dist_50 (50/120 of the time)
~~~~

#### `expression`

**Type**: class

**Allowed input range**: `[a-zA-Z0-9_!@@$|.()\[\]{}:]+`

**Synopsis**: Evaluate string expression of classes in normal form

A way of aliasing class combinations.

**Example**:\
 \

~~~~ {.verbatim}
classes:

  "class_name" expression => "solaris|(linux.specialclass)";
  "has_toor"   expression => userexists("toor");
~~~~

#### `or`

**Type**: clist

**Allowed input range**: `[a-zA-Z0-9_!@@$|.()\[\]{}:]+`

**Synopsis**: Combine class sources with inclusive OR

The class on the left-hand side will be defined if any one (or more) of
the class expressions on the right-hand side are true. This is useful
construction for writing expressions that contain special functions.

**Example**:\
 \

~~~~ {.verbatim}
classes:

    "compound_test" 

      or => { classmatch("linux_x86_64_2_6_22.*"), "suse_10_3" };
~~~~

#### `persistence`

**Type**: int

**Allowed input range**: `0,99999999999`

**Synopsis**: Make the class persistent (cached) to avoid re-evaluation,
time in minutes

This feature can be used to avoid recomputing expensive classes
calculations on each invocation. This is useful if a class discovered is
essentially constant or only slowly varying, such as a hostname or alias
from a non-standard naming facility.

**Example**:\
 \

~~~~ {.verbatim}
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
~~~~

For example, to create a conditional inclusion of costly class
definitions, put them into a separate bundle in a file classes.cf.

~~~~ {.verbatim}
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
 
~~~~

Then create classes.cf

~~~~ {.verbatim}
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
~~~~

#### `not`

**Type**: class

**Allowed input range**: `[a-zA-Z0-9_!@@$|.()\[\]{}:]+`

**Synopsis**: Evaluate the negation of string expression in normal form

This negates the effect of the promiser-pattern regular expression. The
class on the left-hand side will only be defined if the class expression
on the right-hand side is false.

**Example**:\
 \

~~~~ {.verbatim}
classes:

   "others"  not => "linux|solaris";
   "no_toor" not => userexists("toor");
~~~~

#### `select_class`

**Type**: clist

**Allowed input range**: `[a-zA-Z0-9_!@@$|.()\[\]{}:]+`

**Default value:** random\_selection

**Synopsis**: Select one of the named list of classes to define based on
host identity

This feature is similar to the `splayclass` function. However, instead
of selecting a class for a moment in time, it always chooses one class
in the list; the same class each time for a given host. This allows
hosts to be distributed across a controlled list of classes (e.g for
load balancing purposes).

The class is chosen deterministically (not randomly) but it is not
possible to say which host will end up in which class in advance. Only
that hosts will always end up in the same class every time.

**Example**:\
 \

~~~~ {.verbatim}
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
~~~~

#### `xor`

**Type**: clist

**Allowed input range**: `[a-zA-Z0-9_!@@$|.()\[\]{}:]+`

**Synopsis**: Combine class sources with XOR

This behaves as the XOR operation on class expressions. It can be used
to define a class if exactly one of the class expressions on the
right-hand side matches.

**Example**:\
 \

~~~~ {.verbatim}
classes:

 "another_global" xor => { "any", "linux", "solaris"};
~~~~
