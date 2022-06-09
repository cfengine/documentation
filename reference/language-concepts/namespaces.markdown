---
layout: default
title: Namespaces
published: true
sorting: 100
tags: [manuals, language, syntax, concepts, namespace]
---

By default all promises are made in the `default` namespace. Specifying a namespace
places the bundle or body in a different namespace to allow re-use of common
names. Using namespaces makes it easier to share and consume policy from other
authors.

Like bundle names and classes, namespaces may only contain alphanumeric and
underscore characters (`a-zA-Z0-9_`).

## Declaration

Namespaces are declared with [`body file control`][file control#namespace]. A
namespace applies within a single file to all subsequently defined bodies
following the namespace declaration until a different namespace has been
declared or until the end of the file.

[%CFEngine_include_example(namespace_declaration.cf)%]

**Notes:**

- Multiple namespaces can be declared within the same file
- The same namespace can be declared in multiple files
- The same namespace can be declared in the same file multiple times

## Methods|usebundle

Methods promises assume you are referring to a bundle in the same namespace as
the promiser. To refer to a bundle in another namespace you *must* specify the
namespace by prefixing the bundle name with the namespace followed by a colon
(`:`).

[%CFEngine_include_example(namespace_methods-usebundle.cf)%]

## Bodies

Bodies are assumed to be within the same namespace as the promiser. To use a body from another namespace the namespace must be specified by prefixing the body name with the namespace followed by a colon (`:`).

A common mistake is forgetting to specify `default:` when using bodies from the standard library which resides in the `default` namespace.

[%CFEngine_include_example(namespace_bodies.cf)%]

## Variables

Variables (except for Special Variables) are assumed to be within the same scope
as the promiser but can also be referenced fully qualified with the namespace.

[%CFEngine_include_example(namespace_variable_references.cf)%]

[Special variables][Special Variables] are always accessible without a namespace
  prefix. For example, `this`, `mon`, `sys`, and `const` fall in this category.

[%CFEngine_include_example(namespace_special_var_exception.cf)%]

**Notes:**

- The [`variables` Augments key][Augments#variables] defines variables in the
  `main` bundle of the `data` namespace by default supports seeding variable
  values in any specified namespace.

## Classes

Promises can only define classes within the current namespace. Classes are
understood to refer to classes in the current namespace if a namespace is not
specified (except for Hard Classes). To refer to a
class in a different namespace prefix the class with the namespace suffixed by a
colon (`:`).

[%CFEngine_include_example(namespace_classes.cf)%]

[Hard classes][Classes and Decisions#Hard Classes] exist in all namespaces and
thus can be referred to from any namespace without qualification.

[%CFEngine_include_example(namespace_hard_classes.cf)%]

