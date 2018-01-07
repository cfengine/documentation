---
layout: default
title: System File Examples
published: true
sorting: 13
tags: [Examples,System Administration,System Files]
---

## Editing password or group files ##

To change the password of a system, we need to edit a file. A file is a complex object – once open there is a new world of possible promises to make about its contents. CFEngine has bundles of promises that are specially for editing.


[%CFEngine_include_snippet(editing_password_or_group_files.cf, .* )%]

## Editing password or group files custom ##

In this example the bundles from the Community Open Promise-Body Library are included directly in the policy instead of being input as a separate file.


[%CFEngine_include_snippet(editing_password_or_group_files_custom.cf, .* )%]

## Log rotation


[%CFEngine_include_snippet(log_rotation.cf, .* )%]

## Garbage collection


[%CFEngine_include_snippet(garbage_collection.cf, .* )%]

## Manage a system file

    Simple template
    Simple versioned template
    Macro template
    Custom editing

### Simple template


[%CFEngine_include_snippet(simple_template.cf, .* )%]

### Simple versioned template

The simplest approach to managing a file is to maintain a master copy by hand, keeping it in a version controlled repository (e.g. svn), and installing this version on the end machine.

We'll assume that you have a version control repository that is located on some independent server, and has been checked out manually once (with authentication) in /mysite/masterfiles.


[%CFEngine_include_snippet(simple_versioned_template.cf, .* )%]

### Macro template

The next simplest approach to file management is to add variables to the template that will be expanded into local values at the end system, e.g. using variables like ‘$(sys.host)’ for the name of the host within the body of the versioned template.


[%CFEngine_include_snippet(macro_template.cf, .* )%]

The macro template file may contain variables, as below, that get expanded by CFEngine.


[%CFEngine_include_snippet(macro_template_1.cf, .* )%]

### Custom editing

If you do not control the starting state of the file, because it is distributed by an operating system vendor for instance, then editing the final state is the best approach. That way, you will get changes that are made by the vendor, and will ensure your own modifications are kept even when updates arrive.


[%CFEngine_include_snippet(custom_editing.cf, .* )%]

Another example shows how to set the values of variables using a data-driven approach and methods from the standard library.

[%CFEngine_include_snippet(custom_editing_1.cf, .* )%]
