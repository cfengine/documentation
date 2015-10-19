---
layout: default
title: Bundles
published: true
sorting: 20
tags: [language, concepts, syntax, body, bundle]
---

A bundle is a collection of promises. They allow to group related promises 
together into named building blocks that can be thought of as "subroutines" in 
the CFEngine promise language. A bundle that groups a number of promises 
related to configuring a web server or a file system would be named 
"webserver" or "filesystem," respectively.

Most promise types are specific to a particular kind of interpretation that 
requires a typed interpreter - the bundle *type*. Bundles belong to the agent 
that is used to keep the promises in the bundle. So `cf-agent` has bundles 
declared as:

```cf3
    bundle agent my_name
    {
    }
```

while `cf-serverd` has bundles declared as:

```cf3
    bundle server my_name
    {
    }
```

and `cf-monitord` has bundles declared as

```cf3
    bundle monitor my_name
    {
    }
```

A number of promises can be made in any kind of bundle since they are of a 
generic input/output nature. These are `vars`, [`classes`][classes], `defaults`,
[`meta`][meta] and `reports` promises.

### Common Bundles

Bundles of type `common` may only contain the promise types that are common to 
all bodies. Their main function is to define cross-component global 
definitions.

```cf3
     bundle common globals
     {
     vars:
     
       "global_var" string = "value";
     
     classes:
     
       "global_class" expression = "value";
     }
```

Common bundles are observed by every agent, whereas the agent 
specific bundle types are ignored by components other than the intended 
recipient.

#### Rules for evaluation of common bundles

These are the specific evaluation differences between common and agent bundles:

* common bundles are automatically evaluated even if they are not in the bundlesequence, as long as they have no parameters
* auto-evaluated common bundles (not in the bundlesequence explicitly) don't evaluate their `reports` promises, so their reports won't be printed.
* when common bundles define a class, it's global ([`scope`][classes#scope] is `namespace`) by default; the classes in agent bundles are local ([`scope`][classes#scope] is `bundle`) by default.
* common bundles can only contain [`meta`][meta], `default`, `vars`, [`classes`][classes], and `reports` promises

### Bundle Parameters

Bundles can be parameterized, allowing for code re-use. If you need to do the 
same thing over and over again with slight variations, using a promise bundle 
is an easy way to avoid unnecessary duplication in your promises.

```
    bundle agent hello_world
    {
      vars:
          "myfiles"     => "/tmp/world.txt";
          "desired_content" string => "hello";
          "userinfo" data => parsejson('{ "mark": 10, "jeang":20, "jonhenrik":30, "thomas":40, "eben":-1 }');

      methods:
          "Hello World"
            usebundle => ensure_file_has_content("$(myfiles)", "$(desired_content)");
        
          "report" usebundle => subtest_c(@(userinfo));
    
    }

    bundle agent ensure_file_has_content(file, content)
    {
      files:
    
          "$(file)"
            handle => "$(this.bundle)_file_content",
            create => "true",
            edit_defaults => empty,
            edit_line => append_if_no_line("$(content)"),
            comment => "Ensure that the given parameter for file '$(file)' has only
                        the contents of the given parameter for content '$(content)'";
    
    }

    bundle agent subtest_c(info)
    {
      reports:
       "user ID of mark is $(info[mark])";
    }
```

You can pass `slist` and `data` variables to other bundles with
the `@(var)` notation.  You do NOT need to qualify the variable name
with the current bundle name.

### Scope

All [variables][variables] in CFEngine are globally accessible. If you
refer to a variable by ‘$(unqualified)’, then it is assumed to belong
to the current bundle. To access any other (scalar) variable, you must
qualify the name, using the name of the bundle in which it is defined:

    $(bundle_name.qualified)

The value of the variable depends on evaluation order, which is not
controllable by the user. Thus you should not assume that you can
evaluate a bundle twice with different variables and get variables
from it that correspond to the second evaluation.  In other words, if you have:

```cf3
bundle agent mybundle(x)
{
  vars:
  "y" string => $(x);
}
```

and call `mybundle(1)` and `mybundle(2)`, the variable `y` could be `1` or `2`.

[Classes][classes and decisions] defined inside `agent` bundles are not visible outside 
those bundles.  [Classes][classes and decisions] defined in `common` bundles 
have global scope, so they are visible everywhere.

Note that namespaced bundles work exactly the same way as
non-namespaced bundles (which are actually in the `default`
namespace).  You just say `namespace:bundle_name` instead of
`bundle_name`.  See [Namespaces] for more details.
