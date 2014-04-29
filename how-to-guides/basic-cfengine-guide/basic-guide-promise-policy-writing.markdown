---
layout: default
title: How to Write and Use Promises and Policy
published: true
sorting: 1
---

## How Promises Work ##

Everything in CFEngine can be thought of as a promise to be kept by different resources in the system. In a system that delivers a web site with Apache httpd, an important promise may be to make sure that `httpd` is installed, running, and accessible on port 80. 

In the simple `hello_world` example shown above, the `promise` is that the `Hello World` message will be sent to the log, which will then trigger other events that will be described below. 

### Summary for Writing, Deploying and Using Promises ###

Writing, deploying, and using CFEngine `promises` will generally follow these simple steps:

1. Using a text editor, create a new file (e.g. `hello_world.cf`).
2. Create a `bundle` and `promise` in the file (see Defining the Promise).
3. Save the file on `policy server` somewhere under `/var/cfengine/masterfiles` (can be under a sub-directory).
4a. Let CFEngine know about the `promise` on the `policy server`, generally in the file `/var/cfengine/masterfiles/promises.cf`, or a file elsewhere but referred to in `promises.cf`.
4b. Alternatively, it is also possible to call promises manually, using `cf-agent`.
5. Verify the `promise` was deployed and successfully run.

## Setting Up a Workflow and Toolchain for Authoring Promises

There are several ways to approach authoring promises and ensuring they are copied into and then deployed properly from the `masterfiles` directory:

1. Create or modify files directly in the `masterfiles` directory.
2. Copy new or modified files into the `masterfiles` directory (e.g. local file copy using `cp`, `scp` over `ssh`).
3. Utilize a version control system (e.g. Git) to push/pull changes or add new files to the `masterfiles` directory.

### Authoring on a Workstation and Pushing to the Hub Using Git + GitHub

#### General Summary ####

1. The "masterfiles" directory contains the promises and other related files (this is true in all situations).
2. Replace the out of the box setup with an initialized `git` repository and remote to a clone hosted on GitHub.
3. Add a promise to `masterfiles` that tells CFEngine to check that `git` repository for changes, and if there are any to merge them into `masterfiles`.
4. When an author wants to create a new promise, or modify an existing one, they clone the same repository on GitHub so that they have a local copy on their own computer.
5. The author will make their edits or additions in their local version of the `masterfiles` repository.
6. After the author is done making their changes commit them using `git commit`.
6. After the changes are commited they are then pushed back to the remote repository on GitHub.
7. As described in step3, CFEngine will pull any new changes that were pushed to GitHub (sometime within a five minute time interval).
8. Those changes will first exist in `masterfiles`, and then afterwards will be deployed to CFEngine hosts that are bootstrapped to the hub.

#### Create a Repository on GitHub for Masterfiles ####

#### Initialize Git Repository in Masterfiles on the Hub ####

#### Create a Remote in Masterfiles on the Hub to Masterfiles on GitHub ####

#### Add a Promise that Pulls Changes to Masterfiles on the Hub from Masterfiles on GitHub ####

#### Test the Workflow With a `Hello World` Promise ####

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

      "Hello World!"

}
```

### Promises in Action ###

#### Manually Executing a Promise ####

1. Assuming the promise file is located at `/var/cfengine/masterfiles/hello_world.cf`, on the command line type the following: 

```# /var/cfengine/bin/cf-agent --no-lock --file /var/cfengine/masterfiles/hello_world.cf --bundlesequence hello_world```

1. The output will include something similar to the following:

```notice: R: Hello World!```


#### Registering a Promise in `promises.cf` ####

Registering the promise with CFEngine consists of some simple steps:

1. On the policy server, open the file `/var/cfengine/masterfiles/promises.cf` in a text editor.
2.  At the end of the `bundlesequence` section add the following line:

```
"hello_world",
```
3.  At the end of the `inputs` section add the following line:

```
"hello_world.cf",
```

With the above information CFEngine will then do the following:

1. The policy server copies the `hello_world promise` defined in `promises.cf` to its own `/var/cfengine/inputs` directory.
2. Hosts pull their own copy of the same `hello_world promise` into its own `/var/cfengine/inputs` directory.
3. The `promise` is executed.
4. In the `hello_world` example an adminstrator, defined in the file `controls/cf_execd.cf`, will be emailed the message `Hello World!`. 

## See Also ##
* [Promises][Promises]