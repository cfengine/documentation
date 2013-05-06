## CFEngine Concepts

One concept in CFEngine should stand out from the rest as being the most important: promises.   Everything else is just an abstraction that allows us to declare promises and model the various actors in the system, but if you wanted to summarize CFEngine concepts in a single sentence that sentence would be:

CFEngine is a platform for defining and delivering promises.

In this chapter, we're going to fill out this conceptual model to talk about promises, but also to talk about some of the terminology CFEngine uses to define how promises relate to the systems you are managing.  In this chapter, you'll start to see some of the syntax used to define promises including types and classes.

### Everything is a Promise

Everything in CFEngine 3 can be interpreted as a promise. Promises can be made about all kinds of different subjects, from file attributes, to the execution of commands, to access control decisions and knowledge relationships.   If you are managing a system that serves web pages you may define a promise that port 80 needs to be open on a web server.   This same web server may also define a promise that a particular directory has a particular set of permissions and the proper owner to serve web pages via Apache.  

This simple but powerful idea allows a very practical uniformity in CFEngine syntax. There is only one grammatical form for statements in the language that you need to know and promise definitions follow this general syntax:

    type:
     
    classes::
     
        "promiser" -> { "promisee1", "promisee2", ... }
     
            attribute_1 => value_1,
            attribute_2 => value_2,
            ...
            attribute_n => value_n;

There are many concepts in the previous code listing: type, class, promiser, promisee, attributes, and values.   This chapter will define all of these concepts individually, but let's focus on the promiser and the promisee.

#### Promise Concepts: Type, Class, Attribute, and Value

A +promiser+ is an object affected by a promise, and this can be anything: a file, a port on a network.   Some entity that is making a promise that a certain fact will be true.   These facts are listed in the form of +attributes+ and +values+.  A file could promise that a permission attribute has a particular value (i.e. 775 permission value) and that an owner attribute has another value (i.e. "root").

When a promise is made in CFEngine it is made to another entity - a +promisee+.  This concept guide doesn't dwell on the promisee, but in certain CFEngine administrative tools the promisee can help provide insight to CFEngine users.  For now all you need to know about a promisee is that it is an optional part of a promise declaration that may become relevant as your system grows in complexity.

The +type+ of the promise tells us what the promise is about: what kind of promise we are dealing with.   The type is a label that has meaning to a CFEngine administrator and which dictates how CFEngine interprets the promise body.

The +classes+ in a promise control the conditions that make the promise valid.   You'll see a listing of available classes later in this chapter, but you can have a class that makes a particular promise defition relevant to a particular operating system or any other context you can think of such as the day of the week. 

Not all of these elements are necessary every time, but when you combine them they enable a wide range of behavior.

#### Promise Example

Next, consider a real promise example .   This promise ensures that there is a file named "test_plain" in the directory "/home/mark/tmp".   It is making a promise to some entity named "system blue team", and the promise is that the file will have a list of owners that is defined by a variable named "usernames".  The create attribute instructs CFEngine to create the file if it doesn't exist.  The comment attribute in this example can be added to any promise.  It has no actual function other than to provide more information to the user in error tracing and auditing.

     # Promise type
     files:
     
         "/home/mark/tmp/test_plain" -> "system blue team",
     
             comment => "Hello World",
             perms   => owner("@(usernames)"),
             create  => "true";

You see several kinds of objects in this example. All literal strings (e.g. "true") in CFEngine 3 must be quoted. This provides absolute consistency and makes type-checking easy and error-correction powerful. All function-like objects (e.g. users("..")) are either built-in special functions or parameterized templates. Not everything in this previous example can be explained without diving into variable references and special functions, but you should be able to decipher what this promise it promising from the clear syntax of a promise.

The key point is that this is a promise that will affect the state of file on the filesystem.   In CFEngine you can do this without having to execute the +touch+, +chmod+, and +chown+ commands.  CFEngine is declarative, you are declaring a contract (or a promise) that you want CFEngine to keep and you are leaving the details up to the tool.

#### Implicit Promises

Promises often contain implicit behavior.   While we generally recommend promise writers be very explicit to make it easy to understand promise, there can be cases which call for simplicity.   For example, the following promise simply prints out a log message "hello world".   In this case, all that was needed was a +type+ "reports" and a string literal which is automatically interpreted as a log message.

     reports:
     
     "hello world";

The same promise could be implemented using the "commands" type in concert with the echo command:

     commands:
     
     "/bin/echo hello world";

The two previous promises have default attributes for everything except the `promiser' which isn't needed as both promises simply cause CFEngine to print a message.

#### Promise Types

There is one mystery yet to be explained: what is a type?  The types your seen so far, "commands", "reports", and "files", these are built-in promise types. Promise types generally belong to a particular component of CFEngine, as the components are designed to keep different kinds of promises. A few types, such as vars, classes and reports are common to all the different component bundles.   Here is a list of types available in CFEngine:

vars::
    A promise to be a variable, representing a value. 

classes::
    A promise to be a class representing a state of the system. 

reports::
    A promise to report a message.

These following promise types may be used only in agent bundles

commands::
    A promise to execute a command. 

databases::
    A promise to configure a database. 

files::
    A promise to configure a file, including its existence, attributes and contents. 

interfaces::
    A promise to configure a network interface. 

methods::
    A promise to take on a whole bundle of other promises. 

packages::
    A promise to install a package. 

storage::
    A promise to verify attached storage.

These promise types belong to other components:

access::
    A promise to grant or deny access to file objects in cf-serverd. 

measurements::
    A promise to measure or sample data from the system, for monitoring or reporting in cf-monitord (CFEngine Nova and above). 

roles::
    A promise to allow certain users to activate certain classes when executing cf-agent remotely, in cf-serverd. 

topics::
    A promise to associate knowledge with a name, and possibly other topics, in cf-know. 

occurrences::
    A promise to point or refer to a knowledge resource, in cf-know.

Some promise types are straightfoward.  The "files" promise type deals with file permissions and file content, and the "packages" promise type allows you to work with packaging systems such as rpm and apt.  Other promise types deal with defining variables and classes to be used in CFEngine and are beyond the scope of this concept guide.  For a full explanation of promise types, see the CFEngine reference manual.

#### Ready to Start?

If you are impatient to get started writing promises, now might be a good time to take a break from Concepts and try out your first promises in the http://cfengine.com/manuals/cf3-tutorial.html#First-promises[CFEngine tutorial].   You may be able to learn promises as you progress through the tutorial, but there are basic concepts such as classes, function, and variables which will in your understand.   If you are in a hurry, go read the Tutorial.  If you want a solid foundation for your use of CFEngine continue reading this concept guide.

### Making Decisions with Classes

When you write promises in CFEngine, you don't write a series of control statements and loops.  You don't write if/else statements CFEngine to control when and how a promise is fulfilled.   Instead you use +classes+ to apply promise bodies to particular environments depending on context.   +classes+ are simply variables, Boolean variables, which evaluate to true or false depending on context.

Let's make it more concrete than that with a few examples.  Consider one of the previous examples in this chapter that manipulated file permissions.   You could decide that this promise is only applicable to machines that are running Max OSX, or you could decide that you only want to implement this promise on the third day of every month.    Classes are simply facts that represent the current state or context of a system and they can be used for much more than just applying specific recipes to different operating systems.  For example, you can use CFEngine classes to increase capacity for a system during business hours and decrease capacity at night.

#### How Classes Work

How does it work?  How are classes made available to CFEngine promises?  CFEngine runs on every computer individually and each time it wakes up the underlying generic agent platform discovers and reads properties of the environment or context in which it runs. It turns these properties of the environment into classes.  This information is effectively cached and may be used to make decisions about configuration.

You can see all of the classes defined on a particular host by running the following command as a privileged user.

    host# cf-promises -v

Do this a few times over the course of a day and you will see that time-varying classes make up an important component of available classes as well as classes that describe the operating system and other attributes of your system.   

#### Hard Classes (Built-in Classes)

There are two categories of classes.  Hard classes which are discovered by CFEngine.   These are classes that describe your operating system, the time of day, the week of the year, etc.   Soft classes are user-defined classes which you can use to implement your own classifications.

The following is a sample of some of the Hard classes available to CFEngine administrators:

* Operating System Classes

** Operating System Architecture - ultrix, sun4, etc.

* Network Classes

** Unqualified Name of Host. CFEngine truncates it at the first dot. Note: www.sales.company.com and www.research.company.com have the same unqualified name – www.

** The IP address octets of any active interface (in the form
ipv4_192_0_0_1, ipv4_192_0_0, ipv4_192_0, ipv4_192).

** User-defined Group of Hosts

* Time Classes

** Day of the Week - Monday, Tuesday, Wednesday,...

** Hour of the Day in Current Time Zone - Hr00, Hr01,... Hr23.

** Hour of the Day in GMT - GMT_Hr00, GMT_Hr01, ...GMT_Hr23.

** Minutes of the Hour - Min00, Min17,... Min45.

** Five Minute Interval of the Hour - Min00_05, Min05_10,... Min55_00.

** Quarter of the Hour - Q1, Q2, Q3, Q4.

** Day of the Month - Day1, Day2,... Day31.

** Month - January, February,... December.

** Year - Yr1997, Yr2004.

** Period of the Day - Night,Morning,Afternoon,Evening (six hour
blocks starting at 00:00 hours).

[NOTE]
####################################################################=
Note that some of the classes are set only if a trusted link can be established with cfenvd, i.e. if both are running with privilege, and the /var/cfengine/state/env_data file is secure. More information about classes can be found in connection with allclasses.
####################################################################=

#### Soft Classes (User-defined Classes)

User-defined or soft classes are defined in bundles. Bundles of type common yield classes that are global in scope.  Classes defined in all other bundle types are local in scope. 

Soft classes are evaluated when the bundle is evaluated. They can be based on test functions or simply
from other classes.  The following example defines a few soft classes local to the myclasses bundle.

* The "solinux" soft class is defined as a combination of the "linux" or the "solaris" hard classes.   This class will evaluate to true if the operating system family is either of these values.

* The "atl_class" soft class is defined as a combination of "linux", "solaris", or the presence of a file named /etc/fstab.   If one of the two hard classes ("linux" or "solaris") evaluate to true or if there is a file named "/etc/fstab" the "alt_class" class will also evaluate to true.

* The "oth_class" soft class is defined as the combination of two fileexists functions - "/etc/shadow" and "/etc/passwd".  If both of these files are present the "oth_class" class evaluates to true.

    bundle agent myclasses
    {
    classes:

    "solinus" expression => "linux||solaris";

    "alt_class" or => { "linux", "solaris", fileexists("/etc/fstab") };

    "oth_class" and => { fileexists("/etc/shadow"), fileexists("/etc/passwd") };

    reports:

    alt_class::

    # This will only report "Boo!" on linux, solaris, or any system
    # on which the file /etc/fstab exists

    "Boo!";
    }

There are a few ways to define a class.  The first form shown for the "solinus" express uses a syntax that combines classes using the "||" or "&&" operators.  This convenient form is useful when you are basing a soft class on a combination of several hard classes.

The list form used for "alt_class" and "oth_class" is used when you need to combine hard classes and functions.  In these two sample classes, the fileexists functions are combined with hard classes "linux" and "solaris" using either and or or combinations.   In an or combination only one of the classes or functions needs to evaluate as true, and in an and combination all of the classes or functions included need to evaluate as true.

#### Combining Classes Together

The previous example combined a series of classes using boolean operators.   Classes may be combined with the operators listed here in order from highest to lowest precedence:

'‘()'::
    The parenthesis group operator. 

'‘!’::
    The NOT operator. 

'‘.’::
    The AND operator. 

'‘&’::
    The AND operator (alternative). 

'‘|’::
    The OR operator. 

'‘||’::
    The OR operator (alternative).

These operators can be combined to form complex expressions.  For example, the following expression would be only true on Mondays or Wednesdays from 2:00pm to 2:59pm on Windows XP systems:

    (Monday|Wednesday).Hr14.WinXP::

#### Class Scopes: A More Complex Example

In a more advanced example, let's consider how common classes with a global scope can be combined with bundle-level classes with a local scope. Promises in bundles of type ‘common’ are global in scope – all other promises are local to the scope of their bundle.

In this example, there are three bundles.  One common bundle named "global" with a global scope.  Classes defined in common bundles can be used throughout your CFEngine configuration.   Two other bundles define classes which are local to those bundles.   Three classes are defined:

* "zero" from the common bundle with a global scope
* "one" from the local_one bundle with a local scope
* "two" from the local_two bundle with a local scope

In the body of the local_two bundle we define a report "Success" which evaluates if "zero.!one.two" is true.   Withing the local_two scope this evaluates to true because the "one" class is not defined.

    body common control
    {   
        bundlesequence => { "global","local_one", "local_two" };
    }

    #################################

    bundle common global
    {
        classes:
            # The soft class "zero" is always satisfied, 
            # and is global in scope
            "zero" expression => "any";
    }

    #################################

    bundle agent local_one
    {
        classes:
            # The soft class "one" is always satisfied, 
            # and is local in scope to local_one
            "one" expression => "any";
    }

    #################################

    bundle agent local_two
    {
        classes:
            # The soft class "two" is always satisfied, 
            # and is local in scope to ls_2
            "two" expression => "any";

        reports:
            zero.!one.two::
                # This report will be generated
                "Success";
    }

### Controlling Frequency in CFEngine

When checking a series of expensive functions and verifying complex promises, you may want to make sure that CFEngine is not checking too frequently. CFEngine incorporates a series of locks which prevent it from checking promises too often, and which prevent it from spending too long trying to check promises it has recently verified. 

This locking mechanism works in such a way that you can start several CFEngine components simultaneously without having to worry about conflicts between these processes. You can control two things about each kind of action in CFEngine:

'‘ifelapsed'::
    The minimum time (in minutes) which should have passed since the last time that promise was verified. It will not be executed again until this amount of  time has elapsed. (Default time is 1 minute.) 

'‘expireafter'::
    The maximum amount (in minutes) of time cf-agent should wait for an old instantiation to finish before killing it and starting again.  You can think about expireafter as a timeout to use when a promise verification may involve an operation that could wait indefinitely. (Default time is 120  minutes.)

You can set these values either globally (for all actions) or for each action separately. If you set global and local values, the local values override the global ones. All times are written in units of minutes. The following global setting is defined in "body agent control".  This setting tells CFEngine not to verify promises until 60 minutes have elapsed.  This would ensure that the global frequency for all promise verification is one hour:

    body agent control
    {
        ifelapsed => "60";	# one hour
    }

This global setting of one hour could be changed for a specific promise body by setting ifelapsed in the promise body.   Here we see a promise which overrides the global 60 minute time period and defines a promise with a frequency of 90 minutes.

    body action example
    {
        ifelapsed => "90";	# 1.5 hours
    }

These locks do not prevent the whole of cf-agent from running, only atomic promise checks. Several different processes (or atoms) can be run concurrently by different cf-agent instnaces. The locks ensure that atoms will never be started by two cf-agents at the same time, or too soon after a verification, causing contention and wasting CPU cycles.       
   
### Datatypes in CFEngine 3

CFEngine variables have two high-level types: scalars and lists. 

* A scalar is a single value, 
* a list is a collection of scalars. 

Each scalar may have one of three types: string, int or real.  Typing is dynamic, so these are interchangeable in many instances with a few exceptions, while CFEngine will try its best to coerce string values into int and real types, if it cannot it will report an error.    String scalars are sequences of characters, integers are whole numbers, and reals are float pointing numbers.  While CFEngine typing is mostly dynamic, arguments to special functions check the defined argument type for consistency. 

Integer constants may use suffixes to represent large numbers.  The following suffixes can be used to create integer values for common powers of 1000.

* 'k' = value times 1000.
* 'm' = value times 1000^2
* 'g' = value times 1000^3

Since computing systems such as storage and memory are based on binary values, CFEngine also provide the following uppercase suffixes to create integer values for common powers of 1024.

* 'K' = value times 1024.
* 'M' = value times 1024^2
* 'G' = value times 1024^3

There is a special suffix which is used to denote percentages.

* '%' meaning percent, used in limited contexts

Lastly, there is a reserved value which can be used to specific a parameter as having no limit at all.

* 'inf' = a constant representing an unlimited value.

### Variables

Just like classes are defined as promises.  Variables (or "variable definitions") are also promises.  Variables can be defined in any promise bundle. CFEngine recognizes two variable object types: scalars and lists (lists contain 0 or more objects), as well as three data-types (string, integer and real).

#### Scalar Variable Expansion

Scalar variables hold a single value.  Here are a series of variable definitions which set a string, an int, and a real variable.  Notice that they are defined in a bundle that has the name "name".  This bundle name can be used as a context when using variables outside of the bundle they are defined in.

    bundle <type> name
    {
        vars:
            "my_scalar" string => "String contents...";
            "my_int" int    => "1234";
            "my_real" real   => "567.89";
    }

In this previous example, the ‘<type>’ indicates that any kind of bundle applies here. 

* Scalar variables are referenced by ‘$(my_scalar)’ (or ‘${my_scalar}’) and they represent a single value at a time.

* Scalars that are written without a context, e.g. ‘$(myvar)’ are local to the current bundle.

* Scalars are globally available everywhere provided one uses the context to reference

In the previous example, a variable defined in the "name" bundle could be reference from outside this bundle by using the syntax '$(name.my_scalar)'.

#### List Substitution and Expansion

List variables hold several values. The are declared as follows:

    bundle <type> name
    {
        vars:
            "my_slist" slist => { "list", "of", "strings" };
            "my_ilist" ilist => { "1234", "5678" };
            "my_rlist" rlist => { "567.89" };
    }

An entire list is referenced with the symbol ‘@’.  Using the scalar reference to a list variable, will cause CFEngine to iterate over the values in the list.  For example, the following variable definition references a list named "shortlist":

    vars:
        "shortlist" slist => { "you", "me" };
        "longlist" slist => { @(shortlist), "plus", "plus" };

The declaration order does not matter – CFEngine will execute the promise to assign the variable ‘@(shortlist)’ before the promise to assign the variable ‘@(longlist)’.  It understand the dependencies between these variable definition promises and will order them accordingly.

To summarize:

* Scalar references to local list variables imply iteration, e.g. suppose we have local list variable ‘@(list)’, then the scalar ‘$(list)’ implies an iteration over every value of the list.

* Lists can be passed in their entirety in any context where a list is expected as ‘@(list)’., e.g.

.Optional Title
[NOTE]
####################################################################=
Using the @ symbol in a string scalar will not result in list substition.  For example, the string value "My list is @(mylist)" will not expand this reference.
####################################################################=

#### Mapping Global and Local Lists

Only local lists can be expanded directly. Thus ‘$(list)’ can be expanded but not ‘$(context.list)’. Global list references have to be mapped into a local context if you want to use them for iteration.  Instead of doing this in some arbitrary way, with possibility of name collisions, CFEngine requires you to make this mapping explicit. There are two possible approaches.

The first uses parameterization to map a global list into a local context.  In the following example, there is a bundle named hardening which takes a list argument.  This list argument is defined in the context "va" and is passed to the hardening bundle via an argument listed in the bundlesequence.

As you can see, the reports section reference both the list passed in as an argument "x" and a local list variable defined in "other".

    body common control
    {
      bundlesequence => { hardening(@(va.tmpdirs)) };
    }

    bundle common va
    {
        vars:
            "tmpdirs"  slist => { "/tmp", "/var/tmp", "/usr/tmp"  };
    }

    bundle agent hardening(x)
    {
        classes:

            "ok" expression => "any";

        vars:

            "other"    slist => { "/tmp", "/var/tmp" };

        reports:

            ok::

                "Do $(x)";
                "Other: $(other)";
    }

This alternative is to map the global reference "va.tmpdirs" within the hardening bundle.  In this next example, the hardening bundle does not take an argument.   What it does is convert the the "va.tmpdirs" list into a local list variable "x" directly.

    body common control
    {
        bundlesequence => { hardening };
    }

    bundle common va
    {
        vars:
            "tmpdirs"  slist => { "/tmp", "/var/tmp", "/usr/tmp"  };
    }

    bundle agent hardening
    {
        classes:
            "ok" expression => "any";

        vars:
            "other"    slist => { "/tmp", "/var/tmp" };
            "x"        slist => { @(va.tmpdirs) };

        reports:
            ok::
                "Do $(x)";
                "Other: $(other)";
    }

#### A List Variable with Nothing (cf_null)

As of CFEngine core version 3.1.0, the value ‘cf_null’ may be used as a NULL value within lists. This value is ignored in list variable expansion, and can be used as a placeholder.

    vars:

      "empty_list" slist => { "cf_null" };

#### Associative Arrays in CFEngine 3

Associative Array variables are written with ‘[’ and ‘]’ brackets.  The following example defines three values in an associative array under the keys "cf-monitord", "cf-serverd", and "cf-execd".  These keys are associated with values, and are sequently printed with the echo command.

    bundle agent example

    {
        vars:

            "component" slist => { "cf-monitord", "cf-serverd", "cf-execd" };

            "array[cf-monitord]" string => "The monitor";
            "array[cf-serverd]" string => "The server";
            "array[cf-execd]" string => "The executor, not executioner";

        commands:

            "/bin/echo $(component) is"

                args => "$(array[$(component)])";

    }

Arrays are associative and may be of type scalar or list. Enumerated arrays are simply treated as a special case of associative arrays, since there are no numerical loops in CFEngine. Special functions exist to extract lists of keys from array variables for iteration purposes.

Here is an example of using a special function getindices() which extracts all of the keys from an associative array.  If this series of promises were executed it would print out two messages, one for each key.

    bundle agent array
    {
        vars:

            "v[index_1]" string => "value_1";
            "v[index_2]" string => "value_2";

            "parameter_name" slist => getindices("v");
        
        reports:

            Yr2013::

                "Found index: $(parameter_name)";

    }

### Loops

If you are looking for loops in CFEngine then we need to reprogram you a little, as you are thinking like a programmer! 

There are no loops.  There is no imperative, procedural language involved in CFEngine promises. CFEngine is not a programming language that is meant to give you low level control, but rather a set of declarations that embody processes.  Loops are executed implicitly in CFEngine, but there is no visible mechanism for it – because that would steal attention from the intention of the promises. The way to express them is through lists.

Loops are really a way to iterate a variable over a list. Try the following.

    body common control
    {
        bundlesequence  => { "example" };
    }

    bundle agent example
    {
        vars:
            "component" slist => { "cf-monitord", "cf-serverd", "cf-execd" };

            "array[cf-monitord]" string => "The monitor";
            "array[cf-serverd]" string => "The server";
            "array[cf-execd]" string => "The executor, not executionist";

        reports:
            cfengine_3::
                "$(component) is $(array[$(component)])";
    }

The output looks something like this:
 
     /usr/local/sbin/cf-agent -f ./unit_loops.cf -K
     
     cf-monitord is The monitor
     cf-serverd is The server
     cf-execd is The executor, not executionist

You see from this that, if we refer to a list variable using the scalar reference operator ‘$()’, CFEngine interprets this to mean “please iterate over all values of the list”. Thus, we have effectively a `foreach' loop, without the attendant syntax.
