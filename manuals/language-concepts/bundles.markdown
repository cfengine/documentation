---
layout: default
title: Bundles
categories: [Manuals, Language Concepts, Bundles]
published: true
alias: manuals-language-concepts-bundles.html
tags: [language, concepts, syntax, body, bundle]
---

Previous: [*Promises*](manuals-language-concepts-promises.html)

****

A bundle is a collection of promises. They allow to group related promises 
together into named building blocks that can be thought of as "subroutines" in 
the CFEngine promise language. A bundle that groups a number of promises 
related to configuring a web server or a file system would be named 
"webserver" or "filesystem", respectively.

Most promise types are specific to a particular kind of interpretation that 
requires a typed interpreter - the bundle *type*. Bundles belong to the agent 
that is used to keep the promises in the bundle. So cf-agent has bundles 
declared as:

```cf3
    bundle agent my_name
    {
    }

while cf-serverd has bundles declared as:

    bundle server my_name
    {
    }
```

Bundles can be parameterized, allowing for code re-use. If you need to do the 
same thing over and over again with slight variations, using a promise bundle 
is an easy way to avoid unnecessary duplication in your promises.

```
    bundle agent hello_world
    {
      vars:
          "myfiles"     => "/tmp/world.txt";
          "desired_content" string => "hello";
    
      methods:
          "Hello World"
            usebundle => ensure_file_has_content("$(myfiles)", "$(desired_content)");
        
    
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
```

### Scope

Variables and classes defined inside bundles are not directly visible outside 
those bundles. All [variables](manuals-language-concepts-variables.html) in 
CFEngine are globally accessible. However, if you refer to a variable by 
‘$(unqualified)’, then it is assumed to belong to the current bundle. To 
access any other (scalar) variable, you must qualify the name, using the name 
of the bundle in which it is defined:

    $(bundle_name.qualified)

Bundles of type `common` may contain common promises. 
[Classes](manuals-language-concepts-classes.html) defined in `common` bundles 
have global scope.

Next: [Bodies](manuals-language-concepts-bodies.html)
