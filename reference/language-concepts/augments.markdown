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

Filenames entered here will appear in the `def.augments_inputs` variable.

**Notes:**

* Files are loaded relative to `sys.policy_entry_dirname`.

* The *inputs* key has precedence over the *vars* key.

* If both the _inputs_ key and `vars.augments_inputs` are populated concurrently,
  the variable `def.augments_inputs` will hold the value set by the *inputs*
  key. The `def.augments_inputs` variable is part of the default inputs in the
  `Masterfiles Policy Framework`.

**Examples:**

```json
{
    "inputs": [ "services/hello-world.cf", "example.cf", "/tmp/my_policy.cf" ],
    "vars": {
        "augments_inputs": [ "goodbye.cf" ]
    }
}
```

The above Augments results in `$(sys.policy_entry_dirname)/services/hello-world.cf`, `$(sys.policy_entry_dirname)/example.cf` and `/tmp/my_policy.cf` being added to inputs.

```json
{
    "vars": {
        "augments_inputs": [ "goodbye.cf" ]
    }
}
```

The above Augments results in `$(sys.policy_entry_dirname)/goodbye.cf` being added to inputs.


```json
{
    "vars": {
        "augments_inputs": [ "goodbye.cf" ]
    }
}
```

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

Any class defined via augments will be evaluated and installed as
[**hard** classes][Classes and Decisions]. Each element
of the array is tested against currently defined classes
as an [anchored regular expression][anchored] unless the string ends with ```::```
indicating it should be interpreted as a
[*class expression*][Classes and Decisions].

Note that augments is processed at the very beginning of agent evaluation. You
can use any **hard** classes, [**persistent** classes][Classes and Decisions]
, or classes defined earlier in the augments list. Test carefully, custom [**soft** classes][Classes and Decisions]
may not be defined early enough for use. Thus:

```
"classes":
{
  "augments_class_from_regex_my_always": [ "any" ],
  "augments_class_from_regex_my_other_apache": [ "server[34]", "debian.*" ],
  "augments_class_from_regex_my_other_always": [ "augments_class_from_regex_my_always" ],
  "augments_class_from_regex_when_MISSING_not_defined": [ "^(?!MISSING).*" ]
  "augments_class_from_regex": [ "cfengine_\\d+" ],
  "augments_class_from_single_class_as_regex": [ "cfengine" ],
  "augments_class_from_single_class_as_expression": [ "cfengine::" ],
  "augments_class_from_classexpression_and": [ "cfengine.cfengine_3::" ],
  "augments_class_from_classexpression_not": [ "!MISSING::" ],
  "augments_class_from_classexpression_or": [ "cfengine|cfengine_3::" ],
  "augments_class_from_classexpression_complex": [ "(cfengine|cfengine_3).!MISSING::" ]
}
```

results in
* `augments_class_from_rgex_my_always` being always defined.

* `augments_class_from_regex_my_other_apache` will be defined if the classes
  `server3` or `server4` are defined, or if any class starting with `debian` is
  defined.

* `augments_class_from_regex_my_other_always` will be defined because
  `augments_class_from_regex_my_always` is listed first and always defined.

* `augments_class_from_regex_when_MISSING_not_defined` will be defined if the
  class `MISSING` is not defined.

* `augments_class_from_single_class_as_regex` will be defined because the class
  `cfengine` is always defined.

* `augments_class_from_single_class_as_expression` will be defined because
  `cfengine` is defined when interpreted as a class expression.

* `augments_class_from_classexpression_and` will be defined because the class
  `cfengine` and the class `cfengine_3` are defined and the class expression
  `cfengine.cfengine_3::` evaluates to true.

* `augments_class_from_classexpression_not` will be defined because the class
  expression `!MISSING::` evaluates to false since the class `MISSING` is not
  defined.

* `augments_class_from_classexpression_or` will be defined because the class
  expression `cfengine|cfengine_3::` evaluates to true since at least one of
  `cfengine` or `cfengine_3` will always be defined by cfengine 3 agents.

* `augments_class_from_classexpression_complex` will be defined because the
  class expression `(cfengine|cfengine_3).!MISSING::` evaluates to true since at
  least one of `cfengine` or `cfengine_3` will always be defined by cfengine 3
  agents and `MISSING` is not defined.

You can see the list of classes thus defined through `def.json` in the output
of `cf-promises --show-classes` (see [Components and Common Control][]). They
will be tagged with the tags `source=augments_file,hardclass`. For instance:

```console
% cf-promises --show-classes=my_
...
augments_class_from_regex_my_always                                                    source=augments_file,hardclass
augments_class_from_regex_my_other_always                                              source=augments_file,hardclass
augments_class_from_regex_my_other_apache                                              source=augments_file,hardclass
```

**See also:**

* Functions that use regular expressions with classes: `classesmatching()`,
  `classmatch()`, `countclassesmatching()`

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

- 3.12.2, 3.14.0 introduced class expression interpretation (`::` suffix) to classes key
- 3.12.0 introduced the `augments` key
- 3.7.3 back port `def.json` parsing in core agent and load `def.json` if present next to policy entry
- 3.8.2 removed core support for `inputs` key, load `def.json` if present next to policy entry
- 3.8.1 `def.json` parsing moved from policy to core agent for resolution of classes and variables to be able to affect control bodies
- 3.7.0 introduced augments concept into the Masterfiles Policy Framework
