---
layout: default
title: methods
categories: [Reference, Promise Types,methods]
published: true
alias: reference-promise-types-methods.html
tags: [reference, bundle agent, methods, promises, promise types]
---

Methods are compound promises that refer to whole bundles of promises.
Methods may be parameterized. Methods promises are written in a form
that is ready for future development. The promiser object is an abstract
identifier that refers to a collection (or pattern) of lower level
objects that are affected by the promise-bundle. Since the use of these
identifiers is for the future, you can simply use any string here for
the time being.

```cf3

    methods:

      "any"

         usebundle = method_id("parameter",...);

```

Methods are useful for encapsulating repeatedly used configuration issues and 
iterating over parameters. They are implemented as bundles that are run 
inline.

```cf3
    bundle agent example
    {
      vars:

       "userlist" slist => { "mark", "jeang", "jonhenrik", "thomas", "eben" };
       "userinfo" data => parsejson('{ "mark": 10, "jeang":20, "jonhenrik":30, "thomas":40, "eben":-1 }');

      methods:

       "any" usebundle => subtest("$(userlist)");
       "amy" usebundle => subtest(@(userlist));
       "amp" usebundle => subtest_c(@(userinfo));
    }

    bundle agent subtest(user)
    {
      commands:

       "/bin/echo Fix $(user)";

      reports:

        "Finished doing stuff for $(user)";
    }

    bundle agent subtest_c(info)
    {
      reports:
       "user ID of mark is $(info[mark])";
    }
```

Methods offer powerful ways to encapsulate multiple issues pertaining to
a set of parameters.

Note in the above that a list can be passed as a implicitly iterated
scalar and as a reference, while a `data` variable (a data container)
can only be passed by reference.

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

```cf3
    bundle agent default
    {
    vars:
        "m" slist  => { "x", "y" };
        "p" string => "myfunction";

    methods:
        "set of $(m)" usebundle => $(m)("one");
        "any"         usebundle => $(p)("two");
    }
```

***

## Attributes

### inherit

**Description:** If true this causes the sub-bundle to inherit the private
classes of its parent

Inheriting the variables is unnecessary as the child can always access the 
parent's variables through a qualified reference using its bundle name. For 
example: `$(bundle.variable)`.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
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
```

**History:** Was introduced in 3.4.0, Enterprise 3.0.0 (2012)

### usebundle

**Type:** `bundle agent`

### useresult

**Description:** Specify the name of a local variable to contain any
result/return value from the child

Return values are limited to scalars.

**Type:** `string`

**Allowed input range:** `[a-zA-Z0-9_$(){}\[\].:]+

**Example:**

```cf3
    bundle agent test
    {
    methods:

       "any" usebundle => child,
             useresult => "my_return_var";

    reports:
        "My return was: \"$(my_return_var[1])\" and \"$(my_return_var[2])\""; 
    }

    bundle agent child
    {
    reports:
       # Map these indices into the useresult namespace

       "this is a return value"  
          bundle_return_value_index => "1";

       "this is another return value"  
          bundle_return_value_index => "2";
    }
```

**History:** Was introduced in 3.4.0 (2012)
