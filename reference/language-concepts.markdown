---
layout: default
title: Language Concepts
published: true
sorting: 50
tags: [overviews, language, syntax, concepts, promises]
---

There is only one grammatical form for statements in the language:

```cf3
    bundle bundle_type name
    {
    promise_type:

      classes::

        "promiser" -> { "promisee1", "promisee2", ... }

            attribute_1 => value_1,
            attribute_2 => value_2,
            ...
            attribute_n => value_n;
    }
```

In addition, CFEngine bodies can be defined and used as attribute values.  Here's a real-life example of a body and its usage.

```cf3
body edit_defaults no_backup
{
      edit_backup => "false";
}

... and elsewhere, noting the attribute name matches the body type ...

  files:
    "myfile" edit_defaults => no_backup;


```

You can recognize *everything* in CFEngine from just those few concepts.

* [**Promise**][promises]

A declaration about the *state* we desire to maintain (e.g., the permissions
or contents of a file, the availability or absence of a service, the
(de)installation of a package).

* [**Bundles**][bundles]

A collection of promises.

* [**Bodies**][bodies]

A part of a promise which details and constrains its nature, possibly in
separate and re-usable parts.  Effectively a body is like a promise attribute that has several parameters.

* [**Classes**][classes and decisions]

CFEngine's boolean classifiers that describe context.

* [**Variables and Datatypes**][variables]

An association of the form "LVALUE *represents* RVALUE", where RVALUE may be a
scalar value or a list of scalar values: a string, integer or real number.

This documentation about the language concepts introduces in addition

* [**normal ordering**][Normal Ordering],
* [**loops**][Loops],
* [**pattern matching and referencing**][Pattern Matching and Referencing],
  and
* [**namespaces**][namespaces]

## Syntax, identifiers and names

The CFEngine 3 language has a few simple rules:

* CFEngine built-in words, names of variables, bundles, body templates and classes may only contain the usual alphanumeric and underscore characters (`a-zA-Z0-9_`)
* All other 'literal' data must be quoted.
* Declarations of promise bundles in the form:

        bundle agent-type identifier
        {
        ...
        }

    where `agent-type` is the CFEngine component responsible for maintaining the promise.

* Declarations of promise body-parts in the form:

        body constraint_type template_identifier
        {
        ...
        }

    matching and expanding on a reference inside a promise of the form `constraint_type => template_identifier`

* attribute expressions in the body of a promise take the form

        left-hand-side (CFEngine_word) => right-hand-side (user defined data).

    This can take several forms:

        cfengine_word => user_defined_template(parameters)
                      user_defined_template
                      builtin_function()
                      "quoted literal scalar"
                      { list }

    In each of these cases, the right hand side is a user choice.

	CFEngine uses many `constraint expressions' as part of the body of a promise. These take the form: left-hand-side (cfengine word) ‘=>’ right-hand-side (user defined data). This can take several forms:

	    cfengine_word => user_defined_template(parameters)
	        user_defined_template
	        builtin_function()
	        "quoted literal scalar"
	        { list }

	In each of these cases, the right hand side is a user choice.

## Filenames and Paths

Filenames in Unix-like operating systems use the forward slash '/'
character for their directory separator. All references to file
locations must be absolute pathnames in CFEngine, i.e. they must
begin with a complete specification of which directory they are in or with a variable reference that resolves to that.
For example:

    /etc/passwd
    /var/cfengine/masterfiles/distfile
    $(sys.masterdir)/distfile # usually the same thing in 3.6

The only place where it makes sense to refer to a file without a
complete directory specification is when searching through
directories for different kinds of file, e.g. in pattern matching

    leaf_name => { "tmp_.*", "output_file", "core" };

Here, one can write core without a path, because one is looking for
any file of that name in a number of directories.

The Windows operating systems traditionally use a different
filename convention. The following are all valid absolute file
names under Windows:

    c:\winnt
    "c:\spaced name"
    c:/winnt
    /var/cfengine/inputs
    //fileserver/share2/dir

The 'drive' name "C:" in Windows refers to a partition or device.
Unlike Unix, Windows does not integrate these seamlessly into a
single file-tree. This is not a valid absolute filename:

    \var\cfengine\inputs

Paths beginning with a backslash are assumed to be win32 paths.
They must begin with a drive letter or double-slash server name.

Note that in many cases, you have `sys.inputdir` and other
[Special Variables] that work equally well on Windows and non-Windows
system.

Note in recent versions of Cygwin you can decide to use the
`/cygdrive` to specify a path to windows file E.g
/cygdrive/c/myfile means c:\\myfile or you can do it straight away
in CFEngine as `c:\myfile`.
