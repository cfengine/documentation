---
layout: default
title: Commands, Scripts, and Execution Examples 
published: true
sorting: 5
tags: [Examples][Commands][Scripts]
---

* [Command or script execution][Commands, Scripts, and Execution#Command or script execution]
* [Change directory for command][Commands, Scripts, and Execution#Change directory for command]
* [Commands example][Commands, Scripts, and Execution#Commands example]
* [Execresult example][Commands, Scripts, and Execution#Execresult example]
* [Methods][Commands, Scripts, and Execution#Methods]
* [Method validation][Commands, Scripts, and Execution#Method validation]
* [Trigger classes][Commands, Scripts, and Execution#Trigger classes]

## Command or script execution ##

Execute a command, for instance to start a MySQL service. Note that simple shell commands like rm or mkdir cannot be managed by CFEngine, so none of the protections that CFEngine offers can be applied to the process. Moreover, this starts a new process, adding to the burden on the system. See CFEngine 3 Best Practices http://cfengine.com/manuals/cf3-bestpractice.html for more information on how to best write policies.

```cf3
body common control
{
bundlesequence  => { "my_commands" };
inputs => { "cfengine_stdlib.cf" };
}


bundle agent my_commands
{
commands:

 Sunday.Hr04.Min05_10.myhost::

  "/usr/bin/update_db";

 any::

  "/etc/mysql/start"

      contain => setuid("mysql");

}
```

## Change directory for command ##
## Commands example ##
## Execresult example ##
## Methods ##
## Method validation ##
## Trigger classes ##