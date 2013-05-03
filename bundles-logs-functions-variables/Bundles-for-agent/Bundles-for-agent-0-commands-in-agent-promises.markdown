---
layout: default
title: commands-in-agent-promises
categories: [Bundles-for-agent,commands-in-agent-promises]
published: true
alias: Bundles-for-agent-commands-in-agent-promises.html
tags: [Bundles-for-agent,commands-in-agent-promises]
---

### `commands` promises in agent

\

~~~~ {.smallexample}
     
     commands:
     
       "/path/to/command args"
     
                  args = "more args",
                  contain = contain_body,
                  module = true/false;
     
~~~~

Command *containment* allows you to make a \`sandbox' around a command,
to run it as a non-privileged user inside an isolated directory tree.
CFEngine `modules` are commands that support a simple protocol (see
below) in order to set additional variables and classes on execution
from user defined code. Modules are intended for use as system probes
rather than additional configuration promises.

In CFEngine 3 commands and processes have been separated cleanly.
Restarting of processes must be coded as a separate command. This
stricter type separation will allow more careful conflict analysis to be
carried out.

Output from commands executed here is quoted inline, but prefixed with
the letter Q to distinguish it from other output; for example, from
`reports`, which is prefixed with the letter R.

It is possible to set classes based on the return code of a
commands-promise in a very flexible way. See the `kept_returncodes`,
`repaired_returncodes` and `failed_returncodes` attributes.

\

~~~~ {.verbatim}
bundle agent example

{
commands:

  "/bin/sleep 10"
     action  => background;

  "/bin/sleep"
     args => "20",
     action  => background;

}
~~~~

\

When referring to executables whose paths contain spaces, you should
quote the entire program string separately so that CFEngine knows the
name of the executable file. For example:

~~~~ {.smallexample}
     
      commands:
     
       windows::
     
        "\"c:\Program Files\my name with space\" arg1 arg2";
     
       linux::
     
        "\"/usr/bin/funny command name\" -a -b -c";
     
~~~~

-   [args in commands](#args-in-commands)
-   [contain in commands](#contain-in-commands)
-   [module in commands](#module-in-commands)

#### `args`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Alternative string of arguments for the command
(concatenated with promiser string)

**Example**:\
 \

~~~~ {.verbatim}
commands:

  "/bin/echo one"

   args => "two three";
~~~~

**Notes**:\
 \

Sometimes it is convenient to separate the arguments to a command from
the command itself. The final arguments are the concatenation with one
space. So in the example above the command would be:

~~~~ {.verbatim}
 /bin/echo one two three
~~~~

#### `contain` (body template)

**Type**: (ext body)

`useshell`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false embed the command in a shell environment

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body contain example
     {
     useshell => "true";
     }
     
~~~~

**Notes**:\
 \

The default is to *not* use a shell when executing commands. Use of a
shell has both resource and security consequences. A shell consumes an
extra process and inherits environment variables, reads commands from
files and performs other actions beyond the control of CFEngine. If one
does not need shell functionality such as piping through multiple
commands then it is best to manage without it. In the Windows version of
CFEngine Nova, the command is run in the the Command Prompt if useshell
is true. \

`umask`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    0
                    77
                    22
                    27
                    72
                    077
                    022
                    027
                    072
~~~~

**Synopsis**: The umask value for the child process

**Example**:\
 \

~~~~ {.verbatim}
     
     body contain example
     {
     umask => "077";
     }
     
~~~~

**Notes**:\
 \

Sets the internal umask for the process. Default value for the mask is
077. On Windows, umask is not supported and is thus ignored by Windows
versions of CFEngine. \

`exec_owner`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: The user name or id under which to run the process

**Example**:\
 \

~~~~ {.verbatim}
     
     body contain example
     {
     exec_owner => "mysql_user";
     }
     
~~~~

**Notes**:\
 \

This is part of the restriction of privilege for child processes when
running `cf-agent` as the root user, or a user with privileges.

Windows requires the clear text password for the user account to run
under. Keeping this in CFEngine policies could be a security hazard.
Therefore, this option is not yet implemented on Windows versions of
CFEngine. \

`exec_group`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: The group name or id under which to run the process

**Example**:\
 \

~~~~ {.verbatim}
     
     body contain example
     {
     exec_group => "nogroup";
     }
     
~~~~

**Notes**:\
 \

This is part of the restriction of privilege for child processes when
running `cf-agent` as the root group, or a group with privileges. It is
ignored on Windows, as processes do not have any groups associated with
them. \

`exec_timeout`

**Type**: int

**Allowed input range**: `1,3600`

**Synopsis**: Timeout in seconds for command completion

**Example**:\
 \

~~~~ {.verbatim}
     
     body contain example
     {
     exec_timeout => "30";
     }
     
~~~~

**Notes**:\
 \

Attempt to time-out after this number of seconds. This cannot be
guaranteed as not all commands are willing to be interrupted in case of
failure. \

`chdir`

**Type**: string

**Allowed input range**: `"?(/.*)`

**Synopsis**: Directory for setting current/base directory for the
process

**Example**:\
 \

~~~~ {.verbatim}
     
     body contain example
     
     {
     chdir => "/containment/directory";
     }
     
~~~~

**Notes**:\
 \

This command has the effect of placing the running command into a
current working directory equal to the parameter given; in other words,
it works like the cd shell command. \

`chroot`

**Type**: string

**Allowed input range**: `"?(/.*)`

**Synopsis**: Directory of root sandbox for process

**Example**:\
 \

~~~~ {.verbatim}
     
     body contain example
     
     {
     chroot => "/private/path";
     }
     
~~~~

**Notes**:\
 \

Sets the path of the directory that will be experienced as the top-most
root directory for the process. In security parlance, this creates a
\`sandbox' for the process. Windows does not support this feature. \

`preview`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false preview command when running in dry-run mode
(with -n)

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body contain example
     {
     preview => "true";
     }
     
~~~~

**Notes**:\
 \

Previewing shell scripts during a dry-run is a potentially misleading
activity. It should only be used on scripts that make no changes to the
system. It is CFEngine best practice to never write change-functionality
into user-written scripts except as a last resort. CFEngine can apply
its safety checks to user defined scripts. \

`no_output`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false discard all output from the command

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body contain example
     {
     no_output => "true";
     }
     
~~~~

**Notes**:\
 \

This is equivalent to piping standard output and error to /dev/null.

#### `module`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               true
               false
               yes
               no
               on
               off
~~~~

**Default value:** false

**Synopsis**: true/false whether to expect the cfengine module protocol

**Example**:\
 \

~~~~ {.verbatim}
commands:

   "/masterfiles/user_script"

     module => "true";
~~~~

**Notes**:\
 \

If true, the module protocol is supported for this script. In other
words, it is treated as a user module. A plug-in module may be written
in any language, it can return any output you like, but lines which
begin with a + sign are treated as classes to be defined (like -D),
while lines which begin with a - sign are treated as classes to be
undefined (like -N).

Lines starting with = are scalar variables to be defined, and lines
beginning with @ are lists. Any other lines of output are cited by
`cf-agent` as being erroneous, so you should normally make your module
completely silent. Here is an example written in shell:

~~~~ {.smallexample}
     #!/bin/sh
     /bin/echo "@mylist= { \"one\", \"two\", \"three\" }"
     /bin/echo "=myscalar= scalar val"
     /bin/echo "+module_class"
~~~~

And here is an example using it:

~~~~ {.verbatim}
body common control
   {
   any::

      bundlesequence  => { 
                         def,
                         modtest
                         };
   }

###################################################################

bundle agent def

{
commands:

  "$(sys.workdir)/modules/module_name" module => "true";

reports:

  #
  # Each module forms a private context with its name as id
  #

 module_class::

  "Module set variable $(module_name.myscalar)";

}

###################################################################

bundle agent modtest

{
vars:

 "mylist" slist => { @(module_name.mylist) };

reports:

 module_class::

  "Module set variable $(mylist)";

}
~~~~

Here is an example module written in Perl:

~~~~ {.smallexample}
     #!/usr/bin/perl
     #
     # module:myplugin
     #
     
       # lots of computation....
     
     if (special-condition)
        {
        print "+specialclass";
        }
     
~~~~

If your module is simple and is best expressed as a shell command, then
we suggest that you *expose* the class being defined in the command
being executed (making it easier to see what classes are used when
reading the promises file). For example, the promises could read as
follows (the two `echo` commands are to ensure that the shell always
exits with a successful execution of a command):

~~~~ {.verbatim}
bundle agent sendmail
{
commands:
    # This next module checks a specific failure mode of dcc, namely
    # more than 3 error states since the last time we ran cf-agent
    is_mailhost::
        "/bin/test `/usr/bin/tail -100 /var/log/maillog | /usr/bin/grep 'Milter (dcc): to error state' | /usr/bin/wc -l` -gt 3  echo '+start_dccm' || echo
''"
            contain => shell_command,
            module => "true";

    start_dccm::
        "/var/dcc/libexec/start-dccm"
            contain => not_paranoid;
}

body contain shell_command
{
    useshell    => "yes";
}

body contain not_paranoid
{
    useshell    => "no";
    exec_owner  => "root";
    umask       => "22";
}
~~~~

Modules inherit the environment variables from cfagent and accept
arguments, just as a regular command does.

~~~~ {.smallexample}
     #!/bin/sh
     #
     # module:myplugin
     #
     
     /bin/echo $*
     
~~~~

Modules define variables in `cf-agent` by outputting strings of the form

~~~~ {.smallexample}
     
     =variablename=value
     
~~~~

These variables end up in a context that has the same name as the
module. When the `$(allclasses)` variable becomes too large to
manipulate conveniently, you can access the complete list of currently
defined classes in the file /var/cfengine/state/allclasses.
