---
layout: default
title: Writing Policy and Promises
published: true
sorting: 2
---

## How Promises Work ##

Everything in CFEngine can be thought of as a promise to be kept by different resources in the system. In a system that delivers a web site using Apache, an important promise may be to make sure that the `httpd` package is installed, running, and accessible on port 80. 

### Summary for Writing, Deploying and Using Promises ###

Writing, deploying, and using CFEngine `promises` will generally follow these simple steps:

1. Using a text editor, create a new file (e.g. `hello_world.cf`).
2. Create a bundle and promise in the file (see [Test the Workflow With a "Hello World" Promise](#test-the-workflow-with-a-hello-world)).
3. Save the file on the policy server somewhere under `/var/cfengine/masterfiles` (can be under a sub-directory).
4a. Let CFEngine know about the `promise` on the `policy server`, generally in the file `/var/cfengine/masterfiles/promises.cf`, or a file elsewhere but referred to in `promises.cf`.
4b. Alternatively, it is also possible to call a bundle manually, using `cf-agent`.
5. Verify the `policy file` was deployed and successfully run.

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

There are two methods possible with GitHub: one is to use the web interface at GitHub.com; the second is to use the GitHub application.

Method One: Create Masterfiles Repository Using GitHub Web Interface 

1a. In the GitHub web interface, click on the `New repository` button.
1b. Or from the `+` drop down menu on the top right hand side of the screen select `New repository`.
2. Fill in a value in the `Repository name` text entry (e.g. cfengine-masterfiles).
3. Select `private` for the type of privacy desired (`public` is also possible, but is not recommended in most situations).
4. Optionally, check the `Initialize this repository with a README` box. (not required):""

Method Two: Create Masterfiles Repository Using the GitHub Application

1. Open the GitHub app and click on the "+ Create" sign to create a new repository.
2. Fill in a value in the `Repository name` text entry (e.g. cfengine-masterfiles).
3. Select `private` for the type of privacy desired (`public` is also possible, but is not recommended in most situations).
4. Select one of your "Accounts" where you want the new repository to be created.
5. Click on the "Create" button at the bottom of the screen. A new repository will be created in your local GitHub folder.


#### Initialize Git Repository in Masterfiles on the Hub ####

1. `> cd /var/cfengine/masterfiles`
2. `> git init`
3. `> git commit -m "First commit"`
4. `> git remote add origin https://github.com/GitUserName/cfengine-masterfiles.git`
5. `> git push -u origin master`

Using the above steps on a private repository will fail with a 403 error. There are different approaches to deal with this:

A) Generate a key pair and add it to GitHub

1. As root, type `ssh-keygen -t rsa`.
2. Hit enter when prompted to `Enter file in which to save the key (/root/.ssh/id_rsa):`.
3. Hit enter again when prompted to `Enter passphrase (empty for no passphrase):`.
4. Type `ssh-agent bash` and then the enter key.
5. Type `ssh-add /root/.ssh/id_rsa`.
6. Type `exit` to leave `ssh-agent bash`.
7. To test, type `ssh -T git@github.com`.
8. Open the generated key file (e.g. `vi /root/.ssh/id_rsa.pub`).
9. Copy the contents of the file to the clipboard (e.g. Ctrl+Shift+C).
10. In the GitHub web interface, click the user account settings button (the icon with the two tools in the top right hand corner).
11. On the next screen, on the left hand side, click `SSH keys`.
12. Click `Add SSH key` on the next screen.
13. Provide a `Title` for the label (e.g. CFEngine).
14. Paste the key contents from the clipboard into the `Key` textarea.
15. Click `Add key`.
16. If prompted to do so, provide your GitHub password, and then click the `Confirm` button.	

B) Or, change the remote url to `https://GitUserName@password:github.com/GitUserName/cfengine-masterfiles.git`. This is not safe in a production environment and should only be used for basic testing purposes (if at all).

#### Create a Remote in Masterfiles on the Hub to Masterfiles on GitHub ####

1. Change back to the `masterfiles` directory, if not already there:
	* `> cd /var/cfengine/masterfiles`
2. Create the remote using the following pattern: 
	* `> git remote add upstream ssh://git@github.com/GitUserName/cfengine-masterfiles.git`.
3. Verify the remote was registered properly by typing `git remote -v` and pressing enter.
	* You will see the remote definition in a list alongside any other previously defined remote enteries.

#### Add a Promise that Pulls Changes to Masterfiles on the Hub from Masterfiles on GitHub ####

1. Create a new file in `/var/cfengine/masterfiles with a unique filename` (e.g. `vcs_update.cf`)
2. Add the following text to the `vcs_update.cf` file:

```cf3
bundle agent vcs_update
    {
    commands:
      "/usr/bin/git"
        args => "pull --ff-only upstream master",
        contain => masterfiles_contain;
    }

body contain masterfiles_contain
    {
      chdir => "/var/cfengine/masterfiles";
    }
```

3. Save the file.
4. Add bundle and file information to `/var/cfengine/masterfiles/promises.cf`. Example (where `...` represents existing text in the file, omitted for clarity:

```cf3
body common control

{

      bundlesequence => {
						...
                        vcs_update,

      };

      inputs => {
                 ...
				 
                  "vcs_update.cf",
      };
```

5. Save the file.

#### Test the Workflow With a "Hello World" Promise ####

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

      "Hello World!"

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
* [Promises][Promises]