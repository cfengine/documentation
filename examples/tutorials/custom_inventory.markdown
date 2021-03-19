---
layout: default
title: Custom Inventory
sorting: 15
published: true
tags: [Examples, Tutorials, Inventory, Enterprise]
---

This tutorial will show you how to add custom inventory attributes that can be
leveraged in policy and reported on in the CFEngine Enterprise Mission Portal.
For a more detailed overview on how the inventory system works please reference
[CFEngine 3 inventory modules][inventory/].

## Overview ##

This tutorial provides instructions for the following:

* [Choose an attribute][Custom Inventory#Choose an Attribute to Inventory]

* [Create and deploy inventory policy][Custom Inventory#Create and Deploy Inventory Policy]

* [Run Reports][Custom Inventory#Run Reports]

**Note:** This tutorial uses the [CFEngine Enterprise Vagrant Environment][Using Vagrant] and files located in the vagrant project directory are automatically available to all hosts.

## Choose an Attribute to Inventory

Writing inventory policy is incredibly easy. Simply add the `inventory` and
`attribute_name=` tags to any variable or [namespace scoped classes][classes#scope].

In this tutorial we will add `Owner` information into the inventory. In this
example we will use a simple shared flat file data source
`/vagrant/inventory_owner.csv`.

On your hosts create `/vagrant/inventory_owner.csv` with the following content:

```
hub, Operations Team <ops@cfengine.com>
host001, Development <dev@cfengine.com>
```

## Create and Deploy Inventory Policy

Now that each of your hosts has access to a data source that provides the Owner
information we will write an inventory policy to report that information.

Create `/var/cfengine/masterfiles/services/tutorials/inventory/owner.cf` with the
following content:

```cf3
bundle agent tutorials_inventory_owner
# @brief Inventory Owner information
# @description Inventory owner information from `/vagrant/inventory_owner.csv`.
{
  vars:
    "data_source" string => "/vagrant/inventory_owner.csv";
    "owners"
      data => data_readstringarray( $(data_source), "", ", ", 100, 512 ),
      if => fileexists( $(data_source) );

    "my_owner"
      string  => "$(owners[$(sys.uqhost)][0])",
      meta    => { "inventory", "attribute_name=Owner" },
      comment => "We need to tag the owner information so that it is correctly
                  reported via the UI.";

  reports:
    inform_mode::
      "$(this.bundle): Discovered Owner='$(my_owner)'"
        if => isvaribale( "my_owner" );
}
bundle agent __main__
# @brief Run tutorials_inventory_owner if this policy file is the entry
{
  methods: "tutorials_inventory_owner";
}
```

**Note:** For the simplicity of this tutorial we assume that
[masterfiles][sys#sys.masterdir] is not configured for policy updates from a
Git repository. If it is, please add the policy to your repository and ensure
it gets to its final destination as needed.

This policy will not be activated until it has been included in
[inputs][Components and Common Control#inputs]. For simplicity we will be
adding it via [Augments][Augments] (`def.json`).

Create `/var/cfengine/masterfiles/def.json` and populate it with the following content:

```json
{
  "inputs": [ "services/tutorials/inventory/owner.cf" ],
  "vars": {
    "control_common_bundlesequence_end": [ "tutorials_inventory_owner" ]
  }
}
```

Any time you modify something, it is *always* a good idea to validate the syntax. You can run `cf-promises` to check policy syntax.

**Policy Validation:**

```console
[root@hub ~]# cf-promises -cf /var/cfengine/masterfiles/promises.cf
[root@hub ~]# echo $?
0
```

No output and return code `0` indicate the policy was successfully validated.

**JSON Validation:**

You can use your favorite JSON validate. I like [`jq`][jq-prpoject], plus it's handy for picking apart API responses so let's install that and use it.

```console
[root@hub ~]# wget -q -O /var/cfengine/bin/jq https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64
[root@hub ~]# chmod +x /var/cfengine/bin/jq
[root@hub ~]# 
```

Once it's installed, we can use it to validate our JSON.

```console
[root@hub ~]# jq '.' < /var/cfengine/masterfiles/def.json
{
  "inputs": [
    "services/tutorials/inventory/owner.cf"
  ],
  "vars": {
    "control_common_bundlesequence_end": [
      "tutorials_inventory_owner"
    ]
  }
}
[root@hub ~]# echo $?
0
```

Pretty printed JSON and a return code of `0` indicate the JSON was successfully validated.

You can also perform a manual policy run and check that the correct owner is discovered.

**Manual Policy Run:**

```console
[root@hub ~]# cf-agent -KIf /var/cfengine/masterfiles/promises.cf -b tutorials_inventory_owner
    info: Using command line specified bundlesequence
R: tutorials_inventory_owner: Discovered Owner='Operations Team <ops@cfengine.com>'
```

Here we ran the policy without locks (`-K`) in inform mode (`-I`), using a
specific policy entry (`-f`) and activating only a specific bundle (`-b`). The
inform output helps us confirm that the owner is discovered from our CSV
properly.

## Reporting

Once you have integrated the policy into `def.json` it will run by all agents
after they have updated their policy. Once the hub has had a chance to collect
reports the `Owner` attribute will be available to select as a Table column for
Inventory Reports. Custom attributes appear under the `User defined` section.

**Note:** It may take up to 15 minutes for your custom inventory attributes to
be collected and made available for reporting.

### Mission Portal

![custom inventory attribute](tutorials_custom_inventory_attribute.png)

You will see the host owner as shown in the following report.

![custom inventory report](tutorials_custom_inventory_report.png)

### Inventory API

Of course, you can also get this information from the [Inventory API][Inventory API].

Let's query the API from the hub itself, and use [`jq`][jq-project] to make it easier to handle the output.

Now that we have jq in place, let's query the Inventory API to see what inventory attributes are available.

```console
[root@hub ~]# curl -s -k --user admin:admin -X GET https://localhost/api/inventory/attributes-dictionary | jq '.[].attribute_name'
"Architecture"
"BIOS vendor"
"BIOS version"
"CFEngine Enterprise license file"
"CFEngine Enterprise license status"
"CFEngine Enterprise license utilization"
"CFEngine Enterprise licenses allocated"
"CFEngine ID"
"CFEngine roles"
"CFEngine version"
"CPU logical cores"
"CPU model"
"CPU physical cores"
"CPU sockets"
"Disk free (%)"
"Host name"
"IPv4 addresses"
"Interfaces"
"MAC addresses"
"Memory size (MB)"
"OS"
"OS kernel"
"OS type"
"Owner"
"Physical memory (MB)"
"Policy Release Id"
"Policy Servers"
"Ports listening"
"Primary Policy Server"
"System UUID"
"System manufacturer"
"System product name"
"System serial number"
"System version"
"Timezone"
"Timezone GMT Offset"
"Uptime minutes"
```

Yes, we can see our attribute `Owner` is reported.

Now, let's query the Inventory API to see what Owners are reported.

```console
[root@hub ~]# curl -s -k --user admin:admin -X POST -H 'content-type: application/json' -d '{ "select": [ "Host name", "Owner" ]}' https://localhost/api/inventory | jq '.data[].rows[]'
[
  "host001.example.com",
  "Development <dev@cfengine.com>"
]
[
  "hub.example.com",
  "Operations Team <ops@cfengine.com>"
]
```

Indeed, we can see each host reporting the values as expected from our CSV file.
