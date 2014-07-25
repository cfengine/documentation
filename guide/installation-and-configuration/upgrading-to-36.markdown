---
layout: default
title: Upgrading to 3.6
published: false
sorting: 30
---

This guide documents our recommendation on how to upgrade an existing installation of CFEngine 3.6.0 or earlier to CFEngine 3.6.1. Upgrading of hosts and of the Enteprise hub and policy server is covered. If you are using a Community installation, you can skip the Enterprise specific parts on the policy server.

Our recommendation is to upgrade the policy server first. The rationale being that this is a dedicated machine with no business-relevant duties, and that the typically mission-critical client machines in your data center can continue to operate based on the policy they have, without connectivity to the policy server.

## Prepare the Hub/Policy Server upgrade

1. Set `trustkeysfrom` to trust all hosts, or at least the policy server, 
    in the masterfiles policy (`update/update_policy.cf`), and deploy that
    policy to all hosts

    CFEngine 3.6 uses LMDB for local databases, whereas older versions of CFEngine typically use TokyoCabinet or QDBM. The classic networking protocol uses the `lastseen` database to verify that the mapping between a peer's IP address and the corresponding hostkey is not changed. Since the 3.6 installation will not have any mappings in the lastseen database, hosts won't trust the IP address of the policy server without that setting.

2. take the hub/policy server offline

    Clients will continue to execute the policy that they have.

3. Make a backup of the hub, esp `/var/cfengine` (or your WORKDIR equivalent)

    In pariticular, make copies of `/var/cfengine/ppkeys` and the license keys that can easily be restored after the upgrade.

4. Save the list of hosts currently connecting to the hub

    * `cf-key -s > /root/3.5/hosts`

5. Optional: Export the data from your existing Enterprise MongoDB

    * download the [`cfmigrate`]() binary
    * this binary will export user/role settings as well as long-living file-changes data from MongoDB
    * no other data will be exported, as it would either way expire after
      one week. If you need continued access to 3.5 compliance data,
      keep the 3.5 MongoDB available
    * the `cfmigrate` tool uses `mongoexport`, which is available from [mongodb.org](http://www.mongodb.org/downloads) (it is included in the Hub package of CFEngine 3.5)
    
## Perform the upgrade of the Hub/Policy Server


1. Stop CFEngine services

    * `service cfengine3 stop`
    * verify empty output of `ps -e | grep cf`

2. Uninstall previous package installation and start fresh

    ```console
    rpm -e cfengine-nova-hub # or dpkg -p cfengine-nova-hub
    rm -rf /var/cfengine
    ```

3. Install the new CFEngine package

    ```console
    rpm -i ~/cfengine-nova-hub-3.6.1.x86_64.rpm # or dpkg --install
    ```

4. Restore ppkeys and license files from backup

5. Merge your masterfiles with the CFEngine 3.6 policy framework

    * Use `cf-promises` to verify that the policy runs with both the previous version of CFEngine (3.0 or 3.5) and with 3.6
    * You'll need another host running the previous version of CFEngine to confirm this

6. Bootstrap the hub to itself

    ```console
    /var/cfengine/bin/cf-agent -B <HUB-IP>
    ```

    Possible error messages regarding processes can be corrected by running
    
    ```console
    cf-agent -f update.cf -IK
    ```

7. Optional: Import data previously exported from MongoDB

    * Verify that users can log into Mission Portal

8. Take the hub/policy server online

    * verify with `cf-key -s` that connections from all clients have been established within 5-10 minutes
    * select some clients to confirm that they have received the new policy

## Prepare Client upgrade

1. Make client packages available in `master_software_updates`

2. Turn on the auto-upgrade policy by setting class `trigger_update` in `update.cf` for a small set of clients, ie change `!any` to an appropriate
    expression

[%CFEngine_include_snippet(update.cf, Trigger binary, };)]

3. Verify that the selected hosts are upgrading successfully

    As an Enterprise user, confirm that the hosts start appearing in Mission Portal after 5-10 minutes. Otherwise, log manually into a set of hosts to confirm the successful upgrade.

## Complete Client upgrade

1. Widen the group of hosts on which the `trigger_update` class is set

2. Continue to verify in Mission Portal that hosts are upgraded correctly and start reporting in

## Finalize

1. Reset the `trustkeysfrom` configuration to the previous value, typically an empty list

2. Switch to the new 3.6 networking protocol to benefit from TLS encryption and improved control attributes in `access` promises

    See [`protocol_version`][Components and Common Control#protocol_version] in [Components and Common Control][] and `allowlegacyconnects` in `body server control`.

