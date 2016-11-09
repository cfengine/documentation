---
layout: default
title: Manual Execution
published: true
sorting: 90
tags: [getting started, installation, faq]
---


# How do I run a standalone policy file?

The `--file` or `-f` option to `cf-agent` specifys the policy file. The `-K` or
`--no-lock` flag and the `-I` or `--inform` options are commonly used in
combination with the `-f` option to ensure that all promises are skipped because
of locking and for the agent to produce informational output like successful
repairs.

```console
[root@hub ~]# cf-agent -KIf ./my_standalone_policy.cf
```

A standalone policy file **may** choose not to specify a `bundlesequence`. In
that case, the `bundlesequence` defaults to `main` so you'll need a bundle
called `main`, or will need to specify the bundlesequence.

# How do I run a specific bundle?

A specific bundle can be activated by passing the `-b` or `--bundlesequence`
options to `cf-agent`. This may be used to activate a specific bundle within a
large policy set or to run a standalone policy that does not include a `body
common control`.

```console
[root@hub ~]# cf-agent -b my_bundle
```

If you want to activate multiple bundles in a sequence simply separate them
with commas (no spaces between).

```console
[root@hub ~]# cf-agent --bundlesequence bundle1,bundle2
```

# How do I define a class for a single run?

You can use the `--define` or `-D` options of `cf-agent`.

```console
[root@hub ~]# cf-agent -D my_class
```

And if you want to define multiple, simply separate them with commas (no spaces
between).

```console
[root@hub ~]# cf-agent --define my_class,my_other_class
```

# Run via cf-execd

Sometimes it's convenient to run `cf-execd` with `--once`. It will execute
`exec_command` as defined in `body executor control`. In the
[Masterfiles Policy Framework][Masterfiles Policy Framework] this
[defaults](https://github.com/cfengine/masterfiles/blob/{{site.cfengine.branch}}/controls/cf_execd.cf)
to update policy ( `update.cf` ) followed by the default policy ( `promises.cf`
). Output from cf-execd executions is logged to
[$(sys.workdir)/outputs][sys#sys.workdir].
