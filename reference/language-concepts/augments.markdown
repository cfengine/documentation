---
layout: default
title: Augments
published: true
sorting: 70
tags: [manuals, language, syntax, concepts, augments]
---

An augments file can be used to define variables and classes to the execution of
**all** CFEngine components **before** any parsing or evaluation happen. It's a
JSON data file, so you should view and edit it with a JSON-aware editor if
possible.This is a convenient way to override defaults defined in the
Masterfiles Policy Framework without modifying the shipped policy itself.

The file `def.json` is found like the policy file to be run:

* with no arguments, it's in `$(sys.inputdir)/def.json` because
  `$(sys.inputdir)/promises.cf` is used
* with `-f /dirname/myfile.cf`, it's in `/dirname/def.json`
* with `-f ./myfile.cf`, it's in `./def.json`

Values will be expanded, so you can use the variables from
[Special Variables][].

An augments file can contain the following keys:

## inputs

Any filenames you put here will appear in the `def.augments_inputs` variable.
The standard set of masterfiles refers to this variable and will autoload those
files.

## vars

Any variables you put here will be put in the `def` bundle scope. Thus:

```
"vars":
{
  "phone": "22-333-4444",
  "myplatform": "$(sys.os)",
}
```

results in the variable `def.phone` with value `22-333-4444` being defined, and
`def.myplatform` with the value of your current OS. Again, note that this
happens before policy is parsed or evaluated.

You can see the list of variables thus defined in the output of `cf-promises
--show-vars` (see [Components and Common Control][]). They will be tagged with
the tag `source=augments_file`. For instance, the above two variables (assuming
you placed the data in `$(sys.inputdir)/def.json`) result in

```
cf-promises --show-vars=default:def
...
default:def.myplatform                   linux                                                        source=augments_file
default:def.phone                        22-333-4444                                                  source=augments_file
```

Variables of other types than string can be defined too, like in this example

```
"vars" : {
    "str1" : "string 1",
    "num1" : 5,
    "num2" : 3.5
    "slist1" : ["sliststr1", "sliststr2"]
    "array1" : {
        "idx1" : "val1",
        "idx2" : "val2"
    }
}
```

## classes

Any class names you put here will be evaluated and installed as **hard classes**
if they match as a class name or a regular expression. Thus:

```
"classes":
{
  "my_always": "any",
  "my_other_apache": [ "server[34]", "debian.*" ],
}
```

results in `my_always` being always defined. `my_other_apache` will be defined
if the classes `server3` or `server4` are defined, or if any class starting
with `debian` is defined. You can use any [**hard** classes][Classes and Decisions].

You can see the list of classes thus defined through `def.json` in the output
of `cf-promises --show-classes` (see [Components and Common Control][]). They
will be tagged with the tags `source=augments_file,hardclass`. For instance,
the above two classes result in:

```
% cf-promises --show-classes=my_
...
my_always                                                    source=augments_file,hardclass
my_other_apache                                              source=augments_file,hardclass
```

## augments

A list of file names that should be merged using `mergedata()` semantic

**Example:**
  
Here we merge a platform specific augments on to the `def.json` loaded next to
the policy entry and see what the resulting variable values will
be.
  
The `def.json` next to the policy entry:
  
```json
{
  "vars":{
    "my_var": "defined in def.json",
    "my_other_var": "Defined ONLY in def.json"
  },
  "augments": [
    "/var/cfengine/augments/$(sys.flavor).json"
  ]
}
```
  
The platform specific augments on a CentOS 6 host:
  
`/var/cfengine/augments/centos_6.json`:
  
```json
{
  "vars": {
    "my_var": "Overridden in centos_6.json",
    "centos_6_var": "Defined ONLY in centos_6.json"
  }
}
```
  
The expected values of the variables defined in the def bundle scope:
  
```console
R: def.my_var == Overridden in centos_6.json
R: def.my_other_var == Defined ONLY in def.json
R: def.centos_6_var == Defined ONLY in centos_6.json
```

# History

- 3.12.0 introduced the `augments` key
- 3.7.3 back port `def.json` parsing in core agent and load `def.json` if present next to policy entry
- 3.8.2 removed core support for `inputs` key, load `def.json` if present next to policy entry
- 3.8.1 `def.json` parsing moved from policy to core agent for resolution of classes and variables to be able to affect control bodies
- 3.7.0 introduced augments concept into the Masterfiles Policy Framework
