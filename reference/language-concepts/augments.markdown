---
layout: default
title: Augments
published: true
sorting: 70
tags: [manuals, language, syntax, concepts, augments]
---

Augments files can be used to define variables and classes for use by
**all** CFEngine components **before** any parsing or evaluation happen. Augments are fundamentally
JSON data files, so you should view and edit them with a JSON-aware editor if
possible. This is a convenient way to override defaults defined in the default policy,
the Masterfiles Policy Framework (MPF), without modifying the shipped policy files.

## Modifying the behavior of the MPF without editing it ##

As an example, you can add your own policy file to inputs and bundle name to the
bundle sequence, without editing `promises.cf` by editing the Augments file
(`/var/cfengine/masterfiles/def.json`):

```json
{
  "inputs": ["services/my_policy_file.cf"],
  "vars":
  {
    "control_common_bundlesequence_end": ["my_bundle_name"]
  }
}
```

In this case, the contents of the policy file, `/var/cfengine/masterfiles/services/my_policy_file.cf`, could look something like this:

```cf3
bundle agent my_bundle_name
{
  files:
    "/tmp/hello"
      create => "true",
      content => "cfengine";
}
```

You can ensure the file is deleted and use the info log output to confirm that the policy is actually being run:

```
$ cf-agent -Kf update.cf && cf-agent -K
$ rm /tmp/hello ; cf-agent -KI
    info: Created file '/tmp/hello', mode 0600
    info: Updated content of '/tmp/hello' with content 'cfengine'
```

In this example, `control_common_bundlesequence_end` is a special variable, handled by the Masterfiles Policy Framework (MPF).
To learn about more variables like this and ways to interact with the MPF without editing it, see the [MPF Reference documentation][Masterfiles Policy Framework].
The rest of this documentation page below focuses on the specifics of how augments files work, independently of everything they can be used for in the MPF.

## Augments Files ##

There are two canonical augments files, `host_specific.json`, and `def.json` which may load additional Augments
as specified by the [_augments_ key][Augments#augments].


### host_specific.json ###

If `$(sys.workdir)/data/host_specific.json` (typically `/var/cfengine/data/host_specific.json`) is the first augments file that is loaded. Any variables defined as a result of processing this file
are automatically tagged with `source=cmdb`. Variables defined from this file can not be overridden by subsequently processed augments files. Policy always wins and thus _can_ overwrite the variable.

**Notes:**

* This file does not support the [_augments_ key][Augments#augments].
* This file does not support expansion of CFEngine variables, including `sys` variables (unlike `def.json`).

### def.json ###

The file `def.json` is found based on the location of the policy entry (the first policy file read by the agent):

* with no arguments, it's in `$(sys.inputdir)/def.json` because
  `$(sys.inputdir)/promises.cf` is used
* with `-f /dirname/myfile.cf`, it's in `/dirname/def.json`
* with `-f ./myfile.cf`, it's in `./def.json`

**Notes:**

* `sys` variables are expanded (unlike `host_specific.json`).
* `def_preferred.json` will be used instead of `def.json` if it is present. This preferential loading can be disabled by providing the `--ignore-preferred-augments` option to the agent.

## Augments Keys ##

An augments file can contain the following keys:

### inputs ###

This key is supported in `def.json`, `def_preferred.json`, and augments loaded by the [_augments_ key][Augments#augments].

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

### variables ###


This key is supported in both `host_specific.json`, `def.json`, `def_preferred.json`, and augments loaded by the [_augments_ key][Augments#augments].

Variables defined here can target a _namespace_ and or _bundle_ scope explicitly. When defined from `host_specific.json`, variables default to the `main` _bundle_ in the `data` _namespace_ (`$(data:main.MyVariable)`).

For example:

```json
{
    "variables": {
        "VariableWithImplicitNamespaceAndBundle": {
            "value": "value"
        }
    }
}
```

Variables can target the _implicit namespace_ while specifying the _bundle_.

For example:

```json
{
    "variables": {
        "my_bundle.VariableWithImplicitNamespace": {
            "value": "value"
        }
    }
}
```

Variables can also target a namespace explicitly.

For example:

```json
{
    "variables": {
        "MyNamespace:my_bundle.Variable": {
            "value": "value"
        }
    }
}
```

The `comment` key is _optional_, if supplied, the comment will be associated with the variable definition as if you had applied the _comment_ attribute to a vars type promise.

For example, this JSON:

```json
{
    "variables": {
        "MyNamespace:my_bundle.Variable": {
            "value": "value",
            "comment": "An optional note about why this variable is important"
        }
    }
}
```

Is equivalent to this policy:

```cf3
body file control
{
      namespace => "MyNamespace";
}
bundle agent my_bundle
{
  vars:
      "Variable"
        string => "value",
        comment => "An optional note about why this variable is important";
}
```

The `tags` key is _optional_, if supplied, the tags will be associated with the variable definition as if you had applied the _meta_ attribute to a vars type promise.

For example, this JSON:

```json
{
    "variables": {
        "MyNamespace:my_bundle.Variable": {
            "value": "value",
            "tags": [ "inventory", "attribute_name=My Inventory" ]
        }
    }
}
```

Is equivalent to this policy:

```cf3
body file control
{
      namespace => "MyNamespace";
}
bundle agent my_bundle
{
  vars:
      "Variable"
        string => "value",
        meta => { "inventory", "attribute_name=My Inventory" };
}
```

**Notes:**
* ```vars``` and ```variables``` keys are allowed concurrently in the same file.
* If ```vars``` and ```variables``` keys in the same augments file define the same variable, the definition provided by the **```variables``` key wins**.

**History:**

* Added in 3.18.0

### vars ###

This key is supported in both `host_sepecific.json`, `def.json`, and `def_preferred.json` and augments loaded by the augments key.

Variables defined here can target a _namespace_ and or _bundle_ scope
explicitly. When defined from `def.json`, variables default to the `def`
_bundle_ in the `default` _namespace_ (`$(default:def.MyVariable)`).

Thus:

```json
{
    "vars": {
        "phone": "22-333-4444",
        "myplatform": "$(sys.os)",
        "MyBundle.MyVariable": "MyValue in MyBundle.MyVariable",
        "MyNamespace:MyBundle.MyVariable": "MyValue in MyNamespace:MyBundle.MyVariable"
    }
}
```

results in the variable `default:def.phone` with value `22-333-4444`,
`default:def.myplatform` with the value of your current OS,
`default:MyBundle.MyVariable` with the value `MyValue in MyBundle.MyVariable`
and `MyNamespace:MyBundle.MyVariable` with the value `MyValue` in
`MyNamespace:MyBundle.MyVariable`.

Again, note that this happens before policy is parsed or evaluated.

You can see the list of variables thus defined in the output of `cf-promises
--show-vars` (see [Components][]). They will be tagged with
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

**Notes:**
* ```vars``` and ```variables``` keys are allowed concurrently in the same file.
* If ```vars``` and ```variables``` keys in the same augments file define the same variable, the definition provided by the **```variables``` key wins**.

**History:**

* 3.18.0 gained ability to specify the _namespace_ and _bundle_ the variable should be defined in.

### classes ###

This key is supported in both `host_sepecific.json`, `def.json`, `def_preferred.json`, and augments loaded by the augments key.

Any class defined via augments will be evaluated and installed as
[**soft** classes][Classes and Decisions]. This key supports both
_array_ and _dict_ formats.

For an array each element of the array is tested against currently defined
classes as an [anchored regular expression][anchored] unless the string ends with ```::``` indicating it should be interpreted as a
[*class expression*][Classes and Decisions].

**For example:**

```json
{
    "classes": {
        "augments_class_from_regex_my_always": [ "any" ],
        "augments_class_from_regex_my_other_apache": [ "server[34]", "debian.*" ],
        "augments_class_from_regex_my_other_always": [ "augments_class_from_regex_my_always" ],
        "augments_class_from_regex_when_MISSING_not_defined": [ "^(?!MISSING).*" ],
        "augments_class_from_regex": [ "cfengine_\\d+" ],
        "augments_class_from_single_class_as_regex": [ "cfengine" ],
        "augments_class_from_single_class_as_expression": [ "cfengine::" ],
        "augments_class_from_classexpression_and": [ "cfengine.cfengine_3::" ],
        "augments_class_from_classexpression_not": [ "!MISSING::" ],
        "augments_class_from_classexpression_or": [ "cfengine|cfengine_3::" ],
        "augments_class_from_classexpression_complex": [ "(cfengine|cfengine_3).!MISSING::" ]
    }
}
```

The `tags`, `comment`, and the mutually exclusive `class_expressions`, and `regular_expressions` subkeys
are supported when using the _dict_ structure.

**For example:**

```json
{
    "classes": {
        "myclass_defined_by_augments_in_def_json_3_18_0_v0": {
            "class_expressions": [ "linux.redhat::", "cfengine|linux::" ],
            "comment": "Optional description about why this class is important",
            "tags": [ "optional", "tags" ]
        },
        "myclass_defined_by_augments_in_def_json_3_18_0_v1": {
            "regular_expressions": [ "linux.*", "cfengine.*" ],
            "tags": [ "optional", "tags" ]
        }
    }
}
```

Note that augments is processed at the very beginning of agent evaluation. You
can use any **hard** classes, [**persistent** classes][Classes and Decisions]
, or classes defined earlier in the augments list. Test carefully,
custom [**soft** classes][Classes and Decisions] may not be defined early enough
for use. Thus:

```json
{
    "classes": {
        "augments_class_from_regex_my_always": [ "any" ],
        "augments_class_from_regex_my_other_apache": [ "server[34]", "debian.*" ],
        "augments_class_from_regex_my_other_always": [ "augments_class_from_regex_my_always" ],
        "augments_class_from_regex_when_MISSING_not_defined": [ "^(?!MISSING).*" ],
        "augments_class_from_regex": [ "cfengine_\\d+" ],
        "augments_class_from_single_class_as_regex": [ "cfengine" ],
        "augments_class_from_single_class_as_expression": [ "cfengine::" ],
        "augments_class_from_classexpression_and": [ "cfengine.cfengine_3::" ],
        "augments_class_from_classexpression_not": [ "!MISSING::" ],
        "augments_class_from_classexpression_or": [ "cfengine|cfengine_3::" ],
        "augments_class_from_classexpression_complex": [ "(cfengine|cfengine_3).!MISSING::" ],
        "myclass_defined_by_augments_in_def_json_3_18_0_v0": {
            "class_expressions": [ "linux.redhat::", "cfengine|linux::" ],
            "comment": "Optional description about why this class is important",
            "tags": [ "optional", "tags" ]
        },
        "myclass_defined_by_augments_in_def_json_3_18_0_v1": {
            "regular_expressions": [ "linux.*", "cfengine.*" ],
            "tags": [ "optional", "tags" ]
        }
    }
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

* `myclass_defined_by_augments_in_def_json_3_18_0_v0` will be defined because
  the class expression `cfengine|linux::` will always be true since there is
  always a `cfengine` class defined.

* `myclass_defined_by_augments_in_def_json_3_18_0_v1` will be defined because the expression `cfengine.**` will match at least one defined class, `cfengine`

You can see the list of classes thus defined through `def.json` in the output
of `cf-promises --show-classes` (see [Components][]). They
will be tagged with the tags `source=augments_file`. For instance:

```console
% cf-promises --show-classes=my
Class name                                                   Meta tags                                Comment
augments_class_from_regex_my_always                          source=augments_file
augments_class_from_regex_my_other_always                    source=augments_file
augments_class_from_regex_my_other_apache                    source=augments_file
myclass_defined_by_augments_in_def_json_3_18_0_v0            optional,tags,source=augments_file       Optional description about why this class is important
myclass_defined_by_augments_in_def_json_3_18_0_v1            optional,tags,source=augments_file
```

**See also:**

* Functions that use regular expressions with classes: `classesmatching()`,
  `classmatch()`, `countclassesmatching()`

**History:**

* 3.18.0
  * Support for dict structure for classes and support for metadata (`comment`, `tags`) added.
  * Classes are defined as _soft_ classes instead of _hard_ classes.


### augments ###

This key is supported in `def.json`, `def_preferred.json`, and augments loaded by the [_augments_ key][Augments#augments].

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

## History

* 3.18.0
  * Introduced `variables` key with support for metadata (`comment`, `tags`) and targeting the _namespace_ and _bundle_.
  * Introduced ability for `vars` to target _namespace_ and _bundle_ `variables` key with support for metadata (`comment`, `tags`).
  * Introduced metadata (`comment`, `tags`) support for `classes` key.
  * Introduced `def_preferred.json` and  `--ignore-preferred-augments` to disable it.
  * Classes defined from augments are now _soft_ classes and not _hard_ classes.
  * Introduced parsing of `$(sys.workdir)/data/host_specific.json`
* 3.12.2, 3.14.0 introduced class expression interpretation (`::` suffix) to classes key
* 3.12.0 introduced the `augments` key
* 3.7.3 back port `def.json` parsing in core agent and load `def.json` if present next to policy entry
* 3.8.2 removed core support for `inputs` key, load `def.json` if present next to policy entry
* 3.8.1 `def.json` parsing moved from policy to core agent for resolution of classes and variables to be able to affect control bodies
* 3.7.0 introduced augments concept into the Masterfiles Policy Framework
