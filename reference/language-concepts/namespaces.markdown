---
layout: default
title: Namespaces
published: true
sorting: 100
tags: [manuals, language, syntax, concepts, namespace]
---

By default all things are in the `default` namespace. Specifying a namespace
places the bundle or body in a different namespace to allow re-use of common
names. Using namespaces makes it easier to share and consume policy from other
authors.

Like bundle names and classes, namespaces may only contain alphanumeric and
underscore characters (`a-zA-Z0-9_`).

### Declaration

Namespaces are declared with [`body file control`][file control#namespace]. A
namespace applies within a single file to all subsequently defined bodies
following the namespace declaration until a different namespace has been
declared or until the end of the file.

[%CFEngine_include_example(namespace_declaration.cf)%]

**Notes:**

- Multiple namespaces can be declared within the same file
- The same namespace can be declared in multiple files
- The same namespace can be declared in the same file multiple times

### Methods|usebundle

Methods promises assume you are referring to a bundle in the same namespace as
the promiser. To refer to a bundle in another namespace you *must* specify the
namespace by prefixing the bundle name with the namespace followed by a colon
(`:`).

[%CFEngine_include_example(namespace_methods-usebundle.cf)%]

### Accessing syntax elements between namespaces and the default namespace

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

**Note** that this means that if you are in a namespace that's not `default`, you *must* qualify classes from `default` fully:

    default:myclass::
    "do something" if => "default:myotherclass";

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

As a workaround, you could have a helper bundle in another namespace
to create classes and variables as needed.

### Exceptions to namespacing rules

Exceptions to the rules above:

* All hard classes can be used as-is from any namespace, without a namespace
  prefix.  These are classes like `linux`.  They will have the
  tag `hardclass`.

* All special variable contexts, as documented in [Special Variables],
  are always accessible without a namespace prefix.  For
  example, `this`, `mon`, `sys`, and `const` fall in this category.
