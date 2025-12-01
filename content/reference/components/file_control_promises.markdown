---
layout: default
title: file control
sorting: 100
aliases:
  - "/reference-components-file_control_promises.html"
---

```cf3
body file control
{
namespace => "name1";
}

bundle agent private
{
  #...
}
```

**History:** Was introduced in 3.4.0, Enterprise 3.0.0 (2012)

This directive can be given multiple times within any file,
outside of body and bundle definitions.

Only [soft classes][Classes and decisions] from common bundles can
be used in class decisions inside `file control bodies`.

### evaluation_order

**Description:** `evaluation_order` in body file control sets the evaluation order for the subsequent bundles in the file.

This setting allows you to change the order in which components execute policy within a given policy file.
By default, CFEngine uses a `classic` evaluation order, where promises are executed in a predefined order based on their type (e.g., `vars` before `files`, `files` before `packages`, etc.).
This is the historical behavior of CFEngine.

By setting `evaluation_order` to `top_down`, you can force components to evaluate promises in the order they are written in the policy file, from top to bottom.
This can make policy evaluation more familiar and possibly easier to write and understand, especially for new users, as the execution flow follows the visual layout of the code.

This attribute can also be set in `body common control` to affect all components and or `body agent control` to affect all files.
If set in multiple places, the value in `body agent control` takes precedence for `cf-agent`.

**Type:** `string`

**Allowed input range:** `(classic|top_down)`

**Default value:** `classic`

**Example:**

```cf3
body file control
{
  evaluation_order => "top_down";
}

bundle agent reports_top_down
{
  reports: "Hello world:";

  commands: "/bin/echo hi";

  reports: "bye:";
}
bundle agent __main__
{
      methods: "reports_top_down";
}

body agent control
{
  evaluation_order => "top_down";
}
```

Executed would result in:

```output
R: Hello world:
  notice: Q: ".../bin/echo hi": hi
R: bye:
```

**See also:** [`evaluation_order` in `body agent control`](/reference/components/cf-agent/#evaluation_order),
[`evaluation_order` in `body common control`][Components#evaluation_order]

**History:** Introduced in CFEngine 3.27.0

### inputs

**Description:** The `inputs` slist contains additional filenames to parse for promises.

The filenames specified are all assumed to be relative to the directory
of the file which references them. Use an absolute file name if you need an absolute path.
Use `sys.libdir` (absolute library path), `sys.local_libdir` (library path relative to the
current masterfiles), and `this.promise_dirname` (the directory of the currently processed
file) to avoid hard-coding paths.

Note that in `this.` variables are not available in `body file control` or `body common control`
but this can be worked around with a `bundle common` vars promise as follows:

```cf3
# one.cf
bundle common one
{
  vars:
    "inputs" slist => { "$(this.promise_dirname)/two.cf" };
}

body file control
{
  inputs => { "@(one.inputs)" };
}

bundle agent main
{
  methods:
    "two";
}
```

```cf3
# two.cf
bundle agent two
{
  reports:
    "hello, from $(this.promise_filename)";
}
```

```sh
$ cf-agent -KIf ./one.cf
R: hello, from /home/agent/./two.cf
```

**See also:** [`inputs`][Components#inputs] in
[`body common control`][Components]

**History:** Was introduced in CFEngine 3.6.0

### namespace

**Description:** The namespace string identifies a private namespace
to switch to in order to protect the current file from duplicate definitions.

**Type:** `string`

**Allowed input range:** `[a-zA-Z0-9_$(){}\[\].:]+`

**Example:**

```cf3
body file control
{
namespace => "name1";
}
```

**Notes:**

**History:** Was introduced in 3.4.0, Enterprise 3.0.0 (2012)

This directive can be given within any file, outside of body and bundle
definitions, to change the [namespace][namespaces] of subsequent bundles
and bodies. A namespace applies until the next namespace declaration in a
file, or until the end of a file. This is similar to how class expressions
apply until the next class expression or end of bundle.

**See also:** `namespaces`
