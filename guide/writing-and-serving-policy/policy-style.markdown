---
layout: default
title: Policy Style Guide
published: true
sorting: 10
tags: [manuals, style, policy]
---

Style is a very personal choice and the contents of this guide should only be
considered suggestions. We invite you to contribute to the growth of this
guide.

## Style Summary

* one indent = 2 spaces
* avoid letting line length surpass 80 characters.
* vertically align opening and closing curly braces unless on same line
* promise type = 1 indent
* context class expression = 2 indents
* promiser = 3 indents
* promise attributes = (we suggest 3 or 4 indents)

## Whitespace and Line Length

Spaces are preferred to tab characters. Lines should not have trailing
whitespace. Generally line length should not surpass 80 characters.

## Curly brace alignment

Generally if opening and closing braces are not on a single line they should
be aligned vertically.

Example:

```cf3

    bundle agent example
    {
      vars:
          "people" slist => {
                              "Obi-Wan Kenobi",
                              "Luke Skywalker",
                              "Chewbacca",
                              "Yoda",
                              "Darth Vader",
                            };

          "cuddly" slist => { "Chewbacca", "Yoda" };
    }
```

## Promise types

Promise types should have 1 indent and each promise type after the first
listed should have a blank line before the next promise type.

This example illustrates the blank line before the "classes" type.

```cf3
    bundle agent example
    {
      vars:
          "policyhost" string => "MyPolicyServerHostname";

      classes:
          "EL5" or => { "centos_5", "redhat_5" };
          "EL6" or => { "centos_6", "redhat_6" };
    }
```

## Context class expressions

Context class expressions should have 2 indents and each context class
expression after the first listed within a given promise type should have a
blank line preceding it.

This example illustrates the blank line before the second context class
expression (solaris) in the files type promise section:

```cf3
    bundle agent example
    {
      files:
        any::
          "/var/cfengine/inputs/"
            copy_from    => update_policy( "/var/cfengine/masterfiles","$(policyhost)" ),
            classes      => policy_updated( "policy_updated" ),
            depth_search => recurse("inf");

        solaris::
          "/var/cfengine/inputs"
            copy_from => update_policy( "/var/cfengine/masterfiles", "$(policyhost" ),
            classes   => policy_updated( "policy_updated" );
    }
```

## Policy Comments

In-line policy comments are useful for debugging and explaining why something
is done a specific way. We encourage you to document your policy thoroughly.

Comments about general body and bundle behavior and parameters should be
placed after the body or bundle definition, before the opening curly brace and
should not be indented. Comments about specific promise behavior should be
placed before the promise at the same indention level as the promiser or on
the same line after the attribute.

```cf3
    bundle agent example(param1)
    # This is an example bundle to illustrate comments
    # param1 - string -
    {
      vars:
          "copy_of_param1" string => "$(param1)";

          "jedi" slist => {
                            "Obi-Wan Kenobi",
                            "Luke Skywalker",
                            "Yoda",
                            "Darth Vader", # He used to be a Jedi, and since he
                                           # tossed the emperor into the Death
                                           # Star's reactor shaft we are including
                                           # him.
                          };
      classes:
          # Most of the time we don't need differentiation of redhat and centos
          "EL5" or => { "centos_5", "redhat_5" };
          "EL6" or => { "centos_6", "redhat_6" };
    }
```

## Policy Reports

It is common and useful to include reports in policy to get detailed
information about what is going on. During a normal agent run the goal is to
have 0 output so reports should always be guarded with a class. Carefully
consider when your policy should generate report output. For policy degbugging
type information (value of variables, classes that were set or not) the
following style is reccomended:


```cf3
bundle agent example
{
  reports:
    DEBUG|DEBUG_example::
      "DEBUG $(this.bundle): Desired Report Output";
}
```

Following this style keeps policy debug reports from spamming logs. It avoids
polluting the `inform_mode` and `verbose_mode` output, and it allows you to get
debug output for ALL policy or just a select bundle which is incredibly useful
when debugging a large policy set.

## Promise Handles

Promise handles uniquely identify a promise within a policy. We suggest a simple naming
scheme of `bundle_name_promise_type_class_restriction_promiser` to keep handles unique and
easily identifiable.  Often it may be easier to omit the handle.

```cf3
bundle agent example
{
  commands:
    dev::
      "/usr/bin/git"
        args    => "pull",
        contain => in_dir("/var/srv/myrepo"),
        ifvarclass => "redhat",
        handle  => "example_commands_dev_redhat_git_pull";
}
```

## Hashrockets (=>)

You may align hash rockets within a promise body scope and for grouped
single line promises.

Example:

```cf3
    bundle agent example
    {
      files:
        any::
          "/var/cfengine/inputs/"
            copy_from    => update_policy( "/var/cfengine/masterfiles","$(policyhost)" ),
            classes      => policy_updated( "policy_updated" ),
            depth_search => recurse("inf");

          "/var/cfengine/modules"
            copy_from => update_policy( "/var/cfengine/modules", "$(policyhost" ),
            classes   => policy_updated( "modules_updated" );

      classes:
          "EL5" or => { "centos_5", "redhat_5" };
          "EL6" or => { "centos_6", "redhat_6" };
    }
```

You may also simply leave them as they are:

```cf3
    bundle agent example
    {
      files:
        any::
          "/var/cfengine/inputs/"
            copy_from => update_policy( "/var/cfengine/masterfiles","$(policyhost)" ),
            classes => policy_updated( "policy_updated" ),
            depth_search => recurse("inf");

          "/var/cfengine/modules"
            copy_from => update_policy( "/var/cfengine/modules", "$(policyhost" ),
            classes => policy_updated( "modules_updated" );

      classes:
          "EL5" or => { "centos_5", "redhat_5" };
          "EL6" or => { "centos_6", "redhat_6" };
    }
```

Which one do you prefer?

## Naming Conventions
### Internal variables & classes

Variables and classes that have no centralized reporting value are considered
"internal". By convention internal variables and classes should be prefixed with
an underscore "_".

## Deprecating Bundles
As your policy library changes over time you may want to deprecate various
bundles in favor of newer implimentations. To indicate that a bundle is
deprecated we recommend the following style.

```cf3
bundle agent old
{
  meta:
    "tags" slist => {
                      "deprecated=3.6.0",
                      "deprecation-reason=More feature rich implimentation",
                      "replaced-by=newbundle",
                    };
}
```
## Automatic reindentation

You can run `contrib/reindent.pl FILE1.cf FILE2.c FILE3.h` to reindent files,
if you don't want to set up Emacs.  It will rewrite them with the new
indentation, using Emacs in batch mode.
