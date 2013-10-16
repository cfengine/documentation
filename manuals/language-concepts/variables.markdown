---
layout: default
title: Variables
categories: [Manuals, Language Concepts, Variables]
published: true
sorting: 50
alias: manuals-language-concepts-variables.html
tags: [manuals, language, syntax, concepts, variables]
---

Just like [classes][classes and decisions] are defined as 
promises, variables (or "variable definitions") are also promises. Variables 
can be defined in any promise [bundle][bundles]. This bundle name can be used 
as a context when using variables outside of the bundle they are defined in.

CFEngine variables have two high-level types: scalars and lists. 

* A scalar is a single value,
* a list is a collection of scalars.

## Scalar Variables

Each scalar may have one of three types: string, int or real. String scalars 
are sequences of characters, integers are whole numbers, and reals are float 
pointing numbers.

```cf3
    vars:
      "my_scalar" string => "String contents...";
      "my_int" int    => "1234";
      "my_real" real   => "567.89";
```

Integer constants may use suffixes to represent large numbers.  The following 
suffixes can be used to create integer values for common powers of 1000.

* 'k' = value times 1000
* 'm' = value times 1000^2
* 'g' = value times 1000^3

Since computing systems such as storage and memory are based on binary values, 
CFEngine also provide the following uppercase suffixes to create integer 
values for common powers of 1024.

* 'K' = value times 1024.
* 'M' = value times 1024^2
* 'G' = value times 1024^3

However, the values must have an integer numeric part (e.g. 1.5M is not 
allowed).

In some contexts, `%` can be used a special suffix to denote percentages.

Lastly, there is a reserved value which can be used to specific a parameter as 
having no limit at all.

* 'inf' = a constant representing an unlimited value.

CFEngine typing is mostly dynamic, and CFEngine will try to coerce string 
values into int and real types, and if it cannot it will report an error. 
However, arguments to built-in [functions][Functions] check the 
defined argument type for consistency.

### Scalar Referencing and Expansion

Scalar variables are referenced by `$(my_scalar)` (or `${my_scalar}`) and 
expand to the single value they hold at that time. if you refer to a variable 
by ‘$(unqualified)’, then it is assumed to belong to the current bundle. To 
access any other (scalar) variable, you must qualify the name, using the name 
of the bundle in which it is defined:

    $(bundle_name.qualified)

## Lists

List variables can be of type `slist`, `ilist` or `rlist` to hold lists of 
strings, integers or reals, respectively.

They are declared as follows:

```cf3
     vars:
         "my_slist" slist => { "list", "of", "strings" };
         "my_ilist" ilist => { "1234", "5678" };
         "my_rlist" rlist => { "567.89" };
```

### List Substitution and Expansion

An entire list is referenced with the symbol ‘@’ and can be passed in their 
entirety in any context where a list is expected as ‘@(list)’. For example, 
the following variable definition references a list named "shortlist":

```cf3
    vars:
        "shortlist" slist => { "you", "me" };
        "longlist" slist => { @(shortlist), "plus", "plus" };
```

The declaration order does not matter – CFEngine will understand the 
dependency, and execute the promise to assign the variable ‘@(shortlist)’ 
before the promise to assign the variable ‘@(longlist)’.

Using the @ symbol in a string scalar will not result in list substitution.  
For example, the string value "My list is @(mylist)" will not expand this 
reference.

Using the scalar reference to a local list variable, will cause CFEngine to 
iterate over the values in the list. E.g. suppose we have local list variable 
‘@(list)’, then the scalar ‘$(list)’ implies an iteration over every value of 
the list.

### Mapping Global and Local Lists

Only local lists can be expanded directly. Thus ‘$(list)’ can be expanded but 
not ‘$(context.list)’. Global list references have to be mapped into a local 
context if you want to use them for iteration.  Instead of doing this in some 
arbitrary way, with possibility of name collisions, CFEngine requires you to 
make this mapping explicit. There are two possible approaches.

The first uses parameterization to map a global list into a local context.

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

In this example, there is a bundle named `hardening` which takes a list 
argument. This list argument is defined in the context `va` and is passed to 
the `hardening` bundle via an argument listed in the `bundlesequence`.

As you can see, the reports section references both the list passed in as an 
argument `x` and a local list variable defined in `other`.

The alternative is to map the global reference "va.tmpdirs" within the 
hardening bundle.

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

This time, the `hardening` bundle does not take an argument. Instead it 
converts the `va.tmpdirs` list into a local list variable "x" directly.

## Data Container Variables

The `data` containers can contain several levels of data structures,
e.g. list of lists of key-value arrays. They are used to store
structured data, such as data read from JSON files.  The variable type
is `data`.

Data containers are obtained from functions that return `data` types,
such as `readjson()` or `parsejson()`, or from merging existing
containers.

They can *NOT* be modified, once created.

**TODO:** More, and examples

## Associative Arrays

Associative array variables are written with `[` and `]` brackets that enclose 
an arbitrary key. These keys are associated with values

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

This example defines three values in an associative array under the keys 
`cf-monitord`, `cf-serverd`, and `cf-execd`. They and are sequently printed 
with the echo command.

Arrays are associative and may be of type scalar or list. Enumerated arrays 
are simply treated as a special case of associative arrays, since there are no 
numerical loops in CFEngine. Special functions exist to extract lists of keys 
from array variables for iteration purposes.

Here is an example of using the function [`getindices()`][getindices] which 
extracts all of the keys from an associative array. If this series of promises 
were executed it would print out two messages, one for each key.

```cf3
    bundle agent array
    {
      vars:

          "v[index_1]" string => "value_1";
          "v[index_2]" string => "value_2";

          "parameter_name" slist => getindices("v");
      
      reports:
          "Found index: $(parameter_name)";
    }
```

