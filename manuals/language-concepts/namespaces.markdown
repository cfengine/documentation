---
layout: default
title: Namespaces
categories: [Manuals, Language Concepts, Namespaces]
published: true
alias: manuals-language-concepts-namespaces.html
tags: [manuals, language, syntax, concepts, namespace]
---

Previous: [Pattern Matching and Referencing](manuals-language-concepts-pattern-matching-and-referencing.html)

****

Namespaces are private bundle and body contexts, allowing multiple files to 
define the bundles and bodies with the same name, without conflict.

To isolate a file into its own namespace, you add a control promise to the 
file before the relevant bundles or bodies. All files start off in the 
`default` namespace if you don't explicitly set this. Once set, this applies 
until the end of the file or the next namespace change.

```cf3
    body file control
    {
       namespace => "myspace"; 
    }
```

To distinguish the bundle `mymethod` in the default namespace from one in 
another namespace, you prefix the bundle name with the namespace, separated by 
a colon.

```cf3
    methods:

      "namespace demo" usebundle => myspace:mymethod("arg1");
      "namespace demo" usebundle => mymethod("arg1","arg2");
```

To distinguish a body from one in another namespace, you can prefix the body name with the namespace, separated by a colon.

```cf3
    files:
       "/file"
          create => "true",
           perms => name1:settings;
```

The default namespace, i.e. that which is implied by not making any namespace 
declarations, can be accessed or referred to by prefixing with the default 
string

```cf3
    files:
      "/file"
         create => "true",
          perms => default:settings;
```

For example, this can be used to refer to standard library objects from within 
a private namespace. Global classes are not handled by namespaces, and you are 
advised to prefix them with the namespace like this:

```cf3
    files:
      "/file"
         create => "true",
         action => if_repaired("namespace_done");
```

This is not prepended automatically because references to this class in class 
expressions cannot be detected and modified automatically.

To access variables or meta-data in bundles in a different namespace, use the 
colon as a namespace prefix:

    $(namespace:bundle.variable)  
    $(namespace:bundle_meta.variable)  

****

Next: [Language Concepts](language-concepts.html)
