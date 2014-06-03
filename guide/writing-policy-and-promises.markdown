---
layout: default
title: Writing Policy and Promises
published: true
sorting: 6
---

## How Promises Work ##

Everything in CFEngine can be thought of as a promise to be kept by different resources in the system. In a system that delivers a web site using Apache, an important promise may be to make sure that the `httpd` package is installed, running, and accessible on port 80. 

### Summary for Writing, Deploying and Using Promises ###

Writing, deploying, and using CFEngine `promises` will generally follow these simple steps:

1. Using a text editor, create a new file (e.g. `hello_world.cf`).
2. Create a bundle and promise in the file (see [Test the Workflow With a "Hello World" Promise][Writing Policy and Promises#Test the Workflow With a "Hello World" Promise]).
3. Save the file on the policy server somewhere under `/var/cfengine/masterfiles` (can be under a sub-directory).
4. Let CFEngine know about the `promise` on the `policy server`, generally in the file `/var/cfengine/masterfiles/promises.cf`, or a file elsewhere but referred to in `promises.cf`.
		* Optional: it is also possible to call a bundle manually, using `cf-agent`.
5. Verify the `policy file` was deployed and successfully run.

#### Example: "Hello World" Promise ####

In the simple `hello_world` example shown below, the `promise` is that the `Hello World` message will be sent to the log. 

1. Create a bundle.

```cf3
bundle agent hello_world
{

}
```

2. Insert the promise type `reports`.

```cf3
bundle agent hello_world
{
  reports:

}
```

3. Add a class expression (optional). The class expression defaults to `any`, but in this example it is explicitly declared.

```cf3
bundle agent hello_world
{
  reports:

    any::

}
```

4. Give attributes required values. In this case only our simple `Hello World!` message string.

```cf3
bundle agent hello_world
{
  reports:

    any::

      "Hello World!";

}
```

### Promises in Action ###

#### Manually Executing a Promise ####

1. Assuming the promise file is located at `/var/cfengine/masterfiles/hello_world.cf`, on the command line type the following: 

```# /var/cfengine/bin/cf-agent --no-lock --file /var/cfengine/masterfiles/hello_world.cf --bundlesequence hello_world```

2. The output will include something similar to the following: `notice: R: Hello World!`.


#### Registering a Promise in `promises.cf` ####

Registering the promise with CFEngine consists of some simple steps:

1. On the policy server, open the file `/var/cfengine/masterfiles/promises.cf` in a text editor.
2.  At the end of the `bundlesequence` section add the following line: `"hello_world",`.
3.  At the end of the `inputs` section add the following line: `"hello_world.cf",`.
4. `/var/cfengine/masterfiles/promises.cf` should then look like something like this (where `...` represents existing text in the file, omitted for clarity):

```cf3
body common control

{

      bundlesequence => {
						...
                        vcs_update,
						hello_world,

      };

      inputs => {
                 ...
				 
                  "vcs_update.cf",
				  "hello_world.cf",
      };
```

With the above information CFEngine will then do the following:

1. The policy server copies the `hello_world promise` defined in `promises.cf` to its own `/var/cfengine/inputs` directory.
2. Hosts pull their own copy of the same `hello_world promise` into its own `/var/cfengine/inputs` directory.
3. The `promise` is executed.
4. In the `hello_world` example an adminstrator, defined in the file `controls/cf_execd.cf`, will be emailed the message `Hello World!`. 

## See Also ##
* [Authoring Policy Tools & Workflow][Authoring Policy Tools & Workflow]
* [Promises][Promises]