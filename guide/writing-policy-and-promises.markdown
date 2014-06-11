---
layout: default
title: Writing Policy and Promises
published: true
sorting: 6
---

* [Policy Workflow][Writing Policy and Promises#Policy Workflow]
* [How Promises Work][Writing Policy and Promises#How Promises Work]
	* [Summary for Writing, Deploying and Using Promises][Writing Policy and Promises#Summary for Writing, Deploying and Using Promises]
* [Executing Policy][Writing Policy and Promises#Executing Policy]

## Policy Workflow ##

CFEngine does not make absolute choices for you, like other tools.  Almost
everything about its behavior is matter of policy and can be changed.

In order to keep operations as simple as possible, CFEngine maintains a
private [working directory][The CFEngine Components#The Working Directory]
on each machine, referred to in documentation as `WORKDIR` and in policy by
the variable [$(sys.workdir)][sys#sys-workdir] By default, this is located at
`/var/cfengine` or `C:\var\CFEngine`. It contains everything CFEngine needs to
run.

The figure below shows how decisions flow through the parts of a system.

![Policy decision and distribution flowchart](policy-decision-flow.png)

* It makes sense to have a single point of coordination. Decisions are
  therefore usually made in a single location (the Policy Definition Point).
  The history of decisions and changes can be tracked by a version control
  system of your choice (e.g. git, Subversion, CVS etc.).

* Decisions are made by editing CFEngine's policy file `promises.cf` (or one
  of its included sub-files). This process is carried out off-line.

* Once decisions have been formalized and coded, this new policy is copied
  to a decision distribution point, [$(sys.masterdir)][sys#sys-masterdir] which
  defaults to `/var/cfengine/masterfiles` on all policy distribution servers.

* Every client machine contacts the policy server and downloads these updates.
  The policy server can be replicated if the number of clients is very large,
  but we shall assume here that there is only one policy server.

Once a client machine has a copy of the policy, it extracts only those promise
proposals that are relevant to it, and implements any changes without human
assistance. This is how CFEngine manages change.

CFEngine tries to minimize dependencies by decoupling processes. By following
this pull-based architecture, CFEngine will tolerate network outages and will
recover from deployment errors easily. By placing the burden of responsibility
for decision at the top, and for implementation at the bottom, we avoid
needless fragility and keep two independent quality assurance processes apart.


## How Promises Work ##

Everything in CFEngine can be thought of as a promise to be kept by different resources in the system. In a system that delivers a web site using Apache, an important promise may be to make sure that the `httpd` package is installed, running, and accessible on port 80. 

### Summary for Writing, Deploying and Using Promises ###

Writing, deploying, and using CFEngine `promises` will generally follow these simple steps:

1. Using a text editor, create a new file (e.g. `hello_world.cf`).
2. Create a bundle and promise in the file (see [Example: "Hello World" Promise][Writing Policy and Promises#Example: "Hello World" Promise]).
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

### Executing Policy ###

#### Manually Executing a Bundle ####

1. Assuming the promise file is located at `/var/cfengine/masterfiles/hello_world.cf`, on the command line type the following: 

		```# /var/cfengine/bin/cf-agent --no-lock --file /var/cfengine/masterfiles/hello_world.cf --bundlesequence hello_world```

2. The output will include something similar to the following: `notice: R: Hello World!`.


#### Registering Policy in `promises.cf` ####

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