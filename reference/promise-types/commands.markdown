---
layout: default
title: commands
published: true
tags: [reference, bundle agent, commands, promises, promise types]
---

Commands and [processes][processes] are separated cleanly. Restarting of
processes must be coded as a separate command. This stricter type separation
allows for more careful conflict analysis to be carried out.

```cf3
     commands:

       "/path/to/command args"

                  args => "more args",
                  contain => contain_body,
                  module => "true|false";
```

Output from commands executed here is quoted inline, but prefixed with
the letter Q to distinguish it from other output; for example, from
`reports`, which is prefixed with the letter `R`.

It is possible to set classes based on the return code of a
commands-promise in a very flexible way. See the `kept_returncodes`,
`repaired_returncodes` and `failed_returncodes` attributes.

```cf3
bundle agent example

{
commands:

  "/bin/sleep 10"
     action  => background;

  "/bin/sleep"
     args => "20",
     action  => background;

}
```

When referring to executables the full path to the executable must be used.
When reffereing to executables whose paths contain spaces, you should quote
the entire program string separately so that CFEngine knows the name of the
executable file. For example:

```cf3
      commands:

       windows::

        "\"c:\Program Files\my name with space\" arg1 arg2";

       linux::

        "\"/usr/bin/funny command name\" -a -b -c";
```
**Note:** Commands executed with CFEngine get the environment variables set in
[`environment`][cf-agent#environment] in body agent control. If you want to set
environment variables for an individual command you can prefix the command with
`env` and set variables before executing the command.

```cf3
bundle agent example
{
  commands:
    "/usr/bin/env MY_ENVIRONMENT_VARIABLE=something_special /tmp/cmd";

    # Or equivlent
    "/usr/bin/env"
      args => "ME=something_special /tmp/cmd";
}
```

**Note**: Some unices leave a hanging pipe on restart (they never manage to
detect the end of file condition). This occurs on POSIX.1 and SVR4 popen calls
which use wait4. For some reason they fail to find and end-of-file for an
exiting child process and go into a deadlock trying to read from an already
dead process.  This leaves a zombie behind (the parent daemon process which
forked and was supposed to exit) though the child continues. A way around this
is to use a wrapper script which prints the line `cfengine-die` to STDOUT after
restarting the process. This causes cfengine to close the pipe forcibly and
continue.

****

## Attributes ##

[%CFEngine_include_markdown(common-attributes-include.markdown)%]

### args

**Description:** Allows to separate the arguments to the command from the
command itself.

Sometimes it is convenient to separate command and arguments. The final arguments are the concatenation with one space.

**Type:** `string`

**Allowed input range:** (arbitrary string)

```cf3
commands:

  "/bin/echo one"

   args => "two three";
```

So in the example above the command would be:

```cf3
 /bin/echo one two three
```

**See also:** `arglist`, `join()`, `concat()`, `format()`

### arglist

**Description:** Allows to separate the arguments to the command from the 
command itself, using an slist.

As with `args`, it is convenient to separate command and arguments.
With `arglist` you can use a slist directly instead of having to
provide a single string as with `args`. That's particularly useful
when there are embedded spaces and quotes in your arguments, but also
when you want to get them directly from a slist without going through
`join()` or other functions.

The `arglist` is **appended** to `args` if that's defined, to preserve
backwards compatibility.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

```cf3
commands:

  "/bin/echo one"

   args => "two three",
   arglist => { "four", "five" };
```

So in the example above the command would be:

```cf3
 /bin/echo one two three four five
```

**History:** Was introduced in CFEngine 3.9.0.

**See also:** `args`, `join()`, `concat()`, `format()`

### contain

**Description:** Allows running the command in a 'sandbox'.

Command containment allows you to make a `sandbox' around a command, to run it
as a non-privileged user inside an isolated directory tree.

**Type:** `body contain`

**Example:**

```cf3
    body contain example
    {
        useshell => "noshell";
           umask => "077";
      exec_owner => "mysql_user";
      exec_group => "nogroup";
    exec_timeout => "60";
           chdir => "/working/path";
          chroot => "/private/path";
    }
```

**See also:** [Common Body Attributes][Promise Types and Attributes#Common Body Attributes]

#### useshell

**Description:** Specifies whether or not to use a shell when executing the command.

The default is to *not* use a shell when executing commands. Use of a
shell has both resource and security consequences. A shell consumes an
extra process and inherits environment variables, reads commands from
files and performs other actions beyond the control of CFEngine.

If one does not need shell functionality such as piping through multiple
commands then it is best to manage without it. In the Windows version of
CFEngine Enterprise, the command is run in the `cmd` Command Prompt if this
attribute is set to `useshell`, or in the PowerShell if the attribute is set
to `powershell`.

**Type:** (menu option)

**Allowed input range:**

```
    useshell
    noshell
    powershell
```

For compatibility, the boolean values are also supported, and map to
`useshell` and `noshell`, respectively.

**Default value:** `noshell`

**Example:**

```cf3
     body contain example
     {
     useshell => "useshell";
     }
```

#### umask

**Description:** Sets the internal umask for the process.

Default value for the mask is 077. On Windows, umask is not supported and is
thus ignored by Windows versions of CFEngine.

**Type:** (menu option)

**Allowed input range:**

```
    0
    77
    22
    27
    72
    002
    077
    022
    027
    072
```

**Example:**

```cf3
     body contain example
     {
     umask => "077";
     }
```

#### exec_owner

**Description:** Specifies the user under which the command executes.

This is part of the restriction of privilege for child processes when
running `cf-agent` as the root user, or a user with privileges.

Windows requires the clear text password for the user account to run
under. Keeping this in CFEngine policies could be a security hazard.
Therefore, this option is not yet implemented on Windows versions of
CFEngine.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body contain example
     {
     exec_owner => "mysql_user";
     }
```

#### exec_group

**Description:** Associates the command with a group.

This is part of the restriction of privilege for child processes when
running `cf-agent` as the root group, or a group with privileges. It is
ignored on Windows, as processes do not have any groups associated with
them.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
     body contain example
     {
     exec_group => "nogroup";
     }
```

#### exec_timeout

**Description:** Attempt to time-out after this number of seconds.

This cannot be guaranteed as not all commands are willing to be interrupted in
case of failure.

**Type:** `int`

**Allowed input range:** `1,3600`

**Example:**

```cf3
     body contain example
     {
     exec_timeout => "30";
     }
```

**See Also:** [`body action expireafter`][Promise Types and Attributes#expireafter],  [`body agent control expireafter`][cf-agent#expireafter], [`body executor control agent_expireafter`][cf-execd#agent_expireafter]

#### chdir

**Description:** Run the command with a working directory.

This attribute has the effect of placing the running command into a
current working directory equal to the parameter given; in other words,
it works like the cd shell command.

**Type:** `string`

**Allowed input range:** `"?(/.*)`

**Example:**

```cf3
     body contain example

     {
     chdir => "/containment/directory";
     }
```

#### chroot

**Description:** Specify the path that will be the root directory for the
process.

The path of the directory will be experienced as the top-most root directory
for the process. In security parlance, this creates a 'sandbox' for the
process. Windows does not support this feature.

**Type:** `string`

**Allowed input range:** `"?(/.*)`

**Example:**

```cf3
     body contain example

     {
     chroot => "/private/path";
     }
```

#### preview

**Description:** This is the preview command when running in dry-run mode
(with -n).

Previewing shell scripts during a dry-run is a potentially misleading
activity. It should only be used on scripts that make no changes to the
system. It is CFEngine best practice to never write change-functionality into
user-written scripts except as a last resort. CFEngine can apply its safety
checks to user defined scripts.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
     body contain example
     {
     preview => "true";
     }
```

#### no_output

**Description:** Allows to discard all output from the command.

Setting this attribute to `true` is equivalent to piping standard output and
error to `/dev/null`.

**Type:** [`boolean`][boolean]

**Default value:** false if `module` is false, true if `module` is true.

**Example:**

```cf3
     body contain example
     {
     no_output => "true";
     }
```

### module

**Description:** Set variables and classes based on command output.

CFEngine `modules` are commands that support a simple protocol in order to set
additional variables and classes on execution from user defined code. Modules
are intended for use as system probes rather than additional configuration
promises. Such a module may be written in any language.

This attribute determines whether or not to expect the CFEngine module protocol. If true, the module protocol is supported for this command:

* lines which begin with a `^` are protocol extensions
  * `^context=xyz` sets the module context to `xyz` instead of the default for any following definitions
  * `^meta=a,b,c` sets the class and variable tags for any following definitions to `a`, `b`, and `c`
  * `^persistence=10` sets any following classes to persist for 10 minutes (use 0 to reset)
  * `^persistence=0` sets any following classes to have no persistence (this is the default)
* lines which begin with a `+` are treated as classes to be defined (like -D). **NOTE:** classes are defined with the [`namespace` scope][Classes and Decisions].
* lines which begin with a `-` are treated as classes to be undefined (like -N)
* lines which begin with `=` are scalar variables to be defined
* lines which begin with `=` and include `[]` are array variables to be defined
* lines which begin with `@` are lists.
* lines which begin with `%` are `data` containers.  The value needs to be valid JSON and will be decoded.

These variables end up in a context that has the same name as the
module, unless the `^context` extension is used.

**NOTE**: All variables and classes defined by the module protocol are defined
in the ```default``` namespace. It is not possible to define variables and
classes in any other namespace. Protocol extensions ( lines that start with `^`
) apply until they are explicitly reset, or until the end of the modules
execution.

All the variables and classes will have at least the tag
`source=module` in addition to any tags you may set.

Any other lines of output are cited by `cf-agent` as being erroneous, so you
should normally make your module completely silent.

**WARNING:** Variables defined by the module protocol are currently limited to
alphanumeric characters and ```_```, ```.```, ```-```, ```[```, ```]``` and
```/```.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

Here is an example module written in shell:

```sh
     #!/bin/sh
     /bin/echo "@mylist= { \"one\", \"two\", \"three\" }"
     /bin/echo "=myscalar= scalar val"
     /bin/echo "=myarray[key]= array key val"
     /bin/echo "%mydata=[1,2,3]"
     /bin/echo "+module_class"
     /bin/echo "^persistence=10"
     /bin/echo "+persistent_10_minute_class"
```

And here is an example using it:

```cf3
    body common control
    {
    bundlesequence  => { def, modtest };
    }

    bundle agent def
    {
    commands:

      "$(sys.workdir)/modules/module_name"
        module => "true";

    reports:

      # Each module forms a private context with its name as id
      module_class::

        "Module set variable $(module_name.myscalar)";
    }


    bundle agent modtest
    {
    vars:

      "mylist" slist => { @(module_name.mylist) };

    reports:

      module_class::

        "Module set variable $(mylist)";
    }
```

Here is an example module written in Perl:

```perl
     #!/usr/bin/perl
     #
     # module:myplugin
     #

       # lots of computation....

     if (special-condition)
        {
        print "+specialclass";
        }
```

If your module is simple and is best expressed as a shell command, then we
suggest that you *expose* the class being defined in the command being
executed (making it easier to see what classes are used when reading the
promises file). For example, the promises could read as follows (the two
`echo` commands are to ensure that the shell always exits with a successful
execution of a command):

```cf3
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
        useshell    => "useshell";
    }

    body contain not_paranoid
    {
        useshell    => "no";
        exec_owner  => "root";
        umask       => "22";
    }
```

Modules inherit the environment variables from `cf-agent` and accept
arguments, just as a regular command does.

**See Also:** [usemodule()][usemodule]
