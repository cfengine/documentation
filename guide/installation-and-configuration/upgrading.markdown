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

## Upgrade the Masterfiles Policy Framework

We would however still recommend to perform a masterfiles upgrade (ideally in a
test environment first) to get all the enhancements and fixes.

The Masterfiles Policy Framework is available in the hub package, separately on
the [download page](http://cfengine.com/community/download/), or directly from
the [masterfiles repository on github](https://github.com/cfengine/masterfiles).

Normally most files can be replaced with new ones, files that typically contain
user modifications include `promises.cf`, `controls/*.cf`, and
`services/main.cf`.

Once the Masterfiles Policy Framework has been upgraded, deployed and verified
working as expected against the current infrastructure you are ready to upgrade
the binaries on the Policy Server.

- [Masterfiles Policy Framework Upgrade Tutorial][`Masterfiles Policy Framework Upgrade`]

## Upgrade Policy Server (3.7 to {{site.cfengine.branch}}.X)

1. Make a backup of the Policy Server, a full backup of `/var/cfengine` (or
   your `WORKDIR` equivalent) is recommended.
   * Stop the CFEngine services.
   * Verify that the output of `ps -e | grep cf` is empty.
   * `cp -r /var/cfengine/ppkeys/ /root/3.7/ppkeys`
   * `tar cvzf /root/3.7/cfengine.tar.gz /var/cfengine`

2. Save the list of hosts currently connecting to the Policy Server.
   * `cf-key -s > /root/3.7/hosts`

3. Install the new CFEngine Policy Server package (you may need to adjust the
   package name based on CFEngine edition, version and distribution).
   * `rpm -U cfengine-nova-hub-{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}.x86_64.rpm` # Red Hat based distribution
   * `dpkg --install cfengine-nova-hub_{{site.cfengine.branch}}.{{site.cfengine.latest_patch_release}}-{{site.cfengine.latest_package_build}}_amd64.deb` # Debian based distribution
   * Check `/var/log/CFEngineHub-Install.log` for errors.
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

4. Bootstrap the Policy Server to itself.

    ```
    /var/cfengine/bin/cf-agent -B <POLICY-SERVER-IP>
    ```

    Any  error messages regarding processes can be corrected by running

    ```
    cf-agent -f update.cf -IK
    ```

5. Start CFEngine services.
   * Verify with `cf-key -s` that connections from all clients have been
     established within 5-10 minutes.

If everything looks good, you are ready to upgrade the clients, please skip to
Prepare Client upgrade (all versions) followed by Complete Client upgrade (all
versions) below.

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
