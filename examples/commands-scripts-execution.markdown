---
layout: default
title: Commands, Scripts, and Execution Examples 
published: true
sorting: 5
tags: [Examples,Commands,Scripts]
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

## Change directory for command

```cf3
body common control

{
bundlesequence  => { "example" };
}

###########################################################


body contain cd(dir)
{
chdir => "${dir}";
useshell => "true";
}

bundle agent example
{
commands:

   "/bin/pwd"
       contain => cd("/tmp");
}
```

## Commands example ##

## Commands example

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

## Execresult example

```cf3
body common control

{
bundlesequence  => { "example" };
}

###########################################################


bundle agent example

{     
vars:

  "my_result" string => execresult("/bin/ls /tmp","noshell");

reports:

  linux::

    "Variable is $(my_result)";

}
```

## Methods

```cf3
body common control

{
bundlesequence  => { "testbundle"  };

version => "1.2.3";
}

###########################################


bundle agent testbundle
{
vars:

 "userlist" slist => { "mark", "jeang", "jonhenrik", "thomas", "eben" };

methods:

 "any" usebundle => subtest("$(userlist)");

}

###########################################


bundle agent subtest(user)

{
commands:

 "/bin/echo Fix $(user)";

reports:

 linux::

  "Finished doing stuff for $(user)";
}
```

## Method validation

```cf3
body common control

{
bundlesequence  => { "testbundle"  };

version => "1.2.3";
}

###########################################


body agent control

{
abortbundleclasses => { "invalid" };
}

###########################################


bundle agent testbundle
{
vars:

 "userlist" slist => { "xyz", "mark", "jeang", "jonhenrik", "thomas", "eben" };

methods:

 "any" usebundle => subtest("$(userlist)");

}

###########################################


bundle agent subtest(user)

{
classes:

  "invalid" not => regcmp("[a-z][a-z][a-z][a-z]","$(user)");

reports:

 !invalid::

  "User name $(user) is valid at 4 letters";

 invalid::

  "User name $(user) is invalid";
}
```

## Trigger classes

```cf3
#######################################################

#

# Insert a number of lines and trigger a followup if edited

#

#######################################################


body common control

{
any::

  bundlesequence  => { "insert" };   
}


#######################################################


bundle agent insert

{
vars:

  "v" string => "
                One potato
                Two potato
                Three potahto
                Four
                ";
 
files:

  "/tmp/test_insert"

     edit_line => Insert("$(insert.v)"),
     edit_defaults => empty,
     classes => trigger("edited");

commands:

 edited::

  "/bin/echo make bananas";

reports:

  edited::

    "The potatoes are bananas";

}

#######################################################

# For the library

#######################################################


bundle edit_line Insert(name)

{
insert_lines:

  "Begin$(const.n) $(name)$(const.n)End";

}

#######################################################


body edit_defaults empty

{
empty_file_before_editing => "true";
}

#######################################################


body classes trigger(x)

{
promise_repaired => { "$(x)" };
}
```