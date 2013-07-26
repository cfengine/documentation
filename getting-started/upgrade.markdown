---
layout: default
title: Upgrade Instructions
sorting: 20
categories: [Getting Started, Upgrade]
published: true
alias: getting-started-upgrade.html
tags: [getting started, enterprise, upgrade]
---

###This upgrade guide assumes that you are upgrading an existing 
###CFEngine installation of one of the following versions:
###2.2.x or 3.0.x or 3.5.0

Upgrading CFEngine Enterprise needs some planning, since there may  
be dependencies on your existing policies and/or changes in naming  
convention/syntax in CFEngine itself. For this reason, it is  
currently a manual process. Automatic upgrade of agents is possible   
through the hub but again, needs careful planning and consideration  
before applying to a large schema.

###Always verify the upgrade in a test environment prior to upgrading 
###production environments!

Before embarking on the upgrade, you should familiarize yourself with the   
[known issues][Known Issues] and have a good understanding of the existing  
configuration of the hub or agents or both. As much as possible is covered  
in this document, taking into consideration its scope and intended audience.   
Other more detailed problems, specific to your own setup may not be  
covered  here. It is therefore important that any questions or doubts you  
have are directed towards your support representative.

Please contact your sales representative, or our support   
engineers through the [support system][support desk]  

### Prerequisites

* CFEngine 3 Enterprise HUB version 2.2.x/3.0.x/3.5.0
* Linux shell

### Before you start: Make a Backup

Backup /var/cfengine/masterfiles to /var/cfengine/masterfiles_$(date)  
using the following command:

<code>
  $ cp -r $WORKDIR/masterfiles $WORKDIR/masterfiles_$(date +%T_%F)
</code>


### Notes that only apply if you're upgrading from 2.2.x

This section can be skipped if you are upgrading from 3.0.x or 3.5.0 to 3.5.1  

As part of the process from 2.x to 3, more structure was introduced to the  
CFEngine working directory, such that CFE_ prefixed files were moved into a  
new subdirectory `/var/cfengine/masterfiles/cfe_internal`  
It's therefore necessary to manually edit to your  
`/var/cfengine/masterfiles/promises.cf` by adding `cfe_internal/`  
to the path of all CFE_ prefixed files.  

For example, in the old form, you might find:

CFE_knowledge.cf

the new form for 3.x would be:

cfe_internal/CFE_knowledge.cf


If there are any references in your policy file to cfengine_stdlib.cf  
ensure that you add the prefix `libraries/` so that CFEngine knows where  
to find the library file in its new location.  

The same applies to file_change.cf. It now lives in the services subdirectory,   
so any reference to it in your policy file(s) should now look like  
this: services/file_change.cf.


### Host Upgrade Process

Obtain the latest CFEngine archive for your distribution. This will   
consist of either an rpm or debian package. Since CFEngine 3.5.0,  
the upgrade process is largely automatic. It relies on you manually   
stopping the existing CFEngine processes and Mission Portal (if applicable)   
and simply following the [installation][Installation] procedure for your  
platform. It's wise to make a backup copy of the content of your  
existing masterfiles subdirectory before proceeding. Be aware of  
the slight changes in policy file syntax that were introduced in 3.5.0.   
You should look at the [known issues][known-issues documentation for  
more information on this minor change.  

To manually stop the CFEngine processes on a hub, use the following commands:  

pkill cf-  
pkill httpd

Now that you've stopped CFEngine, you can go to the [installation][Installation] instructions.  


### Automatic Agent Upgrade Process

Please note that although it is possible to upgrade agents through the hub,   
for Debian format (.deb) packages (both `x86_64` and `i386`) it is necessary   
to edit the `update.cf` on each agent before proceeding. The reason for this  
is that the naming convention used in 2.2.3 is at odds with the one that has  
since been adopted by CFEngine and in the wider community. As a result, the  
`update.cf` script in v2.2.3 clients expects i686 (hard coded) and x86_64 for   
the architecture part in the package name. So package upgrade will only work  
for .deb packages if the package is renamed before it is copied into the  
relevant architecture subdirectory under:  

`/var/cfengine/master_software_updates`.

For example, if your upgrade package is named like this:

`cfengine-nova_3.5.0XXXX_amd64.deb` or `cfengine-nova_3.5.0XXXX_i386.deb`

you should rename them so they look like this:

`cfengine-nova_3.5.0XXXX_x86_64.deb` or `cfengine-nova_3.5.0XXXX_i686.deb`

*before* copying them into 

`/var/cfengine/master_software_updates/<arch subdirectory>` on the hub

