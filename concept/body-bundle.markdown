## Defining Promises: Bodies and Bundles

CFEngine's promises are declarative, you tell CFEngine what promises
you want it to keep, and it keeps them.  This declarative approach has
some distinct advantages over automation based on a procedural (or
imperative) language - a language which requires you to spell out
every step in detail.  In the procedural approach to automation,
instead of leaving the details up to CFEngine you become responsible
for every last detail of a process.  With CFEngine you can clearly
specify the desired end-state of a system in the form of promises and
let CFEngine take care of the rest.

This specification is called a promise, and this chapter introduces
the promise syntax.  After reading this chapter you should understand
how to write a promise, what the components of a promise body are, and
how to bundle related promises together.

### Promises Bodies

Promises are the fundamental statements in CFEngine. They are the
"atoms" that make up an entire system based on a series of
comittments.  While the idea of a promise is very simple - a
committment or a guarantee to satisfy a condition - the definition of
a promise can grow complicated.  Complex promises are best understood
by breaking them down into independent components. This section
explores the structure of a promise declaration which includes the
following concepts and components:

* Promise - This is the object that formally makes a promise. It is always
    the affected object, since objects can only make promises about
    their own state or behavior in CFEngine. 

* Promise body - Contains the details and content of the promise. We use this word in the sense of 'body of a contract' or
    the 'body of a document'  (like <body>) tags in HTML, for example.

* Promisee (optional) - This is a possible stakeholder, someone who is interested in the
    outcome of the promise. It is used as documentation, and it is
    used in the commercial CFEngine product. 

Here is a very abstract definition of what a promise looks like:

    CFEngine_attribute_type => user_defined_value or template

#### Defining a Promise Body 

The CFEngine reserved word body is used to define parameterized
templates for bodies to hide the details of complex promise
specifications. For complex body lists, you must fill in a body
declaration as an `attachment' to the promise.  For example the
following promise uses a user defined promise body named "myexample":

    files:

        "/tmp/promiser"      # Promiser

        perms => myexample;  # The body is just one line, 
                         # but needs an attachment

The promiser in this example is a file "/tmp/promiser" and the promise
is that the "perms" attribute type is associated with a named,
user-defined promise body "myexample".  Next, let's take a look at
this "myexample" promise body.

The body of this "myexample" promise consists of configuration for the
file permissions, the file owners, and the file groups.  We can this
definition a "body attachment".  "myexample" is declared like this,
with a "type" that matches the left hand side "perms" of the
declaration in the promise:

    body perms myexample
    {
        mode => "644";
        owners => { "mark", "sarah", "angel" };
        groups => { "users", "sysadmins", "mythical_beasts" };
    }

Body attachments are required items. In this example, "myexample"
needed to be defined in a body attachment that was separate from the
definition of the promise.  This separation is essential to preserve
readability in a compex system.  Earlier versions of CFEngine allowed
for inline attach definitions, but this often led to deeply nested,
difficult to understand promise declarations.

The structure of a promise is the following.

    promiser
        LVALUE => RVALUE;
     
    body LVALUE RVALUE
    {
        LVALUE => RVALUE;
        LVALUE => RVALUE;
    }

Another way of looking at it is this:

    promiser
        CFEngine_word => user_defined_value

    body CFEngine_word user_defined_value
    {
        CFEngine_word => user_defined_value;
        CFEngine_word => user_defined_value;
    }

#### Implicit, Control Bodies

There are two types of promises: the promises you configure to manage
your own infrastructure, and implicit promises that configure the
basic operation of CFEngine.  Some of these implicit, hard-coded
promises are built-in to CFEngine and control the basic operation of
tools such as cf-agent and cf-serverd.

In these cases you don't define the promise using the syntax from the
previous section.  Instead we can influence the behavior of these
implicit promises by defining new promise bodies for these control
promises. Each agent, (CFEngine software component) has a special body
whose name is control, used for setting these parameters. For cf-agent
and cf-serverd the following promise bodies configure the
bundlesequence to execute on a cf-agent and the clients allowed to
connect to a cf-serverd:

    body agent control
    { 
        bundlesequence => { "test" };
    }

    body server control
    {
        allowconnects         => { "127.0.0.1" , "::1", @(def.acl) };
    }

### Promise Bundles

A bundle is a collection of related promises.  You organize processes
together into elements that can be thought of as "subroutines" in the
CFEngine promise language. The purpose of bundles is to allow you
greater flexibility to break down the contents of your policies and
give them logical names.  If you have a number of promises related to
configuring a web server or a file system you can name those bundles
"webserver" or "filesystem" respectively.

Bundles also allow you to re-use promise code by parameterizing it.
If you need to do the same thing over and over again with slight
variations, using a promise bundle is an easy way to avoid unnecessary
duplication in your promises.

Like bodies, bundles also have `types'. Bundles belong to the agent
that is used to keep the promises in the bundle. So cf-agent has
bundles declared as:

    bundle agent my_name
    {
    }

The cf-serverd program has bundles declared as:

    bundle server my_name
    {
    }

#### Promise Bundle Scope

Variables and classes defined inside bundles are not directly visible
outside those bundles. All variables in CFEngine are globally
accessible, however if you refer to a variable by ‘$(unqualified)’,
then it is assumed to belong to the current bundle. To access any
other (scalar) variable, you must qualify the name using the name of
the bundle in which it is defined: ‘$(bundle_name.qualified)’.

Some promise types, like var, classes may be made by any agent. These
are called common promises. Bundles of type common are special. They
may contain common promises. Classes defined in common bundles have
global scope.

### A Simple Syntax Pattern

The syntax of CFEngine follows a simple pattern in all cases and has a few simple rules:

* CFEngine built-in words, and identifiers of your choosing (the names
  of variables, bundles, body templates and classes) may only contain
  the usual alphanumeric and underscore characters (‘a-zA-Z0-9_’).

* All other `literal' data must be quoted.

Declarations of promise bundles in the form:

    bundle agent-type identifier
    {
        ...
    }

Declarations of promise body-parts in the form:

    body constraint_type template_identifier
    {
        ...
    }

matching and expanding on a reference inside a promise of the form ‘constraint_type => template_identifier’.

CFEngine uses many `constraint expressions' as part of the body of a
promise. These take the form: left-hand-side (cfengine word) ‘=>’
right-hand-side (user defined data). This can take several forms:

    cfengine_word => user_defined_template(parameters)
        user_defined_template
        builtin_function()
        "quoted literal scalar"
        { list }

In each of these cases, the right hand side is a user choice.

Once you have learned this pattern, it will make sense anywhere in the
program. The figure below illustrates this pattern. Some words are
reserved by CFEngine, and are used as types or categories for talking
about promises. Other words (in blue) are to be defined by you. Look
at the examples and try to identify these patterns yourself.

