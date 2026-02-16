# Introduction to CFEngine Policy Language

CFEngine policy describes the **desired state** of your systems.
Instead of writing scripts that run step-by-step, you write **promises** -- declarations of how things should be.
CFEngine's agent (`cf-agent`) then evaluates these promises and makes changes only when the actual state differs from the desired state.

## Structure of a policy file

A CFEngine policy file (`.cf`) is made up of **bundles** and **bodies**.
A bundle is a collection of related promises, grouped by **promise type**.

Here is the simplest possible policy:

```cf3
bundle agent __main__
{
  reports:
    "Hello, world!";
}
```

Run it with:

```console
cf-agent --no-lock --file ./hello.cf
```

Output:

```
R: Hello, world!
```

Key points:

- `bundle agent __main__` -- a bundle of type `agent`, named `__main__`. The `__main__` name tells CFEngine to run this bundle when executing the file directly.
- `reports:` -- a **promise type** section. All promises below it (until the next promise type) are report promises.
- `"Hello, world!"` -- the **promiser**. For reports, it is the message to print.

## Variables (`vars`)

Variables are defined using `vars` promises.
You reference them with `$(variable_name)` for scalar values and `@(variable_name)` for lists.

```cf3
bundle agent __main__
{
  vars:
    "greeting"
      string => "Hello";
    "user"
      string => "Alice";

  reports:
    "$(greeting), $(user)!";
}
```

Output:

```
R: Hello, Alice!
```

### Lists and iteration

Lists automatically iterate when expanded in other promises:

```cf3
bundle agent __main__
{
  vars:
    "users"
      slist => { "alice", "bob", "charlie" };

  reports:
    "Welcome, $(users)!";
}
```

Output:

```
R: Welcome, alice!
R: Welcome, bob!
R: Welcome, charlie!
```

### Variable types

| Type     | Description                 | Example                                        |
| -------- | --------------------------- | ---------------------------------------------- |
| `string` | A scalar string             | `"name" string => "web-01";`                   |
| `int`    | An integer                  | `"port" int => "8080";`                        |
| `slist`  | A list of strings           | `"pkgs" slist => { "nginx", "curl" };`         |
| `data`   | A structured data container | `"conf" data => parsejson('{"key":"value"}');` |

## Classes (conditions)

Classes are how CFEngine represents conditions.
A class is either **defined** or **not defined** -- there is no "false", only defined or undefined.
Many classes are built-in (called **hard classes**), such as `linux`, `ubuntu_22`, `Monday`, `Hr14`.

### Defining classes

```cf3
bundle agent __main__
{
  classes:
    "webserver"
      expression => fileexists("/etc/nginx/nginx.conf");

  reports:
    webserver::
      "This machine is a web server.";
    !webserver::
      "This machine is NOT a web server.";
}
```

Key points:

- `expression` evaluates a class expression or function call.
- The class `webserver` is defined if the file exists.

### Combining classes

```cf3
bundle agent __main__
{
  classes:
    "dev_environment"
      expression => "!production.!staging";
    "needs_update"
      or => { "Monday", "Thursday" };

  reports:
    dev_environment::
      "Running in development.";
    needs_update::
      "Today is an update day.";
}
```

- `.` (or `&`) means AND, `|` means OR, `!` means NOT.
- You can also use `and`, `or`, and `not` attributes for readability.

## Class guards

Class guards are lines ending with `::` that restrict which promises are evaluated.
They apply to all promises below them (within the same promise type) until the next guard.

```cf3
bundle agent __main__
{
  reports:
    linux::
      "This is a Linux system.";
    windows::
      "This is a Windows system.";
    any::
      "This prints on every system.";
}
```

- `any::` is a built-in class that is always defined.
- Guards cannot contain function calls. For dynamic conditions, use the `if` attribute instead.

## The `if` and `unless` attributes

For per-promise conditions, especially those involving function calls, use `if` or `unless`:

```cf3
bundle agent __main__
{
  reports:
    "User root exists"
      if => userexists("root");

    "No such user: nobody"
      unless => userexists("nobody");
}
```

## Files promises

Files promises manage file creation, content, permissions, and more.

### Creating a file with content

```cf3
bundle agent __main__
{
  files:
    "/tmp/hello"
      content => "Hello, CFEngine!";
}
```

CFEngine checks the current state first. If `/tmp/hello` already has the correct content, no changes are made.

### Creating a file and setting permissions

```cf3
bundle agent __main__
{
  files:
    "/tmp/config.ini"
      create => "true",
      perms  => mog("644", "root", "root");
}
```

- `create => "true"` ensures the file exists.
- `mog()` is a standard library body that sets mode, owner, and group.

### Ensuring a line is present in a file

```cf3
bundle agent __main__
{
  files:
    "/etc/motd"
      create    => "true",
      edit_line => insert_lines("Welcome to this server!");
}
```

- `edit_line` references a bundle that modifies file content.
- `insert_lines()` is from the standard library and adds the line only if it is not already present.

## Commands promises

Commands promises execute external programs.
The promiser must be the **full path** to the executable.

```cf3
bundle agent __main__
{
  commands:
    "/usr/bin/systemctl restart nginx"
      if => fileexists("/etc/nginx/nginx.conf");
}
```

### Separating command and arguments

```cf3
bundle agent __main__
{
  vars:
    "service"
      string => "nginx";

  commands:
    "/usr/bin/systemctl"
      args => "reload $(service)";
}
```

## Reports promises

Reports promises print messages to standard output (prefixed with `R:`).
They are useful for debugging and auditing.

```cf3
bundle agent __main__
{
  vars:
    "os"
      string => "$(sys.os)";

  reports:
    "Running on: $(os)";
    "Hostname: $(sys.fqhost)";
    "Today is $(sys.date)";
}
```

### Built-in variables

CFEngine provides many built-in variables under `sys.*`, `const.*`, and others.
For example, `$(sys.fqhost)` is the fully qualified hostname and `$(sys.date)` is the current date.

## Methods promises

Methods promises call other bundles.
This is how you organize policy into reusable, composable pieces.

```cf3
bundle agent __main__
{
  methods:
    "Setup NTP"
      usebundle => configure_ntp;
    "Setup SSH"
      usebundle => configure_ssh;
}

bundle agent configure_ntp
{
  files:
    "/etc/ntp.conf"
      content => "server pool.ntp.org";
}

bundle agent configure_ssh
{
  files:
    "/etc/ssh/sshd_config"
      content => "PermitRootLogin no";
}
```

### Passing parameters to bundles

```cf3
bundle agent __main__
{
  vars:
    "users"
      slist => { "alice", "bob" };

  methods:
    "Create user $(users)"
      usebundle => ensure_user("$(users)");
}

bundle agent ensure_user(name)
{
  commands:
    "/usr/sbin/useradd $(name)"
      if => not(userexists("$(name)"));

  reports:
    "Ensured user: $(name)";
}
```

Because `users` is a list, CFEngine automatically iterates and calls `ensure_user` once per item.

## Function calls

Functions are called on the right-hand side of promise attributes.
They can return strings, lists, data containers, or classes.

```cf3
bundle agent __main__
{
  vars:
    "file_content"
      string => readfile("/etc/hostname");
    "random_num"
      int => randomint(1, 100);
    "users"
      slist => splitstring("alice,bob,charlie", ",", 10);

  classes:
    "has_nginx"
      expression => fileexists("/usr/sbin/nginx");

  reports:
    "Hostname from file: $(file_content)";
    "Random number: $(random_num)";
    "User: $(users)";
    has_nginx::
      "nginx is installed.";
}
```

Common functions:

| Function            | Description                                     |
| ------------------- | ----------------------------------------------- |
| `fileexists()`      | Check if a file exists                          |
| `readfile()`        | Read file contents into a string                |
| `execresult()`      | Run a shell command and capture output          |
| `returnszero()`     | Check if a command exits with code 0            |
| `userexists()`      | Check if a system user exists                   |
| `randomint()`       | Generate a random integer                       |
| `splitstring()`     | Split a string into a list                      |
| `parsejson()`       | Parse a JSON string into a data container       |
| `canonify()`        | Convert a string to a valid class/variable name |
| `string_mustache()` | Render a Mustache template with data            |

## Variable expansion

Variable expansion uses `$(...)` for scalar values and `@(...)` for list values:

```cf3
bundle agent __main__
{
  vars:
    "pkg"
      string => "nginx";
    "pkgs"
      slist => { "curl", "wget" };

  reports:
    # Scalar expansion
    "Install package: $(pkg)";

    # List expansion (iterates automatically)
    "Also install: $(pkgs)";
}
```

### Referencing variables from other bundles

Variables from other bundles are accessed using `$(bundle_name.variable_name)`:

```cf3
bundle common settings
{
  vars:
    "domain"
      string => "example.com";
}

bundle agent __main__
{
  reports:
    "Domain is $(settings.domain)";
}
```

## Putting it all together

Here is a more complete example combining multiple concepts:

```cf3
bundle agent __main__
{
  vars:
    "packages"
      slist => { "nginx", "curl", "vim" };
    "config_dir"
      string => "/etc/myapp";

  classes:
    "config_exists"
      expression => fileexists("$(config_dir)/app.conf");

  methods:
    "Install packages"
      usebundle => install_packages(@(packages));
    "Configure app"
      usebundle => configure_app($(config_dir));

  reports:
    config_exists::
      "Application config already exists.";
    !config_exists::
      "Application config will be created.";
}

bundle agent install_packages(pkgs)
{
  packages:
    "$(pkgs)"
      policy => "present",
      package_module => apt_get;
}

bundle agent configure_app(dir)
{
  files:
    "$(dir)/."
      create => "true";

    "$(dir)/app.conf"
      content => "# App configuration
server_port=8080
log_level=info";
}
```

## Summary of key concepts

| Concept                | Description                                                       |
| ---------------------- | ----------------------------------------------------------------- |
| **Bundle**             | A named collection of promises, the basic organizational unit     |
| **Promise type**       | Category of promise within a bundle (vars, files, commands, etc.) |
| **Promiser**           | The left-hand side of a promise -- what is being promised about   |
| **Attributes**         | Key-value settings on the right-hand side of a promise            |
| **Classes**            | Boolean conditions that control which promises are evaluated      |
| **Class guards**       | Lines ending with `::` that restrict promises to certain contexts |
| **Variable expansion** | `$(var)` expands a scalar, `@(var)` expands a list                |
| **Functions**          | Built-in operations called in attribute values                    |
| **Methods**            | Promises that invoke other bundles for modularity                 |
| **Bodies**             | Reusable groups of attributes (like functions for configuration)  |

## Next steps

- Explore the [Promise types reference](content/reference/promise-types/) for all available promise types and their attributes.
- Browse [Functions](content/reference/functions/) for the full list of built-in functions.
- Check out [CFEngine Build](https://build.cfengine.com) for ready-to-use modules.
- See the [Getting started tutorial](content/getting-started/) for installation and guided setup.
