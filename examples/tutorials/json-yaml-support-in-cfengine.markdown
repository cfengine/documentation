---
layout: default
title: JSON and YAML Support in CFEngine
published: true
sorting: 2
tags: [json, yaml]
---

## Introduction

JSON is a well-known data language. It even has a specification (See http://json.org).

YAML is another well-known data language. It has a longer, much more complex specification (See http://yaml.org).

CFEngine has core support for JSON and YAML.  Let's see what it can do.

## Problem statement

We'd like to read, access, and merge JSON-sourced data structures:
they should be weakly typed, arbitrarily nested, with consistent
quoting and syntax.

We'd like to read, access, and merge YAML-sourced data structures just
like JSON-sourced, to keep policy and internals simple.

In addition, we must not break backward compatibility with CFEngine
3.5 and older, so we'd like to use the standard CFEngine array `a[b]`
syntax.

## Data containers

A new data type, the data container, was introduced in 3.6.

It's simply called `data`.  The documentation with some examples is at https://cfengine.com/docs/master/reference-promise-types-vars.html#data-container-variables

## Reading JSON

There are many ways to read JSON data; here are a few:

* `readjson()`: read from a JSON file, e.g. `"mydata" data => readjson("/my/file", 100k);`
* `parsejson()`: read from a JSON string, e.g. `"mydata" data => parsejson('{ "x": "y" }');`
* `data_readstringarray()` and `data_readstringarrayidx()`: read text data from a file, split it on a delimiter, and make them into structured data.
* `mergedata()`: merge data containers, slists, and classic CFEngine arrays, e.g. `"mydata" data => mergedata(container1, slist2, array3);`

`mergedata` in particular is very powerful.  It can convert a slist or a classic CFEngine array to a data container easily: `"mydata" data => mergedata(myslist);`

## Reading YAML

There are two ways to read YAML data:

* `readyaml()`: read from a YAML file, e.g. `"mydata" data => readyaml("/my/file.yaml", 100k);`
* `parseyaml()`: read from a YAML string, e.g. `"mydata" data => parseyaml('- arrayentry1');`

Since these functions return data containers, everything about
JSON-sourced data structures applies to YAML-sourced data structures
as well.

## Accessing JSON

To access JSON data, you can use:

* the `nth()` function to access an array element, e.g. `"myx" string => nth(container1, 0);`
* the `nth` function to access a map element, e.g. `"myx" string => nth(container1, "x");`
* the `a[b]` notation, e.g. `"myx" string => "$(container1[x])";`.  You can nest, e.g. `a[b][c][0][d]`.  This only works if the element is something that can be expanded in a string.  So a number or a string work.  A list of strings or numbers works.  A key-value map under `x` won't work.
* the `getindices()` and `getvalues()` functions, just like classic CFEngine arrays

## A full example

This example can be saved and run. It will load a key-value map where
the keys are class names and the values are hostname regular
expressions or class names.

* if your host name is `c` or `b` or the classes `c` or `b` are defined, the `dev` class will be defined
* if your host name is `flea` or the class `flea` is defined, the `prod` class will be defined
* if your host name is `a` or the class `a` is defined, the `qa` class will be defined
* if your host name is `linux` or the class `linux` is defined, the `private` class will be defined

Easy, right?

```cf3
body common control
{
      bundlesequence => { "run" };
}

bundle agent run
{
  vars:
      "bykey" data => parsejson('{ "dev": ["c", "b"], "prod": ["flea"], "qa": ["a"], "private": ["linux"] }');

      "keys" slist => getindices("bykey");

  classes:
      # define the class from the key name if any of the items under the key match the host name
      "$(keys)" expression => regcmp("$(bykey[$(keys)])", $(sys.host));

      # define the class from the key name if any of the items under the key are a defined class
      "$(keys)" expression => classmatch("$(bykey[$(keys)])");

  reports:
      "keys = $(keys)";
      "I am in class $(keys)" if => $(keys);
}
```

So, where's the magic? Well, if you're familiar with classic CFEngine
arrays, you will be happy to hear that the exact same syntax works
with them. In other words, data containers don't change how you use
CFEngine. You still use `getindices` to get the keys, then iterate
through them and look up values.

Well, you can change

```cf3
      "bykey" data => parsejson('{ "dev": ["c", "b"], "prod": ["flea"], "qa": ["a"], "private": ["linux"] }');
```

with

```cf3
      "bykey" data => data_readstringarray(...);
```

and read the same container from a text file. The file should be
formatted like this to produce the same data as above:

```
dev c b
prod flea
qa a
private linux
```

You can also use


```cf3
      "bykey" data => readjson(...);
```

and read the same container from a JSON file.

## Summary

Using JSON and YAML from CFEngine is easy and does not change how you use CFEngine.  Try it out and see for yourself!
