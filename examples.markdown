---
layout: default
title: CFEngine Examples 
categories: [Examples]
published: true
alias: examples.html
tags: [Examples]
---

You can find more examples for CFEngine Code in the
[GitHub repository](https://github.com/cfengine/design-center/tree/master/examples).

## Running the Example policies

The policy files can be found in `/var/cfengine/share/doc/examples`. You can 
test them locally by copying the respective _example___file.cf_ file into
`/var/cfengine/inputs` and running:

	/var/cfengine/bin/cf-agent -f example_file.cf

## Integrating the Example into your Main Policy

The following steps makes the example policy part of your main policy. Some examples require
addition steps - see the respective documentation page for details.

1. Copy the file from `/var/cfengine/share/doc/examples` to
    `/var/cfengine/masterfiles`.

2. Delete the `body common control` section in
    `/var/cfengine/masterfiles/example_file.cf`:

``` cf3
    body common control
	{
	    bundlesequence  => { "testbundle" };
	}
```

3. Insert the example's bundle name in the `bundlesequence` section
    of the main policy file `/var/cfengine/masterfiles/promises.cf` on
    the policy server:

```cf3
    bundlesequence => {
        ...
        "testbundle",
        ...
    };
```

4. Insert the policy file name in the `inputs` section of the main policy file
    `/var/cfengine/masterfiles/promises.cf` on the policy server:

```cf3
     inputs => {
         ...
         "example_file.cf",
         ...
    };
```

The example policy will now be executed every five minutes along with the rest
of your main policy.
