---
layout: default
title: vars-in-common-promises
categories: [Bundles-for-common,vars-in-common-promises]
published: true
alias: Bundles-for-common-vars-in-common-promises.html
tags: [Bundles-for-common,vars-in-common-promises]
---

### `vars` promises in \*

\

Variables in CFEngine are defined as promises that an identifier
represents a particular value. Variables in CFEngine are dynamically
typed as strings, integers and real numbers. Lists of these types are
also possible.

Arrays are `associative` and use square brackets [] to enclose an
arbitrary key.

\

~~~~ {.verbatim}
bundle agent example

{     
vars:

  "scalar1" string => "SCALAR 1";
  "list1" slist => { "LIST1_1", "LIST1_2" } ;
  "array[1]" string => "ARRAY 1";
  "array[2]" string => "ARRAY 2";

  "i" slist => getindices("array");

reports:

  cfengine_3::

    "Scalar $(scalar1)";
    "List $(list1)";
    "Array $(array[$(i)])";
}

~~~~

\

-   [string in vars](#string-in-vars)
-   [int in vars](#int-in-vars)
-   [real in vars](#real-in-vars)
-   [slist in vars](#slist-in-vars)
-   [ilist in vars](#ilist-in-vars)
-   [rlist in vars](#rlist-in-vars)
-   [policy in vars](#policy-in-vars)

#### `string`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: A scalar string

**Example**:\
 \

~~~~ {.verbatim}
vars:

 "xxx"    string => "Some literal string...";

 "yyy"    string => readfile( "/home/mark/tmp/testfile" , "33" );
~~~~

**Notes**:\
 \

In previous versions of CFEngine lists were represented (as in the
shell) using separated scalars; similar to the PATH variable. In
CFEngine 3 lists are kept as an independent type.

#### `int`

**Type**: int

**Allowed input range**: `-99999999999,9999999999`

**Synopsis**: A scalar integer

**Example**:\
 \

~~~~ {.verbatim}
vars:

 "scalar" int    => "16k";

 "ran"    int    => randomint(4,88);

 "dim_array" int =>  readstringarray("array_name","/etc/passwd","#[^\n]*",":",10,4000);
~~~~

**Notes**:\
 \
 Int variables are strings that are expected to be used as integer
numbers. The typing in CFEngine is dynamic, so the variable types are
interchangeable. However, when you declare a variable to be type `int`,
CFEngine verifies that the value you assign to it looks like an integer
(e.g., 3, -17, 16K).

Integer values may use suffices k, K, m, M, and so forth. However, they
must only have an integer numeric part (e.g. 1.5M is not allowed).

k

The value multiplied by 1000. \

K

The value multiplied by 1024. \

m

The value multiplied by 1000 \* 1000. \

M

The value multiplied by 1024 \* 1024. \

g

The value multiplied by 1000 \* 1000 \* 1000. \

G

The value multiplied by 1024 \* 1024 \* 1024. \

%

A percentage between 1 and 100 - mainly for use in a storage context.

The value inf may also be used to represent an unlimited positive value.

#### `real`

**Type**: real

**Allowed input range**: `-9.99999E100,9.99999E100`

**Synopsis**: A scalar real number

**Example**:\
 \

~~~~ {.verbatim}
vars:
   
 "scalar" real   => "0.5";
~~~~

**Notes**:\
 \
 Real variables are strings that are expected to be used as real
numbers. The typing in CFEngine is dynamic, so the variable types are
interchangeable, but when you declare a variable to be type `real`,
CFEngine verifies that the value you assign to it looks like a real
number (e.g., 3, 3.1415, .17, 6.02e23, -9.21e-17).

Real numbers are not used in many places in CFEngine, but they are
useful for representing probabilities and performance data.

#### `slist`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: A list of scalar strings

**Example**:\
 \

~~~~ {.verbatim}
vars:

 "xxx"    slist  => {  "literal1",  "literal2" };

 "yyy"    slist  => { 
                    readstringlist(
                                  "/home/mark/tmp/testlist",
                                  "#[a-zA-Z0-9 ]*",
                                  "[^a-zA-Z0-9]",
                                  15,
                                  4000
                                  ) 
                    };

 "zzz"    slist  => { readstringlist("/home/mark/tmp/testlist2","#[^\n]*",",",5,4000) };

~~~~

**Notes**:\
 \
 Some functions return `slist`s (see [Introduction to
functions](#Introduction-to-functions)), and an `slist` may contain the
values copied from another `slist`, `rlist`, or `ilist` (see [List
variable substitution and
expansion](#List-variable-substitution-and-expansion), see [policy in
vars](#policy-in-vars)).

#### `ilist`

**Type**: ilist

**Allowed input range**: `-99999999999,9999999999`

**Synopsis**: A list of integers

**Example**:\
 \

~~~~ {.verbatim}
vars:

  "variable_id"

       ilist => { "10", "11", "12" };
~~~~

**Notes**:\
 \

Integer lists are lists of strings that are expected to be treated as
integers. The typing in CFEngine is dynamic, so the variable types are
interchangeable, but when you declare a variable to be type `ilist`,
CFEngine verifies that each value you assign to it looks like an integer
(e.g., 3, -17, 16K).

Some functions return `ilist`s (see [Introduction to
functions](#Introduction-to-functions)), and an `ilist` may contain the
values copied from another `slist`, `rlist`, or `ilist` (see [List
variable substitution and
expansion](#List-variable-substitution-and-expansion), see [policy in
vars](#policy-in-vars)).

#### `rlist`

**Type**: rlist

**Allowed input range**: `-9.99999E100,9.99999E100`

**Synopsis**: A list of real numbers

**Example**:\
 \

~~~~ {.verbatim}
vars:

  "varid" rlist => { "0.1", "0.2", "0.3" };
~~~~

**Notes**:\
 \
 Real lists are lists of strings that are expected to be used as real
numbers. The typing in CFEngine is dynamic, so the variable types are
interchangeable, but when you declare a variable to be type `rlist`,
CFEngine verifies that each value you assign to it looks like a real
number (e.g., 3, 3.1415, .17, 6.02e23, -9.21e-17).

Some functions return `rlist`s (see [Introduction to
functions](#Introduction-to-functions)), and an `rlist` may contain the
values copied from another `slist`, `rlist`, or `ilist` (see [List
variable substitution and
expansion](#List-variable-substitution-and-expansion), see [policy in
vars](#policy-in-vars)).

#### `policy`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               free
               overridable
               constant
               ifdefined
~~~~

**Synopsis**: The policy for (dis)allowing (re)definition of variables

**Example**:\
 \

~~~~ {.verbatim}
vars:

  "varid" string => "value...",
          policy => "constant";
~~~~

**Notes**:\
 \

Variables can either be allowed to change their value dynamically (be
redefined) or they can be constant. The use of private variable spaces
in CFEngine 3 makes it unlikely that variable redefinition would be
necessary in CFEngine 3.

The value `constant` indicates that the variable value may not be
changed. The values `free` and `overridable` are synonymous, and
indicated that the variable's value may be changed.

The value `ifdefined` applies only to lists and implies that unexpanded
or undefined lists are dropped. The default behaviour is otherwise to
retain this value as an indicator of the failure to quench the variable
reference, for example:

~~~~ {.verbatim}
   
    "one" slist => { "1", "2", "3" };

   "list" slist => { "@(one)", @(two) },

            policy => "ifdefined";
~~~~

This would result in @(list) being the same as @(one), and the reference
to @(two) would disappear. This is useful for combining lists,
\`inheritance-style' where one can extend a base with special cases if
they are defined.

**Default value**:\
 \

`policy = constant`
