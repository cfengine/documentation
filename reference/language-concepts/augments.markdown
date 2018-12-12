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

Any filenames you put here will appear in the `def.augments_inputs`
variable. The standard set of masterfiles refers to this variable and will
autoload those files.

## vars

Any variables you put here will be put in the `def` scope. Thus:

```
"vars":
{
  "phone": "22-333-4444",
  "myplatform": "$(sys.os)",
}
```

results in the variable `def.phone` with value `22-333-4444` being defined,
and `def.myplatform` with the value of your current OS. Again, note that this
happens before policy is parsed or evaluated.

You can see the list of variables thus defined in the output of `cf-promises
--show-vars` (see [Components and Common Control][]). They will be tagged with
the tag `source=augments_file`. For instance, the above two variables
(assuming you placed the data in `$(sys.inputdir)/def.json`) result in

```
cf-promises --show-vars
...
default:def.myplatform                   linux                                                        source=augments_file
default:def.phone                        22-333-4444                                                  source=augments_file
```

## classes

Any class names you put here will be evaluated and installed as **hard classes**
if they match the [anchored regular expression][anchored]. You can use any
[**hard** classes][Classes and Decisions], persistent classes, or classes
defined earlier in the augments list. Thus:

```
"classes":
{
  "my_always": [ "any" ],
  "my_other_apache": [ "server[34]", "debian.*" ],
  "my_other_always": [ "my_always" ],
  "when_MISSING_not_defined": [ "^(?!MISSING).*" ]
}
```

results in `my_always` being always defined. `my_other_apache` will be defined
if the classes `server3` or `server4` are defined, or if any class starting with
`debian` is defined. `my_other_always` will be defined because `my_always` is
always defined, and listed first. `when_MISSING_not_defined` will be defined if
the class `MISSING` is not defined.

You can see the list of classes thus defined through `def.json` in the output
of `cf-promises --show-classes` (see [Components and Common Control][]). They
will be tagged with the tags `source=augments_file,hardclass`. For instance,
the above two classes result in:

```
% cf-promises --show-classes
...
my_always                                                    source=augments_file,hardclass
my_other_always                                              source=augments_file,hardclass
my_other_apache                                              source=augments_file,hardclass
```
**See also:**

* Functions that use regular expressions with classes: `classesmatching()`, `classmatch()`, `countclassesmatching()`

# History

- 3.7.3 back port `def.json` parsing in core agent and load `def.json` if present next to policy entry
- 3.8.2 removed core support for `inputs` key, load `def.json` if present next to policy entry
- 3.8.1 `def.json` parsing moved from policy to core agent for resolution of classes and variables to be able to affect control bodies
- 3.7.0 introduced augments concept into the Masterfiles Policy Framework
