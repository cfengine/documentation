---
layout: default
title: guest_environments
published: true
tags: [reference, bundle agent, guest_environments, promises, promise types, virtual machines, agent, promises, libvirt, KVM, VMWare]
---

Guest environment promises describe enclosed computing environments that
can host physical and virtual machines, Linux containers, Solaris zones, grids, clouds or
other enclosures, including embedded systems. CFEngine will support the
convergent maintenance of such inner environments in a fixed location,
with interfaces to an external environment.

CFEngine currently seeks to add convergence properties to existing
interfaces for automatic self-healing of guest environments. The current
implementation integrates with *libvirt*, supporting host virtualization
for Xen, KVM, VMWare, Docker, etc. Thus CFEngine, running on a virtual host, can
maintain the state and deployment of virtual guest machines defined
within a *libvirt* framework, or a Docker framework. Guest environment promises are not meant
to manage what goes on within the virtual guests. For that purpose you
should run CFEngine directly on the virtual machine, as if it were any
other machine.



```cf3
 kvm_hosts::

  "unique_name1"

       guest_details => kvm_host("$(host)","$(uuid)","$(kernel)","1024000"),
       guest_state   => "create";

  docker_host::

  "unique_name2"
       guest_details => ubuntu_stem_cell,
       guest_state   => "create";

```

CFEngine currently provides a convergent interface to guests via *libvirt*, Docker, and
other interfaces.

***

## Attributes ##

[%CFEngine_include_markdown(common-attributes-include.markdown)%]


### guest_type

**Allowed input range:** lxc,xen,kvm,esx,vbox,test,xen_net,kvm_net,esx_net,test_net,zone,ec2,eucalyptus,docker

**Description:** The type of virtual environment being defined.


### guest_state

**Description:** The `environment_state` defines the desired dynamic state
 of the specified environment.

**Type:** (menu option)

**Allowed input range:**

* `create`

The guest machine is allocated, installed and left in a running state.

* `delete`

The guest machine is shut down and deallocated, but no files are removed.

* `running`

The guest machine is in a running state, if it previously exists.

* `suspended`

The guest exists in a suspended state or a shutdown state. If the guest
is running, it is suspended; otherwise it is ignored.

* `down`

The guest machine is shut down, but not deallocated.

**Example:**

```cf3
guest_environments:

 linux::

 "my-kvm1"
                 comment => "Keep this vm suspended",
           guest_details => kvm,
             guest_state => "suspended";

```


### guest_details

**Type:** `body guest_details`



#### guest_cpus

**Allowed input range:** 0-9999
**Description:** Number of virtual CPUs in the environment
**Type:** `int`

#### guest_memory
**Allowed input range:** 0-9999
**Description:**  Amount of primary storage (RAM) in the virtual environment (KB)
**Type:** `int`

#### guest_disk
**Allowed input range:**
**Description:** Amount of secondary storage (DISK) in the virtual environment (MB)
**Type:** `int`

#### guest_image_path
**Allowed input range:** CF_ABSPATHRANGE
**Description:** The path to an image with which to initialize the virtual environment
**Type:** `string`

#### guest_image_name
**Description:** The name of the image which forms the initial state of the virtual environment
**Type:** `string`

#### guest_libvirt_xml
**Allowed input range:** CF_ANYSTRING
**Description:** A string containing a libvirt specific set of promises for the virtual instance. This
XML excerpt replaces many of the other options, and is passed raw into the libvirt framework.

**Example:**
```cf3
body guest_details kvm_host(host,uuid,kernel,initrd,kickstartcmd,macaddress,memory)
{
guest_type => "kvm";

guest_libvirt_xml =>

 "<domain type='kvm'>
  <name>$(host)</name>
  <uuid>$(uuid)</uuid>
  <memory>$(memory)</memory>
  <vcpu>1</vcpu>
  <os>
    <type arch='x86_64'>hvm</type>
    <kernel>$(kernel)</kernel>
    <initrd>$(initrd)</initrd>
    <cmdline>$(kickstartcmd)</cmdline>
    <boot dev='hd'/>
  </os>
  <features>
    <acpi/>
    <apic/>
    <pae/>
  </features>
  <clock offset='utc'/>
  <on_poweroff>destroy</on_poweroff>
  <on_reboot>destroy</on_reboot>
  <on_crash>destroy</on_crash>
  <devices>
    <emulator>/usr/bin/kvm</emulator>
    <disk type='file' device='disk'>
      <driver name='qemu' type='qcow2'/>
      <source file='$(diskStorage)/$(host).img'/>
      <target dev='hda' bus='ide'/>
      <alias name='ide0-0-0'/>
      <address type='drive' controller='0' bus='0' unit='0'/>
    </disk>
    <interface type='bridge'>
      <mac address='$(macaddress)'/>
      <source bridge='vlan1180_br0'/>
      <model type='virtio'/>
    </interface>
    <input type='mouse' bus='ps2'/>
    <graphics type='vnc' port='5901' autoport='yes'>
      <listen type='address' address='0.0.0.0'/>
    </graphics>
  </devices>
</domain>
";
}
```

#### guest_addresses
**Allowed input range:** ANYSTRING
**Description:** The IP addresses of the environment's network interfaces (currently unused)

#### guest_network
**Allowed input range:** any
**Description:** The hostname of the virtual network (currently unused)
