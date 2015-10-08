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

Normally most files can be replaced with new ones, the only ones that are likely changed by you are *def.cf* and *promises.cf*.
For these two files, we would need to do a diff between your version and the new version and integrate the diff instead of replacing the whole file.

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
  * ```
    rpm -i cfengine-nova-hub-3.7.0.x86_64.rpm # Red Hat based distribution
    ```
  * ```
    dpkg --install cfengine-nova-hub_3.7.0-1_amd64.deb # Debian based distribution
    ``` 
3. Copy the merged masterfiles from the perparation you did above.
  * ```
    rm -rf /var/cfengine/masterfiles/*
    ```
  * ```
    cp /root/3.7/masterfiles/* /var/cfengine/masterfiles/
    ```
4. Bootstrap the Policy Server to itself.

    ```
    /var/cfengine/bin/cf-agent -B <POLICY-SERVER-IP>
    ```

    Any  error messages regarding processes can be corrected by running
    
    ```
    cf-agent -f update.cf -IK
    ```
5. Take the Policy Server online.
  * Verify with `cf-key -s` that connections from all clients have been established within 5-10 minutes.
  * Select some clients to confirm that they have received the new policy and are running it without error.


## Prepare Client upgrade (all versions)

1. Make client packages available on the Policy Server in
   `/var/cfengine/master_software_updates`, under the appropriate directories
   for the OS distributions you use.
2. Turn on the auto-upgrade policy by setting the `trigger_upgrade` class. Set
   `masterfiles/controls/VER/update_def.cf` or the `augments_file` also known
   as `def.json` for a small set of clients. For example in the appropriate
   `update_def.cf` file(s) change `!any`  to an appropriate class like an IP
   network `ipv4_10_10_1|ipv4_10_10_2` or in `def.json` 

   ```json
   {
      "classes": {
       "trigger_upgrade": [ "ipv4_10_10_1", "ipv4_10_10_2" ]
      }
   }
   ```

3. Verify that the selected hosts are upgrading successfully.

    As an Enterprise user, confirm that the hosts start appearing in Mission Portal after 5-10 minutes. Otherwise, log manually into a set of hosts to confirm the successful upgrade.

## Complete Client upgrade (all versions) ##

1. Widen the group of hosts on which the `trigger_upgrade` class is set.
2. Continue to verify from `cf-key -s` or in the Enterprise Mission Portal that hosts are upgraded correctly and start reporting in.
3. Verify that the list of hosts you captured before the upgrade, e.g. in `/root/3.6/hosts` correspond to what you see is now reporting in.
