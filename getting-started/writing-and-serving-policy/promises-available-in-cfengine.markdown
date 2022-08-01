---
layout: default
title: Promises Available in CFEngine
sorting: 4
published: true
tags: [overviews, promises]
---

### meta - information about promise bundles ###

Meta-data promises have no internal function. They are intended to be used to represent arbitrary information about promise bundles. Formally, meta promises are implemented as variables, and the values map to a variable context called bundlename_meta. The values can be used as variables and will appear in CFEngine Enterprise variable reports.

See [`meta`][meta].

### vars - a variable, representing a value ###

Variables in CFEngine are defined as promises that an identifier of a certain type represents a particular value. Variables can be scalars or lists of types string, int, real or data.

The allowed characters in variable names are alphanumeric (both upper and lower case) and underscore. Associative arrays using the string type and square brackets [] to enclose an arbitrary key are being deprecated in favor of the data variable type.

See `vars`.

### defaults - a default value for bundle parameters ###

Defaults promises are related to variables. If a variable or parameter in a promise bundle is undefined, or its value is defined to be invalid, a default value can be promised instead.

CFEngine does not use Perl semantics: i.e. undefined variables do not map to the empty string, they remain as variables for possible future expansion. Some variables might be defined but still contain unresolved variables. To handle this you will need to match the `$(abc)` form of the variables.

See `defaults`.

### classes - a class, representing a state of the system ###

Classes promises may be made in any bundle. Classes that are set in common bundles are global in scope, while classes in all other bundles are local.

Note: The term class and context are sometimes used interchangeably.

See [`classes`][classes].

### users - add or remove users ###

User promises are promises made about local users on a host. They express which users should be present on a system, and which attributes and group memberships the users should have.

Every user promise has at least one attribute, policy, which describes whether or not the user should be present on the system. Other attributes are optional; they allow you to specify UID, home directory, login shell, group membership, description, and password.

A bundle can be associated with a user promise, such as when a user is created in order to do housekeeping tasks in his/her home directory, like putting default configuration files in place, installing encryption keys, and storing a login picture.

History: Introduced in CFEngine 3.6.0

See `users`.

### files - configure a file ###

Files promises are an umbrella for attributes of files. Operations fall basically into three categories: create, delete and edit.

See `files`.

### packages - install a package ###

CFEngine supports a generic approach to integration with native operating support for packaging. Package promises allow CFEngine to make promises regarding the state of software packages conditionally, given the assumption that a native package manager will perform the actual manipulations. Since no agent can make unconditional promises about another, this is the best that can be achieved.

See `packages`.

### guest_environments ###

Guest environment promises describe enclosed computing environments that can host physical and virtual machines, Solaris zones, grids, clouds or other enclosures, including embedded systems. CFEngine will support the convergent maintenance of such inner environments in a fixed location, with interfaces to an external environment.

CFEngine currently seeks to add convergence properties to existing interfaces for automatic self-healing of guest environments. The current implementation integrates with libvirt, supporting host virtualization for Xen, KVM, VMWare, etc. Thus CFEngine, running on a virtual host, can maintain the state and deployment of virtual guest machines defined within the libvirt framework. Guest environment promises are not meant to manage what goes on within the virtual guests. For that purpose you should run CFEngine directly on the virtual machine, as if it were any other machine.

See `guest_environments`.

### methods - take on a whole bundle of other promises ###

Methods are compound promises that refer to whole bundles of promises. Methods may be parameterized. Methods promises are written in a form that is ready for future development. The promiser object is an abstract identifier that refers to a collection (or pattern) of lower level objects that are affected by the promise-bundle. Since the use of these identifiers is for the future, you can simply use any string here for the time being.

See `methods`.

### processes - start or terminate processes ###

Process promises refer to items in the system process table, i.e., a command in some state of execution (with a Process Control Block). Promiser objects are patterns that are unanchored, meaning that they match line fragments in the system process table.

See `processes`.

### services - start or stop services ###

A service is a set of zero or more processes. It can be zero if the service is not currently running. Services run in the background, and do not require user intervention.

Service promises may be viewed as an abstraction of process and commands promises. An important distinguisher is however that a single service may consist of multiple processes. Additionally, services are registered in the operating system in some way, and get a unique name. Unlike processes and commands promises, this makes it possible to use the same name both when it is running and not.

Some operating systems are bundled with a lot of unused services that are running as default. At the same time, faulty or inherently insecure services are often the cause of security issues. With CFEngine, one can create promises stating the services that should be stopped and disabled.

The operating system may start a service at boot time, or it can be started by CFEngine. Either way, CFEngine will ensure that the service maintains the correct state (started, stopped, or disabled). On some operating systems, CFEngine also allows services to be started on demand, when they are needed. This is implemented though the inetd or xinetd daemon on Unix. Windows does not support this.

CFEngine also allows for the concept of dependencies between services, and can automatically start or stop these, if desired. Parameters can be passed to services that are started by CFEngine.

See `services`.

### commands - execute a command ###

Commands and processes are separated cleanly. Restarting of processes must be coded as a separate command. This stricter type separation allows for more careful conflict analysis to be carried out.

See `commands`.

### storage - verify attached storage ###

Storage promises refer to disks and filesystem properties.

See `storage`.

### databases - configure a database ###

CFEngine can interact with commonly used database servers to keep promises about the structure and content of data within them.

There are two main cases of database management to address: small embedded databases and large centralized databases.

Databases are often centralized entities that have a single point of management. While large monolithic database can be more easily managed with other tools, CFEngine can still monitor changes and discrepancies. In addition, CFEngine can also manage smaller embedded databases that are distributed in nature, whether they are SQL, registry or future types.

For example, creating 100 new databases for test purposes is a task for CFEngine; but adding a new item to an important production database is not a recommended task for CFEngine.

See `databases`.

### access - grant or deny access to file objects ###

Access promises are conditional promises made by resources living on the server.

The promiser is the name of the resource affected and is interpreted to be a path, unless a different resource_type is specified. Access is then granted to hosts listed in admit_ips, admit_keys and admit_hostnames, or denied using the counterparts deny_ips, deny_keys and deny_hostnames.

You layer the access policy by denying all access and then allowing it only to selected clients, then denying to an even more restricted set.

See `access`.

### roles - allow certain users to activate certain classes ###

Roles promises are server-side decisions about which users are allowed to define soft-classes on the server's system during remote invocation of cf-agent. This implements a form of Role Based Access Control (RBAC) for pre-assigned class-promise bindings. The user names cited must be attached to trusted public keys in order to be accepted. The regular expression is anchored, meaning it must match the entire name.

See `roles`.

### measurements - measure or sample data from the system ###

This is an Enterprise-only feature.

By default,CFEngine's monitoring component cf-monitord records performance data about the system. These include process counts, service traffic, load average and CPU utilization and temperature when available.

CFEngine Enterprise extends this in two ways. First it adds a three year trend summary based any 'shift'-averages. Second, it adds customizable measurements promises to monitor or log very specific user data through a generic interface. The end-result is to either generate a periodic time series, like the above mentioned values, or to log the results to custom-defined reports.

Promises of type measurement are written just like all other promises within a bundle destined for the agent concerned, in this case monitor. However, it is not necessary to add them to the bundlesequence, because cf-monitord executes all bundles of type monitor.

See `measurements`.

### reports - report a message ###

Reports promises simply print messages. Outputting a message without qualification can be a dangerous operation. In a large installation it could unleash an avalanche of messaging.

See `reports`.
