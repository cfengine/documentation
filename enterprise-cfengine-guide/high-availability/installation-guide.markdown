---
layout: default
published: true
title: Installation Guide
tags: [cfengine enterprise, high availability]
---

## Overview ##

This is tutorial describing installation steps of **CFEngine High Availability** feature. It is suitable for both upgrading existing CFEngine installations to HA and for installing HA from scratch.
Before starting installation we strongly recommend reading CFEngine High Availability overview. More detailed information can be found [here][High Availability].

## Installation procedure ##

As with most High Availability systems, setting it up requires carefully following a series of steps with dependencies on network components. The setup can therefore be error-prone, so if you are a CFEngine Enterprise customer we recommend that you contact support for assistance if you do not feel 100% comfortable of doing this on your own.

Please also make sure you are having valid HA licenses for passive hub so that it will be able to handle all your CFEngine clients in case of failover.

### Hardware configuration and OS pre-configuration steps ###

* CFEngine 3.6.2 hub package for RHEL6 or CentOS6.
* We recommend selecting dedicated interface used for PostgreSQL replication and optionally one for heartbeat.
* We recommend having one shared IP address assigned for interface where MP is accessible (optionally) and one where PostgreSQL replication is configured (mandatory).
* Both active and passive hub machines must be configured so that host names are different.
* Basic hostname resolution works (hub names can be placed in */etc/hosts* or DNS configured).

### Example configuration used in this tutorial ###

In this tutorial we are using following network configuration:

* Two nodes acting as active and passive where active node name is node1 and passive node name is node2.
* Each node having three NICs so that eth0 is used for heartbeat, eth1 is used for PostgreSQL replication and eth2 is used for MP and bootstrapping clients.
* IP addresses configured as follows:

| Node            | eth0         | eth1           | eth2            |
|-----------------|:-------------|:---------------|:----------------|
|node1            | 192.168.0.10 | 192.168.10.10  | 192.168.100.10  |
|node2            | 192.168.0.11 | 192.168.10.11  | 192.168.100.11  |
|node3 (optional) | ---          | 192.168.10.12  | 192.168.100.11  |
|cluster shared   | ---          | 192.168.10.100 | 192.168.100.100 |

Detailed network configuration is shown on the picture below:

![HAGuideNetworkSetup](ha_network_setup.png)


## Installing cluster management tools ##

Before you begin you should have corosync (version 1.4.1 or higher) and pacemaker (version 1.1.10-14.el6_5.3 or higher) installed on both nodes. For your convenience we also recommend having pcs installed. Detailed instructions how to install and set up all components are accessible [here](http://clusterlabs.org/) and [here](http://corosync.github.io/corosync/). Please also note that for RHEL 6 additional components might be needed to establish cluster using recommended by Red Hat option. One of those components is cman.

Once pacemaker and corosync are successfully installed on both nodes please follow steps below to set up it as needed by CFEngine High Availability. Please note that most of those instructions use method recommended by Red Hat High Availability project.

In order to operate cluster, proper fencing must be configured but description how to fence cluster and what mechanism use is out of the scope of this document. For reference please use following guide: 


**IMPORTANT:** please carefully follow the indicators describing if given step should be performed on active, passive or both nodes.

1. Make sure that the hostnames of all nodes nodes are node1, node2 and node3 respectively. Running the command ```uname -n | tr '[A-Z]' '[a-z]'``` should return the correct node name. Make sure that the DNS or entries in /etc/hosts are updated so that hosts can be accessed using their host names.

2. In order to use pcs software to manage cluster create user designated to manage cluster ```passwd hacluster``` on both cluster nodes.

3. Make sure that pcsd demon is started and configure both nodes so that it will be enabled to boot on startup on each node.

    On RHEL 7:
    ```bash
    systemctl start pcsd.service
    systemctl enable pcsd.service
    ```

    On RHEL 6:
    ```bash
    /etc/init.d/pcsd start
    chkconfig pcsd on
    ```

4. Authenticate hacluster user for each node of the cluster. Run below command only form the MASTER node (node1):

    ```bash
    pcs cluster auth node1 node2
    ```

    As a result you should see message similar to one below:
    ```
    Username: hacluster
    Password:
    node1: Authorized
    node2: Authorized
    ````
5. Create cluster executing following command from MASTER node (node1):

    ```bash
    pcs cluster setup --start --name cfcluster node1 node2
    ```

    This will create cfcluster cluster consisting of node1 and node2.

6. Enable the cluster services to start on boot of each of cluster nodes:

    ```bash
    pcs cluster enable --all
    ```

7. At this point cluster should be up and running without any resource and STONITH/fencing configured. Running ```pcs status``` should print something similar to one below.

    ```bash
    Cluster name: cfcluster
    Last updated: Tue Jul  7 09:29:10 2015
    Last change: Fri Jul  3 08:41:24 2015
    Stack: cman
    Current DC: node1 - partition with quorum
    Version: 1.1.11-97629de
    2 Nodes configured
    0 Resources configured

    Online: [ node1 node2 ]

    Full list of resources:
    ```


## PostgreSQL configuration ##

**Before starting this make sure that cluster is not running.**

1. Install CFEngine hub package on both active and passive node.
2. On active node bootstrap hub to itself to start acting as policy server (this step can be skipped if you are upgrading existing installation to High Availability).
3. On passive node bootstrap it to active hub. While bootstrapping trust between both hubs will be established and keys will be exchanged.
4. After successful bootstrapping passive to active bootstrap passive to itself. From now on it will start operate as a hub so that it will be capable to collect reports and serve policy files. Please notice that while bootstrapping passive to itself you can see following message:

    ```
    "R: This host assumes the role of policy server
    R: Updated local policy from policy server
    R: Failed to start the server
    R: Did not start the scheduler
    R: You are running a hard-coded failsafe. Please use the following command instead.
        "/var/cfengine/bin/cf-agent" -f /var/cfengine/inputs/update.cf
    2014-09-29T17:36:24+0000   notice: Bootstrap to '10.100.100.116' completed successfully!"
    ```

5. Configure PostgreSQL on active **active node**:
   1. Create two directories owned by PostgreSQL user: /var/cfengine/state/pg/data/pg_archive and /var/cfengine/state/pg/tmp
   2. Modify *postgresql.conf* configuration file
        
        ```bash
        echo "listen_addresses = '*'
        wal_level = hot_standby
        max_wal_senders=5
        wal_keep_segments = 32
        hot_standby = on
        restart_after_crash = off

        #not needed but makes failover faster and cluster more stable
        checkpoint_segments = 8
        wal_keep_segments = 8
        archive_mode = on
        archive_command = 'cp %p /var/cfengine/state/pg/pg_arch/%f'
        " >> /var/cfengine/state/pg/data/postgresql.conf
        ```

        **NOTE:** In above configuration *wal_keep_segments* value specifies minimum number of segments (16 megabytes each) retained in PostgreSQL WAL logs directory in case a standby server needs to fetch them for streaming replication. It should be adjusted to number of clients handled by CFEngine hub and available disk space. Having installation with 1000 clients handled by CFEngine hub and assuming passive hub should be able to catch up with active one after 24 hours break, the value should be set close to 250 (4 GB of additional disk space).

   3. Modify *pg_hba.conf* configuration file to enable access to PostgreSQL form listed host. Please note that 192.168.10.10, 192.168.10.11 and 192.168.10.12 are IP addresses of node1, node2 and node3 respectively.

        ```bash
        echo "host replication all 192.168.10.10/32 trust
        host replication all 192.168.10.11/32 trust
        #use one below only in case of having 3rd node used as database backup
        host replication all 192.168.10.12/32 trust
        local replication all trust
        host replication all 127.0.0.1/32 trust
        host replication all ::1/128 trust
        " >> /var/cfengine/state/pg/data/pg_hba.conf
        ```

        **IMPORTANT:** Above configuration allows accessing hub with cfpostgres user without any authentication from both cluster nodes. For security reasons we strongly advise to create replication user in PostgreSQL and protect access using password or certificate. What is more we advise using ssl-secured replication instead of described here unencrypted method.

   4. Create PostgreSQL archive directory ```mkdir /var/cfengine/state/pg/pg_arch/``` and make cfpostgres user owner of it ```chown -R cfpostgres:cfpostgres /var/cfengine/state/pg/pg_arch/```. 

        **IMPORTANT:** If archive directory location is different make sure to change archive_command entry in postgresql.conf and restore_command command described later in this doccument.

   5. Adding above changes needs PostgreSQL server to be restarted!

        ```
        cd /tmp && su cfpostgres -c "/var/cfengine/bin/pg_ctl -w -D /var/cfengine/state/pg/data stop -m fast"
        cd /tmp && su cfpostgres -c "/var/cfengine/bin/pg_ctl -w -D /var/cfengine/state/pg/data -l /var/log/postgresql.log start"
        ```

6. Configure PostgreSQL on **passive node**:
   1. Remove PostgreSQL directory running following command `rm -rf /var/cfengine/state/pg/data/*`
   2. Do database backup running `su cfpostgres -c "cd /tmp && /var/cfengine/bin/pg_basebackup -h node1 -U cfpostgres -D /var/cfengine/state/pg/data -X stream -P`
   3. Configure *recovery.conf* file indicating PostgreSQL running as hot-standby replica

        ```
        echo "standby_mode = 'on'
        #192.168.10.100 is the shared over cluster IP address of active/master cluster node
        primary_conninfo = 'host=192.168.10.100 port=5432 user=cfpostgres application_name=node2'
        #not needed by recommended for faster failover and more stable cluster operations
        restore_command = 'cp /var/cfengine/state/pg/pg_arch/%f %p'
        " > /var/cfengine/state/pg/data/recovery.conf
        ```

    **NOTE:** change host and application_name to point to host names of active and passive nodes respectively.

7.  Start PostgreSQL on passive hub using following command:

    ```
    cd /tmp && su cfpostgres -c "/var/cfengine/bin/pg_ctl -w -D /var/cfengine/state/pg/data -l /var/log/postgresql.log start"
    ```

9. Repeat steeps 6 and 7 on node3 if 3rd node is used as database backup.



Verify PostgreSQL status on passive instance running `echo "select pg_is_in_recovery();" | /var/cfengine/bin/psql cfdb`.
Above should return `t` indicating that slave is working in recovery mode.

Verify if passive DB instance is connected to active running following command on active hub `echo "select * from pg_stat_replication;" | /var/cfengine/bin/psql cfdb`.
Above should return one entry indicating that host *node1* is connected to database in streaming replication mode.


### CFEngine configuration ###

**Before starting this step make sure that PostgreSQL is running on both active and passive nodes and passive node is being replicated.**

1. Create HA configuration file on both active and passive hubs like below:

    ```
    echo "cmp_master: PRI
    cmp_slave: HS:async,HS:sync,HS:alone
    cmd: /usr/sbin/crm_attribute -l reboot -n cfpgsql-status -G -q" > /var/cfengine/ha.cfg
    ```

2. Create HA JSON configuration file as below:

    ```
    echo "{
    \"192.168.100.10\":
    {
     \"sha\": \"c14a17325b9a1bdb0417662806f579e4187247317a9e1739fce772992ee422f6\",
     \"internal_ip\": \"192.168.100.10\",
    },
    \"192.168.100.11\":
    {
     \"sha\": \"b492eb4b59541c02a13bd52efe17c6a720e8a43b7c8f8803f3fc85dee7951e4f\",
     \"internal_ip\": \"192.168.100.11\",
    }
    }" > /var/cfengine/masterfiles/cfe_internal/enterprise/ha/ha_info.json
    ```

    The `internal_ip` attribute is the IP address of the hub (the one you used to bootstrapped itself to) and `sha` is the key of the hub. The `sha` key can be found by running `cf-key -s` the on the respective hub and match that to the `internal_ip`.

3. Modify */var/cfengine/masterfiles/def.cf* and enable HA by uncommenting `"enable_cfengine_enterprise_hub_ha" expression => "enterprise_edition";` line (make sure to comment or remove line `"enable_cfengine_enterprise_hub_ha" expression => "!any";`).

4. Run *update.cf* to make sure that new policy is copied from *masterfiles* to *inputs* `cf-agent -f update.cf` on active first and then on passive. From this point on PostgreSQL will not be managed by CFEngine and will be left unmanaged before pgsql cluster resource will be properly configured.


### Cluster resources configuration ###

1. Configure shared cluster IP address used for PostgreSQL database replication.

   ```bash
   pcs resource create cfvirtip IPaddr2 ip=192.168.10.100 cidr_netmask=24 --group cfengine
   ```

   This will create shared IP addredd added to the appropriate interface (where 192.168.10.x address already exists).

2. Verify that cfvirtip resource is properly configured and running.

   ```bash
   [roott@node1] pcs status
   Cluster name: cfcluster
   Last updated: Tue Jul  7 09:29:10 2015
   Last change: Fri Jul  3 08:41:24 2015
   Stack: cman
   Current DC: node1 - partition with quorum
   Version: 1.1.11-97629de
   2 Nodes configured
   1 Resources configured

   Online: [ node1 node2 ]

   Full list of resources:

   Resource Group: cfengine
       cfvirtip   (ocf::heartbeat:IPaddr2):   Started node1 
   ```

    **IMPORTANT** If the fencing is not configured resources might not be started by default. To enable resource start please run one of the following commands ``` pcs cluster enable --all``` or ```pcs resource debug-start cfvirtip```.

2. Stop PostgreSQL on all nodes.

3. Download latest version of PostgreSQL RA as the default one is known to have a bug while using Master/Slave configuration.

    ```bash
    wget https://raw.github.com/ClusterLabs/resource-agents/a6f4ddf76cb4bbc1b3df4c9b6632a6351b63c19e/heartbeat/pgsql
    cp pgsql /usr/lib/ocf/resource.d/heartbeat/
    chmod 755 /usr/lib/ocf/resource.d/heartbeat/pgsql
    ```

4. Create PostgreSQL resource (recommended way with PostgreSQL archive mode enabled).

    ```bash
    pcs resource create cfpgsql pgsql pgctl="/var/cfengine/bin/pg_ctl" psql="/var/cfengine/bin/psql" pgdata="/var/cfengine/state/pg/data" pgdba="cfpostgres" repuser="cfpostgres" tmpdir="/var/cfengine/state/pg/tmp" rep_mode="async" node_list="node1 node2" primary_conninfo_opt="keepalives_idle=60 keepalives_interval=5 keepalives_count=5" master_ip="192.168.10.100" restart_on_promote="true" logfile="/var/log/postgresql.log" config="/var/cfengine/state/pg/data/postgresql.conf" check_wal_receiver=true restore_command="cp /var/cfengine/state/pg/pg_arch/%f %p" op monitor timeout="60s" interval="3s"  on-fail="restart" role="Master" op monitor timeout="60s" interval="4s" on-fail="restart" 
    ```

    You can use following command for minimum setup (no archive enabled): 

    ```bash
    pcs resource create cfpgsql pgsql pgctl="/var/cfengine/bin/pg_ctl" psql="/var/cfengine/bin/psql" pgdata="/var/cfengine/state/pg/data" pgdba="cfpostgres" repuser="cfpostgres" tmpdir="/var/cfengine/state/pg/tmp" rep_mode="async" node_list="node1 node2" primary_conninfo_opt="keepalives_idle=60 keepalives_interval=5 keepalives_count=5" master_ip="192.168.10.100" restart_on_promote="true" logfile="/var/log/postgresql.log" config="/var/cfengine/state/pg/data/postgresql.conf" op monitor timeout="60s" interval="3s"  on-fail="restart" role="Master" op monitor timeout="60s" interval="4s" on-fail="restart" 
    ```

5. Configure PostgreSQL to work in Master/Slave (active/stndby) mode:

    ```bash
    pcs resource master mscfpgsql cfpgsql master-max=1 master-node-max=1 clone-max=2 clone-node-max=1 notify=true
    ```

6. After those steeps clusrter should be up and running. To verify following run one of the commands below.

    ```bash
    [root@node1] pcs status
    Cluster name: cfcluster
    Last updated: Tue Jul  7 10:48:21 2015
    Last change: Fri Jul  3 08:41:24 2015
    Stack: cman
    Current DC: node1 - partition with quorum
    Version: 1.1.11-97629de
    2 Nodes configured
    3 Resources configured

    Online: [ node1 node2 ]

    Full list of resources:

    Resource Group: cfengine
        cfvirtip   (ocf::heartbeat:IPaddr2):   Started node1 
    Master/Slave Set: mscfpgsql [cfpgsql]
         Masters: [ node1 ]
         Slaves: [ node2 ]

    [root@node2 vagrant]# crm_mon -Afr1
    Last updated: Tue Jul  7 10:50:07 2015
    Last change: Tue Jul  7 10:30:03 2015
    Stack: cman
    Current DC: node2 - partition with quorum
    Version: 1.1.11-97629de
    2 Nodes configured
    3 Resources configured

    Online: [ node1 node2 ]

    Full list of resources:

    Resource Group: cfengine
         cfvirtip   (ocf::heartbeat:IPaddr2):   Started node1 
    Master/Slave Set: mscfpgsql [cfpgsql]
         Masters: [ node1 ]
         Slaves: [ node2 ]

    Node Attributes:
        * Node node1:
        + cfpgsql-data-status               : LATEST    
        + cfpgsql-master-baseline           : 000000000B000090
        + cfpgsql-receiver-status           : ERROR     
        + cfpgsql-status                    : PRI       
        + master-cfpgsql                    : 1000      

    * Node node2:
        + cfpgsql-data-status               : STREAMING|ASYNC
        + cfpgsql-receiver-status           : normal    
        + cfpgsql-status                    : HS:alone  
        + master-cfpgsql                    : -INFINITY
    ```

    **IMPORTANT:** Please make sure that *cfpgsql-status* for the active node is reported as *PRI* and passive as *HS:alone* or *HS:async*.

7. **Enjoy your working CFEngine High Availability setup!**


### Troubleshooting ###

1. If either IPaddr2 or pgslq resource is not running try to enable it first ```pcs cluster enable --all```. If this is not causing the resources are being started you can try to run those in debug mode with this command ```pcs resource debug-start <resource-name>```. The later one should print more log message why resources are not started.

2. If ```crm_mon -Afr1``` is printing errors similar to one below

    ```
    [root@node1]# pcs status
    Cluster name: cfcluster
    Last updated: Tue Jul  7 11:27:23 2015
    Last change: Tue Jul  7 11:02:40 2015
    Stack: cman
    Current DC: node1 - partition with quorum
    Version: 1.1.11-97629de
    2 Nodes configured
    3 Resources configured

    Online: [ node1 ]
    OFFLINE: [ node2 ]

    Full list of resources:

     Resource Group: cfengine
         cfvirtip   (ocf::heartbeat:IPaddr2):   Started node1 
     Master/Slave Set: mscfpgsql [cfpgsql]
         Stopped: [ node1 node2 ]

    Failed actions:
        cfpgsql_start_0 on node1 'unknown error' (1): call=13, status=complete, last-rc-change='Tue Jul  7 11:25:32 2015', queued=1ms, exec=137ms
    ```

    you can try to clear the errors using ```pcs resource cleanup <resource-name>``` to clean errors for appropriate resource and make cluster to restart it.

    ```bash
    [root@node1 vagrant]# pcs resource cleanup cfpgsql
    Resource: cfpgsql successfully cleaned up

    [root@node1 vagrant]# pcs status
    Cluster name: cfcluster
    Last updated: Tue Jul  7 11:29:36 2015
    Last change: Tue Jul  7 11:29:08 2015
    Stack: cman
    Current DC: node1 - partition with quorum
    Version: 1.1.11-97629de
    2 Nodes configured
    3 Resources configured

    Online: [ node1 ]
    OFFLINE: [ node2 ]

    Full list of resources:

     Resource Group: cfengine
         cfvirtip   (ocf::heartbeat:IPaddr2):   Started node1 
     Master/Slave Set: mscfpgsql [cfpgsql]
         Masters: [ node1 ]
         Stopped: [ node2 ]
    ```

3. After cluster crush make sure to always start the node that is supposed to be a Master and then the one that should be Slave. If the cluster is not running on the given node after restart you can enable it by running the following command:

    ```bash
    [root@node2 vagrant]# pcs cluster start
    Starting Cluster...
    ```

