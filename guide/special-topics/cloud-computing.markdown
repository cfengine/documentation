---
layout: default
title: Cloud Computing
published: true
sorting: 80
tags: [overviews, special topics, guide]
---

# What is Cloud Computing?

Cloud Computing refers to the commoditization of computing, i.e. a world in
which computers may be borrowed on demand from a resource pool, like renting a
car or loaning a book from the library. The term `Cloud' comes from a model of
the Internet, where the precise details of how everything fits together are
fuzzy. In a strongly networked environment, it might matter less where objects
are physically located.

Commoditization of computers is an important strategy for business because it
has the potential to eliminate a lot of the investment overhead for equipment
during times of rapid change, as well as to recycle no-longer needed resources
and save on redundant investment. You may think of Cloud Computing as
`Recycle-able Computing' – a world in which you can use something for a short
time and then discard it, without fear of waste.

# Is Cloud Computing for everything and everyone?

Cloud Computing does for computers what the database did for information.
Instead of having to keep reams of paper physically on site, databases allowed
us to virtualize the information and care less about where the data were stored.
Today we can call up a resource easily and cheaply from a database, and have
someone else manage the service for us. Cloud computing allows us to dial up a
new computer, like a book from the library, and then return it to the pool for
others to use when we are done. It frees us from thinking about the specific
location of the host, and we can appoint someone to manage this abstraction for
us.

Of course, this has negative aspects too. In a security environment, you do
indeed want to know exactly where your resources are. If you are storing
diamonds, you want a bank not a library, and you want to know exactly where the
physical objects are. The same is true for valuable data and computers.

Cloud Computing might be popular in the contemporary press, but it should be
seen in clear terms as one strategy of several for managing resources
efficiently. Some people still buy books, cars and dig wells, while others loan
books, rent cars and get water from the water authority. Different economic
models have different applications.

# How does CFEngine enable Cloud Computing?

CFEngine has technology that can quickly bring machines, either real or virtual,
from an uninitiated state to a fully working and customized state in seconds or
minutes, without any human intervention. It can thus turn a generic resource
into a specialized managed service on demand. CFEngine makes it extremely cheap
to rebuild systems from scratch. This is exactly what a vibrant recycling regime
needs to work efficiently.

# Permanent infra-structure with vibrant change

Not all your computers should be disposable. Certain key infrastructure items
like DNS servers, directory servers, databases, etc are part of a permanent
infrastructure. What you need there is unwavering stability, not agility and
impermanence.

CFEngine's lightweight repair capabilities are not only suitable for building
machines quickly, but also for maintaining their state over time. It only pays
to `rent services' (either from yourself or from a third party cloud provider)
if you use the service infrequently, or your needs are constantly changing. The
lack of permanence of cloud services can itself become an overhead if what you
really need is constancy and security.

The overhead of investment in physical infrastructure is cheap if that one term
investment will last you for a long time, unchanged. For that reason, cloud
services will never solve everyone's needs all the time. It is merely one
product of choice.

# How does Cloud relate to virtualization?

Virtualization is the tool that makes Cloud Computing practical. Every time a
physical machine needs to be deployed or retired, it requires the physical
presence of a human. To deploy or recycle a physical machine, somehow usually
has to touch the box.

To deploy and tear down a virtual machine, however, no one needs to touch
anything literally. Machines can be installed, moved and retired on command,
using the physical computers as the host for a purely software process.
Virtualization turns computer deployment into a software application.

CFEngine can help to manage the deployment of virtual machines, by working on
the physical host directly. It can also run on every virtual machine to manage
them in a seamless process in which no one needs to think about what kind of
machine software is running on. CFEngine can bring stability to the hosts or the
virtual guests, or it can keep virtual machines running without the need to
reboot[^1].

# Isn't virtualization inefficient?

Virtualized computers run as software simulations, adding an extra layer of
overhead. Using virtual machines is thus not as fast or processor-efficient as
using real machines, however the processing overhead is written off in different
ways.

About 70-80% of the electrical power used by a computer is wasted just by
turning it on. Only the remaining 20% go to solving real problems. However, most
computers are very under-utilized (2-5%), so that many more machines than
necessary are switched on at any one moment, compounding the cost of merely
being switched on with an additional cost of cooling. This expense costs
datacentres money every day. By squeezing 5-10 virtual machines into a single
physical host container, one has a net saving of electrical power and man-power
and often indistinguishable performance.

Virtualization is a form of packaging, which enables service providers to
separate services more easily with a `Chinese Wall' barrier. This is useful when
dealing with services belonging to different companies or different users on the
same physical host. The packaging aspect of virtual machines is therefore a form
of `information management'.

# Challenges for Cloud Computing

Dealing with scale, rapid change and impermanence could quickly lead to a
processing overhead for humans, i.e. in the management of the cloud computers.
In order to cope, some models force an oversimplification onto the user, forcing
them to make do with second best (a `cheap rental').

However, the requirements of computing are getting more complicated, not less.
Even as this new economic management of resources comes into focus, companies
are having to deal with increasing legislation about privacy, security,
compliance with audits, and more. CFEngine addresses this challenge by
integrating transparency of process and business goals into its scalable
approach to continuous maintenance.

The approach used by CFEngine is to:


 * Help to bring comprehension to the scope of the problem (Knowledge Management
   and Model-based Desired State Computing).

 * Help to implement change quickly and cheaply (through Lightweight
   Automation).

 * Help to bring measurable assurance about the state of compliance with policy
   (continuous maintenance).

CFEngine's model promise-based computing provides both a language of assurance
for keeping promises, and a measuring stick against which compliance can be
measured. It is not necessary to make ad hoc judgements; every statement about
the system can be documented and woven into a narrative about the system that
can be understood both by technicians and management stakeholders.

* Deployment and maintaining real or virtual machines

* Instant Managed services from `stem cell' hosts

* Modelling the required properties of all machines and allowing non-experts
  insight into that model to see how their business goals are being handled.

* Focus on outcomes rather than implementation.

* Bring systems from any state into compliance.

# What if I change my mind about Cloud Computing?

CFEngine can be used in a public or in a private cloud, and it can be used on
local servers, desktops and even mobile devices. CFEngine is designed to be
simple and lightweight, but powerful in its concepts and capabilities. It
out-performs most other management software and imposes fewer limitations. If
you want to move a service or a server-role, it is a simple matter to do so.
CFEngine will continue to manage the service no matter what the underlying
resource model.

# The future - molecular computing

At CFEngine, we believe that Cloud Computing is just a rehearsal for a real
change in the way computing services are managed. In the future, the
capabilities that assured management of recycle-able parts bring to services
will allow atomic services to be combined into new and complex fabrics of
functionality. The chemistry of these services will enable businesses and other
organizations to express unique functions by combining a standard set of
elementary parts. CFEngine's role in such a fabric would be the same as today:
bringing self-maintaining, knowledge-based management to an infrastructure where
users are free to make the most of shared pools.

Footnotes

[1]: Rebooting a virtual machine in the cloud often means losing all of its special properties, so one needs to be ready to rebuild in case of catastrophe.
