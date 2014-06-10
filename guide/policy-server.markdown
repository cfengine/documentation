---
layout: default
title: The Policy Server
sorting: 5
published: true
tags: [guide, policy server]
---

## What is the Policy Server? 

The policy server makes important files available to client machines.

The policy server itself only makes important files available on the network. It is up to the clients for which the server is responsible to pull the files themselves. The server will not do this on behalf of its clients.

### Adding Promises to promises.cf ###

Assuming there is a promise called "**hello_world**" defined in a file located at **/var/cfengine/masterfiles/hello_world.cf**:

1. On the policy server, open the file **/var/cfengine/masterfiles/promises.cf** in a text editor.
2. At the end of the **bundlesequence** section add the following line:

		
		"hello_world",
		
3. At the end of the **inputs** section add the following line:

		
		"hello_world.cf",
		

##### Alternative Configuration Approach for promises.cf #####

Bundles and promises can be included in files outside of **promises.cf**.

1. Create a file called **/var/cfengine/masterfiles/z01PromiseSetup.cf**
2. In it add the following content:
		
		bundle common z01_promise_setup
		{
		vars:
			"bundles" slist => {"", };

			"promise_files" slist => { "", };

		}
		
3. Assuming there is a promise called "**hello_world**" defined in a file located at **/var/cfengine/masterfiles/hello_world.cf**, modify **/var/cfengine/masterfiles/z01PromiseSetup.cf**:
		
		bundle common z01_promise_setup
		{
		vars:
			"bundles" slist => { "hello_world",	} ;

			"promise_files" slist => { "hello_world.cf", } ;

		}
		
4. In **promises.cf**, at the end of the **bundlesequence** section, replace **"hello_world",** with the following two lines:

		"z01_promise_setup",
		@(z01_promise_setup.bundles),
		
5. Also in **promises.cf**, at the end of the **inputs** section, replace **"hello_world.cf",** with the following two lines:

		"z01PromiseSetup.cf",
		@(z01_promise_setup.promise_files),
		

Note: It can take up to 10 minutes for these changes to propogate across the entire system.

See Also: [Policy Server Setup][Policy Server Setup]

