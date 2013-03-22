## 1 CFEngine 3.4.2.dbc9cd62119efa46809f33f4e3b95fa0e6edc4b5 – Getting started



CFEngine is a suite of programs for integrated autonomic management
of either individual or networked computers. It has existed as as
software suite since 1993 and this version published under the GNU
Public License (GPL v3) and a Commercial Open Source License
(COSL). CFEngine is Copyright by **CFEngine AS**, a company founded
by CFEngine author Mark Burgess.

This document describes major version 3 of CFEngine, which is a
significant departure from earlier versions, and represents the
newest and most carefully researched technology available for
configuration management. It is both simpler and more powerful.
CFEngine 3 will exist as both free open source and commercial
enterprise versions:

-   **Community Edition** - a free and gratis core of the software
    (available now).
-   **Enterprise** - a commercial enhanced version for basic
    enterprise needs (available now; previously known as Nova).

This document is valid for **all versions** of CFEngine. Whenever a
feature is only available in a specific version, that fact will be
noted in the documentation for that feature (if there is no note,
then that feature is available in all versions).

CFEngine 3 has been changed to be both a more powerful tool and a
much simpler tool. CFEngine 3's language interface is not backwards
compatible with the CFEngine 2 configuration language, but it
interoperates with CFEngine 2 so that it is "run-time compatible".
This means that you can change over to version 3 slowly, with low
risk and at your own speed.

With CFEngine 3 you can install, configure and maintain computers
using powerful hands-free tools. You can also integrate knowledge
management and diagnosis into the processes.

CFEngine differs from most management systems in being

-   Open software (GPL or COSL).
-   Lightweight and generic.
-   Non-reliant on a working network to function correctly.
-   Capable of making each and every host autonomous



### 1.1 Software components

CFEngine 3 consists of a number of components. The names of the
programs are intentionally different from those in CFEngine 2 to
help disambiguate them (and some CFEngine 2 components have been
merged and/or eliminated). The starred components are new to
CFEngine 3:

-   [cf-agent](/manuals/cf3-Reference#cf_002dagent)
-   [cf-execd](/manuals/cf3-Reference#cf_002dexecd)
-   [cf-know](/manuals/cf3-Reference#cf_002dknow)
-   [cf-monitord](/manuals/cf3-Reference#cf_002dmonitord)
-   [cf-promises](/manuals/cf3-Reference#cf_002dpromises)
-   [cf-runagent](/manuals/cf3-Reference#cf_002drunagent)
-   [cf-serverd](/manuals/cf3-Reference#cf_002dserverd)
-   [cf-report](/manuals/cf3-Reference#cf_002dreport)
-   [cf-key](/manuals/cf3-Reference#cf_002dkey)
-   [cf-hub](/manuals/cf3-Reference#cf_002dhub)




#### 1.1.1 cf-agent

Active agent – responsible for maintaining promises about the state
of your system (in CFEngine 2 the agent was called `cfagent`). You
can run `cf-agent` manually, but if you want to have it run on a
regular basis, you should use
[cf-execd](/manuals/cf3-Reference#cf_002dexecd) (instead of using
`cron`).

`cf-agent` keeps the promises made in
[common](/manuals/cf3-Reference#Bundles-for-common) and
[agent](/manuals/cf3-Reference#Bundles-for-agent) bundles, and is
affected by [common](/manuals/cf3-Reference#control-common) and
[agent](/manuals/cf3-Reference#control-agent) control bodies.




#### 1.1.2 cf-execd

Scheduler – responsible for running cf-agent on a regular (and
user-configurable) basis (in CFEngine 2 the scheduler was called
`cfexecd`).

EXECUTOR `cf-execd` keeps the promises made in
[common](/manuals/cf3-Reference#Bundles-for-common) bundles, and is
affected by [common](/manuals/cf3-Reference#control-common) and
[executor](/manuals/cf3-Reference#control-executor) control
bodies.




#### 1.1.3 cf-know\*

Knowledge modelling agent – responsible for building and analysing
a semantic knowledge network.

`cf-know` keeps the promises made in
[common](/manuals/cf3-Reference#Bundles-for-common) and
[knowledge](/manuals/cf3-Reference#Bundles-for-knowledge) bundles,
and is affected by [common](/manuals/cf3-Reference#control-common)
and [knowledge](/manuals/cf3-Reference#control-knowledge) control
bodies.




#### 1.1.4 cf-monitord

Passive monitoring agent – responsible for collecting information
about the status of your system (which can be reported upon or used
to enforce promises or influence when promises are enforced). In
CFEngine 2 the passive monitoring agent was known as `cfenvd`.

`cf-monitord` keeps the promises made in
[common](/manuals/cf3-Reference#Bundles-for-common) and
[monitor](/manuals/cf3-Reference#Bundles-for-monitor) bundles, and
is affected by [common](/manuals/cf3-Reference#control-common) and
[monitor](/manuals/cf3-Reference#control-monitor) control bodies.




#### 1.1.5 cf-promises

Promise validator – used to verify that the promises used by the
other components of CFEngine are syntactically valid. `cf-promises`
does not execute any promises, but can syntax-check all of them.




#### 1.1.6 cf-runagent

Remote run agent – used to execute `cf-agent` on a remote machine
(in CFEngine 2 the remote run agent was called `cfrun`).
`cf-runagent` does not keep any promises, but instead is used to
ask another machine to do so.




#### 1.1.7 cf-serverd

Server – used to distribute policy and/or data files to clients
requesting them and used to respond to requests from `cf-runagent`
(in CFEngine 2 the remote run agent was called `cfservd`).

`cf-serverd` keeps the promises made in
[common](/manuals/cf3-Reference#Bundles-for-common) and
[server](/manuals/cf3-Reference#Bundles-for-server) bundles, and is
affected by [common](/manuals/cf3-Reference#control-common) and
[server](/manuals/cf3-Reference#control-server) control bodies.




#### 1.1.8 cf-report

Self-knowledge extractor – takes data stored in CFEngine's embedded
databases and converts them to human readable form

`cf-report` keeps the promises made in
[common](/manuals/cf3-Reference#Bundles-for-common) bundles, and is
affected by [common](/manuals/cf3-Reference#control-common) and
[reporter](/manuals/cf3-Reference#control-reporter) control
bodies.




#### 1.1.9 cf-key

Key generation tool – run once on every host to create
public/private key pairs for secure communication (in CFEngine 2
the key generation tool was called `cfkey`). `cf-key` does not keep
any promises.




#### 1.1.10 cf-hub

A data aggregator used as part of the commercial product. This stub
is not used in the community edition of CFEngine.

