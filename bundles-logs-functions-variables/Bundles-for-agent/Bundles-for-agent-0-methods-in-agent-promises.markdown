---
layout: default
title: methods-in-agent-promises
categories: [Bundles-for-agent,methods-in-agent-promises]
published: true
alias: Bundles-for-agent-methods-in-agent-promises.html
tags: [Bundles-for-agent,methods-in-agent-promises]
---

### `methods` promises in agent

\

Methods are compound promises that refer to whole bundles of promises.
Methods may be parameterized. Methods promises are written in a form
that is ready for future development. The promiser object is an abstract
identifier that refers to a collection (or pattern) of lower level
objects that are affected by the promise-bundle. Since the use of these
identifiers is for the future, you can simply use any string here for
the time being.

~~~~ {.smallexample}
     
      methods:
     
        "any"
     
           usebundle = method_id("parameter",...);
     
~~~~

Methods are useful for encapsulating repeatedly used configuration
issues and iterating over parameters.

In CFEngine 2 methods referred to separate sub-programs executed as
separate processes. Methods are now implemented as bundles that are run
inline.

\

~~~~ {.verbatim}

bundle agent example
{
vars:

 "userlist" slist => { "mark", "jeang", "jonhenrik", "thomas", "eben" };

methods:

 "any" usebundle => subtest("$(userlist)");

}

###########################################

bundle agent subtest(user)

{
commands:

 "/bin/echo Fix $(user)";

reports:

 linux::

  "Finished doing stuff for $(user)";
}

~~~~

\

Methods offer powerful ways to encapsulate multiple issues pertaining to
a set of parameters.

Because a method is just an encapsulation, there is a subtlety about how
to interpret a successful method invocation. Before version 3.1.0, a
method was considered repaired if executed (similar to `commands`).
However, this led to unnecessary logging of executions, even if not
actual encapsulated promise was kept. In version 3.1.0 this has been
changed so that a method promise is considered kept if the method is
expanded. A method promise is thus never considered repaired.

Starting from version 3.1.0, methods may be specified using variables.
Care should be exercised when using this approach. In order to make the
function call uniquely classified, CFEngine requires the promiser to
contain the variable name of the method if the variable is a list.

~~~~ {.verbatim}
bundle agent default
{
vars:
    "m" slist  => { "x", "y" };
    "p" string => "myfunction";

methods:
    "set of $(m)" usebundle => $(m) ("one");
    "any"         usebundle => $(p)("two");
    
}
~~~~

-   [inherit in methods](#inherit-in-methods)
-   [usebundle in methods](#usebundle-in-methods)
-   [useresult in methods](#useresult-in-methods)

#### `inherit`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               true
               false
               yes
               no
               on
               off
~~~~

**Synopsis**: If true this causes the sub-bundle to inherit the private
classes of its parent

**Default value**: false

**Example**:\
 \

~~~~ {.verbatim}
bundle agent name
{
methods:

  "group name" usebundle => my_method,
                 inherit => "true";
}


body edit_defaults example
{
inherit => "true";
}
~~~~

**Notes**:\
 \

*History*: Was introduced in 3.4.0, Enterprise 3.0.0 (2012)

The `inherit` constraint can be added to the CFEngine code in two
places; for `edit_defaults` and in `methods` promises. If set to true,
it causes the child-bundle named in the promise to inherit only the
classes of the parent bundle. Inheriting the variables is unnecessary as
the child can always access the parent's variables by a qualified
reference using its bundle name. For example: \$(bundle.variable).

#### `usebundle`

**Type**: (ext bundle) (Separate Bundle)

#### `useresult`

**Type**: string

**Allowed input range**: `[a-zA-Z0-9_$(){}\[\].:]+`

**Synopsis**: Specify the name of a local variable to contain any
result/return value from the child

**Example**:\
 \

~~~~ {.verbatim}
body common control
{
bundlesequence => { "test" };
}


bundle agent test
{
methods:

   "any" usebundle => child,
    useresult => "my_return_var";


reports:

  cfengine_3::

    "My return was: \"$(my_return_var[1])\" and \"$(my_return_var[2])\""; 
    
}

bundle agent child
{
reports:

 cfengine_3::

   # Map these indices into the useresult namespace

   "this is a return value"  
      bundle_return_value_index => "1";

   "this is another return value"  
      bundle_return_value_index => "2";

}
~~~~

**Notes**:\
 \

*History*: Was introduced in 3.4.0 (2012)

Return values are limited to scalars.
