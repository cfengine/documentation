---
layout: default
title: Upgrading to 3.7
published: true
sorting: 30
---

This guide documents our recommendation on how to upgrade an existing installation of CFEngine Community 3.5/3.6 and CFEngine Enterprise 3.5/3.6 to CFEngine 3.7.0.

Our recommendation is to upgrade the Policy Server first. The rationale is that it is normally a dedicated machine with no business-relevant duties, so the risk is lower.

## Upgrade masterfiles and Policy Server (3.7.X to 3.7.X+1)

If you are doing a minor-minor 3.7 upgrade (e.g. from 3.7.0 to 3.7.1), the upgrade is easier.
We would however still recommend to perform a masterfiles upgrade (ideally in a test environment first) to get all the enhancements and fixes.
The masterfiles are available in the hub package and separately on the [download page](http://cfengine.com/community/download/) (Community and Enterprise editions share masterfiles as of 3.6).

From 3.6.1 to 3.6.5, the following masterfiles files have changed:

* cfe_internal/CFE_cfengine.cf
* cfe_internal/CFE_hub_specific.cf
* cfe_internal/CFE_knowledge.cf
* cfe_internal/cfengine_processes.cf
* cfe_internal/core/deprecated/cfengine_processes.cf
* cfe_internal/core/host_info_report.cf
* cfe_internal/core/limit_robot_agents.cf
* cfe_internal/core/log_rotation.cf
* cfe_internal/core/main.cf
* cfe_internal/enterprise/CFE_hub_specific.cf
* cfe_internal/enterprise/CFE_knowledge.cf
* cfe_internal/enterprise/file_change.cf
* cfe_internal/enterprise/ha/ha.cf
* cfe_internal/enterprise/ha/ha_def.cf
* cfe_internal/enterprise/ha/ha_info.json
* cfe_internal/enterprise/main.cf
* cfe_internal/ha/ha.cf
* cfe_internal/ha/ha_def.cf
* cfe_internal/ha/ha_info.json
* cfe_internal/host_info_report.cf
* cfe_internal/update/cfe_internal_dc_workflow.cf
* cfe_internal/update/cfe_internal_local_git_remote.cf
* cfe_internal/update/cfe_internal_update_from_repository.cf
* cfe_internal/update/update_bins.cf
* cfe_internal/update/update_policy.cf
* cfe_internal/update/update_processes.cf
* controls/3.4/cf_serverd.cf
* controls/3.5/cf_agent.cf
* controls/3.5/cf_execd.cf
* controls/3.5/cf_hub.cf
* controls/3.5/cf_monitord.cf
* controls/3.5/cf_runagent.cf
* controls/3.5/cf_serverd.cf
* controls/3.5/def.cf
* controls/3.5/reports.cf
* controls/3.5/update_def.cf
* controls/3.6/cf_agent.cf
* controls/3.6/cf_execd.cf
* controls/3.6/cf_hub.cf
* controls/3.6/cf_monitord.cf
* controls/3.6/cf_runagent.cf
* controls/3.6/cf_serverd.cf
* controls/3.6/def.cf
* controls/3.6/reports.cf
* controls/3.6/update_def.cf
* controls/3.7/cf_agent.cf
* controls/3.7/cf_execd.cf
* controls/3.7/cf_hub.cf
* controls/3.7/cf_monitord.cf
* controls/3.7/cf_runagent.cf
* controls/3.7/cf_serverd.cf
* controls/3.7/def.cf
* controls/3.7/reports.cf
* controls/3.7/update_def.cf
* controls/cf_agent.cf
* controls/cf_execd.cf
* controls/cf_hub.cf
* controls/cf_monitord.cf
* controls/cf_runagent.cf
* controls/cf_serverd.cf
* def.cf
* example_def.json
* inventory/any.cf
* inventory/freebsd.cf
* inventory/linux.cf
* inventory/redhat.cf
* lib/3.5/cfe_internal.cf
* lib/3.5/common.cf
* lib/3.5/files.cf
* lib/3.5/packages.cf
* lib/3.5/paths.cf
* lib/3.5/reports.cf
* lib/3.6/autorun.cf
* lib/3.6/cfe_internal.cf
* lib/3.6/cfe_internal_hub.cf
* lib/3.6/common.cf
* lib/3.6/files.cf
* lib/3.6/packages.cf
* lib/3.6/paths.cf
* lib/3.6/reports.cf
* lib/3.6/services.cf
* lib/3.6/stdlib.cf
* lib/3.6/storage.cf
* lib/3.7/autorun.cf
* lib/3.7/bundles.cf
* lib/3.7/cfe_internal.cf
* lib/3.7/cfe_internal_hub.cf
* lib/3.7/cfengine_enterprise_hub_ha.cf
* lib/3.7/commands.cf
* lib/3.7/common.cf
* lib/3.7/databases.cf
* lib/3.7/edit_xml.cf
* lib/3.7/examples.cf
* lib/3.7/feature.cf
* lib/3.7/files.cf
* lib/3.7/guest_environments.cf
* lib/3.7/monitor.cf
* lib/3.7/packages.cf
* lib/3.7/paths.cf
* lib/3.7/processes.cf
* lib/3.7/services.cf
* lib/3.7/stdlib.cf
* lib/3.7/storage.cf
* lib/3.7/users.cf
* lib/3.7/vcs.cf
* libraries/cfengine_stdlib.cf
* modules/packages/apt_get
* modules/packages/yum
* promises.cf
* services/autorun.cf
* services/file_change.cf
* services/main.cf
* sketches/meta/api-runfile.cf
* update.cf
* update/cfe_internal_dc_workflow.cf
* update/cfe_internal_local_git_remote.cf
* update/cfe_internal_update_from_repository.cf
* update/update_bins.cf
* update/update_policy.cf
* update/update_processes.cf

Normally most files can be replaced with new ones, the only ones that are likely changed by you are *def.cf* and *promises.cf*.
For these two files, we would need to do a diff between your version and the new version and integrade the diff instead of replacing the whole file.

When the new masterfiles have been created and *cf-promises promises.cf* and *cf-promises update.cf* succeeds, you are ready to upgrade the Policy Server. That entails to

* stop the CFEngine services
* upgrade the hub package
* replace /var/cfengine/masterfiles with your new integrated masterfiles
* replace (or merge with your changes) */var/cfengine/state/pg/data/postgresql.conf* with */var/cfengine/share/postgresql/postgresql.conf.cfengine* to update your database configuration.
* restart the CFEngine services

Check the version with */var/cfengine/bin/cf-promises -V*, and if you are running Enterprise, the Mission Portal About page.

If your clients get promise failures (not kept) similar to "Can't stat file '/var/cfengine/master_software_updates/cf-upgrade/linux.x86_64/cf-upgrade' on '<SERVER-IP>' in files.copy_from promise" you can download and unpack [cf-upgrade.tar.gz](http://cfengine.package-repos.s3.amazonaws.com/tools/cf-upgrade-for-linux.tar.gz) on your Policy Server. This is caused by a known issue where some host packages lacked this utility, which is resolved in recent versions.

If everything looks good, you are ready to upgrade the clients, please skip to Prepare Client upgrade (all versions) followed by Complete Client upgrade (all versions) below.


## Prepare masterfiles and the Policy Server for upgrade (3.6 to 3.7)

1. Merge your masterfiles with the CFEngine 3.7 policy framework on an infrastructure separate from your existing CFEngine installation.
  * Identify existing modifications to the masterfiles directory.  If patches from version control are unavailable or require verification, a copy of /var/cfengine/masterfiles from a clean installation of your previous version can help identify changes which will need to be applied to a new 3.7 install.
  * The 3.7 masterfiles can be found in a clean installation of CFEngine (hub package on Enterprise), under /var/cfengine/masterfiles.  Apply any customizations against a copy of the 3.7 masterfiles in a well-known location, e.g. `/root/3.7/masterfiles`.
  * Use `cf-promises` to verify that the policy runs with 3.7, by running `cf-promises /root/3.7/masterfiles/promises.cf` and `cf-promises /root/3.7/masterfiles/update.cf`.
  * Use `cf-promises` to verify that the policy runs with you previous version of CFEngine (e.g. 3.6), by running the same commands as above on a node with that CFEngine version.
  * The merged masterfiles should now be based on the 3.7 framework, include your policies and work on both the version you are upgrading from and with 3.7.
2. On your existing Policy Server, stop the CFEngine services.
  * `service cfengine3 stop`
  * Verify that the output of `ps -e | grep cf` is empty.

    Clients will continue to execute the policy that they have.
3. Make a backup of the Policy Server, a full backup of `/var/cfengine` (or your `WORKDIR` equivalent) is recommended.
 * `cp -r /var/cfengine/ppkeys/ /root/3.6/ppkeys`
 * `tar cvzf /root/3.6/cfengine.tar.gz /var/cfengine`
4. Save the list of hosts currently connecting to the Policy Server.
  * `cf-key -s > /root/3.6/hosts`
    

## Perform the upgrade of the Policy Server (3.6 to 3.7)

1. Ensure the CFEngine services are still stopped (only on the Policy Server).
  * Verify that the output of `ps -e | grep cf` is empty.
2. Install the new CFEngine Policy Server package (you may need to adjust the package name based on CFEngine edition, version and distribution).
  * ```console
    rpm -i cfengine-nova-hub-3.7.0.x86_64.rpm # Red Hat based distribution
    ```
  * ```console
    dpkg --install cfengine-nova-hub_3.7.0-1_amd64.deb # Debian based distribution
    ``` 
3. Copy the merged masterfiles from the perparation you did above.
  * ```console
    rm -rf /var/cfengine/masterfiles/*
    ```
  * ```console
    cp /root/3.7/masterfiles/* /var/cfengine/masterfiles/
    ```
4. Bootstrap the Policy Server to itself.

    ```console
    /var/cfengine/bin/cf-agent -B <POLICY-SERVER-IP>
    ```

    Any  error messages regarding processes can be corrected by running
    
    ```console
    cf-agent -f update.cf -IK
    ```
5. Take the Policy Server online.
  * Verify with `cf-key -s` that connections from all clients have been established within 5-10 minutes.
  * Select some clients to confirm that they have received the new policy and are running it without error.


## Prepare Client upgrade (all versions)

1. Make client packages available on the Policy Server in `/var/cfengine/master_software_updates`, under the appropriate directories for the OS distributions you use.
2. Turn on the auto-upgrade policy by setting class `trigger_upgrade` in `update.cf` for a small set of clients, i.e. change `!any` to an appropriate class like an IP network (e.g. `ipv4_10_10_1|ipv4_10_10_2`).
3. Verify that the selected hosts are upgrading successfully.

    As an Enterprise user, confirm that the hosts start appearing in Mission Portal after 5-10 minutes. Otherwise, log manually into a set of hosts to confirm the successful upgrade.

## Complete Client upgrade (all versions) ##

1. Widen the group of hosts on which the `trigger_upgrade` class is set.
2. Continue to verify from `cf-key -s` or in the Enterprise Mission Portal that hosts are upgraded correctly and start reporting in.
3. Verify that the list of hosts you captured before the upgrade, e.g. in `/root/3.6/hosts` correspond to what you see is now reporting in.
