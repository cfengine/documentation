---
layout: default
title: vars
published: true
tags: [reference, bundle common, vars, promises]
---

[Variables][variables] in CFEngine are defined
as promises that an identifier of a certain type represents a particular
value. Variables can be scalars or lists of types `string`, `int`, `real`
or `data`.

The allowed characters in variable names are alphanumeric (both upper and lower case)
and undercore. `Associative` arrays using the string type and square brackets `[]` to
enclose an arbitrary key are being deprecated in favor of the `data` variable type.

## Scalar Variables

### string

**Description:** A scalar string

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**


```cf3
    vars:

     "xxx"    string => "Some literal string...";
     "yyy"    string => readfile( "/home/mark/tmp/testfile" , "33" );
```

### int

**Description:** A scalar integer

**Type:** `int`

**Allowed input range:** `-99999999999,99999999999`

**Example:**

```cf3
    vars:

     "scalar" int    => "16k";
     "ran"    int    => randomint(4,88);
     "dim_array" int =>  readstringarray(
         "array_name",
         "/etc/passwd",
         "#[^\n]*",
         ":",
         10,
         4000);
```

**Notes:**

Int variables are strings that are expected to be used as integer numbers. The
typing in CFEngine is dynamic, so the variable types are interchangeable.
However, when you declare a variable to be type `int`, CFEngine verifies that
the value you assign to it looks like an integer (e.g., 3, -17, 16K).

### real

**Description:** A scalar real number

**Type:** `real`

**Allowed input range:** `-9.99999E100,9.99999E100`

**Example:**

```cf3
    vars:

     "scalar" real   => "0.5";
```

**Notes:**

Real variables are strings that are expected to be used as real numbers. The
typing in CFEngine is dynamic, so the variable types are interchangeable, but
when you declare a variable to be type `real`, CFEngine verifies that the
value you assign to it looks like a real number (e.g., 3, 3.1415, .17,
6.02e23, -9.21e-17).

Real numbers are not used in many places in CFEngine, but they are useful for
representing probabilities and performance data.

## List variables

Lists are specified using curly brackets `{}` that enclose a comma-separated
list of values. The order of the list is preserved by CFEngine.

### slist

**Description:** A list of scalar strings

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
    vars:

     "xxx"    slist  => {  "literal1",  "literal2" };
     "xxx1"   slist  => {  "1", @(xxx) }; # interpolated in order
     "yyy"    slist  => {
                        readstringlist(
                                      "/home/mark/tmp/testlist",
                                      "#[a-zA-Z0-9 ]*",
                                      "[^a-zA-Z0-9]",
                                      15,
                                      4000
                                      )
                        };

     "zzz"    slist  => { readstringlist(
        "/home/mark/tmp/testlist2",
        "#[^\n]*",
        ",",
        5,
        4000)
        };
```

**Notes:**

Some [functions][Functions] return `slist`s, and an `slist`
may contain the values copied from another `slist`, `rlist`, or `ilist`. See
[`policy`](#policy).

### ilist

**Description:** A list of integers

**Type:** `ilist`

**Allowed input range:** `-99999999999,9999999999`

**Example:**

```cf3
    vars:

      "variable_id"

           ilist => { "10", "11", "12" };

      "xxx1" ilist  => {  "1", @(variable_id) }; # interpolated in order
```

**Notes:**

Integer lists are lists of strings that are expected to be treated as
integers. The typing in CFEngine is dynamic, so the variable types are
interchangeable, but when you declare a variable to be type `ilist`,
CFEngine verifies that each value you assign to it looks like an integer
(e.g., 3, -17, 16K).

Some [functions][Functions] return `ilist`s, and an `ilist` may
contain the values copied from another `slist`, `rlist`, or `ilist`. See
[`policy`](#policy)

### rlist

**Description:** A list of real numbers

**Type:** `rlist`

**Allowed input range:** `-9.99999E100,9.99999E100`

**Example:**

```cf3
    vars:

      "varid" rlist => { "0.1", "0.2", "0.3" };

      "xxx1" rlist  => {  "1.3", @(varid) }; # interpolated in order
```

**Notes:**

Real lists are lists of strings that are expected to be used as real
numbers. The typing in CFEngine is dynamic, so the variable types are
interchangeable, but when you declare a variable to be type `rlist`,
CFEngine verifies that each value you assign to it looks like a real
number (e.g., 3, 3.1415, .17, 6.02e23, -9.21e-17).

Some [functions][Functions] return `rlist`s, and an `rlist` may
contain the values copied from another `slist`, `rlist`, or `ilist`. See [`policy`](#policy)

## Data container variables

The `data` variables are obtained from functions that return data
containers, such as `readjson()`, `readyaml()`, `parsejson()`, or
`parseyaml()`, the various `data_*` functions, or from merging
existing data containers with `mergedata()`. They can *NOT* be
modified, once created.

### Inline YAML and JSON data

Data containers can be specified inline, without calling functions.

Inline YAML data has to begin with the `---` preamble followed by a newline. This preamble
is normally optional but here (for inline YAML) it's required by
CFEngine. To generate that in CFEngine, use `$(const.n)` or a literal
newline as shown in the example.

Inline JSON or YAML data may contain CFEngine variable references.
They will be expanded at runtime as if they were simply calls to
`readjson()` or `readyaml()`, which also means that syntax error in
the JSON or YAML data will only be caught when your policy is actually
being evaluated.

If the inline JSON or YAML data does **not** contain CFEngine variable
references, it will be parsed at compile time, which means that
`cf-promises` will be able to find syntax errors in your JSON or YAML
data early. Thus it is highly recommended that you try to avoid
variable references in your inline JSON or YAML data.

For example:
#### Inline Yaml example

[%CFEngine_include_example(inline-yaml.cf)%]

#### Inline Json example

[%CFEngine_include_example(inline-json.cf)%]

### Passing data containers to bundles

Data containers can be passed to another bundle with the
`@(varname)` notation, similarly to the list passing notation.

### Some useful tips for using data containers

* to extract just `container[x]`, use `mergedata("container[x]")`
* to wrap a container in an array, use `mergedata("[ container ]")`
* to wrap a container in a map, use `mergedata('{ "mykey": container }')`
* they act like "classic" CFEngine arrays in many ways
* `getindices()` and `getvalues()` work on any level, e.g. `getvalues("container[x][y]")`
* in reports, you have to reference a part of the container that can be expressed as a string.  So for instance if you have the container `c` with data `{ "x": { "y": 50 }, "z": [ 1,2,3] }` we have two top-level keys, `x` and `z`.  If you report on `$(c[x])` you will not get data, since there is no string there.  But if you ask for `$(c[x][y])` you'll get `50`, and if you ask for `$(c[z])` you'll get implicit iteration on `1,2,3` (just like a slist in a "classic" CFEngine array).
* read the examples below carefully to see some useful ways to access data container contents

Iterating through a data container is only guaranteed to respect list
order (e.g. `[1,3,20]` will be iterated in that order). Key order for
maps, as per the JSON standard, is not guaranteed. Similarly, calling
`getindices()` on a data container will give the list order of indices
0, 1, 2, ... but will not give the keys of a map in any particular
order.  Here's an example of iterating in list order:

[%CFEngine_include_snippet(container_iteration.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(container_iteration.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

Often you need to iterate through the keys of a container, and the
value is a key-value property map for that key. The example here shows
how you can pass the "animals" container and an "animal" key inside it
to a bundle, which can then report and use the data from the key-value
property map.

[%CFEngine_include_snippet(container_key_iteration.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(container_key_iteration.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

### data

**Description:** A data container structure

**Type:** `data`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
    vars:

     "loaded1" data => readjson("/tmp/myfile.json", 40000);
     "loaded2" data => parsejson('{"key":"value"}');
     "loaded3" data => readyaml("/tmp/myfile.yaml", 40000);
     "loaded4" data => parseyaml('- key2: value2');
     "merged1" data => mergedata(loaded1, loaded2, loaded3, loaded4);

     # JSON or YAML can be inlined since CFEngine 3.7
     "inline1" data => '{"key":"value"}'; # JSON
     "inline2" data => '---$(const.n)- key2: value2'; # YAML requires "---$(const.n)" header

```

***

## Attributes ##

### policy

**Description:** The policy for (dis)allowing (re)definition of variables

Variables can either be allowed to change their value dynamically (be
redefined) or they can be constant.

**Type:** (menu option)

**Allowed input range:**

```
    free
    overridable
    constant
    ifdefined
```

**Default value:**

`policy = free`

**Example:**

```cf3
    vars:

      "varid" string => "value...",
              policy => "free";
```

**Notes:**

The policy `free` and `overridable` are synonyms.  The policy `constant` is
deprecated, and has no effect. All variables are `free` or `overridable` by
default which means the variables values may be changed.

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

For example:

```cf3
example_com::
  "domain"
     string => "example.com",
    comment => "Define a global domain for hosts in the example.com domain";

# The promise above will be overridden by one of the ones below on hosts
# within the matching subdomain

one_example_com::
  "domain"
     string => "one.example.com",
    comment => "Define a global domain for hosts in the one.example.com domain";

two_example_com::
  "domain"
     string => "two.example.com",
    comment => "Define a global domain for hosts in the two.example.com domain";
```

(Promises within the same bundle are evaluated top to bottom, so vars promises further down in a bundle can overwrite previous values of a variable. See [**normal ordering**][Normal Ordering] for more information).

## Defining variables in foreign bundles

As a general rule, variables can only be defined or re-defined from within the
bundle where they were defined. There are a few notable exceptions to this
general rule which are described below.

### Meta type promises

Variables defined by the *meta* promise type are defined in a bundle scope with the same name as the executing bundle suffixed with ```meta```.

**Example policy:**

```cf3
    bundle agent example_meta_vars
    {
      meta:
        "tags" slist => { "autorun" };
    
      vars:
        "myvar" string => "my value";
    
      reports:
        "$(with)" with => string_mustache( "{{%-top-}}", variablesmatching_as_data( ".*example_meta_vars.*" ) );
    
    }
    bundle agent __main__
    {
       methods: "example_meta_vars";
    }
```

**Example output:**

```
    R: {
      "default:example_meta_vars.myvar": "my value",
      "default:example_meta_vars_meta.tags": [
        "autorun"
      ]
    }
```

### Injecting variables into undefined bundles

Variables can be directly set in foreign bundles if the bundle is not defined.

**Example policy:**

```cf3
    bundle agent example_variable_injection
    {
      vars:
        "undefined.myvar" string => "my value";
        "cant_push_this.myvar" string => "my value";
    
      reports:
        "$(with)" with => string_mustache( "{{%-top-}}", variablesmatching_as_data( ".*myvar.*" ) );
    
    }
    bundle agent cant_push_this
    {
          # If a bundle is defined, you can't simply define a variable in it from
          # another bundle, unless the variable is defined via the module protocol.
    }
    bundle agent __main__
    {
       methods: "example_variable_injection";
    }
```

**Example output:**

```
       error: Ignoring remotely-injected variable 'myvar'
       error: Remote bundle variable injection detected!
       error: Variable identifier 'cant_push_this.myvar' is not legal
       error: Promise belongs to bundle 'example_variable_injection' in file '/tmp/example_variable_injection.cf' near line 6
       error: Ignoring remotely-injected variable 'myvar'
       error: Remote bundle variable injection detected!
       error: Variable identifier 'cant_push_this.myvar' is not legal
       error: Promise belongs to bundle 'example_variable_injection' in file '/tmp/example_variable_injection.cf' near line 6
       error: Remote bundle variable injection detected!
       error: Variable identifier 'cant_push_this.myvar' is not legal
       error: Promise belongs to bundle 'example_variable_injection' in file '/tmp/example_variable_injection.cf' near line 6
       error: Remote bundle variable injection detected!
       error: Variable identifier 'cant_push_this.myvar' is not legal
       error: Promise belongs to bundle 'example_variable_injection' in file '/tmp/example_variable_injection.cf' near line 6
       error: Remote bundle variable injection detected!
       error: Variable identifier 'cant_push_this.myvar' is not legal
       error: Promise belongs to bundle 'example_variable_injection' in file '/tmp/example_variable_injection.cf' near line 6
       error: Remote bundle variable injection detected!
       error: Variable identifier 'cant_push_this.myvar' is not legal
       error: Promise belongs to bundle 'example_variable_injection' in file '/tmp/example_variable_injection.cf' near line 6
    R: {
      "default:undefined.myvar": "my value"
    }
       error: Remote bundle variable injection detected!
       error: Variable identifier 'cant_push_this.myvar' is not legal
       error: Promise belongs to bundle 'example_variable_injection' in file '/tmp/example_variable_injection.cf' near line 6
       error: Remote bundle variable injection detected!
       error: Variable identifier 'cant_push_this.myvar' is not legal
       error: Promise belongs to bundle 'example_variable_injection' in file '/tmp/example_variable_injection.cf' near line 6
       error: Remote bundle variable injection detected!
       error: Variable identifier 'cant_push_this.myvar' is not legal
       error: Promise belongs to bundle 'example_variable_injection' in file '/tmp/example_variable_injection.cf' near line 6
       error: Remote bundle variable injection detected!
       error: Variable identifier 'cant_push_this.myvar' is not legal
       error: Promise belongs to bundle 'example_variable_injection' in file '/tmp/example_variable_injection.cf' near line 6
```

### Module protocol

The module protocol allows specification of *context* (the bundle scope within which a variable gets defined).

**Example policy:**

```cf3
    bundle agent example_variable_injection_via_module
    {
      commands:
        "/bin/echo '^context=undefined$(const.n)=myvar=my value" module => "true";
        "/bin/echo '^context=cant_push_this$(const.n)=myvar=my value" module => "true";
    
      reports:
        "$(with)" with => string_mustache( "{{%-top-}}", variablesmatching_as_data( ".*myvar.*" ) );
    
    }
    bundle agent cant_push_this
    {
        # If a bundle is defined, you can't simply define a variable in it from
        # another bundle, unless the variable is defined via the module protocol.
    }
    bundle agent __main__
    {
       methods: "example_variable_injection_via_module";
    }
```

**Example output:**

```
    R: {
      "default:cant_push_this.myvar": "my value",
      "default:undefined.myvar": "my value"
    }
```

### Augments

Augments defines variables in the *def* bundle scope.

This augments file that defines `my_var` will be used for all examples shown here (`/tmp/def.json`).

```json
{
  "vars": {
    "my_var": "My value defined from augments"
    }
}
```

This example policy illustrates how augments defines variables in the def bundle scope (`/tmp/example.cf`).

```cf3
bundle common def
{
  vars:
    "some_var"
      string => "My value for $(this.promiser) defined in Policy";
}
bundle agent __main__
{
  reports:
    "$(with)"
      with => string_mustache( "{{%-top-}}", variablesmatching_as_data( "default:def.*") );
}
```

This command shows the execution and output from the policy above.

```console
cf-agent -Kf /tmp/example.cf
```

```
R: {
  "default:def.jq": "jq --compact-output --monochrome-output --ascii-output --unbuffered --sort-keys",
  "default:def.my_var": "My value defined from augments",
  "default:def.some_var": "My value for some_var defined in Policy"
}
```

Note, augments defines the variables at the start of agent initialization. The variables can be re-defined by policy during evaluation.

This example policy illustrates how policy will, by default, re-define variables set via augments (`/tmp/example2.cf`).

```cf3
bundle common def
{
  vars:
    "some_var"
      string => "My value for $(this.promiser) defined in Policy";
    "my_var"
      string => "My value for $(this.promiser) defined in Policy";
}
bundle agent __main__
{
  reports:
    "$(with)"
      with => string_mustache( "{{%-top-}}", variablesmatching_as_data( "default:def.*") );
}
```

This command shows the execution and output from the policy above.

```console
cf-agent -Kf /tmp/example2.cf
```

```
R: {
  "default:def.jq": "jq --compact-output --monochrome-output --ascii-output --unbuffered --sort-keys",
  "default:def.my_var": "My value for my_var defined in Policy",
  "default:def.some_var": "My value for some_var defined in Policy"
}
```

Thus augments can be used to override defaults if the policy is instrumented to support it.

This example policy illustrates how policy can be instrumented to avoid re-definition of variables set via augments (`/tmp/example3.cf`).

```cf3
bundle common def
{
  vars:
    "some_var"
      string => "My value for $(this.promiser) defined in Policy";

    # Here we set my_var if it has not yet been defined (as in the case where
    # augments would define it before the policy was evaluated).

    "my_var"
      string => "My value for $(this.promiser) defined in Policy",
      unless => isvariable( $(this.promiser) );

}
bundle agent __main__
{
  reports:
    "$(with)"
      with => string_mustache( "{{%-top-}}", variablesmatching_as_data( "default:def.*") );
}
```

This command shows the execution and output from the policy above.

```console
cf-agent -Kf /tmp/example3.cf
```

```
R: {
  "default:def.jq": "jq --compact-output --monochrome-output --ascii-output --unbuffered --sort-keys",
  "default:def.my_var": "My value defined from augments",
  "default:def.some_var": "My value for some_var defined in Policy"
}
```

