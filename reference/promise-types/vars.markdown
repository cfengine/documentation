---
layout: default
title: vars
categories: [Reference, Promise Types, vars]
published: true
alias: reference-promise-types-vars.html
tags: [reference, bundle common, vars, promises]
---

[Variables](manuals-language-concepts-variables.html) in CFEngine are defined 
as promises that an identifier of a certain type represents a particular 
value. Variables can be scalars or lists of types `string`, `int` or `real`. 
Arrays are `associative` and use square brackets `[]` to enclose an-arbitrary 
key.

***

## Scalar Variables

### string

**Description**: A scalar string

**Type**: `string`

**Allowed input range**: (arbitrary string)

**Example**:  


```cf3
    vars:

     "xxx"    string => "Some literal string...";
     "yyy"    string => readfile( "/home/mark/tmp/testfile" , "33" );
```

### int

**Description**: A scalar integer

**Type**: `int`

**Allowed input range**: `-99999999999,9999999999`

**Example**:  

```cf3
    vars:

     "scalar" int    => "16k";
     "ran"    int    => randomint(4,88);
     "dim_array" int =>  readstringarray("array_name","/etc/passwd","#[^\n]*",":",10,4000);
```

**Notes**:  

Int variables are strings that are expected to be used as integer numbers. The 
typing in CFEngine is dynamic, so the variable types are interchangeable. 
However, when you declare a variable to be type `int`, CFEngine verifies that 
the value you assign to it looks like an integer (e.g., 3, -17, 16K).

### real

**Description**: A scalar real number

**Type**: `real`

**Allowed input range**: `-9.99999E100,9.99999E100`

**Example**:  

```cf3
    vars:
   
     "scalar" real   => "0.5";
```

**Notes**:  

Real variables are strings that are expected to be used as real numbers. The 
typing in CFEngine is dynamic, so the variable types are interchangeable, but 
when you declare a variable to be type `real`, CFEngine verifies that the 
value you assign to it looks like a real number (e.g., 3, 3.1415, .17, 
6.02e23, -9.21e-17).

Real numbers are not used in many places in CFEngine, but they are useful for 
representing probabilities and performance data.

***

## List variables

Lists are specified using curly brackets `{}` that enclose a 
comma-separated list of values.

### slist

**Description**: A list of scalar strings

**Type**: `slist`

**Allowed input range**: (arbitrary string)

**Example**:  

```cf3
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
```

**Notes**:

Some [functions](reference-functions.html]) return `slist`s, and an `slist` 
may contain the values copied from another `slist`, `rlist`, or `ilist`. See 
`policy`. **TODO: NEED anchors in pages**

### ilist

**Description**: A list of integers

**Type**: `ilist`

**Allowed input range**: `-99999999999,9999999999`

**Example**:  

```cf3
    vars:

      "variable_id"

           ilist => { "10", "11", "12" };
```

**Notes**:  

Integer lists are lists of strings that are expected to be treated as
integers. The typing in CFEngine is dynamic, so the variable types are
interchangeable, but when you declare a variable to be type `ilist`,
CFEngine verifies that each value you assign to it looks like an integer
(e.g., 3, -17, 16K).

Some [functions](reference-functions.htm) return `ilist`s, and an `ilist` may 
contain the values copied from another `slist`, `rlist`, or `ilist`. See 
`policy`

### rlist

**Description**: A list of real numbers

**Type**: `rlist`

**Allowed input range**: `-9.99999E100,9.99999E100`

**Example**:  

```cf3
    vars:

      "varid" rlist => { "0.1", "0.2", "0.3" };
```

**Notes**:  
   
Real lists are lists of strings that are expected to be used as real
numbers. The typing in CFEngine is dynamic, so the variable types are
interchangeable, but when you declare a variable to be type `rlist`,
CFEngine verifies that each value you assign to it looks like a real
number (e.g., 3, 3.1415, .17, 6.02e23, -9.21e-17).

Some [functions](reference-functions.html) return `rlist`s, and an `rlist` may 
contain the values copied from another `slist`, `rlist`, or `ilist`. See `policy`

***

## Attributes

### policy

**Description**: The policy for (dis)allowing (re)definition of variables

Variables can either be allowed to change their value dynamically (be
redefined) or they can be constant.

**Type**: (menu option)

**Allowed input range**:   

```cf3
    free
    overridable
    constant
    ifdefined
```

**Default value**:  

`policy = constant`

**Example**:  

```cf3
    vars:

      "varid" string => "value...",
              policy => "constant";
```

**Notes**:  

The policy `constant` indicates that the variable value may not be changed. 
The policies `free` and `overridable` are synonymous, and indicated that the 
variable's value may be changed.

The policy `ifdefined` applies only to lists and implies that unexpanded or 
undefined lists are dropped. The default behavior is otherwise to retain this 
value as an indicator of the failure to quench the variable reference, for 
example:

```cf3
    "one" slist => { "1", "2", "3" };

    "list" slist => { "@(one)", @(two) },
          policy => "ifdefined";
```
This results in `@(list)` being the same as `@(one)`, and the reference to 
`@(two)` disappears. This is useful for combining lists.
