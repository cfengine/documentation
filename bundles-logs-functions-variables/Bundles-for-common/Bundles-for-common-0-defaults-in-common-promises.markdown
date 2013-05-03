---
layout: default
title: defaults-in-common-promises
categories: [Bundles-for-common,defaults-in-common-promises]
published: true
alias: Bundles-for-common-defaults-in-common-promises.html
tags: [Bundles-for-common,defaults-in-common-promises]
---

### `defaults` promises in \*

\

Defaults promises are related to variables. If a variable or parameter
in a promise bundle is undefined, or its value is defined to be invalid,
a default value can be promised instead.

CFEngine does not use Perl semantics: i.e. undefined variables do not
map to the empty string, they remain as variables for possible future
expansion.

Some variables might be defined but still contain unresolved variables.
To handle this you will need to match the `$(abc)` form of the
variables.

~~~~ {.verbatim}
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

   !nothing::

   "a = '$(a)', b = '$(b)', c = '$(c)' d = '$(d)'";
}
~~~~

Another example:

~~~~ {.verbatim}
bundle agent example

{     
defaults:

  "X" string => "I am a default value";
  "Y" slist => { "I am a default list item 1", "I am a default list item 2" };

methods:

 "example" usebundle => mymethod("","bbb");

reports:

 !xyz::

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

  !xyz::

     "The value of a is $(a)";
     "The value of b is $(b)";

     "The value of no_return is $(no_return)";

}
~~~~

\

-   [if\_match\_regex in defaults](#if_005fmatch_005fregex-in-defaults)
-   [string in defaults](#string-in-defaults)
-   [slist in defaults](#slist-in-defaults)

#### `if_match_regex`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: If this regular expression matches the current value of
the variable, replace it with default

If a parameter or variable is already defined in the current context,
and the value matches this regular expression, it will be deemed invalid
and replaced with the default value.

**Example**:\
 \

~~~~ {.verbatim}
bundle agent mymethod(a,b)
{
defaults:

  "a" string => "AAAAAAAAA",   if_match_regex => "";
  "b" string => "BBBBBBBBB",   if_match_regex => "";
}
~~~~

#### `string`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: A scalar string

In previous versions of CFEngine lists were represented (as in the
shell) using separated scalars; similar to the PATH variable. In
CFEngine 3 lists are kept as an independent type.

**Example**:\
 \

~~~~ {.verbatim}
vars:

 "xxx"    string => "Some literal string...";

 "yyy"    string => readfile( "/home/mark/tmp/testfile" , "33" );
~~~~

#### `slist`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: A list of scalar strings

Some functions return `slist`s (see [Introduction to
functions](#Introduction-to-functions)), and an `slist` may contain the
values copied from another `slist`, `rlist`, or `ilist` (see [List
variable substitution and
expansion](#List-variable-substitution-and-expansion), and [policy in
vars](#policy-in-vars)).

**Example**:\
 \

~~~~ {.verbatim}
vars:

 "xxx"    slist  => {  "literal1",  "literal2" };

 "yyy"    slist  => { 
                    readstringlist(
                                  "/home/mark/tmp/testlist",
                                  "#[a-zA-Z0-9 ]*",
                                  "[^a-zA-Z0-9]",
                                  15,
                                  4000
                                  ) 
                    };

 "zzz"    slist  => { readstringlist("/home/mark/tmp/testlist2","#[^\n]*",",",5,4000) };

~~~~
