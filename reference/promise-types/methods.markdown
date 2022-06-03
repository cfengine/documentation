---
layout: default
title: methods
published: true
tags: [reference, bundle agent, methods, promises, promise types]
---

Methods are compound promises that refer to whole bundles of promises.
Methods may be parameterized.

```cf3

    methods:

      "any"

         usebundle => method_id("parameter",...);

```

Methods are useful for encapsulating repeatedly used configuration issues and
iterating over parameters. They are implemented as bundles that are run
inline. Note that if the bundle you specify requires no parameters you
may omit the `usebundle` attribute and give the bundle name directly in
the promiser string.

```cf3
    bundle agent example
    {
      vars:

       "userlist" slist => { "mark", "jeang", "jonhenrik", "thomas", "eben" };
       "userinfo" data => parsejson('{ "mark": 10, "jeang":20, "jonhenrik":30, "thomas":40, "eben":-1 }');

      methods:
       # Activate subtest once for each list item
       "any" usebundle => subtest("$(userlist)");

       # Activate subtest once passing the entire list
       "amy" usebundle => subtest(@(userlist));

       # Pass a data type variable aka data container
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

As of version 3.5.0 a methods promise outcome is tied to the outcomes of its
promises. For example if you activate a bundle and it has a promise that is
not_kept, the bundle itself would have an outcome of not_kept. If you activate
a bundle that has one promise that is repaired, and one promise that is kept,
the bundle will have an outcome of repaired. A method will only have an outcome
of kept if all promises inside that bundle are also kept.
[This acceptance test](https://github.com/cfengine/core/blob/master/tests/acceptance/21_methods/method_outcomes.cf)
illustrates the behavior.

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

Please note that method names must be either simple strings or slists.
They can't be array references, for instance.  As a rule, they can
only look like `$(name)` where `name` is either a string or an slist.
They can't be `"$(a)$(b)"`, `$(a[b])`, and so on.

Here's a full example of how you might encode bundle names and
parameters in a slist, if you need to pack and unpack method calls in
a portable (e.g. written in a file) format.

[%CFEngine_include_snippet(unpack_method_calls.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

```
2013-12-11T13:33:31-0500   notice: /run/methods/'call'/unpack/methods/'relay'/call_1: R: call_1: called with parameters a and b
2013-12-11T13:33:31-0500   notice: /run/methods/'call'/unpack/methods/'relay'/call_2: R: call_2: called with parameters x and y
2013-12-11T13:33:31-0500   notice: /run/methods/'call'/unpack/methods/'relay'/call_2: R: call_2: called with parameters p and q
```

***

## Attributes ##

[%CFEngine_include_markdown(common-attributes-include.markdown)%]

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

**See also:** [reports bundle_return_value_index attribute][reports#bundle_return_value_index]

**History:** Was introduced in 3.4.0 (2012)
