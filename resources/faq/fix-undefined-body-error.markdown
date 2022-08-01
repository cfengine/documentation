---
layout: default
title: How do I fix undefined body errors?
published: true
sorting: 90
tags: [getting started, installation, faq]
---

When running policy you see `error: Undefined body`. For example:

`cf-promises -f ./large-files.cf`:
```
./large-files.cf:14:0: error: Undefined body tidy with type delete
./large-files.cf:16:0: error: Undefined body recurse with type depth_search
```

The above errors indicate that the `tidy` and `recurse` bodies are not found in
inputs. Bodies and bundles must either be defined within the same policy file or
included from [body common control inputs][Components#inputs]
or [body file control inputs][file control#inputs].

# Example: Add stdlib via body common control

```cf3
body common control
{
        bundlesequence => { "file_remover" };
        inputs => { "$(sys.libdir)/stdlib.cf" };
}
```

# Example: Add stdlib via body file control

Body file control allows you to build modular policy. Body file control inputs
are typically relative to the policy file itself.

```cf3
bundle file_remover_control
{
  vars:
    "inputs" slist => {
                        "$(sys.libdir)/stdlib.cf",
                        "$(this.promise_dirname)/custom_policy.cf",
                      };
}
body file control
{
  inputs => { @(file_remover_control.inputs) };
}
```

# Tip: Locate bodies or bundles with cf-locate

`cf-locate` is a small utility that makes searching for and referencing body or
bundle definitions quick and easy. Simply download the utility from
[core/contrib/cf-locate](https://github.com/cfengine/core/tree/master/contrib/cf-locate)
into your `$PATH` and make it executable.

Find which policy file a bundle or body is defined in:

```console
[root@hub ~]# cf-locate always

-> body or bundle matching 'always' found in /var/cfengine/masterfiles/lib/3.6/common.cf:260
body classes always(x)
```

Reference a bundle or bodies full implementation:

```console
[root@hub ~]# cf-locate -f always /var/cfengine/masterfiles

-> body or bundle matching 'always' found in /var/cfengine/masterfiles/lib/3.6/common.cf:260
body classes always(x)
# Define a class no matter what the outcome of the promise is

{
      promise_repaired => { "$(x)" };
      promise_kept => { "$(x)" };
      repair_failed => { "$(x)" };
      repair_denied => { "$(x)" };
      repair_timeout => { "$(x)" };
}
```
