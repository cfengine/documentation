---
layout: default
title: Upgrade Instructions
sortkey: 2
categories: [Getting Started, Upgrade]
published: true
alias: getting-started-upgrade.html
tags: [getting started, upgrade]
---

###<center>This upgrade guide assumes that you are upgrading an existing CFEngine installation</center>
###<center>of one of the following versions: 2.1.x/2.2.x/3.0.x to CFEngine 3.5.0</center>

Upgrading CFEngine Enterprise needs some planning, since there may be dependencies on 
your existing policies and/or changes in naming convention/syntax in CFEngine itself. For this reason, it is currently a manual process. Automatic upgrade of agents is possible through the hub but again, needs careful planning and consideration before applying to a large schema.

Before embarking on the upgrade, you should familiarize yourself with the known issues and have a good understanding of the existing configuration of the
hub or agents or both. As much as possible is convered in this document, taking into consideration its scope and intended audience. Other more detailed problems,
specific to your own setup may not be covered here. It is therefore imperative that  any questions or doubts you have are directed towards your support representative.

Please do not hesitate to contact your sales 
representative, or our support engineers through the [support 
system](https://cfengine.zendesk.com/home)


**<center>ALWAYS TEST UPGRADE IN A TEST ENVIRONMENT PRIOR TO UPGRADING PRODUCTION 
ENVIRONMENTS</center>**




### Prerequisites

* CFEngine 3 Enterprise HUB version 2.1.x/2.2.x/3.0.x
* Linux shell

**Making a Backup of Important CFEngine Files Before you Start**

Backup /var/cfengine/masterfiles to /var/cfengine/masterfiles_$(date) using
the following command:

<code>
  $ cp -r $WORKDIR/masterfiles $WORKDIR/masterfiles_$(date +%T_%F)
</code>


* move/copy/update some files to the new policy framework (for more details 
  about the new framework, see 3.0.0-Release_Notes_CFEngine_3_Enterprise.txt)
 
* update /var/cfengine/bin/cf-twin to the latest version
  $ cp -vf $WORKDIR/bin/cf-agent $WORKDIR/bin/cf-twin

* remove MongoDB lock file
  $ rm -f $WORKDIR/state/mongod.lock

**NB: This section can be skipped if you are upgrading from 3.0.x to 3.5**

As part of the process from 2.x to 3, more structure was introduced to the 
cfengine working directory, such that CFE_prefixed files were moved into a new 
subdirectory `/var/cfengine/masterfiles/cfe_internal`
It's therefore necessary to make some edits to your 
`/var/cfengine/masterfiles/promises.cf` by adding cfe_internal/ to the path of all CFE_ prefixed files.

For example, in the old form, you might find:

`CFE_knowledge.cf`

the new form for 3.x would be:

`cfe_internal/CFE_knowledge.cf`

A list of files that this applies to is:

CFE_knowledge.cf
CFE_hub_specific.cf
CFE_cfengine.cf 

Add cfe_internal/example_use_goals.cf to inputs section in '$WORKDIR/masterfiles/promises.cf.'

Ensure that libraries/ is added as a prefix to any reference to cfengine_stdlib.cf.

Add services/ to path of file_change.cf (we group services together in a directory to avoid ending up cluttering the content of masterfiles when there are many service policies)
     
Add cfe_internal_hub_vars to bundlesequence section.
    
Add cfsketch_run to bundlesequence and cf-sketch-runfile.cf to inputs section.
     

If you've never added your custom-built promises to /var/cfengine/bin/masterfiles/failsafe.cf or /var/cfengine/masterfiles/update.cf?
we replace update.cf with update_bins.cf and update_policy.cf:

      $ sed -i 's/"update.cf",/"update_bins.cf",\n                    "update_policy.cf",/g' $WORKDIR/masterfiles/promises.cf

       * rename goal_1 to goal_infosec
      $ sed -i 's/goal_1/goal_infosec/g' $WORKDIR/masterfiles/promises.cf

       * rename goal_2 to goal_complicance
      $ sed -i 's/goal_2/goal_compliance/g' $WORKDIR/masterfiles/promises.cf

       * remove commercial_customer class
      $ sed -i '/commercial_customer::/d' $WORKDIR/masterfiles/promises.cf

       * remove nova_edition and constellation_editon classes
      $ sed -i '/nova_edition.*::/d' $WORKDIR/masterfiles/promises.cf

       * remove garbage_collection because we have one in CFE_cfengine.cf
      $ sed -i '/maintenance.*goal_3/d' $WORKDIR/masterfiles/promises.cf
      $ sed -i '/comment.*rotation.*Nova/d' $WORKDIR/masterfiles/promises.cf
      $ sed -i '/usebundle.*garbage_collection/d' $WORKDIR/masterfiles/promises.cf

       * since the depends_on attribute has changed behavior (see the release notes), having it there might cause problems.
      $ sed -i '/depends_on/d' $WORKDIR/masterfiles/services/file_change.cf
      $ sed -i '/depends_on/d' $WORKDIR/masterfiles/update.cf

## Once the edits are done...


* please make sure your policy is correct by verifying the resultant policy files.

    * verify for syntax errors
      $ /var/cfengine/bin/cf-promises -f /var/cfengine/masterfiles/failsafe.cf
      $ /var/cfengine/bin/cf-promises -f /var/cfengine/masterfiles/promises.cf

    * if there is no error, please run failsafe to start up all CFEngine processes
      $ /var/cfengine/bin/cf-agent -f /var/cfengine/masterfiles/failsafe.cf -IK

    * We highly recommend cosmetic re-work of the resulting policy to ensure readability. See our new 3.0.0 framework in /var/cfengine/share/NovaBase

    * You should keep all control bodies (body agent/executor/server/hub/reporter/monitor/runagent control) and server access_rule() bundle to at least have some suggested attributes

 * If you have ever added your custom-built promises to /var/cfengine/bin/masterfiles/failsafe.cf or /var/cfengine/masterfiles/update.cf?":

    * you should synchronize the contents in failsafe.cf and update.cf manually. 

     *** For example; the promiser "/var/cfengine/bin/mongod <parameters>" in bundle update in update.cf: please change it to run in file-based configuration mode (this bundle is called update_policy in the 3.0.0 policy framework) .
       
       vars:

        "mongodb_dir"        string => "$(sys.workdir)/state",
                            comment => "Directory where MongoDB files will be stored on hub - if changed: requires DB shutdown and move of files",
                             handle => "cfe_internal_update_policy_mongodb_dir";

        "mongodb_conf_file"  string => translatepath("$(inputs_dir)/failsafe/mongod.conf"),
                            comment => "Path to MongoDB configuration file",
                             handle => "cfe_internal_update_policy_mongodb_conf_file";

       commands:

        !windows.am_policy_hub.start_mongod::
        
         "/var/cfengine/bin/mongod --dbpath $(update_policy.mongodb_dir) --config $(update_policy.mongodb_conf_file) > /dev/null < /dev/null 2>&1"

    * some contents of your current bundle agent update_bins in update.cf might be outdated. Please keep it similar to `/var/cfengine/share/NovaBase/failsafe/update_bins.cf` as much as possible.

## Something went wrong - how can I rollback my binary version and configuration?

 * remove /var/cfengine/masterfiles and /var/cfengine/inputs directories
 * rename /var/cfengine/masterfiles_$(date) to /var/cfengine/masterfiles
 * remove the 3.5.0 cfengine-nova-hub package
 * reinstall your previous cfengine packages
 * rebootstrap the HUB. MP should be up and running in less than 10 minutes



## Upgrade procedure for the hosts

For host upgrades there are 2 approaches: manual or automatic upgrade.

### Manual

Update cfengine-nova on each client by rpm, dpkg or corresponding Windows command. For Linux/UNIX systems, update cf-twin as follows:

    $ cp -vf /var/cfengine/bin/cf-agent /var/cfengine/bin/cf-twin

For Windows systems copy/overwrite the content of `C:\Program Files\Cfengine\bin` to `C:\Program Files\Cfengine\bin-twin`

### Automatic

On the hub, copy the client cfengine-nova packages to the operating system specific distribution directories in `/var/cfengine/master_software_updates` and CFEngine 3 Enterprise will take care of the rest.

#Known Issues

Policy file parser is stricter in CFEngine 3.5.0 . The parser is now fully compliant with the CFEngine [language syntax reference](https://cfengine.com/tmp_docs/manuals-language-concepts.html) The main difference you will encounter is that promiser/promisee no longer allows a comma at the end of the line. This will cause your existing policies to produce errors when they are read by CFEngine 3.5.0. 

An example of what you might see as a result of this issue can be found below:

```cf3
/var/cfengine/inputs/CFE_hub_specific.cf:621:28: error: syntax error
Q: ".../cf-execd"":    "/usr/sbin/a2enmod php5",
Q: ".../cf-execd"":                            ^
Q: ".../cf-execd"": /var/cfengine/inputs/CFE_hub_specific.cf:621:28: error: Expected attribute, got ','
Q: ".../cf-execd"":    "/usr/sbin/a2enmod php5",
Q: ".../cf-execd"":                            ^
```

This can be remedied by editing the policy and removing the comma at the end of the appropriate promiser/promisee line.

###Agent package upgrade through the hub from v2.2.3
Please note that although it is possible to upgrade agents through the hub, for Debian format (.deb) packages (both x86_64 and i386) it is necessary to edit your update.cf on each agent before proceeding. The reason for this is that the naming convention used in 2.2.3 is at odds with the one that has since been adopted by CFEngine and in the wider community. As a result, the update.cf script in v2.2.3 clients expects i686 (hard coded) and x86_64 for the architecture part in the package name. So package upgrade will only work for .deb packages if the package is renamed before it is copied into the relevant architecture subdirectory under /var/cfengine/master_software_updates. For example, if your upgrade package is named like this:

cfengine-nova_3.5.0XXXX_amd64.deb or cfengine-nova_3.5.0XXXX_i386.deb

you should rename them so they look like this:

cfengine-nova_3.5.0XXXX_x86_64.deb or cfengine-nova_3.5.0XXXX_i686.deb

 *before* copying them into 

/var/cfengine/master_software_updates/<arch subdirectory> on the hub


