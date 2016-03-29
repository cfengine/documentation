---
layout: default
title: Upgrading to 3.6
published: true
sorting: 30
---

This guide documents our recommendation on how to upgrade an existing installation of CFEngine Community 3.4/3.5 and CFEngine Enterprise 3.0/3.5 to CFEngine 3.6.1, as well as upgrades from 3.6.

Our recommendation is to upgrade the Policy Server first. The rationale is that it is normally a dedicated machine with no business-relevant duties, so the risk is lower.

## Upgrade masterfiles and Policy Server (3.6.X to 3.6.X+1)

If you are doing a minor-minor 3.6 upgrade (e.g. from 3.6.5 to 3.6.6), the upgrade is easier.
We would however still recommend to perform a masterfiles upgrade (ideally in a test environment first) to get all the enhancements and fixes.
The masterfiles are available in the hub package and separately on the [download page](http://cfengine.com/community/download/) (Community and Enterprise editions share masterfiles as of 3.6).

Normally these new files did not exist in the preivous version or can be completely replaced by the old ones, the only ones that are likely changed by you are *def.cf* and *promises.cf*.
For these two files, we would need to do a diff between your version and the new version and integrade the diff instead of replacing the whole file.

When the new masterfiles have been created and *cf-promises promises.cf* and *cf-promises update.cf* succeeds, you are ready to upgrade the Policy Server. That entails to

* stop the CFEngine services
* upgrade the hub package
* replace /var/cfengine/masterfiles with your new integrated masterfiles
* replace (or merge with your changes) */var/cfengine/state/pg/data/postgresql.conf* with */var/cfengine/share/postgresql/postgresql.conf.cfengine* to update your database configuration.
* start the CFEngine services

Check the version with */var/cfengine/bin/cf-promises -V*, and if you are running Enterprise, the Mission Portal About page.

If your clients get promise failures (not kept) similar to "Can't stat file '/var/cfengine/master_software_updates/cf-upgrade/linux.x86_64/cf-upgrade' on '<SERVER-IP>' in files.copy_from promise" you can download and unpack [cf-upgrade.tar.gz](http://cfengine.package-repos.s3.amazonaws.com/tools/cf-upgrade-for-linux.tar.gz) on your Policy Server. This is caused by a known issue where some host packages lacked this utility, which is resolved in recent versions.

If everything looks good, you are ready to upgrade the clients, please skip to Prepare Client upgrade (all versions) followed by Complete Client upgrade (all versions) below.


## Prepare masterfiles and the Policy Server for upgrade (3.5 to 3.6)

1. Merge your masterfiles with the CFEngine 3.6 policy framework on an infrastructure separate from your existing CFEngine installation.
  * Identify existing modifications to the masterfiles directory.  If patches from version control are unavailable or require verification, a copy of /var/cfengine/masterfiles from a clean installation of your previous version can help identify changes which will need to be applied to a new 3.6 install.
  * The 3.6 masterfiles can be found in a clean installation of CFEngine (hub package on Enterprise), under /var/cfengine/masterfiles.  Apply any customizations against a copy of the 3.6 masterfiles in a well-known location, e.g. `/root/3.6/masterfiles`.
  * Use `cf-promises` to verify that the policy runs with 3.6, by running `cf-promises /root/3.6/masterfiles/promises.cf` and `cf-promises /root/3.6/masterfiles/update.cf`.
  * Use `cf-promises` to verify that the policy runs with you previous version of CFEngine (e.g. 3.5), by running the same commands as above on a node with that CFEngine version.
  * The merged masterfiles should now be based on the 3.6 framework, include your policies and work on both the version you are upgrading from and with 3.6.
2. Set `trustkeysfrom` to trust all hosts, or at least the Policy Server,
    in the merged masterfiles policy, e.g. /root/3.6/masterfiles/update/update_policy.cf`.

    CFEngine 3.6 uses LMDB for local databases, whereas older versions of CFEngine typically use TokyoCabinet or QDBM. The classic networking protocol uses the `lastseen` database to verify that the mapping between a peer's IP address and the corresponding hostkey is not changed. Since the 3.6 installation will not have any mappings in the lastseen database, hosts won't trust the IP address of the policy server without that setting.
3. Optional, Enterprise only: Export the data from your existing Enterprise MongoDB.
  * Download the [`cfmigrate`](http://cfengine.package-repos.s3.amazonaws.com/tools/cfmigrate) binary.
  * This binary will export user/role settings as well as long-living file-changes data from MongoDB.
  * No other data will be exported, as it would either way expire after
    one week. If you need continued access to 3.5 compliance data,
    keep the 3.5 MongoDB available.
  * The `cfmigrate` tool uses `mongoexport`, which is available from [mongodb.org](http://www.mongodb.org/downloads) (it is included in the hub package of CFEngine 3.5).
4. On your existing Policy Server, stop the CFEngine services.
  * `service cfengine3 stop`
  * Verify that the output of `ps -e | grep cf` is empty.

    Clients will continue to execute the policy that they have.
5. Make a backup of the Policy Server, a full backup of `/var/cfengine` (or your `WORKDIR` equivalent) is recommended.
 * `cp -r /var/cfengine/ppkeys/ /root/3.5/ppkeys`
 * `tar cvzf /root/3.5/cfengine.tar.gz /var/cfengine`
6. Save the list of hosts currently connecting to the Policy Server.
  * `cf-key -s > /root/3.5/hosts`


## Perform the upgrade of the Policy Server (3.5 to 3.6)

1. Ensure the CFEngine services are still stopped (only on the Policy Server).
  * Verify that the output of `ps -e | grep cf` is empty.
2. Uninstall the previous CFEngine package to start fresh (you may need to adjust the package name based on the CFEngine edition).
  * Red Hat based distributions:

    ```console
    rpm -e cfengine-nova-hub
    rm -rf /var/cfengine
    ```
  * Debian based distributions:

    ```console
    dpkg -p cfengine-nova-hub
    rm -rf /var/cfengine
    ```
3. Install the new CFEngine Policy Server package (you may need to adjust the package name based on CFEngine edition, version and distribution).
  * Red Hat based distributions:

    ```console
    rpm -i cfengine-nova-hub-3.6.1.x86_64.rpm
    ```
  * Debian based distributions:

    ```console
    dpkg --install cfengine-nova-hub_3.6.1-1_amd64.deb
    ```
4. Restore ppkeys and any Enterprise license file (default location is /var/cfengine/masterfiles/license.dat) from backup.

    ```console
    cp /root/3.5/ppkeys/* /var/cfengine/ppkeys/
    ```
5. Copy the merged masterfiles from the perparation you did above.

    ```console
    rm -rf /var/cfengine/masterfiles/*
    cp /root/3.6/masterfiles/* /var/cfengine/masterfiles/
    ```
6. Bootstrap the Policy Server to itself.

    ```console
    /var/cfengine/bin/cf-agent -B <POLICY-SERVER-IP>
    ```

    Any  error messages regarding processes can be corrected by running

    ```console
    cf-agent -f update.cf -IK
    ```

7. Optional: Import data previously exported from MongoDB using the [`cfmigrate`](http://cfengine.package-repos.s3.amazonaws.com/tools/cfmigrate) binary.
  * Verify that users can log into Mission Portal.

8. Take the Policy Server online.
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
3. Verify that the list of hosts you captured before the upgrade, e.g. in `/root/3.5/hosts` correspond to what you see is now reporting in.

## Finalize (3.5 to 3.6)

1. Reset the `trustkeysfrom` configuration to the previous value, typically an empty list.
2. Optional: Switch to the new 3.6 networking protocol to benefit from TLS encryption and
    improved control attributes in `access` promises.
3. Optional: Recursively purge `*.tcdb` and `*.tcdb.lock` files from `/var/cfengine`

    See [`protocol_version`][Components and Common Control#protocol_version] in
    [Components and Common Control][] and [`allowlegacyconnects`][cf-serverd#allowlegacyconnects] in
    [`body server control`][cf-serverd#Control Promises].
