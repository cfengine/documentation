---
layout: default
title: Upgrading
published: true
sorting: 30
---

This guide documents our recommendation on how to upgrade an existing
installation of CFEngine Community 3.7 and 3.8 and CFEngine Enterprise 3.7 and 3.8 to
CFEngine {{site.cfengine.branch}}.

We recommend upgrading the Masterfiles Policy Framework first so that you can
verify that the new policy will work with your old clients across the
infrastructure. Once the latest policy has been deployed successfully we
recommend upgrading the Policy Server and finally the remote agents.

Upgrading to {{site.cfengine.branch}} from versions older than 3.7 is more
complicated as some functionality introduced in {{site.cfengine.branch}}
is not compatible with versions 3.6 and earlier.
For more information about upgrading from 3.6 see [Upgrade from 3.6](#upgrade-from-36).

## Upgrade masterfiles and Policy Server ({{site.cfengine.branch}}.X to {{site.cfengine.branch}}.X+1)

If you are doing a minor-minor {{site.cfengine.branch}} upgrade (e.g. from
{{site.cfengine.branch}}.0 to {{site.cfengine.branch}}.1), the upgrade is
easier.

We would however still recommend to perform a masterfiles upgrade (ideally in a
test environment first) to get all the enhancements and fixes.

The Masterfiles Policy Framework is available in the hub package and separately
on the [download page](http://cfengine.com/community/download/)

Normally most files can be replaced with new ones, the only ones that are
likely changed by you are *def.cf* and *promises.cf*.  For these two files, we
would need to do a diff between your version and the new version and integrate
the diff instead of replacing the whole file.

For more detailed information on how to upgrade masterfiles please see Prepare masterfiles for upgrade section below.

When the new masterfiles have been created and *cf-promises promises.cf* and
*cf-promises update.cf* succeeds, you are ready to upgrade the Policy Server.
That entails to

* replace /var/cfengine/masterfiles with your new integrated masterfiles
* stop the CFEngine services
* upgrade the hub package
* replace (or merge with your changes)
  */var/cfengine/state/pg/data/postgresql.conf* with
  */var/cfengine/share/postgresql/postgresql.conf.cfengine* to update your
  database configuration.
* restart the CFEngine services

Check the version with */var/cfengine/bin/cf-promises -V*, and if you are
running Enterprise, the Mission Portal About page.

If your clients get promise failures (not kept) similar to "Can't stat file '/var/cfengine/master_software_updates/cf-upgrade/linux.x86_64/cf-upgrade' on '<SERVER-IP>' in files.copy_from promise" you can download and unpack [cf-upgrade.tar.gz](http://cfengine.package-repos.s3.amazonaws.com/tools/cf-upgrade-for-linux.tar.gz) on your Policy Server. This is caused by a known issue where some host packages lacked this utility, which is resolved in recent versions.

If everything looks good, you are ready to upgrade the clients, please skip to
Prepare Client upgrade (all versions) followed by Complete Client upgrade (all
versions) below.

## Upgrade Policy Server (3.7 to {{site.cfengine.branch}}.X)

1. Make a backup of the Policy Server, a full backup of `/var/cfengine` (or
   your `WORKDIR` equivalent) is recommended.
   * `cp -r /var/cfengine/ppkeys/ /root/3.7/ppkeys`
   * `tar cvzf /root/3.7/cfengine.tar.gz /var/cfengine`

2. Save the list of hosts currently connecting to the Policy Server.
   * `cf-key -s > /root/3.7/hosts`

3. Prepare masterfiles following instructions in the Prepare masterfiles for
   upgrade section below.

4. Copy the merged masterfiles from the preparation you did above.
   * `rm -rf /var/cfengine/masterfiles/*`
   * `cp /root/{{site.cfengine.branch}}/masterfiles/* /var/cfengine/masterfiles/`

5. On your existing Policy Server, stop the CFEngine services.
   * `service cfengine3 stop`
   * Verify that the output of `ps -e | grep cf` is empty.

   **Note:** Clients will continue to execute the policy that they have.

6. Install the new CFEngine Policy Server package (you may need to adjust the
   package name based on CFEngine edition, version and distribution).
   * `rpm -U cfengine-nova-hub-{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}.x86_64.rpm` # Red Hat based distribution
   * `dpkg --install cfengine-nova-hub_{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}_amd64.deb` # Debian based distribution
   * Check `/var/log/CFEngineHub-Install.log/` for errors.
   * Use the following snippet to see potential updates for your `postgresql.conf` and make changes accordingly.

     ```
     # If total memory is lower than 3GB, we use the default pgsql conf file
     # If total memory is beyond 64GB, we use a shared_buffers of 16G
     # Otherwise, we use a shared_buffers equal to 25% of total memory
     total=$(awk '/^MemTotal:.*[0-9]+\skB/ {print $2}' /proc/meminfo)

     echo "$total" | grep -q '^[0-9]\+$'
     if [ $? -ne 0 ] ;then
       echo "Error calculating total memory for setting postgresql shared_buffers";
     else
       upper=$(( 64 * 1024 * 1024 ))  #in KB
       lower=$(( 3 * 1024 * 1024 ))   #in KB

       if [ "$total" -gt "$lower" ]; then
         maint="2GB"
         if [ "$total" -ge "$upper" ]; then
           shared="16GB"
           effect="11GB"        #70% of 16G
         else
           shared=$(( $total * 25 / 100 / 1024 ))   #in MB
           shared="$shared""MB"
           effect=$(( $total * 70 / 100 / 1024 ))   #in MB
           effect="$effect""MB"
         fi
         sed -i -e "s/^.effective_cache_size.*/effective_cache_size=$effect/" /var/cfengine/share/postgresql/postgresql.conf.cfengine
         sed -i -e "s/^shared_buffers.*/shared_buffers=$shared/" /var/cfengine/share/postgresql/postgresql.conf.cfengine
         sed -i -e "s/^maintenance_work_mem.*/maintenance_work_mem=$maint/" /var/cfengine/share/postgresql/postgresql.conf.cfengine
         diff -u /var/cfengine/state/pg/data/postgresql.conf /var/cfengine/share/postgresql/postgresql.conf.cfengine
       else
         echo "Warning: not enough total memory needed to set shared_buffers=2GB"
       fi
     fi
     ```

7. Bootstrap the Policy Server to itself (this step might not be needed if
   Policy Server is reporting correctly).

    ```
    /var/cfengine/bin/cf-agent -B <POLICY-SERVER-IP>
    ```

    Any  error messages regarding processes can be corrected by running

    ```
    cf-agent -f update.cf -IK
    ```

8. Take the Policy Server online.
   * Verify with `cf-key -s` that connections from all clients have been
     established within 5-10 minutes.
   * Select some clients to confirm that they have received the new policy and
     are running it without error.

## Prepare masterfiles for upgrade

1. Merge your masterfiles with the CFEngine {{site.cfengine.branch}} policy framework on an infrastructure separate from your existing CFEngine installation.
2. Identify existing modifications to the masterfiles directory.  If patches from version control are unavailable or require verification, a copy of /var/cfengine/masterfiles from a clean installation of your previous version can help identify changes which will need to be applied to a new {{site.cfengine.branch}} install.
3. The {{site.cfengine.branch}} masterfiles can be found in a clean installation of CFEngine (hub package on Enterprise), under /var/cfengine/masterfiles.  Apply any customizations against a copy of the {{site.cfengine.branch}} masterfiles in a well-known location, e.g. `/root/{{site.cfengine.branch}}/masterfiles`.
4. Use `cf-promises` to verify that the policy runs with {{site.cfengine.branch}}, by running `cf-promises /root/{{site.cfengine.branch}}/masterfiles/promises.cf` and `cf-promises /root/{{site.cfengine.branch}}/masterfiles/update.cf`.
5. Use `cf-promises` to verify that the policy runs with you previous version of CFEngine (e.g. 3.7), by running the same commands as above on a node with that CFEngine version.
6. The merged masterfiles should now be based on the {{site.cfengine.branch}} framework, include your policies and work on both the version you are upgrading from and with {{site.cfengine.branch}}.

## Upgrade from 3.6

As 3.6 policy is not compatible with {{site.cfengine.branch}} some additional steps must be performed to fulfill the upgrade procedure.

1. Beginning with version 3.9 the [Masterfiles Policy Framework][The Policy Framework] defaults to the new packages promise implementation for inventory of [packages installed][packagesmatching] and [packages updates][packageupdatesmatching]. See [package_inventory][Components and Common Control#package_inventory] in body common control for details on modifying the default sources for package inventory.
   There are `body common control` `package_inventory` and `package_module` attributes which are  not recognized by versions 3.6 and earlier.
   While upgrading from 3.6.x make sure that both are commented, so that existing 3.6.x hosts
   can communicate with the {{site.cfengine.branch}} hub and can validate policy.
   After migrating all the clients to the newest CFEngine version, make sure that both previously commented
   parameters are uncommented so that the new package promise can be used as the default one.


## Prepare Client upgrade (all versions)

1. Make client packages available on the Policy Server in
   `/var/cfengine/master_software_updates`, under the appropriate directories
   for the OS distributions you use.
2. Turn on the auto-upgrade policy by setting the `trigger_upgrade` class. Set
   `masterfiles/controls/CLIENT_VER/update_def.cf` (where CLIENT_VER is the minor version your clients are on, e.g. 3.7)
   or the `augments_file` (also known as `def.json`) for a small set of clients. For example in the appropriate
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

    As an Enterprise user, confirm that the hosts start appearing in Mission Portal after 5-10 minutes. The easiest way to do this is to use an Inventory Report and add the "CFEngine Version" column. Otherwise, log manually into a set of hosts to confirm the successful upgrade.

## Complete Client upgrade (all versions) ##

1. Widen the group of hosts on which the `trigger_upgrade` class is set.
2. Continue to verify from `cf-key -s` or in the Enterprise Mission Portal that hosts are upgraded correctly and start reporting in.
3. Verify that the list of hosts you captured before the upgrade, e.g. in `/root/3.7/hosts` correspond to what you see is now reporting in.


## Optional steps

The steps listed here are not necessary unless you have special needs.

### Migrating Mission Portal database

This step is not needed unless you are upgrading from CFEngine 3.8 or lower, to
CFEngine 3.9 or higher, and you are unable to use the automatic migration.

Normally the package upgrade will do the migration for you, but if you have a
very big database, or for other reasons don't have enough space to hold database
backup files in the `/var/cfengine/state/pg` directory, you may perform these
steps manually.

1. Before installing the new version of CFEngine, dump the current content of
   the database to a file using `pg_dump`. You need to do this for each of the
   three databases, like this:

```
su cfpostgres -c "/var/cfengine/bin/pg_dump cfdb > cfdb-backup.sql"
su cfpostgres -c "/var/cfengine/bin/pg_dump cfsettings > cfsettings-backup.sql"
su cfpostgres -c "/var/cfengine/bin/pg_dump cfmp > cfmp-backup.sql"
```

2. Shut down CFEngine and then delete or move the `/var/cfengine/state/pg/data`
   directory in order to prevent the automatic migration by the package scripts.

3. Install the new CFEngine package.

4. Restore the database dump into the new PostgreSQL database by running:

```
su cfpostgres -c "/var/cfengine/bin/psql cfdb < cfdb-backup.sql"
su cfpostgres -c "/var/cfengine/bin/psql cfsettings < cfsettings-backup.sql"
su cfpostgres -c "/var/cfengine/bin/psql cfmp < cfmp-backup.sql"
```
