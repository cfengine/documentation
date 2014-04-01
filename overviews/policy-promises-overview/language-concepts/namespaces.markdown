---
layout: default
title: Namespaces
categories: [Manuals, Language Concepts, Namespaces]
published: true
sorting: 90
alias: manuals-language-concepts-namespaces.html
tags: [manuals, language, syntax, concepts, namespace]
---

Namespaces are private bundle and body "playgrounds", allowing
multiple files to define the bundles and bodies with the same name in
different namespaces without conflict.  They are key to writing
reusable policies.

### Specifying a namespace

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

### Accessing syntax elements between namespaces and the default namespace

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

If you don't make any namespace declarations, you'll be in the
`default` namespace.  Bundles, bodies, classes, and variables from the
`default` namespace can be accessed like any other:

```cf3
    files:
      "/file"
         create => "true",
          perms => default:settings;
```

If you use the standard library from your own namespace, remember to
specify this `default:` prefix.

To access classes, variables, or meta-data in bundles in a different namespace, use the 
colon as a namespace prefix:

    $(namespace:bundle.variable)
    $(namespace:bundle_meta.variable)

Note that this means that if you are in a namespace that's not `default`, you *must* qualify classes from `default` fully:

    default:myclass::
    "do something" ifvarclass => "default:myotherclass";

### Namespacing of classes and variables created in policy

In policy, you can't create classes outside your own namespace.  So
the following, for example, will create the class `mynamespace:done`
if it runs in the namespace `mynamespace`.

```cf3
    files:
      "/file"
         create => "true",
         action => if_repaired("done");
```

Similarly, variables you create in a namespaced bundle have to be
prefixed like `mynamespace:mybundle.myvar` from outside your
namespace, but can use `mybundle.myvar` inside the namespace and
`myvar` inside `mybundle`.

### Exceptions to namespacing rules

Exceptions to the rules above:

* All hard classes can be used as-is, without a namespace
  specification.  These are classes like `linux`.  They will have the
  tag `hardclass`.

* All special variable contexts, as documented in [Special Variables],
  are always accessible without a namespace specification.  For
  example, `this`, `mon`, `sys`, and `const` fall in this category.
