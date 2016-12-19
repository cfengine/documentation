---
layout: default
title: defaults
published: true
tags: [reference, bundle common, defaults, promises]
---

Defaults promises are related to [variables][variables]. If a variable or
parameter in a promise bundle is undefined, or its value is defined to be
invalid, a default value can be promised instead.

CFEngine does not use Perl semantics: i.e. undefined variables do not map to
the empty string, they remain as variables for possible future expansion. Some
variables might be defined but still contain unresolved variables. To handle
this you will need to match the `$(abc)` form of the variables.

```cf3
    body common control
    {
    bundlesequence => { "main" };
    }

    bundle agent main
    {
    methods:

      "example"  usebundle => test("one","x","","$(four)");

    }

    bundle agent test(a,b,c,d)
    {
    defaults:

     "a" string => "default a", if_match_regex => "";
     "b" string => "default b", if_match_regex => "x";
     "c" string => "default c", if_match_regex => "";
     "d" string => "default d", if_match_regex => "\$\([a-zA-Z0-9_.]+\)";

    reports:

       "a = '$(a)', b = '$(b)', c = '$(c)' d = '$(d)'";
    }
```

Another example:

```cf3
bundle agent example
{
defaults:

  "X" string => "I am a default value";
  "Y" slist => { "I am a default list item 1", "I am a default list item 2" };

methods:

 "example" usebundle => mymethod("","bbb");

reports:

   "The default value of X is $(X)";
   "The default value of Y is $(Y)";
}

###########################################################

bundle agent mymethod(a,b)
{
vars:

  "no_return" string => "ok"; # readfile("/dont/exist","123");

defaults:

  "a" string => "AAAAAAAAA",   if_match_regex => "";
  "b" string => "BBBBBBBBB",   if_match_regex => "";
  "no_return" string => "no such file";

reports:

     "The value of a is $(a)";
     "The value of b is $(b)";

     "The value of no_return is $(no_return)";
}
```

***

## Attributes ##

### if_match_regex

**Description:** If this [anchored][anchored] regular expression matches the
current value of the variable, replace it with default.

If a parameter or variable is already defined in the current context, and the
value matches this regular expression, it will be deemed invalid and replaced
with the default value.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

[%CFEngine_include_example(defaults.cf)%]

