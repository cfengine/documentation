---
layout: default
title: Variables
categories: [Manuals, Language Concepts, Variables]
published: true
alias: manuals-language-concepts-variables.html
tags: [manuals, language, syntax, concepts, variables]
---

Just like classes are defined as promises, variables (or "variable definitions") are also promises.
Variables can be defined in any promise bundle. CFEngine recognizes two variable object types: scalars and lists
(lists contain 0 or more objects), as well as three data-types (string, integer and real).

### Scalar Variables

Scalar variables hold a single value. Here are a series of variable definitions which set a string, an int, and a real variable. Notice that they are defined in a bundle that has the name `name`. This bundle name can be used as a context
when using variables outside of the bundle they are defined in.

```cf3
    bundle <type> name
    {
        vars:
            "my_scalar" string => "String contents...";
            "my_int" int    => "1234";
            "my_real" real   => "567.89";
    }
```

In this previous example, the `type` indicates that any kind of bundle applies here. 

#### Scalar Referencing and Expansion

* Scalar variables are referenced by ‘$(my_scalar)’ (or ‘${my_scalar}’) and they represent a
  single value at a time.
* Scalars that are written without a context, e.g. ‘$(myvar)’ are local to the current bundle.
* Scalars are globally available everywhere provided one uses the context to reference

In the previous example, a variable defined in the "name" bundle could be reference from outside this bundle by using the syntax '$(name.my_scalar)'.

### Lists

List variables hold several values. The are declared as follows:

```cf3
    bundle <type> name
    {
        vars:
            "my_slist" slist => { "list", "of", "strings" };
            "my_ilist" ilist => { "1234", "5678" };
            "my_rlist" rlist => { "567.89" };
    }
```

#### List Substitution and Expansion

An entire list is referenced with the symbol ‘@’ and can be passed in their entirety in any context
where a list is expected as ‘@(list)’. For example, the following variable definition references a list
named "shortlist":

```cf3
    vars:
        "shortlist" slist => { "you", "me" };
        "longlist" slist => { @(shortlist), "plus", "plus" };
```

The declaration order does not matter – CFEngine will understand the dependency, and execute the promise to assign the variable ‘@(shortlist)’ before the promise to assign the variable ‘@(longlist)’.

Using the @ symbol in a string scalar will not result in list substitution.  For example, the string value "My list is @(mylist)" will not expand this reference.

Using the scalar reference to a local list variable, will cause CFEngine to iterate over the values in the list. E.g. suppose we have local list variable ‘@(list)’, then the scalar ‘$(list)’ implies an iteration over every value of the list.

#### Mapping Global and Local Lists

Only local lists can be expanded directly. Thus ‘$(list)’ can be expanded but not ‘$(context.list)’. Global list references have to be mapped into a local context if you want to use them for iteration.  Instead of doing this in some arbitrary way, with possibility of name collisions, CFEngine requires you to make this mapping explicit. There are two possible approaches.

The first uses parameterization to map a global list into a local context.  In the following example, there is a bundle named hardening which takes a list argument.  This list argument is defined in the context "va" and is passed to the hardening bundle via an argument listed in the `bundlesequence`.

As you can see, the reports section reference both the list passed in as an argument "x" and a local list variable defined in "other".

```cf3
    body common control
    {
      bundlesequence => { hardening(@(va.tmpdirs)) };
    }

    bundle common va
    {
        vars:
            "tmpdirs"  slist => { "/tmp", "/var/tmp", "/usr/tmp"  };
    }

    bundle agent hardening(x)
    {
        classes:

            "ok" expression => "any";

        vars:

            "other"    slist => { "/tmp", "/var/tmp" };

        reports:

            ok::

                "Do $(x)";
                "Other: $(other)";
    }
```

This alternative is to map the global reference "va.tmpdirs" within the hardening bundle.  In this next example, the hardening bundle does not take an argument.   What it does is convert the the "va.tmpdirs" list into a local list variable "x" directly.

```cf3
    body common control
    {
        bundlesequence => { hardening };
    }

    bundle common va
    {
        vars:
            "tmpdirs"  slist => { "/tmp", "/var/tmp", "/usr/tmp"  };
    }

    bundle agent hardening
    {
        classes:
            "ok" expression => "any";

        vars:
            "other"    slist => { "/tmp", "/var/tmp" };
            "x"        slist => { @(va.tmpdirs) };

        reports:
            ok::
                "Do $(x)";
                "Other: $(other)";
    }
```

#### A List Variable with Nothing (cf_null)

As of CFEngine core version 3.1.0, the value ‘cf_null’ may be used as a NULL value within lists. This value is ignored in list variable expansion, and can be used as a placeholder.

    vars:

      "empty_list" slist => { "cf_null" };

#### Associative Arrays in CFEngine 3

Associative Array variables are written with ‘[’ and ‘]’ brackets. The following example defines three values in an associative array under the keys "cf-monitord", "cf-serverd", and "cf-execd".  These keys are associated with values, and are sequently printed with the echo command.

```cf3
    bundle agent example

    {
        vars:

            "component" slist => { "cf-monitord", "cf-serverd", "cf-execd" };

            "array[cf-monitord]" string => "The monitor";
            "array[cf-serverd]" string => "The server";
            "array[cf-execd]" string => "The executor, not executioner";

        commands:

            "/bin/echo $(component) is"

                args => "$(array[$(component)])";

    }
```

Arrays are associative and may be of type scalar or list. Enumerated arrays are simply treated as a special case of associative arrays, since there are no numerical loops in CFEngine. Special functions exist to extract lists of keys from array variables for iteration purposes.

Here is an example of using a special function `getindices()` which extracts all of the keys from an associative array. If this series of promises were executed it would print out two messages, one for each key.

```cf3
    bundle agent array
    {
        vars:

            "v[index_1]" string => "value_1";
            "v[index_2]" string => "value_2";

            "parameter_name" slist => getindices("v");
        
        reports:

            Yr2013::

                "Found index: $(parameter_name)";

    }
```

