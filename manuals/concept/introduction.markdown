## Introduction


### Managing Environments Seamlessly

CFEngine was designed to enable scalable configuration management in
any kind of environment with an emphasis on supporting larger systems
with partial of unreliable connectivity. While almost every other
system for configuration management assumes a reliable network
connection to enable top-down authority of central servers. These
systems tend to fail in the following environments:

- Systems with partial or unreliable connectivity (e.g. mobile
    phones, airplanes, a submarine).

- Low Bandwidth Systems (e.g. a satellite or space probe).

- Low Power Systems (e.g. ad hoc sensors or kitchen appliances).

CFEngine doesn't depend on or assume the presence of reliable
infrastructure. It works opportunistically in any environment, using
the fewest possible resources, and it has a limited set of software
dependencies. It can run anywhere, and this lean approach to
CFEngine's architecture makes it possible to support both traditional
server-based approaches to configuration as well as more novel
platforms for configuration including embedded and mobile systems.

At this point, you might be wondering if CFEngine makes sense for your
requirements. After all, not everyone is managing on a sensor network,
submarine, or space probe, right? Well, not quite, even the best
networks can have reliability issues, and as systems move to the cloud
and rely more on networks and systems not under your direct control
designing for efficiency and disconnection can yield benefits.

CFEngine's design allows you to create fault-tolerant, available systems
which are independent of external requirements. CFEngine works in all
the places you think it should, and all the new places you haven't even
thought of yet.

### Managing Expectations with Promises

One of the hardest things in management is to make everyone aware of
their roles and tasks, and to be able to rely on others to do the same.
Trust is an economic time-saver. If you can't trust you have to verify
everything, and that is expensive.

When you make a promise to someone or when someone makes a promise to
you, it is an effort to improve trust. You are telling someone, "trust
me to deliver this report to you by tomorrow." A promise is the
documentation of an intention to act or behave in some manner, and
CFEngine is based not on top-down, authoritative directions but on a
series of promised that each client is responsible for delivering on.

CFEngine works on a simple notion of promises. Everything in CFEngine
can be thought of as a promise to be kept by different resources in the
system. In a system that delivers a web site with Apache httpd, an
imprtant promise may be to make sure that httpd is installed, running,
and accessible on port 80, and in a system which needs to satisfy
mid-day traffic on a busy web site a promise may be to ensure that there
are 20 application servers running during normal business hours.

This promises are not top-down directives for a central authority to act
upon, they are the rules which clients are responsible for implementing.
Try running a large organization on top-down authority alone. Try to
managing a group of people without empowering and tristing them to make
independent decisions. In CFEngine, we've implemented a system that
emphasizes the promise a client makes to the overall CFEngine network,
and we can create large systems of scale because we don't create a bulky
centralized authority. Something we consider a single point-of-failure
both when managing machines and people.

Combining promises with patterns to describe where and when promises
should apply is what CFEngine is all about.

### The Importance of Automation

Users are good at making decisions and awful at reliable implementation.
Machines are pitiful at making decisions and very good at reliable
implementation. It makes sense to let each side do the job that they are
good at. With CFEngine, an emphasis is placed not on describing the
intricate process for completing each task. Instead, users make
decisions and write promises for machines to implement and satisfy.

A CFEngine user will declare a promise in CFEngine and a CFEngine client
will then translate this promise into a series of actions to implement.
For the most part, CFEngine clients understand how to deliver on
promises, and they don't need to be given explicit instructions for
completing tasks. If it your job to come up with a suitable promise, to
make decisions about the systems you are managing, and it if the
client's job to automate and deliver a promise.

This separation of concerns is often violated in systems that require
users to write explict instructions for even the simplest tasks. If the
client isn't given the power to make decisions about how to implement
promises, then you really haven't automated anything. If you can't trust
the "self-discipline" of individual nodes to deliver on simple promise,
then, as a user, you are really the one responsible for writing and
debugging long procedural automation routines.

This user-centric focus on automation often results in configuration
management systems which are full of ad-hoc, one-off implementations of
important process. These ad-hoc systems are often full of mystery. When
a system is based on ad-hoc, user-driven configuration:

- Others have no idea how a system has been assembled and how it is being managed.

- There is no record of changes or intentions. The only way to understand a complex, ad-hoc system is to walk through the code line by line.

- Systems should be considered damaged, they are figuratively "scarred" from the ad-hoc intervention of a user.

People opposed to automation often say that it dehumanizes their work.
In fact the opposite is true: forcing humans to do the work of machines,
in repetitive and reliable ways is what dehumanizes people. The only way
to make progress with a bad habit is to recognize it as one and be
willing to abandon the habit.

### What is CFEngine?

At its code, CFEngine is a simple framework based on promises which
supplies a rich standard library of tools to implement and manage very
large systems. The following diagram captures the scope of CFEngine.

![](fig/introduction-cfdude.png)

For many users, CFEngine is simply a configuration tool – i.e. software
for deploying and patching systems according to a policy. Policy is
described using promises. Every statement in CFEngine 3 is a promise to
be kept at some time or location. More than this, however, CFEngine is
not like otherautomation tools that \`roll out' an image of some
software once and hope for the best. Every promise that you make in
CFEngine is continuously verified and maintained. It is not a one-off
operation, but a process that can repairing itself should anything
deviate from the policy.

That clearly places CFEngine in the realm of automation, which often
begs the question: so it's just another scripting language? Certainly,
CFEngine contains a powerful scripting language, but it is not like any
other. CFEngine doesn't use a scripting language like Perl, Python or
Ruby for a reason as these languages often complicate systems and
encourage users to write long procedures instead of declarative
promises. CFEngine language is a language of promises, in which you
express very high-level intentions about a system. CFEngine then takes
the promises and compiles them into real-world action.

### Why does Knowledge Matter?

Above all, CFEngine promotes a human understanding of complex processes.
Its promises are easily documentable using comments that the system
remembers and reminds us about in error reporting. It hides irrelevant
and transitory details of implementation so that the intentions behind
the promises are highlighted for all to see. This means that the
knowledge of your organization can be encoded into a terse,
easy-to-understand CFEngine language based on promises.

It is this human understanding of large systems that often makes the
difference between a sustainable automation effort, and an effort that
fails to gain traction:

1.  Technical descriptions are hard to remember. You might understand
    your configuration decisions when you are writing them, but a few
    months later when something goes wrong, you will probably have
    forgotten what you were thinking. That costs you time and effort to
    diagnose.

2.  Organizations are fragile to the loss of those individuals who code
    policy. If they leave, often there is no one left who can understand
    or fix the system. Only with proper documentation is it possible to
    immunize against loss.


