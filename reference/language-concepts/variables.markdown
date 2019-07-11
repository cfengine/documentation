---
layout: default
title: Variables
published: true
sorting: 60
tags: [manuals, language, syntax, concepts, variables]
---

Just like [classes][classes and decisions] are defined as
promises, variables (or "variable definitions") are also promises. Variables
can be defined in any promise [bundle][bundles]. This bundle name can be used
as a context when using variables outside of the bundle they are defined in.

CFEngine variables have three high-level types: scalars, lists, and
data containers.

* A scalar is a single value,
* a list is a collection of scalars.
* a data container is a lot like a JSON document, it can be a key-value map or an array or anything else allowed by the JSON standard with unlimited nesting.

## Scalar Variables

Each scalar may have one of three types: string, int or real. String scalars
are sequences of characters, integers are whole numbers, and reals are float
pointing numbers.

```cf3
    vars:
      "my_scalar" string => "String contents...";
      "my_int" int       => "1234";
      "my_real" real     => "567.89";
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

Lastly, there is a reserved value which can be used to specify a parameter as
having no limit at all.

* 'inf' = a constant representing an unlimited value.

  ```inf``` is a special value that in the code corresponds to the magic number of ```999999999``` (nine nines). Thus any function that accepts a number, can accept inf without a problem. Keep in mind though that you can get a higher number if you set the upper limit manually, but that's almost never a problem.

  For a few functions ```inf``` is being treated specially and truly means "there is no limit" instead of "nine nines limit". This is the case for the ```maxbytes``` parameter and applies to most read* functions.

CFEngine typing is mostly dynamic, and CFEngine will try to coerce string
values into int and real types, and if it cannot it will report an error.
However, arguments to built-in [functions][Functions] check the
defined argument type for consistency.

### Scalar Referencing and Expansion

Scalar variables are referenced by `$(my_scalar)` (or `${my_scalar}`) and
expand to the single value they hold at that time. If you refer to a variable
by `$(unqualified)`, then it is assumed to belong to the current bundle. To
access any other (scalar) variable, you must qualify the name, using the name
of the bundle in which it is defined:

    $(bundle_name.qualified)

### Quoting

When quoting strings cfengine allows the use of `'`, `"`, and or `` ` ``. This
allows flexibilty when defining strings that contain quotes. Single or double
quotes can be escaped with `\` however, please note that backticks (`` ` ``) can **not**
be escaped.

[%CFEngine_include_example(quoting.cf)%]

### Scalar Size Limitations

At the moment, up to 4095 bytes can fit into a scalar variable.  This
limitation may be removed in the future.

If you try to expand strings in a variable or string context that add
up to more that 4095 bytes, you will notice this limitation as well.
The functions `eval()` to do math, `string_head()` and `string_tail()`
to extract a certain number of characters from either end of a string,
and `string_length()` to find a string's length may be helpful.

See `readfile()` for more detail on reading values from a file.

See `data_readstringarray()` and `data_readstringarrayidx()` for a way
to read large files' contents into a data container without going
through scalar variables or arrays.

## Lists

List variables can be of type `slist`, `ilist` or `rlist` to hold lists of
strings, integers or reals, respectively.

Every element of a list is subject to the same size limitations as a
regular scalar.

They are declared as follows:

```cf3
     vars:
         "my_slist" slist => { "list", "of", "strings" };
         "my_ilist" ilist => { "1234", "5678" };
         "my_rlist" rlist => { "567.89" };
```

### List Substitution and Expansion

An entire list is referenced with the symbol ‘@’ and can be passed in their
entirety in any context where a list is expected as `@(list)`. For example,
the following variable definition references a list named "shortlist":

```cf3
    vars:
        "shortlist" slist => { "you", "me" };
        "longlist" slist => { @(shortlist), "plus", "plus" };
```

The declaration order does not matter – CFEngine will understand the
dependency, and execute the promise to assign the variable `@(shortlist)`
before the promise to assign the variable `@(longlist)`.

Using the @ symbol in a string scalar will not result in list substitution.
For example, the string value "My list is @(mylist)" will not expand this
reference.

Using the scalar reference to a local list variable, will cause CFEngine to
iterate over the values in the list. E.g. suppose we have local list variable
`@(list)`, then the scalar `$(list)` implies an iteration over every value of
the list.

In some function calls, `listname` instead of `@(listname)` is
expected.  See the specific function's documentation to be sure.

## Data Container Variables

The `data` containers can contain several levels of data structures,
e.g. list of lists of key-value arrays. They are used to store
structured data, such as data read from JSON or YAML files. The
variable type is `data`.

Data containers are obtained from functions that return `data` types,
such as `readjson()` or `parsejson()`, `readyaml()` or `parseyaml()`,
or from merging existing containers.

They can **NOT** be *modified*, once created, but they can be re-defined.

Data containers do not have the size limitations of regular scalar
variables.

[%CFEngine_include_example(reference_values_inside_data.cf)%]

## Associative Arrays

Note that associative arrays are being deprecated in favor of the `data`
variable type. It is recommended to use the `data` variable type instead
whenever possible to ensure future compatibility of your CFEngine policy.

Every value in an associative array is subject to the same size
limitations as a regular scalar.

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
`cf-monitord`, `cf-serverd`, and `cf-execd`. They are sequentially printed
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

