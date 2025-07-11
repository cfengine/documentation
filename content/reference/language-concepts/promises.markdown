---
layout: default
title: Promises
sorting: 30
---

One concept in CFEngine should stand out from the rest as being the most
important: promises. Everything else is just an abstraction that allows us to
declare promises and model the various actors in the system.

## Everything is a promise

Everything in CFEngine 3 can be interpreted as a promise. Promises can be made
about all kinds of different subjects, from file attributes, to the execution
of commands, to access control decisions and knowledge relationships. If you
are managing a system that serves web pages you may define a promise that port
80 needs to be open on a web server. This same web server may also define a
promise that a particular directory has a particular set of permissions and
the proper owner to serve web pages via Apache.

This simple but powerful idea allows a very practical uniformity in CFEngine
syntax.

### Promise types

The `promise_type` defines what kind of object is making the promise. The type
dictates how CFEngine interprets the promise body. These promise types are
straightforward: The `files` promise type deals with file permissions and file
content, and the `packages` promise type allows you to work with packaging
systems such as rpm and apt.

Some promise types are common to all CFEngine components, while others can
only be executed by one of them. `cf-serverd` cannot keep `packages` promises,
and `cf-agent` cannot keep `access` promises. See the
[Promise type reference][Promise types] for a comprehensive
list of promise types.

### The promiser

The promiser is an object affected by a promise, and this can be anything: a
file, a port on a network. It is the entity that is making a promise that a
certain fact will be true. These facts are listed in the form of
**attributes** and **values**. A file could promise that a permission
attribute has a particular value (i.e. 775 permission value) and that an owner
attribute has another value (i.e. "root").

When a promise is made in CFEngine it is made to another entity - a
**promisee**. A promisee is an optional part of a promise declaration. The
promisee can help provide insight into the system's configuration, and may
become relevant as your system grows in complexity.

The **classes** in a promise control the conditions that make the promise
valid. Examples are the operating system on which the policy is executed, or
the day of the week. More about that in the [classes and decision
making][classes and decisions] section.

Not all of these elements are necessary every time, but when you combine them
they enable a wide range of behavior.

### Promise example

```cf3
# Promise type
files:
    "/home/mark/tmp/test_plain" -> "system blue team",
        create  => "true",
        perms   => owner("@(usernames)"),
        comment => "Hello World";
```

In this example, the promise is about a file named `test_plain` in the
directory `/home/mark/tmp`, and the promise is made to some entity named
`system blue team`. The `create` attribute instructs CFEngine to create the
file if it doesn't exist. It has a list of owners that is defined by a
variable named "usernames" (see the documentation about
[Bodies][bodies] for more details on this last
expression).

The comment attribute in this example can be added to any promise. It has no
actual function other than to provide more information to the user in error
tracing and auditing.

This is a promise that will affect the state of a file on the filesystem. In
CFEngine you can do this without having to execute the `touch`, `chmod`, and
`chown` commands. CFEngine is declarative: you declare a contract (or a
promise) that you want CFEngine to keep and you leave the details up to the
tool.

### Promise locking

When a promise is validated (has an outcome of kept or repaired) it is locked
for [body agent control ifelapsed][cf-agent#ifelapsed] minutes (1 by default). Locks are based on a
hash of the promise (promiser, associated attributes, and context).

Promise locks can be useful for controlling frequency.

`access`, `classes`, `defaults`, `meta`, `roles` and `vars` type promises do not
participate in locking.

**See also:** [ifelapsed in body agent control][cf-agent#ifelapsed], [ifelapsed action body attribute][Promise types#ifelapsed]

### Promise attributes

Promise attributes have a type and a value. The type can be any of the
[datatypes][datatypes] that are allowed for variables, and in addition

* Boolean - allowed input values are
    * `"true"`/`"false"`
    * `"on"`/`"off"`
    * `"yes"`/`"no"`

* `irange[min, max]` and `rrange[min, max]` - a range of integer or real
  values, created via the [`irange()`][irange] and [`rrange()`][rrange]
  functions

* `clist` - a list of classes or class expressions. Note that these
   attributes can take both strings (which are evaluated as class expressions)
   and functions that return type `class`

* Menu option - one value from a list of values

* [`body` *type*][bodies] - a complex set of
  attributes expressed in a separate, reusable block

* [`bundle` *type*][bundles] - a separate bundle
  that is used as a sub-routine or a sub-set of promises

**Note:** The language does not specifically disallow the use of the same
attribute multiple times within a given promise. As a general rule the last
definition wins but the behavior is not clearly defined and this should be
avoided.

For example, the following promises use the same attribute multiple times.

```cf3
bundle agent bad_example
{
  classes:

    "myclass"
      expression => "cfengine",
      expression => "my_other_class";

  files:
    "/tmp/example"
      perms => m( 600 ),
      perms => owner( "root" ),
      perms => group( "root" );
}
```

### Implicit promises

Some promise types can have implicit behavior. For example, the following
promise simply prints out a log message "hello world".

```cf3
reports:
  "hello world";
```

The same promise could be implemented using the `commands` type, invoking the
echo command:

```cf3
commands:
  "/bin/echo hello world";
```

These two promises have default attributes for everything except the
_promiser_. Both promises simply cause CFEngine to print a message.
