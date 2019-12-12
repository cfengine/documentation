---
layout: default
title: classes
published: true
tags: [bundle common, classes, promises]
---

[Classes][classes] promises may be made in any
bundle. Classes that are set in `common` bundles are global in scope,
while classes in all other bundles are local.

**Note:** The term class and context are sometimes used interchangeably.

```cf3
    bundle common g
    {
    classes:

      "one" expression => "any"; # always defined
      "two"; # always defined

      "client_network" expression => iprange("128.39.89.0/24");
    }
```

**Note:** You can use the following attributes to make a complete promise.

* and
* expression
* dist
* or
* not
* xor

If you omit any of them, the class is always defined (as if you said `expression
=> "any"`).

For example, the following promise defines the class `web` when a file exists:

```cf3
bundle agent example
{
  classes:
      "web"
        if => fileexists("/etc/httpd/httpd.conf");
}
```

**History:** The context attributes `expression`, `and`, `or`, `not`, `xor`,
`dist` were made optional in CFEngine 3.9.0. Before that, one of them was
required. So the following examples were the valid equivalents of the example
above before 3.9.0:

```
bundle agent example
{
  classes:
      "web"
        expression => fileexists("/etc/httpd/httpd.conf");

      "webserver"
        expression => "any",
        if => fileexists("/etc/httpd/httpd.conf");
}
```

***

## Attributes ##

### and

**Description:** Combine class sources with AND

The class on the left-hand side is set if all of the class expressions listed
on the right-hand side are true.

**Type:** `clist`

**Allowed input range:** `[a-zA-Z0-9_!@@$|.()\[\]{}:]+`

**Example:**

```cf3
    classes:

      "compound_class" and => { classmatch("host[0-9].*"), "Monday", "Hr02" };
```

**Notes:**

If an expression contains a mixture of different object types that need to be
ANDed together, this list form is more convenient than providing an
expression.

### dist

**Description:** Generate a probabilistic class distribution

Always set one generic class and one additional class, randomly weighted on a
probability distribution.

**Type:** `rlist`

**Allowed input range:** `-9.99999E100,9.99999E100`

**Example:**

```cf3
    classes:

      "my_dist"

        dist => { "10", "20", "40", "50" };
```

**Notes:**

In the example above the values sum up to `10+20+40+50 = 120`. When generating
the distribution, CFEngine picks a number between `1-120`, and set the class
`my_dist` as well as one of the following classes:

```cf3
    my_dist_10 (10/120 of the time)
    my_dist_20 (20/120 of the time)
    my_dist_40 (40/120 of the time)
    my_dist_50 (50/120 of the time)
```

### expression

**Description:** Evaluate string expression of classes in normal form

Set the class on the left-hand side if the expression on the right-hand side
evaluates to true. With classes, the notion of "true" is not a boolean state,
because classes can never be false. They are not booleans. They can be defined
or undefined, but it's important to understand that a class may be defined
**during** the execution of the agent, so the result of an expression may
change during execution.

Expressions can be:

* class names, with or without a namespace

* the literals `true` (always defined) and `false` (never defined) that allow JSON booleans to be used inside expressions

* the logical *and* operation, expressed as `a&b` or `a.b`, which is true if both `a` and `b` are true

* the logical *or* operation, expressed as `a|b`, which is true if either `a` or `b` are true

* the logical *not* operation, expressed as `!a`, which is true if `a` is not
  true. Note again here that `a` could **become** true during the execution. So
  if you have `"myclass" expression => "!x"` and `x` starts undefined but is
  defined later, you could have both `x` **and** `myclass` defined!

* parenthesis `(whatever)` which operate as expected to prioritize expression evaluation

* the return value of a function that returns a class, such as `fileexists()` `and()` `userexists()` etc.

**Type:** `class`

**Allowed input range:** `[a-zA-Z0-9_!@@$|.()\[\]{}:]+`

**Example:**

```cf3
    classes:

      "class_name" expression => "solaris|(linux.specialclass)";
      "has_toor"   expression => userexists("toor");

      # it's unlikely a machine will become Linux during execution
      # so this is fairly safe
      "not_linux"   expression => "!linux";

      "a_or_b"   expression => "a|b";
      # yes, it's OK to define a class twice, and this is the same outcome
      # with different syntax
      "a_and_b"   expression => "a&b";
      "a_and_b"   expression => "a.b";

      # yes, it's OK to define a class twice, and this is the same outcome
      # with different syntax
      "linux_and_has_toor" expression => and(userexists("toor"), "linux");
      "linux_and_has_toor" and => { userexists("toor"), "linux" };
```

### or

**Description:** Combine class sources with inclusive OR

The class on the left-hand side will be set if any one (or more) of
the class expressions on the right-hand side are true.

**Type:** `clist`

**Allowed input range:** `[a-zA-Z0-9_!@@$|.()\[\]{}:]+`

**Example:**

```cf3
classes:

    "compound_test"

      or => { classmatch("linux_x86_64_2_6_22.*"), "suse_10_3" };
```

**Notes:**

This is useful construction for writing expressions that contain functions.

### persistence

**Description:** Make the class persistent to avoid re-evaluation

The value specifies time in minutes.

**Type:** `int`

**Allowed input range:** `0,99999999999`

**Example:**

```cf3
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
```

**Notes:**

This feature can be used to avoid recomputing expensive classes calculations
on each invocation. This is useful if a class discovered is essentially
constant or only slowly varying, such as a hostname or alias from a
non-standard naming facility.
Persistent classes are always global and can not be set to local
by **scope** directive.

For example, to create a conditional inclusion of costly class evaluations,
put them into a separate bundle in a file `classes.cf.`

```cf3
    # promises.cf

    body common control
    {
    persistent_classes::
      bundlesequence => { "test" };

    !persistent_classes::
      bundlesequence => {  "setclasses", "test" };

    !persistent_classes::
      inputs => { "classes.cf" };
    }


    bundle agent test
    {
    reports:

      !my_persistent_class::
       "no persistent class";

      my_persistent_class::
        "persistent class defined";
    }
```

Then create `classes.cf`

```cf3
    # classes.cf

    bundle common setclasses
    {
    classes:

      "persistent_classes"            # timer flag
             expression => "any",
            persistence => "480";

      "my_persistent_class"
                    or => { ...long list or heavy function... } ,
           persistence => "480";

    }
```

**History:** Was introduced in CFEngine 3.3.0

**See also:** [`persistance` classes attribute][classes#persistence], [`persist_time` in classes body][Promise Types and Attributes#persist_time]

### not

**Description:** Evaluate the negation of string expression in normal form

The class on the left-hand side will be set if the class expression on the
right-hand side evaluates to false.


**Type:** `class`

**Allowed input range:** `[a-zA-Z0-9_!@@$|.()\[\]{}:]+`

**Example:**

```cf3
    classes:

       "others"  not => "linux|solaris";
       "no_toor" not => userexists("toor");
```

**Notes:**

Knowing that something is not the case is not the same as not knowing whether
something is the case. That a class is not set could mean either. See the note
on [Negative Knowledge][classes and decisions].

### scope

**Description:** Scope of the class set by this promise.

**Type:** (menu option)

**Allowed input range:**

```
    namespace
    bundle
```

**Default value:** `bundle` in agent bundles, `namespace` in common bundles

**Example:**

```cf3
    classes:
      "namespace_context"
          scope => "namespace";

      "bundle_or_namespace_context"; # without an explicit scope, depends on bundle type

      "bundle_context"
          scope => "bundle";
```

**See also:** [`scope` in `body classes`][Promise Types and Attributes#scope]

### select_class

**Description:** Select one of the named list of classes to define based on
host's fully qualified domain name, the primary IP address and the UID that
cf-agent is running under.

The class is chosen deterministically (not randomly) but it is not
possible to say which host will end up in which class in advance. Only
that hosts will always end up in the same class every time.

**Type:** `clist`

**Allowed input range:** `[a-zA-Z0-9_!@@$|.()\[\]{}:]+`

**Example:**

```cf3
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
```

**Notes:**

This feature is similar to the [`splayclass` function][splayclass]. However,
instead of selecting a class for a moment in time, it always chooses one class
in the list; the same class each time for a given host. This allows hosts to
be distributed across a controlled list of classes (e.g for load balancing
purposes).

If a list is used as the input to select_class the promise will only actuate if
the list is expandable. If the list has not yet been evaluated, the
select_class will be skipped and wait for a subsequent evaluation pass.

Given stable input, this functions output will not change between executions of the same version of CFEngine. It's output should not change between versions of CFEngine within the same minor release (3.12.0 -> 3.12.1). It's output may change between minor versions (3.12.0 -> 3.13.0).

### xor

**Description:** Combine class sources with XOR

The class on the left-hand side is set if an odd number of class expressions
on the right-hand side matches. This is most commonly used with two class
expressions.

**Type:** `clist`

**Allowed input range:** `[a-zA-Z0-9_!@@$|.()\[\]{}:]+`

**Example:**

```cf3
    classes:

    "order_lunch" xor => { "Friday", "Hr11"}; # we get pizza every Friday
```
