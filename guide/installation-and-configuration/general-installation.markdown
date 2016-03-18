---
layout: default
title: General Installation
published: true
sorting: 20
tags: [guide, installation, install]
---

[%CFEngine_include_markdown(include-install-bootstrap-configure-summary.markdown)%]

## Before Installation ##

Check the [Pre-Installation Checklist][Pre-Installation Checklist] and [Supported Platforms and Versions][Supported Platforms and Versions] for requirements and other information that is useful for the installation procedure.

## Install Packages ##

CFEngine Enterprise is provided in two packages; one is for the Policy
Server (hub) and the other is for each Host (client). 

Note: See [Installing Community][Installing Community] for the community version of CFEngine)

**Log in as root** and then follow these steps to install CFEngine Enterprise:

1. On the designated Policy Server, install the `cfengine-nova-hub` package:

    ```
        [RedHat/CentOS/SUSE] $ rpm -i <server hub package>.rpm
        [Debian/Ubuntu]      $ dpkg -i <server hub package>.deb
    ```

2. On each Host, install the `cfengine-nova` package:

    ```
        [RedHat/CentOS/SUSE] $ rpm -i <agent package>.rpm
        [Debian/Ubuntu]      $ dpkg -i <agent package>.deb
    ```

Note: Install actions logged to `/var/logs/cfengine-install.log`.

## Bootstrap ##

Bootstrapping a client means to configure it initially.  With CFEngine, the default bootstrap:

* records the server's address (accessible as `sys.policy_hub`) and public key, and gives the server the client's key to establish trust (see [Bootstrapping][Networking#Bootstrapping])
* copies **all** the contents of `/var/cfengine/masterfiles` on the policy server (AKA `sys.masterdir`) to `/var/cfengine/inputs` (AKA `sys.inputdir`).  See `update.cf` for details.

Run the bootstrap command, **first** on the policy server:

1. Find the IP address of your Policy Server:

		
	    $ ifconfig
		

2. Run the bootstrap command:

		
        $ sudo /var/cfengine/bin/cf-agent --bootstrap <IP address of policy server>
		

The bootstrap command must then be run on any client attaching itself to this server, using the ip address of the policy server (i.e. exactly the same as the command run on the policy server itself).

## Post-Installation Configuration ##

CFEngine itself is configured through policy as well (see [Components and Common Control][] and 
[The Policy Framework][] for details). The following basic changes to the default policy will configure 
`cf-serverd` and `cf-execd` for your environment.

### def.cf or def.json ###

1. Find the following line:
		
		"domain"  string    => "your.domain.here",
		
2. Change **your.domain.here** to your domain name, e.g. **example.com**.

#### def.json ###

Starting with CFEngine 3.7, the file `def.json` (typically
`/var/cfengine/inputs/def.json` for the main `promises.cf`) can be
used instead of `def.cf` for many settings.

`def.json` can add variables and classes to the execution of **all** CFEngine
components **before** any parsing or evaluation happen. It's a JSON data file,
so you should view and edit it with a JSON-aware editor if possible.

Values will be expanded, so you can use the variables from
[Special Variables][].

The file `def.json` is found like the policy file to be run:

* with no arguments, it's in `$(sys.inputdir)/def.json` because `$(sys.inputdir)/promises.cf` is used
* with `-f /dirname/myfile.cf`, it's in `/dirname/def.json`
* with `-f myfile.cf`, it's in `./def.json`

Currently `def.json` can contain three keys:

* `inputs`: any filenames you put here will appear in the `def.augments_inputs`
  variable. The standard set of masterfiles refers to this variable and will
  autoload those files.

**Note:** In CFEngine 3.8.1 it was possible to use `inputs` to autoload inputs
  without referencing the `def.augments_inputs` variable. This would happen
  before all evaluation stages. However, this functionality turned out to be
  problematic and was removed in later versions.

* `vars`: any variables you put here will be put in the `def` scope. Thus:

```
"vars":
{
  "phone": "22-333-4444",
  "myplatform": "$(sys.os)",
}
```

results in the variable `def.phone` with value `22-333-4444` being
defined, and `def.myplatform` with the value of your current OS.
Again, note that this happens before policy is parsed or evaluated.

You can see the list of variables thus defined in the output of
`cf-promises --show-vars` (see [Components and Common Control][]).
They will be tagged with the tag `source=augments_file`. For instance,
the above two variables (assuming you placed the data in
`$(sys.inputdir)/def.json`) result in

```
cf-promises --show-vars
...
default:def.myplatform                   linux                                                        source=augments_file
default:def.phone                        22-333-4444                                                  source=augments_file
```

* `classes`: any class names you put here will be evaluated and
installed as **hard classes** if they match as a class name or a
regular expression. Thus:

```
"classes":
{
  "my_always": "any",
  "my_other_apache": [ "server[34]", "debian.*" ],
}
```

results in `my_always` being always defined. `my_other_apache` will be
defined if the classes `server3` or `server4` are defined, or if any
class starting with `debian` is defined. You can use any classes
listed in [Hard and Soft Classes][Hard and Soft Classes#Hard Classes].

You can see the list of classes thus defined through `def.json` in the
output of `cf-promises --show-classes` (see
[Components and Common Control][]). They will be tagged with the tags
`source=augments_file,hardclass`. For instance, the above two classes
result in:

```
% cf-promises --show-classes
...
my_always                                                    source=augments_file,hardclass
my_other_apache                                              source=augments_file,hardclass
```

### controls/cf_execd.cf ###

1. Find the following line:
		
		mailto => "some-admin-list@me.local";
		
2. Change **some-admin-list@me.local** to your email address.

Note: On some systems this modification should hopefully work without needing to make any additional changes elsewhere. However, any emails sent from the system might also end up flagged as spam and sent directly to a user's junk mailbox.

### Server IP Address and Hostname ###

Edit `/etc/hosts` and add an entry for the IP address and hostname of the server.

### CFEngine Enterprise Post-Installation Setup ###

See: [What steps should I take after installing CFEngine Enterprise?][FAQ#What steps should I take after installing CFEngine Enterprise]


## More Detailed Installation Guides ##

Although most install procedures follow the same general workflow, there are several ways of installing CFEngine depending on your environment and which version of CFEngine you are using.

* [Installing Enterprise for Production][Installing Enterprise for Production]
* Install and test the latest version using our [native version][Installing Enterprise 25 Free], for free!
* Installing CFEngine on virtual machine instances using [Amazon Web Services' (AWS) EC2 service][Using Amazon Web Services]
	* This is especially useful for people running Windows on their workstation or laptop.
* Install and test the latest version using our pre-packaged [Vagrant environment][Using Vagrant]
* [Installing CFEngine Community Edition][Installing Community]

## Next Steps ##

* Learn about [Writing and Serving Policy][Writing and Serving Policy]

