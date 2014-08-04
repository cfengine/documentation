---
layout: default
title: Upgrading to 3.6
published: true
sorting: 30
---

This guide documents our recommendation on how to upgrade an existing installation of CFEngine Community 3.4/3.5 and CFEngine Enterprise 3.0/3.5 to CFEngine 3.6.1.

Our recommendation is to upgrade the Policy Server first. The rationale is that it is normally a dedicated machine with no business-relevant duties, so the risk is lower.

## Prepare the Policy Server upgrade

1. Merge your masterfiles with the CFEngine 3.6 policy framework.

  * The 3.6 masterfiles can be found in a clean installation of CFEngine (hub package on Enterprise), under /var/cfengine/masterfiles
  * Apply your existing masterfiles on top of the 3.6 masterfiles and save it to a well-known location, e.g. `/root/3.6/masterfiles`
  * Use `cf-promises` to verify that the policy runs with both your previous version of CFEngine (3.0 or 3.5) and with 3.6
  * The merged masterfiles should now be based on the 3.6 framework, include your policies and work on both the version you are upgrading from and with 3.6
2. Set `trustkeysfrom` to trust all hosts, or at least the Policy Server, 
    in the merged masterfiles policy, e.g. /root/3.6/masterfiles/update/update_policy.cf`.

    CFEngine 3.6 uses LMDB for local databases, whereas older versions of CFEngine typically use TokyoCabinet or QDBM. The classic networking protocol uses the `lastseen` database to verify that the mapping between a peer's IP address and the corresponding hostkey is not changed. Since the 3.6 installation will not have any mappings in the lastseen database, hosts won't trust the IP address of the policy server without that setting.
3. Optional, Enterprise only: Export the data from your existing Enterprise MongoDB

  * Download the [`cfmigrate`](http://s3.amazonaws.com/cfengine.package-repos/tools/cfmigrate) binary
  * This binary will export user/role settings as well as long-living file-changes data from MongoDB
  * No other data will be exported, as it would either way expire after
    one week. If you need continued access to 3.5 compliance data,
    keep the 3.5 MongoDB available
  * The `cfmigrate` tool uses `mongoexport`, which is available from [mongodb.org](http://www.mongodb.org/downloads) (it is included in the hub package of CFEngine 3.5)
4. Stop CFEngine services (on the Policy Server only)

  * `service cfengine3 stop`
  * Verify that the output of `ps -e | grep cf` is empty

    Clients will continue to execute the policy that they have.
5. Make a backup of the Policy Server, a full backup of `/var/cfengine` (or your `WORKDIR` equivalent) is recommended.
 * `cp -r /var/cfengine/ppekys/ /root/3.5/ppkeys`
 * `tar cvzf /root/3.5/cfengine.tar.gz /var/cfengine`
6. Save the list of hosts currently connecting to the Policy Server.

  * `cf-key -s > /root/3.5/hosts`
    

## Perform the upgrade of the Policy Server

1. Ensure the CFEngine services are still stopped (only on the Policy Server).
  * Verify that the output of `ps -e | grep cf` is empty
2. Uninstall the previous CFEngine package to start fresh (you may need to adjust the package name based on the CFEngine edition).
  * ```console
    rpm -e cfengine-nova-hub # Red Hat based distribution
    ```
  * ```console
    dpkg -p cfengine-nova-hub # Debian based distribution
    ``` 
  * ```console
    rm -rf /var/cfengine
    ```
3. Install the new CFEngine Policy Server package (you may need to adjust the package name based on CFEngine edition, version and distribution).
  * ```console
    rpm -i cfengine-nova-hub-3.6.1.x86_64.rpm # Red Hat based distribution
    ```
  * ```console
    dpkg --install cfengine-nova-hub_3.6.1-1_amd64.deb # Debian based distribution
    ``` 
4. Restore ppkeys and any Enterprise license file (default location is /var/cfengine/masterfiles/license.dat) from backup.
  * ```console
    cp /root/3.5/ppkeys/* /var/cfengine/ppkeys/
    ```
5. Copy the merged masterfiles from the perparation you did above.
  * ```console
    rm -rf /var/cfengine/masterfiles/*
    ```
  * ```console
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
7. Optional: Import data previously exported from MongoDB.

  * Verify that users can log into Mission Portal
8. Take the Policy Server online.

  * Verify with `cf-key -s` that connections from all clients have been established within 5-10 minutes
  * Select some clients to confirm that they have received the new policy and are running it without error


## Prepare Client upgrade

1. Make client packages available in `master_software_updates`, under the appropriate directories for the OS distributions you use.
2. Turn on the auto-upgrade policy by setting class `trigger_update` in `update.cf` for a small set of clients, i.e. change `!any` to an appropriate class like an IP network (e.g. `10_10_1|10_10_2`).
3. Verify that the selected hosts are upgrading successfully.

    As an Enterprise user, confirm that the hosts start appearing in Mission Portal after 5-10 minutes. Otherwise, log manually into a set of hosts to confirm the successful upgrade.

## Complete Client upgrade

1. Widen the group of hosts on which the `trigger_update` class is set.
2. Continue to verify from `cf-key -s` or in the Enterprise Mission Portal that hosts are upgraded correctly and start reporting in.
3. Verify that the list of hosts you captured before the upgrade, e.g. in `/root/3.5/hosts` correspond to what you see is now reporting in.

## Finalize

1. Reset the `trustkeysfrom` configuration to the previous value, typically an empty list.
2. Optional: Switch to the new 3.6 networking protocol to benefit from TLS encryption and 
    improved control attributes in `access` promises.

    See [`protocol_version`][Components and Common Control#protocol_version] in
    [Components and Common Control][] and [`allowlegacyconnects`][cf-serverd#allowlegacyconnects] in
    [`body server control`][cf-serverd#Control Promises].
