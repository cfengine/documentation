---
layout: default
title: guest_005fenvironments-in-agent-promises
categories: [Bundles-for-agent,guest_005fenvironments-in-agent-promises]
published: true
alias: Bundles-for-agent-guest_005fenvironments-in-agent-promises.html
tags: [Bundles-for-agent,guest_005fenvironments-in-agent-promises]
---

### `guest_environments` promises in agent

\

Guest environment promises describe enclosed computing environments that
can host physical and virtual machines, Solaris zones, grids, clouds or
other enclosures, including embedded systems. CFEngine will support the
convergent maintenance of such inner environments in a fixed location,
with interfaces to an external environment.

CFEngine currently seeks to add convergence properties to existing
interfaces for automatic self-healing of guest environments. The current
implementation integrates with *libvirt*, supporting host virtualization
for Xen, KVM, VMWare, etc. Thus CFEngine, running on a virtual host, can
maintain the state and deployment of virtual guest machines defined
within the *libvirt* framework. Guest environment promises are not meant
to manage what goes on within the virtual guests. For that purpose you
should run CFEngine directly on the virtual machine, as if it were any
other machine.

\

~~~~ {.verbatim}
 site1::

  "unique_name1"

       environment_resources => myresources("2GB","512MB"),
       environment_interface => mymachine("hostname"),
            environment_type => "xen",
            environment_state => "running",
            environment_host => "atlas";

  "unique_name2"

            environment_type => "xen_network",
           environment_state => "create",
            environment_host => "atlas";
~~~~

\

CFEngine currently provides a convergent interface to *libvirt*.

-   [environment\_host in
    guest\_environments](#environment_005fhost-in-guest_005fenvironments)
-   [environment\_interface in
    guest\_environments](#environment_005finterface-in-guest_005fenvironments)
-   [environment\_resources in
    guest\_environments](#environment_005fresources-in-guest_005fenvironments)
-   [environment\_state in
    guest\_environments](#environment_005fstate-in-guest_005fenvironments)
-   [environment\_type in
    guest\_environments](#environment_005ftype-in-guest_005fenvironments)

#### `environment_host`

**Type**: string

**Allowed input range**: `[a-zA-Z0-9_]+`

**Synopsis**: A class indicating which physical node will execute this
guest machine

**Example**:\
 \

~~~~ {.verbatim}
guest_environments:

 linux::

 "host1"
                 comment => "Keep this vm suspended",
   environment_resources => myresources,
        environment_type => "kvm",
       environment_state => "suspended",
        environment_host => "ubuntu";
~~~~

**Notes**:\
 \

The promise will only apply to the machine with this class set. Thus,
CFEngine must be running locally on the hypervisor for the promise to
take effect.

This attribute is required.

*History*: this feature was introduced in Nova 2.0.0 (2010), Community
3.3.0 (2012)

#### `environment_interface` (body template)

**Type**: (ext body)

`env_addresses`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: The IP addresses of the environment's network interfaces

**Example**:\
 \

~~~~ {.verbatim}
     
     body environment_interface vnet(primary)
     {
     env_name      => "$(this.promiser)";
     env_addresses => { "$(primary)" };
     
     host1::
     
       env_network => "default_vnet1";
     
     host2::
     
       env_network => "default_vnet2";
     
     }
~~~~

**Notes**:\
 \

The IP addresses of the virtual machine can be overridden here at run
time. \

`env_name`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: The hostname of the virtual environment

**Example**:\
 \

~~~~ {.verbatim}
     body environment_interface vnet(primary)
     {
     env_name      => "$(this.promiser)";
     env_addresses => { "$(primary)" };
     
     host1::
       env_network => "default_vnet1";
     
     host2::
       env_network => "default_vnet2";
     }
~~~~

**Notes**:\
 \

The \`hostname' of a virtual guest may or may not be the same as the
identifier used as \`promiser' by the virtualization manager. \

`env_network`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: The hostname of the virtual network

**Example**:\
 \

~~~~ {.verbatim}
     
     body environment_interface vnet(primary)
          {
          env_name      => "$(this.promiser)";
          env_addresses => { "$(primary)" };
     
          host1::
            env_network => "default_vnet1";
     
          host2::
            env_network => "default_vnet2";
          }
     
~~~~

#### `environment_resources` (body template)

**Type**: (ext body)

`env_cpus`

**Type**: int

**Allowed input range**: `0,99999999999`

**Synopsis**: Number of virtual CPUs in the environment

**Example**:\
 \

~~~~ {.verbatim}
     
     body environment_resources my_environment
     {
     env_cpus => "2";
     env_memory => "512"; # in KB
     env_disk => "1024";  # in MB
     }
     
~~~~

**Notes**:\
 \

The maximum number of cores or processors in the physical environment
will set a natural limit on this value.

This attribute conflicts with `env_spec`. \

`env_memory`

**Type**: int

**Allowed input range**: `0,99999999999`

**Synopsis**: Amount of primary storage (RAM) in the virtual environment
(KB)

**Example**:\
 \

~~~~ {.verbatim}
     
     body environment_resources my_environment
     {
     env_cpus => "2";
     env_memory => "512"; # in KB
     env_disk => "1024";  # in MB
     }
     
~~~~

**Notes**:\
 \

The maximum amount of memory in the physical environment will set a
natural limit on this value.

This attribute conflicts with `env_spec`. \

`env_disk`

**Type**: int

**Allowed input range**: `0,99999999999`

**Synopsis**: Amount of secondary storage (DISK) in the virtual
environment (MB)

**Example**:\
 \

~~~~ {.verbatim}
     
     body environment_resources my_environment
     {
     env_cpus => "2";
     env_memory => "512"; # in KB
     env_disk => "1024";  # in MB
     }
     
~~~~

**Notes**:\
 \

This parameter is currently unsupported, for future extension.

This attribute conflicts with `env_spec`. \

`env_baseline`

**Type**: string

**Allowed input range**: `"?(/.*)`

**Synopsis**: The path to an image with which to baseline the virtual
environment

**Example**:\
 \

~~~~ {.verbatim}
     
     env_baseline => "/path/to/image";
     
~~~~

**Notes**:\
 \

This function is for future development. \

`env_spec`

**Type**: string

**Allowed input range**: `.*`

**Synopsis**: A string containing a technology specific set of promises
for the virtual instance

**Example**:\
 \

~~~~ {.verbatim}
     body environment_resources virt_xml(host)
     {
     env_spec => 
     
     "domain type='xen'>
       name>$(host)/name>
       os>
         type>linux/type>
         kernel>/var/lib/xen/install/vmlinuz-ubuntu10.4-x86_64/kernel>
         initrd>/var/lib/xen/install/initrd-vmlinuz-ubuntu10.4-x86_64/initrd>
         cmdline> kickstart=http://example.com/myguest.ks /cmdline>
       /os>
       memory>131072/memory>
       vcpu>1/vcpu>
       devices>
         disk type='file'>
           source file='/var/lib/xen/images/$(host).img'/>
           target dev='sda1'/>
         /disk>
         interface type='bridge'>
           source bridge='xenbr0'/>
           mac address='aa:00:00:00:00:11'/>
           script path='/etc/xen/scripts/vif-bridge'/>
         /interface>
         graphics type='vnc' port='-1'/>
         console tty='/dev/pts/5'/>
       /devices>
     /domain>
     ";
     }
     
~~~~

**Notes**:\
 \
 The preferred way to specify the resources of an environment on
creation; in other words, when `environment_state` is create.

This attribute conflicts with `env_cpus`, `env_memory` and `env_disk`.

*History*: Was introduced in version 3.1.0b1,Nova 2.0.0b1 (2010)

#### `environment_state`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               create
               delete
               running
               suspended
               down
~~~~

**Synopsis**: The desired dynamical state of the specified environment

**Example**:\
 \

~~~~ {.verbatim}
guest_environments:

 linux::

 "bishwa-kvm1"
                 comment => "Keep this vm suspended",
   environment_resources => myresources,
        environment_type => "kvm",
       environment_state => "suspended",
        environment_host => "ubuntu";

~~~~

**Notes**:\
 \

The allowed states have the following convergent semantics.

create

The guest machine is allocated, installed and left in a running state. \

delete

The guest machine is shut down and deallocated but no files are removed.
\

running

The guest machine is in a running state, if it previously exists. \

suspended

The guest exists in a suspended state or a shutdown state. If the guest
is running, it is suspended; otherwise it is ignored. \

down

The guest machine is shut down, but not deallocated.

#### `environment_type`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               xen
               kvm
               esx
               vbox
               test
               xen_net
               kvm_net
               esx_net
               test_net
               zone
               ec2
               eucalyptus
~~~~

**Synopsis**: Virtual environment type

**Example**:\
 \

~~~~ {.verbatim}
bundle agent my_vm_cloud
{
guest_environments:

 scope::

   "vguest1"

       environment_resources => my_environment_template,
       environment_interface => vnet("eth0,192.168.1.100/24"),
       environment_type      => "test",
       environment_state     => "create",
       environment_host      => "atlas";

   "vguest2"

       environment_resources => my_environment_template,
       environment_interface => vnet("eth0,192.168.1.101/24"),
       environment_type      => "test",
       environment_state     => "delete",
       environment_host      => "atlas";
}
~~~~

**Notes**:\
 \

The currently supported types are those supported by *libvirt*. More
will be added in the future.
