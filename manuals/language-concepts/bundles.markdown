---
layout: default
title: Bundles
categories: [Manuals, Language Concepts, Bundles]
published: true
sorting: 20
alias: manuals-language-concepts-bundles.html
tags: [language, concepts, syntax, body, bundle]
---

A bundle is a collection of promises. They allow to group related promises 
together into named building blocks that can be thought of as "subroutines" in 
the CFEngine promise language. A bundle that groups a number of promises 
related to configuring a web server or a file system would be named 
"webserver" or "filesystem", respectively.

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
generic input/output nature. These are `vars`, `classes`, `defaults`, `meta` 
and `reports` promises.

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

Variables and classes defined inside bundles are not directly visible outside 
those bundles. All [variables][variables] in 
CFEngine are globally accessible. However, if you refer to a variable by 
‘$(unqualified)’, then it is assumed to belong to the current bundle. To 
access any other (scalar) variable, you must qualify the name, using the name 
of the bundle in which it is defined:

    $(bundle_name.qualified)

Bundles of type `common` may contain common promises. 
[Classes][classes and decisions] defined in `common` bundles 
have global scope.

Note that namespaced bundles work exactly the same way as
non-namespaced bundles (which are actually in the `default`
namespace).  You just say `namespace:bundle_name` instead of
`bundle_name`.
