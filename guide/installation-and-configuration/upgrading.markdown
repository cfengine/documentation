---
layout: default
title: Upgrading
published: true
sorting: 30
---

This guide documents our recommendation on how to upgrade an existing
installation of CFEngine Enterprise to {{site.cfengine.branch}}. Community users
can use these instructions as a guide skipping the parts that are not relevant.

In short, the steps are:

1. [Backup][Upgrading#Backup]
2. [Masterfiles Policy Framework upgrade][Upgrading#Masterfiles Policy Framework upgrade]
3. [Enterprise Hub binary upgrade][Upgrading#Enterprise Hub binary upgrade]
4. [Agent binary upgrade][Upgrading#Agent binary upgrade]

**Notes:**

- Upgrades are supported from any [currently supported version][supported versions].

- Clients should not run *newer* versions of binaries than the hub. While it may
  work in many cases, Enterprise reporting does not currently guarantee forward
  compatibility. For example, a host running 3.15.0 will not be able to report
  to a hub running 3.12.3.

## Backup

Backups are made during the hub package upgrade, but it's prudent to take a full
backup from your policy hub before making any changes so that you can recover if
anything goes wrong.

1. Stop the CFEngine services.

   For systemd managed systems:

   ```console
   root@hub:~# systemctl stop cfengine3
   ```

   For SysVinit:

    ```console
   root@hub:~# service cfengine3 stop
   ```

2. Create an archive containing **all** cfengine information.

   Ensure you have enough disk space where your backup archive will be created.

   ```console
   root@hub:~# tar -czf /tmp/$(date +%Y-%m-%d)-cfengine-full-backup.tar.gz /var/cfengine /opt/cfengine
   ```

   For systemd managed systems:

   ```console
   root@hub:~# find /usr/lib/systemd -name 'cf-*' -o -name 'cfengine*' | tar cfz /tmp/$(date +%Y-%m-%d)-cfengine-systemd-backup.tar.gz -T -
   ```

   For SysVinit:

   ```console
   root@hub:~# find /etc -name 'cfengine*' | tar cfz /tmp/$(date +%Y-%m-%d)-cfengine-init-backup.tar.gz -T -
   ```

   **See also:** [Hub administration backup and restore][Backup and Restore]

3. Copy the archive to a safe location.

4. Start the CFEngine services.

   For systemd managed systems:

   ```console
   root@hub:~# systemctl start cfengine3
   ```

   For SysVinit:

    ```console
   root@hub:~# service cfengine3 start
   ```

## Masterfiles Policy Framework upgrade

The Masterfiles Policy Framework is available in the hub package, separately on
the [download page](http://cfengine.com/community/download/), or directly from
the [masterfiles repository on github](https://github.com/cfengine/masterfiles).

Normally most files can be replaced with new ones, files that typically contain
user modifications include `promises.cf`, `controls/*.cf`, and
`services/main.cf`.

- [Masterfiles Policy Framework Upgrade Tutorial][Masterfiles Policy Framework Upgrade]

Once the Masterfiles Policy Framework has been qualified and distributed to all
agents you are ready to begin binary upgrades.

## Enterprise Hub binary upgrade

1. Ensure the CFEngine services are **running**

   For systemd managed systems:

   ```console
   root@hub:~# systemctl start cfengine3
   ```

   For SysVinit:

    ```console
   root@hub:~# service cfengine3 start
   ```

2. Install the new Enterprise Hub package (you may need to adjust the package
   name based on CFEngine edition, version and distribution). By default,
   backups made during upgrade are placed in `/var/cfengine/state/pg/backup`,
   this can be overridden by **exporting** `BACKUP_DIR` before package upgrade.

   **Red Hat/CentOS:**

   ```console
   root@hub:~# export BACKUP_DIR="/mnt/plenty-of-free-space"
   root@hub:~# rpm -U cfengine-nova-hub-{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}.el6.x86_64.rpm
   ```

   **Debian/Ubuntu:**

   ```console
   root@hub:~# export BACKUP_DIR="/mnt/plenty-of-free-space"
   root@hub:~# dpkg --install cfengine-nova-hub_{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}_amd64-deb7.deb
   ```

   *Community does not have a hub specific package.*

3. Check `/var/log/CFEngine-Install.log` for errors.

4. Run the policy on the hub several times or wait for the system to converge.

   ```console
   root@hub:~# for i in 1 2 3; do /var/cfengine/bin/cf-agent -KIf update.cf; /var/cfengine/bin/cf-agent -KI; done
   ```

## Agent binary upgrade

1. Publish binary packages under
   `/var/cfengine/master_software_updates/$(sys.flavor)_$(sys.arch)/` on the
   policy server. To automatically download packages for all supported platforms
   execute the self upgrade policy with the
   `cfengine_master_software_content_state_present` class defined.

   For example:

   ```console
   root@hub:~# cf-agent -KIf standalone_self_upgrade.cf --define cfengine_master_software_content_state_present
   ```

2. Define the `trigger_upgrade` class to allow hosts to attempt self upgrade. In
   this example hosts with IPv4 addresses in 192.0.2.0/24 or 203.0.113.0/24
   network range, or hosts running cfengine 3.10.x except for cfengine 3.10.2.
   It's recommended to start with a small scope, and gradually increase until
   all hosts are upgraded.

   ```json
   {
      "classes": {
       "trigger_upgrade": [
         "ipv4_192_0_2",
         "ipv4_203_0_13",
         "cfengine_3_10_(?!2$)\d+"
       ]
      }
   }
   ```

   **Note:** The negative look ahead regular expression is useful because it
   automatically turns off on hosts after they reach the target version.

3. Verify that the selected hosts are upgrading successfully.

   - Mission Portal [Inventory reporting interface][Reporting UI#Inventory Management]
     ![Inventory Management](Reports-Inventory-1.png)

   - [Inventory API][Inventory API]

     ```console
     root@hub:~# curl -k \
     --user <admin>:<password> \
     -X POST \
     https://hub.localdomain/api/inventory  \
     -H 'content-type: application/json' \
     -d '{
           "sort":"Host name",
           "filter":{
              "CFEngine version":{
                 "not_match":"{{site.cfengine.branch}}.0"
              }
           },
           "select":[
              "Host name",
              "CFEngine version"
            ]
         }'
     ```

   Once all hosts have been upgraded ensure the `trigger_upgrade` class is no
   longer defined so that agents stop trying to self upgrade.
