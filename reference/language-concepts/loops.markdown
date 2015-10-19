---
layout: default
title: Loops
published: true
sorting: 70
tags: [manuals, language, syntax, concepts, loops]
---

There are no explicit loops in CFEngine, instead there are lists. To make a
loop, you simply refer to a list as a scalar and CFEngine will assume a loop
over all items in the list.

It's as if you said "I know three colors: red green blue. Let's talk
about color."

```cf3
    body common control
    {
        bundlesequence  => { "color_example" };
    }

    bundle agent color_example
    {
        vars:
            "color" slist => { "red", "green", "blue" };

        reports:
            "Let's talk about $(color)";
    }
```

CFEngine will implicitly loop over each `$(color)`:

```
% cf-agent -K -f ./test_colors.cf

R: Let's talk about red
R: Let's talk about green
R: Let's talk about blue

```

Here's a more complex example.

```cf3
    body common control
    {
        bundlesequence  => { "example" };
    }

    bundle agent example
    {
        vars:
            "component" slist => { "cf-monitord", "cf-serverd", "cf-execd" };

            "array[cf-monitord]" string => "The monitor";
            "array[cf-serverd]" string => "The server";
            "array[cf-execd]" string => "The executor, not executionist";

        reports:
            "$(component) is $(array[$(component)])";
    }
```

In this example, the list `component` has three elements. The list as a whole
may be referred to as `@(component)`, in order to pass the whole list to a
promise where a list is expected. However, if we write `$(component)`,
i.e. the scalar variable, then CFEngine will substitute each scalar from the
list in turn, and thus iterate over the list elements using a loop.

The output looks something like this:

    $ cf-agent unit_loops.cf

    2013-06-12T18:56:01+0200   notice: R: cf-monitord is The monitor
    2013-06-12T18:56:01+0200   notice: R: cf-serverd is The server
    2013-06-12T18:56:01+0200   notice: R: cf-execd is The executor, not executionist

You see from this that, if we refer to a list variable using the scalar
reference operator `$()`, CFEngine interprets this to mean “please iterate
over all values of the list”. Thus, we have effectively a `foreach' loop,
without the attendant syntax.

If a variable is repeated, its value is tied throughout the expression; so the
output of:

```cf3
    body common control
    {
        bundlesequence  => { "example" };
    }

    bundle agent example
    {
    vars:
      "component" slist => { "cf-monitord", "cf-serverd", "cf-execd" };

      "array[cf-monitord]" string => "The monitor";
      "array[cf-serverd]" string => "The server";
      "array[cf-execd]" string => "The executor, not executioner";

    commands:
       "/bin/echo $(component) is"
                args => "$(array[$(component)])";
    }
```

is as follows:

    2013-06-12T18:57:34+0200   notice: Q: ".../bin/echo cf-mo": cf-monitord is The monitor
    2013-06-12T18:57:34+0200   notice: Q: ".../bin/echo cf-se": cf-serverd is The server
    2013-06-12T18:57:34+0200   notice: Q: ".../bin/echo cf-ex": cf-execd is The executor, not executioner

### Iterating Across Multiple Lists

CFEngine can iterate across multiple lists simultaneously.

```cf3
    bundle agent iteration
    {
    vars:
        "stats"   slist => { "value", "av", "dev" };

        "monvars" slist => {
                           "rootprocs",
                           "otherprocs",
                           "diskfree",
                           "loadavg"
                           };
    reports:
        "mon.$(stats)_$(monvars) is $(mon.$(stats)_$(monvars))";
    }
```

This example uses two lists, `stats` and `monvars`. We can now iterate over both lists in the same promise. The reports that we thus generate will report on `value_rootprocs`, `av_rootprocs`, and `dev_rootprocs`, followed next by `value_otherprocs`, `av_otherprocs`, etc, ending finally with `dev_loadavg`.

The order of iteration is an implementation detail and should not be expected to be consistent.  Use the `sort()` function if you need to sort a list in a predictable way.
