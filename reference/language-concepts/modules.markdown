---
layout: default
title: Modules
published: true
tags: [language, concepts, syntax, modules]
---

Modules allow users to extend the capabilities of CFEngine in a modular way, they can be easily added and upgraded independently of when you upgrade your CFEngine version. Several different types of modules are available.

{% comment %}
## cfbs Modules

cfbs (CFEngine Build System) Modules provide a way to share and consume CFEngine related assets. Policy, Modules and Data can all be distributed as cfbs modules.

### Specification
{% endcomment %}

## Promise Modules

Promise modules allow for the implementation of [*custom* promise types][promise-type-custom], extending the CFEngine Language. They communicate with `cf-agent` using the [*Promise Module Protocol*][promise-type-custom-protocol].

**History:**

* Introduced 3.17.0

## Package Modules

[Package Modules][Package Modules] implement the logic behind *packages* type promises, superseding the *package\_method* based implementation. They interact with package managers like `yum`, `apt`, `msiexec`, and `pip` to determine which packages are currently installed or have updates available as well as installing, upgrading or un-installing packages.

Package modules communicate with `cf-agent` via the [Package Module Protocol][package-modules-the-api].

**History:**

* Introduced 3.7.0

## Variables and Classes Modules

Variables and Classes Modules are the original way to extend CFEngine. The Variable and Class Module Protocol allows for *variables* and *classes* to be defined. The protocol can be interpreted by functions like [`usemodule()`][usemodule] and [`read_module_protocol()`](read_module_protocol) as well as output from [*commands* type promises][commands] with the [`module => "true"`][commands#module] attribute.

The choice of interpretation can depend on many factors but a primary differentiate between functions and classes relate to CFEngine's evaluation details. Functions are evaluated during early during policy execution unless they are explicitly guarded to delay execution. Commands promises are not executed until the bundle is actuated for it's three pass evaluation.

Variables and Classes Modules are intended for use as system probes rather than additional configuration promises, especially now that promise modules are available.

### Specification

The protocol is *line based*. Lines that begin with `^` apply to all following lines.

*   **`^context=BundleName`:** Sets the bundle scope in which *variables* will be defined
*   **`^meta=Tag1,Tag2`:** Sets a comma separated list of tags that are applied to defined *variables* and *classes*
*   **`^persistence=X`:** Sets the number of minutes for which *classes* should persist
*   **`+ClassName`:** Defines a namespace scoped class
*   **`-ClassName`:** Undefines a class
*   **`=VariableName=`:** Defines a string variable
*   **`VariableName[KEY]=`:** Defines an associative array key value
*   **`@VariableName=`:** Defines a list of strings
*   **`%VariableName=`:** Must be valid JSON and defines a data container

**Notes:**

*   It is not possible to define variables or classes in a namespace other than the default (`default`).
*   If no context is provided, the context is the canonified leaf name of the module. For example, if the module is `/tmp/path/my-module.sh` the default context would be `my_module_sh` in the `default` namespace (`default:my_module_sh`).
*   All *variables* and *classes* will be tagged with `source=module` in addition to any specified tags.
*   All lines of output that do not match the module protocol are treated as *errors*.
*   Variable names defined by the module protocol are limited to alphanumeric characters and `_`, `.`, `-`, `[`, `]`, `@`, and `/`.

**Examples:**

A Variables and Classes module written in shell:

```sh
#!/bin/sh
/bin/echo "@mylist= { \"one\", \"two\", \"three\" }"
/bin/echo "=myscalar= scalar val"
/bin/echo "=myarray[key]= array key val"
/bin/echo "%mydata=[1,2,3]"
/bin/echo "+module_class"
/bin/echo "^persistence=10"
/bin/echo "+persistent_10_minute_class"
```

**History:**

-   Introduced in 3.0.0
-   `^context`, `^meta` Added in 3.6.0
-   `^persistence` Added in 3.8.0
-   `@` allowed in variables (intended for keys in classic array) 3.15.0, 3.12.3, 3.10.7 (2019)
-   `/` allowed in variables (intended for keys in classic array) 3.14.0, 3.12.2, 3.10.6 (2019)

