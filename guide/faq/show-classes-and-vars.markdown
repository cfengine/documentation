---
layout: default
title: How can I tell what Classes and Variables are defined?
published: true
sorting: 90
tags: [getting started, installation, faq]
---

You can see a high level overview of the first order classes and variables using
`cf-promises --show-classes` and `cf-promises --show-vars`.

Both of those commands will take an optional regular expression you can use to
filter the classes or variables. For example `cf-promises --show-classes=MT`
will show all the classes that contain `MT` like `GMT_July`.

You can see the variables and namespace scoped classes defined at the end of an
agent execution by using the ```--show-evaluated-vars``` or
```--show-evaluated-classes``` options to `cf-agent`. In addition to the
variables and classes shown by `cf-promsies --show-classes` or `cf-promises
--show-vars` this will show variables and namespace scoped classes that get
defined during a full agent run where the system may be modified and more policy
is evaluated.

# Show first order classes with cf-promises

```console
[root@hub ~]# cf-promises --show-classes
Class name                                                   Meta tags
10_0_2_15                                                    inventory,attribute_name=none,source=agent,hardclass
127_0_0_1                                                    inventory,attribute_name=none,source=agent,hardclass
192_168_33_2                                                 inventory,attribute_name=none,source=agent,hardclass
2_cpus                                                       source=agent,derived-from=sys.cpus,hardclass
64_bit                                                       source=agent,hardclass
Day26                                                        time_based,source=agent,hardclass
GMT_Day26                                                    time_based,source=agent,hardclass
GMT_Hr01                                                     time_based,source=agent,hardclass
GMT_Hr01_Q1                                                  time_based,source=agent,hardclass
GMT_Hr1                                                      time_based,source=agent,hardclass
GMT_July                                                     time_based,source=agent,hardclass
GMT_Lcycle_0                                                 time_based,source=agent,hardclass
GMT_Min05_10                                                 time_based,source=agent,hardclass
GMT_Min08                                                    time_based,source=agent,hardclass
GMT_Night                                                    time_based,source=agent,hardclass
GMT_Q1                                                       time_based,source=agent,hardclass
GMT_Tuesday                                                  time_based,source=agent,hardclass
GMT_Yr2016                                                   time_based,source=agent,hardclass
Hr01                                                         time_based,source=agent,hardclass
Hr01_Q1                                                      time_based,source=agent,hardclass
Hr1                                                          time_based,source=agent,hardclass
July                                                         time_based,source=agent,hardclass
Lcycle_0                                                     time_based,source=agent,hardclass
Min05_10                                                     time_based,source=agent,hardclass
Min08                                                        time_based,source=agent,hardclass
Night                                                        time_based,source=agent,hardclass
PK_SHA_30017fd4f85914d0fa2d8c733958b5508d8383363d937e6385a41629e06ca1ca inventory,attribute_name=none,source=agent,derived-from=sys.key_digest,hardclass
Q1                                                           time_based,source=agent,hardclass
Tuesday                                                      time_based,source=agent,hardclass
Yr2016                                                       time_based,source=agent,hardclass
_have_bin_env                                                source=promise
_stdlib_has_path_awk                                         source=promise
_stdlib_has_path_bc                                          source=promise
_stdlib_has_path_cat                                         source=promise
_stdlib_has_path_chkconfig                                   source=promise
_stdlib_has_path_cksum                                       source=promise
_stdlib_has_path_createrepo                                  source=promise
_stdlib_has_path_crontab                                     source=promise
_stdlib_has_path_crontabs                                    source=promise
_stdlib_has_path_curl                                        source=promise
_stdlib_has_path_cut                                         source=promise
_stdlib_has_path_dc                                          source=promise
_stdlib_has_path_df                                          source=promise
_stdlib_has_path_diff                                        source=promise
_stdlib_has_path_dig                                         source=promise
_stdlib_has_path_domainname                                  source=promise
_stdlib_has_path_echo                                        source=promise
_stdlib_has_path_egrep                                       source=promise
_stdlib_has_path_env                                         source=promise
_stdlib_has_path_ethtool                                     source=promise
_stdlib_has_path_find                                        source=promise
_stdlib_has_path_free                                        source=promise
_stdlib_has_path_getfacl                                     source=promise
_stdlib_has_path_git                                         source=promise
_stdlib_has_path_grep                                        source=promise
_stdlib_has_path_groupadd                                    source=promise
_stdlib_has_path_groupdel                                    source=promise
_stdlib_has_path_hostname                                    source=promise
_stdlib_has_path_ifconfig                                    source=promise
_stdlib_has_path_init                                        source=promise
_stdlib_has_path_ip                                          source=promise
_stdlib_has_path_iptables                                    source=promise
_stdlib_has_path_iptables_save                               source=promise
_stdlib_has_path_logger                                      source=promise
_stdlib_has_path_ls                                          source=promise
_stdlib_has_path_lsattr                                      source=promise
_stdlib_has_path_lsof                                        source=promise
_stdlib_has_path_netstat                                     source=promise
_stdlib_has_path_nologin                                     source=promise
_stdlib_has_path_npm                                         source=promise
_stdlib_has_path_perl                                        source=promise
_stdlib_has_path_ping                                        source=promise
_stdlib_has_path_pip                                         source=promise
_stdlib_has_path_printf                                      source=promise
_stdlib_has_path_realpath                                    source=promise
_stdlib_has_path_rpm                                         source=promise
_stdlib_has_path_sed                                         source=promise
_stdlib_has_path_service                                     source=promise
_stdlib_has_path_shadow                                      source=promise
_stdlib_has_path_sort                                        source=promise
_stdlib_has_path_svc                                         source=promise
_stdlib_has_path_sysctl                                      source=promise
_stdlib_has_path_systemctl                                   source=promise
_stdlib_has_path_tar                                         source=promise
_stdlib_has_path_test                                        source=promise
_stdlib_has_path_tr                                          source=promise
_stdlib_has_path_useradd                                     source=promise
_stdlib_has_path_userdel                                     source=promise
_stdlib_has_path_virtualenv                                  source=promise
_stdlib_has_path_wc                                          source=promise
_stdlib_has_path_wget                                        source=promise
_stdlib_has_path_yum                                         source=promise
_stdlib_path_exists_awk                                      source=promise
_stdlib_path_exists_cat                                      source=promise
_stdlib_path_exists_chkconfig                                source=promise
_stdlib_path_exists_cksum                                    source=promise
_stdlib_path_exists_crontab                                  source=promise
_stdlib_path_exists_crontabs                                 source=promise
_stdlib_path_exists_curl                                     source=promise
_stdlib_path_exists_cut                                      source=promise
_stdlib_path_exists_df                                       source=promise
_stdlib_path_exists_diff                                     source=promise
_stdlib_path_exists_domainname                               source=promise
_stdlib_path_exists_echo                                     source=promise
_stdlib_path_exists_egrep                                    source=promise
_stdlib_path_exists_env                                      source=promise
_stdlib_path_exists_ethtool                                  source=promise
_stdlib_path_exists_find                                     source=promise
_stdlib_path_exists_free                                     source=promise
_stdlib_path_exists_getfacl                                  source=promise
_stdlib_path_exists_git                                      source=promise
_stdlib_path_exists_grep                                     source=promise
_stdlib_path_exists_groupadd                                 source=promise
_stdlib_path_exists_groupdel                                 source=promise
_stdlib_path_exists_hostname                                 source=promise
_stdlib_path_exists_ifconfig                                 source=promise
_stdlib_path_exists_init                                     source=promise
_stdlib_path_exists_ip                                       source=promise
_stdlib_path_exists_iptables                                 source=promise
_stdlib_path_exists_iptables_save                            source=promise
_stdlib_path_exists_logger                                   source=promise
_stdlib_path_exists_ls                                       source=promise
_stdlib_path_exists_lsattr                                   source=promise
_stdlib_path_exists_netstat                                  source=promise
_stdlib_path_exists_nologin                                  source=promise
_stdlib_path_exists_perl                                     source=promise
_stdlib_path_exists_printf                                   source=promise
_stdlib_path_exists_rpm                                      source=promise
_stdlib_path_exists_sed                                      source=promise
_stdlib_path_exists_service                                  source=promise
_stdlib_path_exists_shadow                                   source=promise
_stdlib_path_exists_sort                                     source=promise
_stdlib_path_exists_svc                                      source=promise
_stdlib_path_exists_sysctl                                   source=promise
_stdlib_path_exists_tar                                      source=promise
_stdlib_path_exists_test                                     source=promise
_stdlib_path_exists_tr                                       source=promise
_stdlib_path_exists_useradd                                  source=promise
_stdlib_path_exists_userdel                                  source=promise
_stdlib_path_exists_wc                                       source=promise
_stdlib_path_exists_wget                                     source=promise
_stdlib_path_exists_yum                                      source=promise
am_policy_hub                                                source=bootstrap,deprecated,alias=policy_server,hardclass
any                                                          source=agent,hardclass
centos                                                       inventory,attribute_name=none,source=agent,hardclass
centos_6                                                     inventory,attribute_name=none,source=agent,hardclass
centos_6_5                                                   inventory,attribute_name=none,source=agent,hardclass
cfengine                                                     inventory,attribute_name=none,source=agent,hardclass
cfengine_3                                                   inventory,attribute_name=none,source=agent,hardclass
cfengine_3_7                                                 inventory,attribute_name=none,source=agent,hardclass
cfengine_3_7_3                                               inventory,attribute_name=none,source=agent,hardclass
cfengine_in_high                                             monitoring,source=environment,hardclass
cfengine_internal_agent_email                                source=promise
cfengine_internal_masterfiles_update                         source=augments_file,hardclass
cfengine_internal_rotate_logs                                source=promise
cfengine_out_high                                            monitoring,source=environment,hardclass
common                                                       cfe_internal,source=agent,hardclass
compiled_on_linux_gnu                                        source=agent,hardclass
cpu0_high                                                    monitoring,source=environment,hardclass
cpu1_high                                                    monitoring,source=environment,hardclass
cpu_high                                                     monitoring,source=environment,hardclass
disable_inventory_LLDP                                       source=promise
disable_inventory_cmdb                                       source=promise
disable_inventory_dmidecode                                  source=promise
disable_inventory_lsb                                        source=promise
diskfree_high_normal                                         monitoring,source=environment,hardclass
enable_cfe_internal_cleanup_agent_reports                    source=promise
enterprise                                                   inventory,attribute_name=none,source=agent,hardclass
enterprise_3                                                 inventory,attribute_name=none,source=agent,hardclass
enterprise_3_7                                               inventory,attribute_name=none,source=agent,hardclass
enterprise_3_7_3                                             inventory,attribute_name=none,source=agent,hardclass
enterprise_edition                                           inventory,attribute_name=none,source=agent,hardclass
entropy_misc_in_low                                          monitoring,source=environment,hardclass
entropy_misc_out_low                                         monitoring,source=environment,hardclass
fe80__a00_27ff_fe9a_9853                                     inventory,attribute_name=none,source=agent,hardclass
fe80__a00_27ff_fefb_e685                                     inventory,attribute_name=none,source=agent,hardclass
feature                                                      source=agent,hardclass
feature_def                                                  source=agent,hardclass
feature_def_json                                             source=agent,hardclass
feature_def_json_preparse                                    source=agent,hardclass
feature_xml                                                  source=agent,hardclass
feature_yaml                                                 source=agent,hardclass
has_proc_1_cmdline                                           source=promise
hub                                                          inventory,attribute_name=none,source=agent,derived-from=sys.fqhost,hardclass
io_writes_high                                               monitoring,source=environment,hardclass
io_writtendata_high                                          monitoring,source=environment,hardclass
ipv4_10                                                      inventory,attribute_name=none,source=agent,hardclass
ipv4_10_0                                                    inventory,attribute_name=none,source=agent,hardclass
ipv4_10_0_2                                                  inventory,attribute_name=none,source=agent,hardclass
ipv4_10_0_2_15                                               inventory,attribute_name=none,source=agent,hardclass
ipv4_127                                                     inventory,attribute_name=none,source=agent,hardclass
ipv4_127_0                                                   inventory,attribute_name=none,source=agent,hardclass
ipv4_127_0_0                                                 inventory,attribute_name=none,source=agent,hardclass
ipv4_127_0_0_1                                               inventory,attribute_name=none,source=agent,hardclass
ipv4_192                                                     inventory,attribute_name=none,source=agent,hardclass
ipv4_192_168                                                 inventory,attribute_name=none,source=agent,hardclass
ipv4_192_168_33                                              inventory,attribute_name=none,source=agent,hardclass
ipv4_192_168_33_2                                            inventory,attribute_name=none,source=agent,hardclass
linux                                                        inventory,attribute_name=none,source=agent,derived-from=sys.class,hardclass
linux_2_6_32_431_el6_x86_64                                  source=agent,derived-from=sys.sysname,derived-from=sys.release,hardclass
linux_x86_64                                                 source=agent,derived-from=sys.sysname,derived-from=sys.machine,hardclass
linux_x86_64_2_6_32_431_el6_x86_64                           source=agent,derived-from=sys.sysname,derived-from=sys.machine,derived-from=sys.release,hardclass
linux_x86_64_2_6_32_431_el6_x86_64__1_SMP_Fri_Nov_22_03_15_09_UTC_2013 source=agent,derived-from=sys.long_arch,hardclass
loadavg_high_ldt                                             source=persistent
localhost                                                    inventory,attribute_name=none,source=agent,based-on=sys.fqhost,hardclass
localhost4                                                   inventory,attribute_name=none,source=agent,based-on=sys.fqhost,hardclass
localhost4_localdomain4                                      inventory,attribute_name=none,source=agent,based-on=sys.fqhost,hardclass
localhost_localdomain                                        inventory,attribute_name=none,source=agent,based-on=sys.fqhost,hardclass
mac_08_00_27_9a_98_53                                        inventory,attribute_name=none,source=agent,hardclass
mac_08_00_27_fb_e6_85                                        inventory,attribute_name=none,source=agent,hardclass
mem_cached_high_normal                                       monitoring,source=environment,hardclass
mem_free_high_normal                                         monitoring,source=environment,hardclass
mem_freeswap_high_normal                                     monitoring,source=environment,hardclass
mem_swap_high_normal                                         monitoring,source=environment,hardclass
mem_total_high_normal                                        monitoring,source=environment,hardclass
messages_high_ldt                                            monitoring,source=environment,hardclass,source=persistent
messages_high_normal                                         monitoring,source=environment,hardclass
net_iface_eth0                                               source=agent,hardclass
net_iface_eth1                                               source=agent,hardclass
net_iface_lo                                                 source=agent,hardclass
nova                                                         inventory,attribute_name=none,source=agent,hardclass
nova_3                                                       inventory,attribute_name=none,source=agent,hardclass
nova_3_7                                                     inventory,attribute_name=none,source=agent,hardclass
nova_3_7_3                                                   inventory,attribute_name=none,source=agent,hardclass
nova_edition                                                 source=agent,hardclass
otherprocs_high_normal                                       monitoring,source=environment,hardclass
policy_server                                                inventory,attribute_name=CFEngine roles,source=bootstrap,hardclass
postgres_in_normal                                           monitoring,source=environment,hardclass
postgres_out_high                                            monitoring,source=environment,hardclass
postgresql_maintenance_supported                             source=promise
redhat                                                       inventory,attribute_name=none,source=agent,hardclass
redhat_derived                                               source=promise,inventory,attribute_name=none
rootprocs_high_normal                                        monitoring,source=environment,hardclass
services_autorun                                             source=augments_file,hardclass
specific_linux_os                                            source=promise
ssh_in_high                                                  monitoring,source=environment,hardclass
users_high                                                   monitoring,source=environment,hardclass
www_in_normal                                                monitoring,source=environment,hardclass
wwws_in_high                                                 monitoring,source=environment,hardclass
x86_64                                                       source=agent,derived-from=sys.machine,hardclass
```

# Show first order variables with cf-promises

```console
[root@hub ~]# cf-promises --show-vars
   error: readjson: data error parsing JSON file '/var/cfengine/inputs/cf_promises_validated': No data
   error: readjson: data error parsing JSON file '/var/cfengine/inputs/cf_promises_validated': No data
   error: readjson: data error parsing JSON file '/var/cfengine/inputs/cf_promises_validated': No data
   error: readjson: data error parsing JSON file '/var/cfengine/inputs/cf_promises_validated': No data
   error: readjson: data error parsing JSON file '/var/cfengine/inputs/cf_promises_validated': No data
   error: readjson: data error parsing JSON file '/var/cfengine/inputs/cf_promises_validated': No data
   error: readjson: data error parsing JSON file '/var/cfengine/inputs/cf_promises_validated': No data
   error: readjson: data error parsing JSON file '/var/cfengine/inputs/cf_promises_validated': No data
Variable name                            Variable value                                               Meta tags
default:access_rules.def#cf_runagent_shell /bin/sh                                                      source=agent
default:access_rules.def#dir_bin         /var/cfengine/bin                                            source=agent
default:access_rules.def#dir_masterfiles /var/cfengine/masterfiles                                    source=agent
default:access_rules.def#dir_modules     /var/cfengine/modules                                        source=agent
default:access_rules.def#dir_plugins     /var/cfengine/plugins                                        source=agent
default:access_rules.def#dir_software    /var/cfengine/master_software_updates                        source=agent
default:apache_sudoer.def#cf_apache_user cfapache                                                     source=agent
default:apache_sudoer.sys#bindir         /var/cfengine/bin                                            source=agent
default:append_user_field.val             {'@(allusers)'}                                             source=promise
default:autorun.bundles                   {'default:inventory_policy','default:hello_world_autorun','default:copy_from_unless_file_exists'} source=promise
default:autorun.sorted_bundles            {'default:copy_from_unless_file_exists','default:hello_world_autorun','default:inventory_policy'} source=promise
default:bundles_common.inputs             {'/var/cfengine/inputs/lib/3.7/paths.cf','/var/cfengine/inputs/lib/3.7/files.cf','/var/cfengine/inputs/lib/3.7/commands.cf'} source=promise
default:cfe_autorun_inventory_LLDP.inventory_control#lldpctl_exec /usr/bin/lldpctl                                             source=agent
default:cfe_autorun_inventory_cmdb.cmdb_dir /var/cfengine/cmdb                                           source=promise,cmdb
default:cfe_autorun_inventory_cmdb.cmdb_file /var/cfengine/cmdb/me.json                                   source=promise,cmdb
default:cfe_autorun_inventory_cmdb.sys#policy_hub 192.168.33.2                                                 source=agent
default:cfe_autorun_inventory_cmdb.sys#workdir /var/cfengine                                                source=agent
default:cfe_autorun_inventory_cpuinfo.const#dollar $                                                            source=agent
default:cfe_autorun_inventory_disk.free  96.00                                                        source=promise,inventory,attribute_name=Disk free (%)
default:cfe_autorun_inventory_disk.mon#value_diskfree 96.00                                                        source=agent
default:cfe_autorun_inventory_dmidecode.dmidefs <non-printable>                                              source=promise
default:cfe_autorun_inventory_dmidecode.dmivars  {'bios-vendor','bios-version','system-serial-number','system-manufacturer','system-version'} source=promise
default:cfe_autorun_inventory_dmidecode.inventory_control#dmidecoder /usr/sbin/dmidecode                                          source=agent
default:cfe_autorun_inventory_fstab.sys#fstab /etc/fstab                                                   source=agent
default:cfe_autorun_inventory_ipv4_addresses.filter_reg 127\.0\.0\.1                                                 source=promise
default:cfe_autorun_inventory_ipv4_addresses.ipv4[10.0.2.15] 10.0.2.15                                                    source=promise,inventory,attribute_name=IPv4 addresses
default:cfe_autorun_inventory_ipv4_addresses.ipv4[192.168.33.2] 192.168.33.2                                                 source=promise,inventory,attribute_name=IPv4 addresses
default:cfe_autorun_inventory_ipv4_addresses.ipv4_addresses  {'10.0.2.15','192.168.33.2'}                                source=promise
default:cfe_autorun_inventory_listening_ports.ports  {'22','80','111','443','5308','5432','6379','50349','53437'} source=promise,inventory,attribute_name=Ports listening
default:cfe_autorun_inventory_loadaverage.mon#value_loadavg 0.01                                                         source=agent
default:cfe_autorun_inventory_loadaverage.value 0.01                                                         source=promise,report
default:cfe_autorun_inventory_memory.free 37.57                                                        source=promise,report
default:cfe_autorun_inventory_memory.mon#value_mem_free 37.57                                                        source=agent
default:cfe_autorun_inventory_memory.mon#value_mem_total 490.29                                                       source=agent
default:cfe_autorun_inventory_memory.total 490.29                                                       source=promise,inventory,attribute_name=Memory size (MB)
default:cfe_autorun_inventory_mtab.inventory_control#mtab /etc/mtab                                                    source=agent
default:cfe_autorun_inventory_packages.paths#path[yum] /usr/bin/yum                                                 source=agent
default:cfe_autorun_inventory_packages.paths#rpm /bin/rpm                                                     source=agent
default:cfe_autorun_inventory_packages.paths#sed /bin/sed                                                     source=agent
default:cfe_autorun_inventory_packages.refresh 0                                                            source=promise
default:cfe_autorun_inventory_packages.sys#workdir /var/cfengine                                                source=agent
default:cfe_autorun_inventory_proc.basefiles  {'consoles','cpuinfo','modules','partitions','version'}     source=promise
default:cfe_autorun_inventory_proc.files[consoles] /proc/consoles                                               source=promise
default:cfe_autorun_inventory_proc.files[cpuinfo] /proc/cpuinfo                                                source=promise
default:cfe_autorun_inventory_proc.files[modules] /proc/modules                                                source=promise
default:cfe_autorun_inventory_proc.files[partitions] /proc/partitions                                             source=promise
default:cfe_autorun_inventory_proc.files[version] /proc/version                                                source=promise
default:cfe_autorun_inventory_proc.inventory_control#proc /proc                                                        source=agent
default:cfe_internal_cleanup_agent_reports.def#max_client_history_size 52428800                                                     source=agent
default:cfe_internal_cleanup_agent_reports.diff_files  {'/var/cfengine/state/diff/classes.diff','/var/cfengine/state/diff/execution_log.diff','/var/cfengine/state/diff/lastseen.diff','/var/cfengine/state/diff/variables.diff'} source=promise
default:cfe_internal_cleanup_agent_reports.files  {'/var/cfengine/state/diff/classes.diff','/var/cfengine/state/diff/execution_log.diff','/var/cfengine/state/diff/lastseen.diff','/var/cfengine/state/diff/variables.diff','/var/cfengine/state/promise_log/1469492995.csv','/var/cfengine/state/promise_log/1469493207.csv','/var/cfengine/state/promise_log/1469493481.csv','/var/cfengine/state/promise_log/1469493814.csv','/var/cfengine/state/promise_log/1469494086.csv','/var/cfengine/state/promise_log/1469494420.csv','/var/cfengine/state/promise_log/1469494693.csv','/var/cfengine/state/promise_log/1469495026.csv','/var/cfengine/state/promise_log/1469495299.csv'} source=promise
default:cfe_internal_cleanup_agent_reports.promise_log_files  {'/var/cfengine/state/promise_log/1469492995.csv','/var/cfengine/state/promise_log/1469493207.csv','/var/cfengine/state/promise_log/1469493481.csv','/var/cfengine/state/promise_log/1469493814.csv','/var/cfengine/state/promise_log/1469494086.csv','/var/cfengine/state/promise_log/1469494420.csv','/var/cfengine/state/promise_log/1469494693.csv','/var/cfengine/state/promise_log/1469495026.csv','/var/cfengine/state/promise_log/1469495299.csv'} source=promise
default:cfe_internal_cleanup_agent_reports.reports_size[/var/cfengine/state/diff/classes.diff] 14449                                                        source=promise
default:cfe_internal_cleanup_agent_reports.reports_size[/var/cfengine/state/diff/execution_log.diff] 11551                                                        source=promise
default:cfe_internal_cleanup_agent_reports.reports_size[/var/cfengine/state/diff/lastseen.diff] 4284                                                         source=promise
default:cfe_internal_cleanup_agent_reports.reports_size[/var/cfengine/state/diff/variables.diff] 104277                                                       source=promise
default:cfe_internal_cleanup_agent_reports.reports_size[/var/cfengine/state/promise_log/1469492995.csv] 1309                                                         source=promise
default:cfe_internal_cleanup_agent_reports.reports_size[/var/cfengine/state/promise_log/1469493207.csv] 0                                                            source=promise
default:cfe_internal_cleanup_agent_reports.reports_size[/var/cfengine/state/promise_log/1469493481.csv] 0                                                            source=promise
default:cfe_internal_cleanup_agent_reports.reports_size[/var/cfengine/state/promise_log/1469493814.csv] 859                                                          source=promise
default:cfe_internal_cleanup_agent_reports.reports_size[/var/cfengine/state/promise_log/1469494086.csv] 0                                                            source=promise
default:cfe_internal_cleanup_agent_reports.reports_size[/var/cfengine/state/promise_log/1469494420.csv] 0                                                            source=promise
default:cfe_internal_cleanup_agent_reports.reports_size[/var/cfengine/state/promise_log/1469494693.csv] 508                                                          source=promise
default:cfe_internal_cleanup_agent_reports.reports_size[/var/cfengine/state/promise_log/1469495026.csv] 0                                                            source=promise
default:cfe_internal_cleanup_agent_reports.reports_size[/var/cfengine/state/promise_log/1469495299.csv] 0                                                            source=promise
default:cfe_internal_cleanup_agent_reports.sys#workdir /var/cfengine                                                source=agent
default:cfe_internal_cleanup_agent_reports.tmpmap  {'0','104277','0','859','0','0','1309','508','14449','0','0','11551','4284'} source=promise
default:cfe_internal_common.inputs        {'/var/cfengine/inputs/lib/3.7/common.cf','/var/cfengine/inputs/lib/3.7/commands.cf'} source=promise
default:cfe_internal_database_cleanup_consumer_status.remove_query DELETE FROM status WHERE ts IN (SELECT ts FROM status ORDER BY ts DESC OFFSET $(row_count)); source=promise
default:cfe_internal_database_cleanup_consumer_status.sys#bindir /var/cfengine/bin                                            source=agent
default:cfe_internal_database_cleanup_diagnostics.index  {'cf_null'}                                                 source=promise
default:cfe_internal_database_cleanup_diagnostics.sys#bindir /var/cfengine/bin                                            source=agent
default:cfe_internal_database_cleanup_promise_log.cleanup_query_notkept SELECT promise_log_partition_cleanup(\'NOTKEPT\', \'1 day\'); source=promise
default:cfe_internal_database_cleanup_promise_log.cleanup_query_repaired SELECT promise_log_partition_cleanup(\'REPAIRED\', \'$(history_length_days) day\'); source=promise
default:cfe_internal_database_cleanup_promise_log.sys#bindir /var/cfengine/bin                                            source=agent
default:cfe_internal_database_cleanup_reports.index  {'cf_null'}                                                 source=promise
default:cfe_internal_database_cleanup_reports.sys#bindir /var/cfengine/bin                                            source=agent
default:cfe_internal_database_partitioning.promise_outcome  {'REPAIRED','NOTKEPT'}                                      source=promise
default:cfe_internal_database_partitioning.query_create_promise_log_NOTKEPT SELECT promise_log_partition_create(NOW() - INTERVAL \'7 day\', 7 + 3, \'NOTKEPT\'); source=promise
default:cfe_internal_database_partitioning.query_create_promise_log_REPAIRED SELECT promise_log_partition_create(NOW() - INTERVAL \'7 day\', 7 + 3, \'REPAIRED\'); source=promise
default:cfe_internal_database_partitioning.sys#bindir /var/cfengine/bin                                            source=agent
default:cfe_internal_httpd_related.sys#workdir /var/cfengine                                                source=agent
default:cfe_internal_httpd_related.tcp_port 80                                                           source=promise
default:cfe_internal_hub_common.inputs    {'/var/cfengine/inputs/lib/3.7/common.cf','/var/cfengine/inputs/lib/3.7/commands.cf'} source=promise
default:cfe_internal_hub_maintain.diagnostics_settings <non-printable>                                              source=promise
default:cfe_internal_hub_maintain.report_settings <non-printable>                                              source=promise
default:cfe_internal_hub_vars.docroot    /var/cfengine/httpd/htdocs                                   source=promise
default:cfe_internal_hub_vars.sys#workdir /var/cfengine                                                source=agent
default:cfe_internal_inputs.input[cfe_internal_management] cfe_internal/CFE_cfengine.cf                                 source=promise
default:cfe_internal_inputs.input[change_management] cfe_internal/enterprise/file_change.cf                       source=promise
default:cfe_internal_inputs.input[core_host_info_report] cfe_internal/core/host_info_report.cf                        source=promise
default:cfe_internal_inputs.input[core_limit_robot_agents] cfe_internal/core/limit_robot_agents.cf                      source=promise
default:cfe_internal_inputs.input[core_log_rotation] cfe_internal/core/log_rotation.cf                            source=promise
default:cfe_internal_inputs.input[core_main] cfe_internal/core/main.cf                                    source=promise
default:cfe_internal_inputs.input[enterprise_hub_specific] cfe_internal/enterprise/CFE_hub_specific.cf                  source=promise
default:cfe_internal_inputs.input[enterprise_knowledge] cfe_internal/enterprise/CFE_knowledge.cf                     source=promise
default:cfe_internal_inputs.input[enterprise_main] cfe_internal/enterprise/main.cf                              source=promise
default:cfe_internal_inputs.inputs        {'cfe_internal/enterprise/file_change.cf','cfe_internal/enterprise/main.cf','cfe_internal/core/log_rotation.cf','cfe_internal/core/host_info_report.cf','cfe_internal/enterprise/CFE_hub_specific.cf','cfe_internal/enterprise/CFE_knowledge.cf','cfe_internal/core/main.cf','cfe_internal/core/limit_robot_agents.cf','cfe_internal/CFE_cfengine.cf'} source=promise
default:cfe_internal_management.bundles   {'cfe_internal_enterprise_main','cfe_internal_core_main'}   source=promise
default:cfe_internal_management.policy[cfe_internal_core_main] cfe_internal_core_main                                       source=promise
default:cfe_internal_management.policy[cfe_internal_enterprise_main] cfe_internal_enterprise_main                                 source=promise
default:cfe_internal_php_runalerts.runalerts_script /var/cfengine/bin/runalerts.sh                               source=promise
default:cfe_internal_php_runalerts.runalerts_stampfiles_dir /var/cfengine/httpd/php                                      source=promise
default:cfe_internal_php_runalerts.sketch[limit] 300                                                          source=promise
default:cfe_internal_php_runalerts.sketch[name] sketch                                                       source=promise
default:cfe_internal_php_runalerts.sketch[running] 10                                                           source=promise
default:cfe_internal_php_runalerts.sleep_time 60                                                           source=promise
default:cfe_internal_php_runalerts.sql[limit] 300                                                          source=promise
default:cfe_internal_php_runalerts.sql[name] sql                                                          source=promise
default:cfe_internal_php_runalerts.sql[running] 20                                                           source=promise
default:cfe_internal_php_runalerts.stale_time 10                                                           source=promise
default:cfe_internal_php_runalerts.sys#workdir /var/cfengine                                                source=agent
default:cfe_internal_postgresql_maintenance.cf_consumer_pid 1095                                                         source=promise
default:cfe_internal_postgresql_maintenance.sys#bindir /var/cfengine/bin                                            source=agent
default:cfe_internal_postgresql_maintenance.sys#workdir /var/cfengine                                                source=agent
default:cfe_internal_postgresql_maintenance.vacuum_cfdb_cmd /var/cfengine/bin/vacuumdb --full --dbname=cfdb              source=promise
default:cfe_internal_postgresql_vacuum.sys#bindir /var/cfengine/bin                                            source=agent
default:cfe_internal_postgresql_vacuum.vacuum_cfdb_cmd /var/cfengine/bin/vacuumdb --analyze --quiet --dbname=cfdb   source=promise
default:cfe_internal_purge_scheduled_reports_older_than_days.cfe_internal_hub_vars#docroot /var/cfengine/httpd/htdocs                                   source=agent
default:cfe_internal_setup_knowledge.cfe_internal_hub_vars#docroot /var/cfengine/httpd/htdocs                                   source=agent
default:cfe_internal_setup_knowledge.def#cf_apache_group cfapache                                                     source=agent
default:cfe_internal_setup_knowledge.def#cf_apache_user cfapache                                                     source=agent
default:cfe_internal_setup_knowledge.sys#workdir /var/cfengine                                                source=agent
default:cfe_internal_update_folders.dirs  {'aix_5_powerpc','aix_6_powerpc','aix_6.1_powerpc','aix_7_powerpc','ubuntu_8_i686','ubuntu_8_x86_64','ubuntu_10_i686','ubuntu_10_x86_64','ubuntu_11_i686','ubuntu_11_x86_64','ubuntu_12_i686','ubuntu_12_x86_64','ubuntu_13_i686','ubuntu_13_x86_64','ubuntu_14_i686','ubuntu_14_x86_64','centos_5_i686','centos_5_x86_64','centos_6_i686','centos_6_x86_64','redhat_4_i686','redhat_4_x86_64','redhat_5_i686','redhat_5_x86_64','redhat_6_i686','redhat_6_x86_64','redhat_7_i686','redhat_7_x86_64','SuSE_10_i686','SuSE_10_x86_64','SuSE_11_i686','SuSE_11_x86_64','debian_5_i686','debian_5_x86_64','debian_6_i686','debian_6_x86_64','debian_7_i686','debian_7_x86_64','debian_8_i686','debian_8_x86_64','windows_i686','windows_x86_64','sunos_5.8_sun4u','sunos_5.8_sun4v','sunos_5.9_sun4u','sunos_5.9_sun4v','sunos_5.10_sun4u','sunos_5.10_sun4v','sunos_5.10_i86pc','hpux_ia64'} source=promise
default:cfe_internal_update_folders.sys#arch x86_64                                                       source=agent
default:cfe_internal_update_folders.sys#flavour centos_6                                                     source=agent
default:cfe_internal_update_folders.sys#workdir /var/cfengine                                                source=agent
default:cfengine_controls.input[cf_agent] controls/3.7/cf_agent.cf                                     source=promise
default:cfengine_controls.input[cf_execd] controls/3.7/cf_execd.cf                                     source=promise
default:cfengine_controls.input[cf_hub]  controls/3.7/cf_hub.cf                                       source=promise
default:cfengine_controls.input[cf_monitord] controls/3.7/cf_monitord.cf                                  source=promise
default:cfengine_controls.input[cf_runagent] controls/3.7/cf_runagent.cf                                  source=promise
default:cfengine_controls.input[cf_serverd] controls/3.7/cf_serverd.cf                                   source=promise
default:cfengine_controls.input[reports] controls/3.7/reports.cf                                      source=promise
default:cfengine_controls.inputs          {'controls/3.7/cf_monitord.cf','controls/3.7/cf_hub.cf','controls/3.7/cf_runagent.cf','controls/3.7/reports.cf','controls/3.7/cf_serverd.cf','controls/3.7/cf_agent.cf','controls/3.7/cf_execd.cf'} source=promise
default:cfengine_controls.sys#cf_version_major 3                                                            source=agent
default:cfengine_controls.sys#cf_version_minor 7                                                            source=agent
default:cfengine_enterprise_hub_ha.classification_bundles  {'cfengine_enterprise_hub_ha'}                              source=promise
default:cfengine_enterprise_hub_ha.inputs  {'cf_null'}                                                 source=promise
default:cfengine_enterprise_hub_ha.management_bundles  {'cfengine_enterprise_hub_ha'}                              source=promise
default:cfengine_stdlib.inputs            {'lib/3.7/stdlib.cf'}                                       source=promise
default:cfengine_stdlib.sys#local_libdir lib/3.7                                                      source=agent
default:cfsketch_g.inputs                 {'cf_null'}                                                 source=promise
default:change_management.watch_files_report_change  {'/etc/shadow'}                                             source=promise
default:change_management.watch_files_report_diffs  {'/etc/passwd','/etc/group','/etc/services'}                source=promise
default:classic_services.all_states       {'start','restart','reload','stop','disable'}               source=promise
default:classic_services.baseinit[bluetoothd] bluetooth                                                    source=promise
default:classic_services.baseinit[mysql] mysqld                                                       source=promise
default:classic_services.baseinit[snmpd] snmpd                                                        source=promise
default:classic_services.baseinit[ssh]   sshd                                                         source=promise
default:classic_services.baseinit[www]   httpd                                                        source=promise
default:classic_services.default[cmd][chkconfig] /etc/init.d/$(service) $(state)                              source=promise
default:classic_services.default[cmd][systemd] /bin/systemctl $(service) $(state)                           source=promise
default:classic_services.default[cmd][sysvinitd] /etc/init.d/$(service) $(state)                              source=promise
default:classic_services.default[cmd][sysvservice] /sbin/service $(service) $(state)                            source=promise
default:classic_services.default[init]   chkconfig                                                    source=promise
default:classic_services.default[pattern] \b$(service)\b                                               source=promise
default:classic_services.default[prefix][chkconfig] /etc/init.d/                                                 source=promise
default:classic_services.default[prefix][systemd] /bin/systemctl                                               source=promise
default:classic_services.default[prefix][sysvinitd] /etc/init.d/                                                 source=promise
default:classic_services.default[prefix][sysvservice] /sbin/service                                                source=promise
default:classic_services.init[rhnsd]     sysvservice                                                  source=promise
default:classic_services.inits            {'sysvinitd','sysvservice','systemd','chkconfig'}           source=promise
default:classic_services.paths#service   /sbin/service                                                source=agent
default:classic_services.paths#systemctl /bin/systemctl                                               source=agent
default:classic_services.pattern[NetworkManager] .*NetworkManager.*                                           source=promise
default:classic_services.pattern[acpid]  .*acpid.*                                                    source=promise
default:classic_services.pattern[anacron] .*anacron.*                                                  source=promise
default:classic_services.pattern[atd]    .*sbin/atd.*                                                 source=promise
default:classic_services.pattern[auditd] .*auditd$                                                    source=promise
default:classic_services.pattern[autofs] .*automount.*                                                source=promise
default:classic_services.pattern[bluetoothd] .*hcid.*                                                     source=promise
default:classic_services.pattern[capi]   .*capiinit.*                                                 source=promise
default:classic_services.pattern[cfengine3] .*cf-execd.*                                                 source=promise
default:classic_services.pattern[conman] .*conmand.*                                                  source=promise
default:classic_services.pattern[cpuspeed] .*cpuspeed.*                                                 source=promise
default:classic_services.pattern[crond]  .*crond.*                                                    source=promise
default:classic_services.pattern[dc_client] .*dc_client.*                                                source=promise
default:classic_services.pattern[dc_server] .*dc_server.*                                                source=promise
default:classic_services.pattern[dnsmasq] .*dnsmasq.*                                                  source=promise
default:classic_services.pattern[dund]   .*dund.*                                                     source=promise
default:classic_services.pattern[fancontrol] .*fancontrol.*                                               source=promise
default:classic_services.pattern[gpm]    .*gpm.*                                                      source=promise
default:classic_services.pattern[haldaemon] .*hald.*                                                     source=promise
default:classic_services.pattern[hddtemp] .*hddtemp.*                                                  source=promise
default:classic_services.pattern[hidd]   .*hidd.*                                                     source=promise
default:classic_services.pattern[irda]   .*irattach.*                                                 source=promise
default:classic_services.pattern[irqbalance] .*irqbalance.*                                               source=promise
default:classic_services.pattern[iscsid] .*iscsid.*                                                   source=promise
default:classic_services.pattern[isdn]   .*isdnlog.*                                                  source=promise
default:classic_services.pattern[lm-sensor] .*psensor.*                                                  source=promise
default:classic_services.pattern[lvm2-monitor] .*vgchange.*                                                 source=promise
default:classic_services.pattern[mcstrans] .*mcstransd.*                                                source=promise
default:classic_services.pattern[mdmonitor] .*mdadm.*                                                    source=promise
default:classic_services.pattern[mdmpd]  .*mdmpd.*                                                    source=promise
default:classic_services.pattern[messagebus] .*dbus-daemon.*                                              source=promise
default:classic_services.pattern[microcode_ctl] .*microcode_ctl.*                                            source=promise
default:classic_services.pattern[multipathd] .*multipathd.*                                               source=promise
default:classic_services.pattern[munin-node] .*munin-node.*                                               source=promise
default:classic_services.pattern[mysql]  .*mysqld.*                                                   source=promise
default:classic_services.pattern[netplugd] .*netplugd.*                                                 source=promise
default:classic_services.pattern[nfs]    .*nfsd.*                                                     source=promise
default:classic_services.pattern[nfslock] .*rpc.statd.*                                                source=promise
default:classic_services.pattern[nscd]   .*nscd.*                                                     source=promise
default:classic_services.pattern[ntpd]   .*ntpd.*                                                     source=promise
default:classic_services.pattern[oddjobd] .*oddjobd.*                                                  source=promise
default:classic_services.pattern[openvpn] .*openvpn.*                                                  source=promise
default:classic_services.pattern[pand]   .*pand.*                                                     source=promise
default:classic_services.pattern[pcscd]  .*pcscd.*                                                    source=promise
default:classic_services.pattern[portmap] .*portmap.*                                                  source=promise
default:classic_services.pattern[postfix] .*postfix.*                                                  source=promise
default:classic_services.pattern[postgresql] .*postmaster.*                                               source=promise
default:classic_services.pattern[rdisc]  .*rdisc.*                                                    source=promise
default:classic_services.pattern[readahead_early] .*readahead.*early.*                                         source=promise
default:classic_services.pattern[readahead_later] .*readahead.*later.*                                         source=promise
default:classic_services.pattern[restorecond] .*restorecond.*                                              source=promise
default:classic_services.pattern[rhnsd]  rhnsd                                                        source=promise
default:classic_services.pattern[rpcgssd] .*rpc.gssd.*                                                 source=promise
default:classic_services.pattern[rpcidmapd] .*rpc.idmapd.*                                               source=promise
default:classic_services.pattern[rpcsvcgssd] .*rpc.svcgssd.*                                              source=promise
default:classic_services.pattern[rsync]  .*rsync.*                                                    source=promise
default:classic_services.pattern[rsyslog] .*rsyslogd.*                                                 source=promise
default:classic_services.pattern[saslauthd] .*saslauthd.*                                                source=promise
default:classic_services.pattern[sendmail] .*sendmail.*                                                 source=promise
default:classic_services.pattern[smartd] .*smartd.*                                                   source=promise
default:classic_services.pattern[snmpd]  /usr/sbin/snmpd                                              source=promise
default:classic_services.pattern[ssh]    .*\Ssshd.*                                                   source=promise
default:classic_services.pattern[svnserve] .*svnserve.*                                                 source=promise
default:classic_services.pattern[syslog] .*syslogd.*                                                  source=promise
default:classic_services.pattern[tcsd]   .*tcsd.*                                                     source=promise
default:classic_services.pattern[tomcat5] .*tomcat5.*                                                  source=promise
default:classic_services.pattern[tomcat6] .*tomcat6.*                                                  source=promise
default:classic_services.pattern[varnish] .*varnish.*                                                  source=promise
default:classic_services.pattern[wpa_supplicant] .*wpa_supplicant.*                                           source=promise
default:classic_services.pattern[www]    .*httpd.*                                                    source=promise
default:classic_services.pattern[xfs]    .*xfs.*                                                      source=promise
default:classic_services.pattern[ypbind] .*ypbind.*                                                   source=promise
default:classic_services.pattern[yum-updatesd] .*yum-updatesd.*                                             source=promise
default:classic_services.stakeholders[acpid]  {'cpu','cpu0','cpu1','cpu2','cpu3'}                         source=promise
default:classic_services.stakeholders[cfengine3]  {'cfengine_in'}                                             source=promise
default:classic_services.stakeholders[mysql]  {'mysql_in'}                                                source=promise
default:classic_services.stakeholders[nfs]  {'nfsd_in'}                                                 source=promise
default:classic_services.stakeholders[postfix]  {'smtp_in'}                                                 source=promise
default:classic_services.stakeholders[rsyslog]  {'syslog'}                                                  source=promise
default:classic_services.stakeholders[sendmail]  {'smtp_in'}                                                 source=promise
default:classic_services.stakeholders[ssh]  {'ssh_in'}                                                  source=promise
default:classic_services.stakeholders[syslog]  {'syslog'}                                                  source=promise
default:classic_services.stakeholders[tomcat5]  {'www_alt_in'}                                              source=promise
default:classic_services.stakeholders[tomcat6]  {'www_alt_in'}                                              source=promise
default:classic_services.stakeholders[www]  {'www_in','wwws_in','www_alt_in'}                           source=promise
default:common_knowledge.list_update_ifelapsed 240                                                          source=promise
default:const.dirsep                     /                                                            source=agent
default:const.dollar                     $                                                            source=agent
default:const.endl                       <non-printable>                                              source=agent
default:const.n                          <non-printable>                                              source=agent
default:const.r                          <non-printable>                                              source=agent
default:const.t                          <non-printable>                                              source=agent
default:control_agent.abortclasses        {'cfengine_3_3','cfengine_3_4'}                             source=promise
default:control_agent.ifelapsed          1                                                            source=promise
default:control_agent.skipidentify       true                                                         source=promise
default:control_common.bundlesequence     {'inventory_control','inventory_control','inventory_any','inventory_autorun','inventory_linux','inventory_lsb','inventory_redhat','inventory_os','def','cfengine_enterprise_hub_ha','cfsketch_run','services_autorun','autorun','cfe_internal_management','main','cfengine_enterprise_hub_ha'} source=promise
default:control_common.inputs             {'controls/3.7/def.cf','controls/3.7/def_inputs.cf','inventory/any.cf','inventory/linux.cf','inventory/lsb.cf','inventory/redhat.cf','inventory/os.cf','sketches/meta/api-runfile.cf','cf_null','cfe_internal/enterprise/file_change.cf','cfe_internal/enterprise/main.cf','cfe_internal/core/log_rotation.cf','cfe_internal/core/host_info_report.cf','cfe_internal/enterprise/CFE_hub_specific.cf','cfe_internal/enterprise/CFE_knowledge.cf','cfe_internal/core/main.cf','cfe_internal/core/limit_robot_agents.cf','cfe_internal/CFE_cfengine.cf','controls/3.7/cf_monitord.cf','controls/3.7/cf_hub.cf','controls/3.7/cf_runagent.cf','controls/3.7/reports.cf','controls/3.7/cf_serverd.cf','controls/3.7/cf_agent.cf','controls/3.7/cf_execd.cf','lib/3.7/stdlib.cf','lib/3.7/autorun.cf','services/main.cf'} source=promise
default:control_common.version           CFEngine Promises.cf 3.7.3                                   source=promise
default:control_executor.exec_command    "/var/cfengine/bin/cf-agent" -f "/var/cfengine/inputs/update.cf" ; "/var/cfengine/bin/cf-agent" -Dcf_execd_initiated source=promise
default:control_executor.mailfrom        root@hub.                                                    source=promise
default:control_executor.mailto          root@                                                        source=promise
default:control_executor.smtpserver      localhost                                                    source=promise
default:control_executor.splaytime       4                                                            source=promise
default:control_file.inputs               {'/var/cfengine/inputs/services/autorun/copy_from_unless_file_exists.cf','/var/cfengine/inputs/services/autorun/hello.cf','/var/cfengine/inputs/services/autorun/inventory_policy.cf'} source=promise
default:control_monitor.forgetrate       0.7                                                          source=promise
default:control_monitor.histograms       true                                                         source=promise
default:control_runagent.hosts            {'127.0.0.1'}                                               source=promise
default:control_server.allowallconnects   {'127.0.0.1','::1','192.168.33.2/16'}                       source=promise
default:control_server.allowconnects      {'127.0.0.1','::1','192.168.33.2/16'}                       source=promise
default:control_server.allowusers         {'root'}                                                    source=promise
default:control_server.cfruncommand      /bin/sh -c ""/var/cfengine/bin/cf-agent" -f /var/cfengine/inputs/update.cf" ; "/var/cfengine/bin/cf-agent" source=promise
default:control_server.denybadclocks     false                                                        source=promise
default:control_server.maxconnections    200                                                          source=promise
default:control_server.trustkeysfrom      {'0.0.0.0/0'}                                               source=promise
default:copy_from_unless_file_exists.sys#inputdir /var/cfengine/inputs                                         source=agent
default:copy_from_unless_file_exists.sys#masterdir /var/cfengine/masterfiles                                    source=agent
default:copy_from_unless_file_exists.sys#policy_hub 192.168.33.2                                                 source=agent
default:copy_from_unless_file_exists_meta.tags  {'autorun'}                                                 source=promise
default:create_solaris_admin_file.solaris_knowledge#admin_nocheck <non-printable>                                              source=agent
default:cronjob.crontab                  /var/spool/cron                                              source=promise
default:darwin_knowledge.brew_name_regex ([\S]+)\s[\S]+                                               source=promise
default:darwin_knowledge.brew_version_regex [\S]+\s([\S]+)                                               source=promise
default:darwin_knowledge.call_brew       $(paths.path[brew])                                          source=promise
default:darwin_knowledge.call_sudo       $(paths.path[sudo])                                          source=promise
default:debian_knowledge.apt_prefix      /usr/bin/env DEBIAN_FRONTEND=noninteractive LC_ALL=C PATH=/bin:/sbin/:/usr/bin:/usr/sbin source=promise
default:debian_knowledge.call_apt_get    /usr/bin/env DEBIAN_FRONTEND=noninteractive LC_ALL=C PATH=/bin:/sbin/:/usr/bin:/usr/sbin $(paths.path[apt_get]) source=promise
default:debian_knowledge.call_aptitude   /usr/bin/env DEBIAN_FRONTEND=noninteractive LC_ALL=C PATH=/bin:/sbin/:/usr/bin:/usr/sbin $(paths.path[aptitude]) source=promise
default:debian_knowledge.call_dpkg       /usr/bin/env DEBIAN_FRONTEND=noninteractive LC_ALL=C PATH=/bin:/sbin/:/usr/bin:/usr/sbin $(paths.path[dpkg]) source=promise
default:debian_knowledge.default_arch    amd64                                                        source=promise
default:debian_knowledge.dpkg_compare_equal /usr/bin/env DEBIAN_FRONTEND=noninteractive LC_ALL=C PATH=/bin:/sbin/:/usr/bin:/usr/sbin $(paths.path[dpkg]) --compare-versions \'$(v1)\' eq \'$(v2)\' source=promise
default:debian_knowledge.dpkg_compare_less /usr/bin/env DEBIAN_FRONTEND=noninteractive LC_ALL=C PATH=/bin:/sbin/:/usr/bin:/usr/sbin $(paths.path[dpkg]) --compare-versions \'$(v1)\' lt \'$(v2)\' source=promise
default:debian_knowledge.dpkg_options    -o Dpkg::Options::=--force-confold -o Dpkg::Options::=--force-confdef source=promise
default:debian_knowledge.list_name_regex ^.i\s+([^\s:]+).*                                            source=promise
default:debian_knowledge.list_version_regex ^.i\s+[^\s]+\s+([^\s]+).*                                    source=promise
default:debian_knowledge.patch_name_regex ^Inst\s+(\S+)\s+.*                                           source=promise
default:debian_knowledge.patch_version_regex ^Inst\s+\S+\s+\[\S+\]\s+\((\S+)\s+.*                         source=promise
default:debian_knowledge.sys#arch        x86_64                                                       source=agent
default:def.acl                           {'192.168.33.2/16'}                                         source=promise,defvar
default:def.augments_inputs               {'cf_null'}                                                 source=promise
default:def.base_log_files                {'/var/cfengine/cf3.hub.runlog','/var/cfengine/promise_summary.log'} source=promise
default:def.cf_apache_group              cfapache                                                     source=promise
default:def.cf_apache_user               cfapache                                                     source=promise
default:def.cf_runagent_shell            /bin/sh                                                      source=promise
default:def.cfe_log_dirs                  {'/var/cfengine/outputs','/var/cfengine/reports'}           source=promise
default:def.cfe_log_files                 {'/var/cfengine/cf3.hub.runlog','/var/cfengine/promise_summary.log','/var/cfengine/cf_notkept.log','/var/cfengine/cf_repair.log','/var/cfengine/state/cf_value.log','/var/cfengine/outputs/dc-scripts.log','/var/cfengine/httpd/logs/access_log','/var/cfengine/httpd/logs/error_log'} source=promise
default:def.def#domain                                                                                source=agent
default:def.dir_bin                      /var/cfengine/bin                                            source=promise
default:def.dir_masterfiles              /var/cfengine/masterfiles                                    source=promise
default:def.dir_modules                  /var/cfengine/modules                                        source=promise
default:def.dir_plugins                  /var/cfengine/plugins                                        source=promise
default:def.dir_reports                  /var/cfengine/reports                                        source=promise
default:def.dir_software                 /var/cfengine/master_software_updates                        source=promise
default:def.domain                                                                                    source=promise
default:def.enterprise_log_files          {'/var/cfengine/cf_notkept.log','/var/cfengine/cf_repair.log','/var/cfengine/state/cf_value.log','/var/cfengine/outputs/dc-scripts.log'} source=promise
default:def.hub_log_files                 {'/var/cfengine/httpd/logs/access_log','/var/cfengine/httpd/logs/error_log'} source=promise
default:def.mailfrom                     root@hub.                                                    source=promise
default:def.mailto                       root@                                                        source=promise
default:def.max_client_history_size      52428800                                                     source=promise
default:def.policy_servers                {'192.168.33.2'}                                            source=promise
default:def.smtpserver                   localhost                                                    source=promise
default:def.sys#bindir                   /var/cfengine/bin                                            source=agent
default:def.sys#domain                                                                                source=agent
default:def.sys#masterdir                /var/cfengine/masterfiles                                    source=agent
default:def.sys#policy_hub               192.168.33.2                                                 source=agent
default:def.sys#uqhost                   hub                                                          source=agent
default:def.sys#workdir                  /var/cfengine                                                source=agent
default:def.trustkeysfrom                 {'0.0.0.0/0'}                                               source=promise,defvar
default:fileinfo.fields                   {'size','gid','uid','ino','nlink','ctime','atime','mtime','mode','modeoct','permstr','permoct','type','devno','dev_minor','dev_major','basename','dirname','linktarget','linktarget_shallow'} source=promise
default:files_common.inputs               {'/var/cfengine/inputs/lib/3.7/common.cf'}                  source=promise
default:hello_world_autorun_meta.tags     {'autorun'}                                                 source=promise
default:host_info_report.host_info_report_output /var/cfengine/reports/host_info_report.txt                   source=promise
default:host_info_report.host_info_report_template /var/cfengine/inputs/cfe_internal/core/../../templates/host_info_report.mustache source=promise
default:host_info_report.sys#workdir     /var/cfengine                                                source=agent
default:host_info_report_cfengine.cfengine_info_files  {'cf_promises_validated','cf_promises_release_id'}          source=promise
default:host_info_report_cfengine.interface_flags  {'lo: up loopback running','eth1: up broadcast running multicast','eth0: up broadcast running multicast'} source=promise
default:host_info_report_cfengine.interface_info  {'eth0: IPv4 10.0.2.15','eth0: up broadcast running multicast','eth1: IPv4 192.168.33.2','eth1: up broadcast running multicast','lo: IPv4 127.0.0.1','lo: up loopback running'} source=promise
default:host_info_report_cfengine.interface_info_unsorted  {'lo: up loopback running','eth1: up broadcast running multicast','eth0: up broadcast running multicast','eth1: IPv4 192.168.33.2','eth0: IPv4 10.0.2.15','lo: IPv4 127.0.0.1'} source=promise
default:host_info_report_cfengine.interface_ips  {'eth1: IPv4 192.168.33.2','eth0: IPv4 10.0.2.15','lo: IPv4 127.0.0.1'} source=promise
default:host_info_report_cfengine.last_agent_run 2016-07-26 01:08:19 UTC                                      source=promise
default:host_info_report_cfengine.sys#inputdir /var/cfengine/inputs                                         source=agent
default:host_info_report_cfengine.sys#masterdir /var/cfengine/masterfiles                                    source=agent
default:host_info_report_cfengine.sys#workdir /var/cfengine                                                source=agent
default:host_info_report_render_txt.host_info_report#host_info_report_output /var/cfengine/reports/host_info_report.txt                   source=agent
default:host_info_report_render_txt.host_info_report#host_info_report_template /var/cfengine/inputs/cfe_internal/core/../../templates/host_info_report.mustache source=agent
default:host_info_report_software.package_names  {'cf_null'}                                                 source=promise
default:host_info_report_software.packages <non-printable>                                              source=promise
default:inventory.bundles                 {'inventory_control','inventory_any','inventory_autorun','inventory_linux','inventory_lsb','inventory_redhat','inventory_os'} source=promise
default:inventory.inputs                  {'inventory/any.cf','inventory/linux.cf','inventory/lsb.cf','inventory/redhat.cf','inventory/os.cf'} source=promise
default:inventory_cmdb_load.bkeys         {'cf_null'}                                                 source=promise
default:inventory_cmdb_load.ckeys         {'cf_null'}                                                 source=promise
default:inventory_control.dmidecoder     /usr/sbin/dmidecode                                          source=promise
default:inventory_control.lldpctl_exec   /usr/bin/lldpctl                                             source=promise
default:inventory_control.lsb_exec       /usr/bin/lsb_release                                         source=promise
default:inventory_control.mtab           /etc/mtab                                                    source=promise
default:inventory_control.proc           /proc                                                        source=promise
default:inventory_control.sys#fstab      /etc/fstab                                                   source=agent
default:inventory_linux.proc_1_cmdline   /sbin/init                                                   source=promise
default:inventory_linux.proc_1_cmdline_split  {'/sbin/init'}                                              source=promise
default:inventory_linux.proc_1_process   /sbin/init                                                   source=promise
default:inventory_lsb.inventory_control#lsb_exec /usr/bin/lsb_release                                         source=agent
default:inventory_lsb.lsb_exec           /usr/bin/lsb_release                                         source=promise
default:inventory_os.description         centos_6 (LSB missing)                                       source=promise,inventory,attribute_name=OS
default:inventory_os.sys#flavor          centos_6                                                     source=agent
default:inventory_policy.cpr             <non-printable>                                              source=promise
default:inventory_policy.masterfiles_cpv <non-printable>                                              source=promise
default:inventory_policy.masterfiles_updated 2016-07-25-19:13                                             source=promise,inventory,attribute_name=Masterfiles Updated
default:inventory_policy.policy_release_id e4dd6005aa7057ceea74b73a08b0c513d4d21a7e                     source=promise,inventory,attribute_name=Policy Release ID
default:inventory_policy.policy_updated  2016-07-26-01:07                                             source=promise,inventory,attribute_name=Policy Updated
default:inventory_policy.state_cpv       <non-printable>                                              source=promise
default:inventory_policy.sys#inputdir    /var/cfengine/inputs                                         source=agent
default:inventory_policy.sys#masterdir   /var/cfengine/masterfiles                                    source=agent
default:inventory_policy.sys#statedir    /var/cfengine/state                                          source=agent
default:inventory_policy_meta.tags        {'autorun'}                                                 source=promise
default:maintain_key_values_meta.tags     {'deprecated=3.6.0','deprecation-reason=Generic reimplementation','replaced-by=set_line_based'} source=promise
default:mon.av_cfengine_in               0.70                                                         monitoring,source=environment
default:mon.av_cfengine_out              1.40                                                         monitoring,source=environment
default:mon.av_cpu                       0.22                                                         monitoring,source=environment
default:mon.av_cpu0                      0.24                                                         monitoring,source=environment
default:mon.av_cpu1                      0.21                                                         monitoring,source=environment
default:mon.av_cpu2                      0.00                                                         monitoring,source=environment
default:mon.av_cpu3                      0.00                                                         monitoring,source=environment
default:mon.av_diskfree                  67.20                                                        monitoring,source=environment
default:mon.av_dns_in                    0.00                                                         monitoring,source=environment
default:mon.av_dns_out                   0.00                                                         monitoring,source=environment
default:mon.av_ftp_in                    0.00                                                         monitoring,source=environment
default:mon.av_ftp_out                   0.00                                                         monitoring,source=environment
default:mon.av_icmp_in                   0.00                                                         monitoring,source=environment
default:mon.av_icmp_out                  0.00                                                         monitoring,source=environment
default:mon.av_imap_in                   0.00                                                         monitoring,source=environment
default:mon.av_imap_out                  0.00                                                         monitoring,source=environment
default:mon.av_imaps_in                  0.00                                                         monitoring,source=environment
default:mon.av_imaps_out                 0.00                                                         monitoring,source=environment
default:mon.av_io_readdata               0.00                                                         monitoring,source=environment
default:mon.av_io_reads                  0.00                                                         monitoring,source=environment
default:mon.av_io_writes                 6.30                                                         monitoring,source=environment
default:mon.av_io_writtendata            0.05                                                         monitoring,source=environment
default:mon.av_ipp_in                    0.00                                                         monitoring,source=environment
default:mon.av_ipp_out                   0.00                                                         monitoring,source=environment
default:mon.av_ldap_in                   0.00                                                         monitoring,source=environment
default:mon.av_ldap_out                  0.00                                                         monitoring,source=environment
default:mon.av_ldaps_in                  0.00                                                         monitoring,source=environment
default:mon.av_ldaps_out                 0.00                                                         monitoring,source=environment
default:mon.av_loadavg                   0.01                                                         monitoring,source=environment
default:mon.av_mem_cached                95.91                                                        monitoring,source=environment
default:mon.av_mem_free                  26.30                                                        monitoring,source=environment
default:mon.av_mem_freeswap              648.39                                                       monitoring,source=environment
default:mon.av_mem_swap                  649.59                                                       monitoring,source=environment
default:mon.av_mem_total                 343.20                                                       monitoring,source=environment
default:mon.av_messages                  0.00                                                         monitoring,source=environment
default:mon.av_microsoft_ds_in           0.00                                                         monitoring,source=environment
default:mon.av_microsoft_ds_out          0.00                                                         monitoring,source=environment
default:mon.av_mongo_in                  0.00                                                         monitoring,source=environment
default:mon.av_mongo_out                 0.00                                                         monitoring,source=environment
default:mon.av_mysql_in                  0.00                                                         monitoring,source=environment
default:mon.av_mysql_out                 0.00                                                         monitoring,source=environment
default:mon.av_netbiosdgm_in             0.00                                                         monitoring,source=environment
default:mon.av_netbiosdgm_out            0.00                                                         monitoring,source=environment
default:mon.av_netbiosns_in              0.00                                                         monitoring,source=environment
default:mon.av_netbiosns_out             0.00                                                         monitoring,source=environment
default:mon.av_netbiosssn_in             0.00                                                         monitoring,source=environment
default:mon.av_netbiosssn_out            0.00                                                         monitoring,source=environment
default:mon.av_nfsd_in                   0.00                                                         monitoring,source=environment
default:mon.av_nfsd_out                  0.00                                                         monitoring,source=environment
default:mon.av_otherprocs                31.50                                                        monitoring,source=environment
default:mon.av_postgres_in               2.10                                                         monitoring,source=environment
default:mon.av_postgres_out              2.10                                                         monitoring,source=environment
default:mon.av_rootprocs                 84.00                                                        monitoring,source=environment
default:mon.av_smtp_in                   0.00                                                         monitoring,source=environment
default:mon.av_smtp_out                  0.00                                                         monitoring,source=environment
default:mon.av_spare                     0.00                                                         monitoring,source=environment
default:mon.av_ssh_in                    2.10                                                         monitoring,source=environment
default:mon.av_ssh_out                   0.00                                                         monitoring,source=environment
default:mon.av_syslog                    0.00                                                         monitoring,source=environment
default:mon.av_tcpack_in                 0.00                                                         monitoring,source=environment
default:mon.av_tcpack_out                0.00                                                         monitoring,source=environment
default:mon.av_tcpfin_in                 0.00                                                         monitoring,source=environment
default:mon.av_tcpfin_out                0.00                                                         monitoring,source=environment
default:mon.av_tcpmisc_in                0.00                                                         monitoring,source=environment
default:mon.av_tcpmisc_out               0.00                                                         monitoring,source=environment
default:mon.av_tcpsyn_in                 0.00                                                         monitoring,source=environment
default:mon.av_tcpsyn_out                0.00                                                         monitoring,source=environment
default:mon.av_temp0                     0.00                                                         monitoring,source=environment
default:mon.av_temp1                     0.00                                                         monitoring,source=environment
default:mon.av_temp2                     0.00                                                         monitoring,source=environment
default:mon.av_temp3                     0.00                                                         monitoring,source=environment
default:mon.av_udp_in                    0.00                                                         monitoring,source=environment
default:mon.av_udp_out                   0.00                                                         monitoring,source=environment
default:mon.av_users                     4.20                                                         monitoring,source=environment
default:mon.av_webaccess                 0.00                                                         monitoring,source=environment
default:mon.av_weberrors                 0.00                                                         monitoring,source=environment
default:mon.av_www_alt_in                0.00                                                         monitoring,source=environment
default:mon.av_www_alt_out               0.00                                                         monitoring,source=environment
default:mon.av_www_in                    0.70                                                         monitoring,source=environment
default:mon.av_www_out                   0.00                                                         monitoring,source=environment
default:mon.av_wwws_in                   0.70                                                         monitoring,source=environment
default:mon.av_wwws_out                  0.00                                                         monitoring,source=environment
default:mon.dev_cfengine_in              1.07                                                         monitoring,source=environment
default:mon.dev_cfengine_out             2.19                                                         monitoring,source=environment
default:mon.dev_cpu                      0.43                                                         monitoring,source=environment
default:mon.dev_cpu0                     0.46                                                         monitoring,source=environment
default:mon.dev_cpu1                     0.40                                                         monitoring,source=environment
default:mon.dev_cpu2                     0.00                                                         monitoring,source=environment
default:mon.dev_cpu3                     0.00                                                         monitoring,source=environment
default:mon.dev_diskfree                 102.91                                                       monitoring,source=environment
default:mon.dev_dns_in                   0.00                                                         monitoring,source=environment
default:mon.dev_dns_out                  0.00                                                         monitoring,source=environment
default:mon.dev_ftp_in                   0.00                                                         monitoring,source=environment
default:mon.dev_ftp_out                  0.00                                                         monitoring,source=environment
default:mon.dev_icmp_in                  0.00                                                         monitoring,source=environment
default:mon.dev_icmp_out                 0.00                                                         monitoring,source=environment
default:mon.dev_imap_in                  0.00                                                         monitoring,source=environment
default:mon.dev_imap_out                 0.00                                                         monitoring,source=environment
default:mon.dev_imaps_in                 0.00                                                         monitoring,source=environment
default:mon.dev_imaps_out                0.00                                                         monitoring,source=environment
default:mon.dev_io_readdata              0.00                                                         monitoring,source=environment
default:mon.dev_io_reads                 0.00                                                         monitoring,source=environment
default:mon.dev_io_writes                10.17                                                        monitoring,source=environment
default:mon.dev_io_writtendata           0.07                                                         monitoring,source=environment
default:mon.dev_ipp_in                   0.00                                                         monitoring,source=environment
default:mon.dev_ipp_out                  0.00                                                         monitoring,source=environment
default:mon.dev_ldap_in                  0.00                                                         monitoring,source=environment
default:mon.dev_ldap_out                 0.00                                                         monitoring,source=environment
default:mon.dev_ldaps_in                 0.00                                                         monitoring,source=environment
default:mon.dev_ldaps_out                0.00                                                         monitoring,source=environment
default:mon.dev_loadavg                  0.02                                                         monitoring,source=environment
default:mon.dev_mem_cached               146.68                                                       monitoring,source=environment
default:mon.dev_mem_free                 41.14                                                        monitoring,source=environment
default:mon.dev_mem_freeswap             992.91                                                       monitoring,source=environment
default:mon.dev_mem_swap                 994.76                                                       monitoring,source=environment
default:mon.dev_mem_total                525.56                                                       monitoring,source=environment
default:mon.dev_messages                 1797.59                                                      monitoring,source=environment
default:mon.dev_microsoft_ds_in          0.00                                                         monitoring,source=environment
default:mon.dev_microsoft_ds_out         0.00                                                         monitoring,source=environment
default:mon.dev_mongo_in                 0.00                                                         monitoring,source=environment
default:mon.dev_mongo_out                0.00                                                         monitoring,source=environment
default:mon.dev_mysql_in                 0.00                                                         monitoring,source=environment
default:mon.dev_mysql_out                0.00                                                         monitoring,source=environment
default:mon.dev_netbiosdgm_in            0.00                                                         monitoring,source=environment
default:mon.dev_netbiosdgm_out           0.00                                                         monitoring,source=environment
default:mon.dev_netbiosns_in             0.00                                                         monitoring,source=environment
default:mon.dev_netbiosns_out            0.00                                                         monitoring,source=environment
default:mon.dev_netbiosssn_in            0.00                                                         monitoring,source=environment
default:mon.dev_netbiosssn_out           0.00                                                         monitoring,source=environment
default:mon.dev_nfsd_in                  0.00                                                         monitoring,source=environment
default:mon.dev_nfsd_out                 0.00                                                         monitoring,source=environment
default:mon.dev_otherprocs               47.92                                                        monitoring,source=environment
default:mon.dev_postgres_in              3.82                                                         monitoring,source=environment
default:mon.dev_postgres_out             3.14                                                         monitoring,source=environment
default:mon.dev_rootprocs                128.21                                                       monitoring,source=environment
default:mon.dev_smtp_in                  0.00                                                         monitoring,source=environment
default:mon.dev_smtp_out                 0.00                                                         monitoring,source=environment
default:mon.dev_spare                    0.00                                                         monitoring,source=environment
default:mon.dev_ssh_in                   3.10                                                         monitoring,source=environment
default:mon.dev_ssh_out                  0.02                                                         monitoring,source=environment
default:mon.dev_syslog                   0.00                                                         monitoring,source=environment
default:mon.dev_tcpack_in                0.00                                                         monitoring,source=environment
default:mon.dev_tcpack_out               0.00                                                         monitoring,source=environment
default:mon.dev_tcpfin_in                0.00                                                         monitoring,source=environment
default:mon.dev_tcpfin_out               0.00                                                         monitoring,source=environment
default:mon.dev_tcpmisc_in               0.00                                                         monitoring,source=environment
default:mon.dev_tcpmisc_out              0.00                                                         monitoring,source=environment
default:mon.dev_tcpsyn_in                0.00                                                         monitoring,source=environment
default:mon.dev_tcpsyn_out               0.00                                                         monitoring,source=environment
default:mon.dev_temp0                    0.00                                                         monitoring,source=environment
default:mon.dev_temp1                    0.00                                                         monitoring,source=environment
default:mon.dev_temp2                    0.00                                                         monitoring,source=environment
default:mon.dev_temp3                    0.00                                                         monitoring,source=environment
default:mon.dev_udp_in                   0.00                                                         monitoring,source=environment
default:mon.dev_udp_out                  0.00                                                         monitoring,source=environment
default:mon.dev_users                    6.29                                                         monitoring,source=environment
default:mon.dev_webaccess                0.00                                                         monitoring,source=environment
default:mon.dev_weberrors                0.00                                                         monitoring,source=environment
default:mon.dev_www_alt_in               0.00                                                         monitoring,source=environment
default:mon.dev_www_alt_out              0.00                                                         monitoring,source=environment
default:mon.dev_www_in                   2.60                                                         monitoring,source=environment
default:mon.dev_www_out                  0.12                                                         monitoring,source=environment
default:mon.dev_wwws_in                  1.07                                                         monitoring,source=environment
default:mon.dev_wwws_out                 0.00                                                         monitoring,source=environment
default:mon.env_time                     Tue Jul 26 01:10:50 2016                                     time_based,source=agent
default:mon.listening_ports               {'443','80','50349','53437','5308','5432','22','111','6379'} monitoring,source=environment
default:mon.listening_tcp4_ports          {'443','80','50349','53437','5308','5432','22','111','6379'} monitoring,source=environment
default:mon.listening_tcp6_ports          {''}                                                        monitoring,source=environment
default:mon.listening_udp4_ports          {''}                                                        monitoring,source=environment
default:mon.listening_udp6_ports          {''}                                                        monitoring,source=environment
default:mon.tcp4_port_addr[111]          0.0.0.0                                                      monitoring,source=environment
default:mon.tcp4_port_addr[22]           0.0.0.0                                                      monitoring,source=environment
default:mon.tcp4_port_addr[443]          ::                                                           monitoring,source=environment
default:mon.tcp4_port_addr[50349]        ::                                                           monitoring,source=environment
default:mon.tcp4_port_addr[5308]         0.0.0.0                                                      monitoring,source=environment
default:mon.tcp4_port_addr[53437]        0.0.0.0                                                      monitoring,source=environment
default:mon.tcp4_port_addr[5432]         127.0.0.1                                                    monitoring,source=environment
default:mon.tcp4_port_addr[6379]         127.0.0.1                                                    monitoring,source=environment
default:mon.tcp4_port_addr[80]           ::                                                           monitoring,source=environment
default:mon.value_cfengine_in            1.00                                                         monitoring,source=environment
default:mon.value_cfengine_out           2.00                                                         monitoring,source=environment
default:mon.value_cpu                    0.32                                                         monitoring,source=environment
default:mon.value_cpu0                   0.34                                                         monitoring,source=environment
default:mon.value_cpu1                   0.30                                                         monitoring,source=environment
default:mon.value_cpu2                   0.00                                                         monitoring,source=environment
default:mon.value_cpu3                   0.00                                                         monitoring,source=environment
default:mon.value_diskfree               96.00                                                        monitoring,source=environment
default:mon.value_dns_in                 0.00                                                         monitoring,source=environment
default:mon.value_dns_out                0.00                                                         monitoring,source=environment
default:mon.value_ftp_in                 0.00                                                         monitoring,source=environment
default:mon.value_ftp_out                0.00                                                         monitoring,source=environment
default:mon.value_icmp_in                0.00                                                         monitoring,source=environment
default:mon.value_icmp_out               0.00                                                         monitoring,source=environment
default:mon.value_imap_in                0.00                                                         monitoring,source=environment
default:mon.value_imap_out               0.00                                                         monitoring,source=environment
default:mon.value_imaps_in               0.00                                                         monitoring,source=environment
default:mon.value_imaps_out              0.00                                                         monitoring,source=environment
default:mon.value_io_readdata            0.00                                                         monitoring,source=environment
default:mon.value_io_reads               0.00                                                         monitoring,source=environment
default:mon.value_io_writes              9.00                                                         monitoring,source=environment
default:mon.value_io_writtendata         0.06                                                         monitoring,source=environment
default:mon.value_ipp_in                 0.00                                                         monitoring,source=environment
default:mon.value_ipp_out                0.00                                                         monitoring,source=environment
default:mon.value_ldap_in                0.00                                                         monitoring,source=environment
default:mon.value_ldap_out               0.00                                                         monitoring,source=environment
default:mon.value_ldaps_in               0.00                                                         monitoring,source=environment
default:mon.value_ldaps_out              0.00                                                         monitoring,source=environment
default:mon.value_loadavg                0.01                                                         monitoring,source=environment
default:mon.value_mem_cached             137.01                                                       monitoring,source=environment
default:mon.value_mem_free               37.57                                                        monitoring,source=environment
default:mon.value_mem_freeswap           926.27                                                       monitoring,source=environment
default:mon.value_mem_swap               927.99                                                       monitoring,source=environment
default:mon.value_mem_total              490.29                                                       monitoring,source=environment
default:mon.value_messages               0.00                                                         monitoring,source=environment
default:mon.value_microsoft_ds_in        0.00                                                         monitoring,source=environment
default:mon.value_microsoft_ds_out       0.00                                                         monitoring,source=environment
default:mon.value_mongo_in               0.00                                                         monitoring,source=environment
default:mon.value_mongo_out              0.00                                                         monitoring,source=environment
default:mon.value_mysql_in               0.00                                                         monitoring,source=environment
default:mon.value_mysql_out              0.00                                                         monitoring,source=environment
default:mon.value_netbiosdgm_in          0.00                                                         monitoring,source=environment
default:mon.value_netbiosdgm_out         0.00                                                         monitoring,source=environment
default:mon.value_netbiosns_in           0.00                                                         monitoring,source=environment
default:mon.value_netbiosns_out          0.00                                                         monitoring,source=environment
default:mon.value_netbiosssn_in          0.00                                                         monitoring,source=environment
default:mon.value_netbiosssn_out         0.00                                                         monitoring,source=environment
default:mon.value_nfsd_in                0.00                                                         monitoring,source=environment
default:mon.value_nfsd_out               0.00                                                         monitoring,source=environment
default:mon.value_otherprocs             45.00                                                        monitoring,source=environment
default:mon.value_postgres_in            3.00                                                         monitoring,source=environment
default:mon.value_postgres_out           3.00                                                         monitoring,source=environment
default:mon.value_rootprocs              120.00                                                       monitoring,source=environment
default:mon.value_smtp_in                0.00                                                         monitoring,source=environment
default:mon.value_smtp_out               0.00                                                         monitoring,source=environment
default:mon.value_spare                  0.00                                                         monitoring,source=environment
default:mon.value_ssh_in                 3.00                                                         monitoring,source=environment
default:mon.value_ssh_out                0.00                                                         monitoring,source=environment
default:mon.value_syslog                 0.00                                                         monitoring,source=environment
default:mon.value_tcpack_in              0.00                                                         monitoring,source=environment
default:mon.value_tcpack_out             0.00                                                         monitoring,source=environment
default:mon.value_tcpfin_in              0.00                                                         monitoring,source=environment
default:mon.value_tcpfin_out             0.00                                                         monitoring,source=environment
default:mon.value_tcpmisc_in             0.00                                                         monitoring,source=environment
default:mon.value_tcpmisc_out            0.00                                                         monitoring,source=environment
default:mon.value_tcpsyn_in              0.00                                                         monitoring,source=environment
default:mon.value_tcpsyn_out             0.00                                                         monitoring,source=environment
default:mon.value_temp0                  0.00                                                         monitoring,source=environment
default:mon.value_temp1                  0.00                                                         monitoring,source=environment
default:mon.value_temp2                  0.00                                                         monitoring,source=environment
default:mon.value_temp3                  0.00                                                         monitoring,source=environment
default:mon.value_udp_in                 0.00                                                         monitoring,source=environment
default:mon.value_udp_out                0.00                                                         monitoring,source=environment
default:mon.value_users                  6.00                                                         monitoring,source=environment
default:mon.value_webaccess              0.00                                                         monitoring,source=environment
default:mon.value_weberrors              0.00                                                         monitoring,source=environment
default:mon.value_www_alt_in             0.00                                                         monitoring,source=environment
default:mon.value_www_alt_out            0.00                                                         monitoring,source=environment
default:mon.value_www_in                 1.00                                                         monitoring,source=environment
default:mon.value_www_out                0.00                                                         monitoring,source=environment
default:mon.value_wwws_in                1.00                                                         monitoring,source=environment
default:mon.value_wwws_out               0.00                                                         monitoring,source=environment
default:my_php_runalerts_script.cfe_internal_php_runalerts#sketch[limit] 300                                                          source=agent
default:my_php_runalerts_script.cfe_internal_php_runalerts#sketch[name] sketch                                                       source=agent
default:my_php_runalerts_script.cfe_internal_php_runalerts#sketch[running] 10                                                           source=agent
default:my_php_runalerts_script.cfe_internal_php_runalerts#sql[limit] 300                                                          source=agent
default:my_php_runalerts_script.cfe_internal_php_runalerts#sql[name] sql                                                          source=agent
default:my_php_runalerts_script.cfe_internal_php_runalerts#sql[running] 20                                                           source=agent
default:my_php_runalerts_script.sys#workdir /var/cfengine                                                source=agent
default:npm_knowledge.call_npm           /usr/bin/npm                                                 source=promise
default:npm_knowledge.npm_installed_regex ^[^ /]+ ([\w\d-._~]+@[\d.]+)                                 source=promise
default:npm_knowledge.npm_list_name_regex ^[^ /]+ ([\w\d-._~]+)@[\d.]+                                 source=promise
default:npm_knowledge.npm_list_version_regex ^[^ /]+ [\w\d-._~]+@([\d.]+)                                 source=promise
default:npm_knowledge.paths#path[npm]    /usr/bin/npm                                                 source=agent
default:package_absent.common_knowledge#list_update_ifelapsed 240                                                          source=agent
default:package_absent.redhat_knowledge#call_yum /usr/bin/yum                                                 source=agent
default:package_absent.redhat_knowledge#check_update_postproc <non-printable>                                              source=agent
default:package_absent.redhat_knowledge#patch_arch_regex ^\S+\.([^\s.]+)\s+\S+\s+\S+\s*$                              source=agent
default:package_absent.redhat_knowledge#patch_name_regex ^(\S+)\.[^\s.]+\s+\S+\s+\S+\s*$                              source=agent
default:package_absent.redhat_knowledge#patch_version_regex ^\S+\.[^\s.]+\s+(\S+)\s+\S+\s*$                              source=agent
default:package_absent.redhat_knowledge#rpm_compare_equal /var/cfengine/bin/rpmvercmp \'$(v1)\' eq \'$(v2)\'           source=agent
default:package_absent.redhat_knowledge#rpm_compare_less /var/cfengine/bin/rpmvercmp  \'$(v1)\' lt \'$(v2)\'          source=agent
default:package_absent.redhat_knowledge#yum_offline_options --quiet -C                                                   source=agent
default:package_absent.redhat_knowledge#yum_options --quiet                                                      source=agent
default:package_absent.rpm_knowledge#call_rpm /bin/rpm                                                     source=agent
default:package_absent.rpm_knowledge#rpm3_arch_regex \S+\s+(\S+).*                                                source=agent
default:package_absent.rpm_knowledge#rpm3_name_regex (\S+).*                                                      source=agent
default:package_absent.rpm_knowledge#rpm3_output_format %{name} %{arch} %{version}-%{release}\n                      source=agent
default:package_absent.rpm_knowledge#rpm3_version_regex \S+\s+\S+\s+(\S+).*                                          source=agent
default:package_latest.common_knowledge#list_update_ifelapsed 240                                                          source=agent
default:package_latest.redhat_knowledge#call_yum /usr/bin/yum                                                 source=agent
default:package_latest.redhat_knowledge#check_update_postproc <non-printable>                                              source=agent
default:package_latest.redhat_knowledge#patch_arch_regex ^\S+\.([^\s.]+)\s+\S+\s+\S+\s*$                              source=agent
default:package_latest.redhat_knowledge#patch_name_regex ^(\S+)\.[^\s.]+\s+\S+\s+\S+\s*$                              source=agent
default:package_latest.redhat_knowledge#patch_version_regex ^\S+\.[^\s.]+\s+(\S+)\s+\S+\s*$                              source=agent
default:package_latest.redhat_knowledge#rpm_compare_equal /var/cfengine/bin/rpmvercmp \'$(v1)\' eq \'$(v2)\'           source=agent
default:package_latest.redhat_knowledge#rpm_compare_less /var/cfengine/bin/rpmvercmp  \'$(v1)\' lt \'$(v2)\'          source=agent
default:package_latest.redhat_knowledge#yum_offline_options --quiet -C                                                   source=agent
default:package_latest.redhat_knowledge#yum_options --quiet                                                      source=agent
default:package_latest.rpm_knowledge#call_rpm /bin/rpm                                                     source=agent
default:package_latest.rpm_knowledge#rpm3_arch_regex \S+\s+(\S+).*                                                source=agent
default:package_latest.rpm_knowledge#rpm3_name_regex (\S+).*                                                      source=agent
default:package_latest.rpm_knowledge#rpm3_output_format %{name} %{arch} %{version}-%{release}\n                      source=agent
default:package_latest.rpm_knowledge#rpm3_version_regex \S+\s+\S+\s+(\S+).*                                          source=agent
default:package_module_knowledge.platform_default yum                                                          source=promise
default:package_present.common_knowledge#list_update_ifelapsed 240                                                          source=agent
default:package_present.redhat_knowledge#call_yum /usr/bin/yum                                                 source=agent
default:package_present.redhat_knowledge#check_update_postproc <non-printable>                                              source=agent
default:package_present.redhat_knowledge#patch_arch_regex ^\S+\.([^\s.]+)\s+\S+\s+\S+\s*$                              source=agent
default:package_present.redhat_knowledge#patch_name_regex ^(\S+)\.[^\s.]+\s+\S+\s+\S+\s*$                              source=agent
default:package_present.redhat_knowledge#patch_version_regex ^\S+\.[^\s.]+\s+(\S+)\s+\S+\s*$                              source=agent
default:package_present.redhat_knowledge#rpm_compare_equal /var/cfengine/bin/rpmvercmp \'$(v1)\' eq \'$(v2)\'           source=agent
default:package_present.redhat_knowledge#rpm_compare_less /var/cfengine/bin/rpmvercmp  \'$(v1)\' lt \'$(v2)\'          source=agent
default:package_present.redhat_knowledge#yum_offline_options --quiet -C                                                   source=agent
default:package_present.redhat_knowledge#yum_options --quiet                                                      source=agent
default:package_present.rpm_knowledge#call_rpm /bin/rpm                                                     source=agent
default:package_present.rpm_knowledge#rpm3_arch_regex \S+\s+(\S+).*                                                source=agent
default:package_present.rpm_knowledge#rpm3_name_regex (\S+).*                                                      source=agent
default:package_present.rpm_knowledge#rpm3_output_format %{name} %{arch} %{version}-%{release}\n                      source=agent
default:package_present.rpm_knowledge#rpm3_version_regex \S+\s+\S+\s+(\S+).*                                          source=agent
default:package_specific.common_knowledge#list_update_ifelapsed 240                                                          source=agent
default:package_specific.redhat_knowledge#call_yum /usr/bin/yum                                                 source=agent
default:package_specific.redhat_knowledge#check_update_postproc <non-printable>                                              source=agent
default:package_specific.redhat_knowledge#patch_arch_regex ^\S+\.([^\s.]+)\s+\S+\s+\S+\s*$                              source=agent
default:package_specific.redhat_knowledge#patch_name_regex ^(\S+)\.[^\s.]+\s+\S+\s+\S+\s*$                              source=agent
default:package_specific.redhat_knowledge#patch_version_regex ^\S+\.[^\s.]+\s+(\S+)\s+\S+\s*$                              source=agent
default:package_specific.redhat_knowledge#rpm_compare_equal /var/cfengine/bin/rpmvercmp \'$(v1)\' eq \'$(v2)\'           source=agent
default:package_specific.redhat_knowledge#rpm_compare_less /var/cfengine/bin/rpmvercmp  \'$(v1)\' lt \'$(v2)\'          source=agent
default:package_specific.redhat_knowledge#yum_offline_options --quiet -C                                                   source=agent
default:package_specific.redhat_knowledge#yum_options --quiet                                                      source=agent
default:package_specific.rpm_knowledge#call_rpm /bin/rpm                                                     source=agent
default:package_specific.rpm_knowledge#rpm3_arch_regex \S+\s+(\S+).*                                                source=agent
default:package_specific.rpm_knowledge#rpm3_name_regex (\S+).*                                                      source=agent
default:package_specific.rpm_knowledge#rpm3_output_format %{name} %{arch} %{version}-%{release}\n                      source=agent
default:package_specific.rpm_knowledge#rpm3_version_regex \S+\s+\S+\s+(\S+).*                                          source=agent
default:package_specific.solaris_adminfile /tmp/cfe-adminfile                                           source=promise
default:package_specific.sys#os          linux                                                        source=agent
default:packages_common.inputs            {'/var/cfengine/inputs/lib/3.7/paths.cf','/var/cfengine/inputs/lib/3.7/files.cf','/var/cfengine/inputs/lib/3.7/common.cf'} source=promise
default:paths.all_paths                   {'awk','ping','sysctl','crontab','logger','crontabs','perl','printf','npm','test','iptables','groupadd','bc','wget','hostname','virtualenv','createrepo','curl','echo','free','lsattr','netstat','useradd','init','egrep','userdel','ethtool','cksum','df','diff','lsof','yum','realpath','sed','tr','dig','cut','svc','ip','ifconfig','nologin','pip','iptables_save','grep','domainname','git','ls','chkconfig','dc','wc','cat','getfacl','groupdel','sort','shadow','rpm','find','systemctl','tar','service','env'} source=promise
default:paths.awk                        /bin/awk                                                     source=promise
default:paths.bc                         /usr/bin/bc                                                  source=promise
default:paths.cat                        /bin/cat                                                     source=promise
default:paths.chkconfig                  /sbin/chkconfig                                              source=promise
default:paths.cksum                      /usr/bin/cksum                                               source=promise
default:paths.createrepo                 /usr/bin/createrepo                                          source=promise
default:paths.crontab                    /usr/bin/crontab                                             source=promise
default:paths.crontabs                   /var/spool/cron                                              source=promise
default:paths.curl                       /usr/bin/curl                                                source=promise
default:paths.cut                        /bin/cut                                                     source=promise
default:paths.dc                         /usr/bin/dc                                                  source=promise
default:paths.df                         /bin/df                                                      source=promise
default:paths.diff                       /usr/bin/diff                                                source=promise
default:paths.dig                        /usr/bin/dig                                                 source=promise
default:paths.domainname                 /bin/domainname                                              source=promise
default:paths.echo                       /bin/echo                                                    source=promise
default:paths.egrep                      /bin/egrep                                                   source=promise
default:paths.env                        /bin/env                                                     source=promise
default:paths.ethtool                    /usr/sbin/ethtool                                            source=promise
default:paths.find                       /usr/bin/find                                                source=promise
default:paths.free                       /usr/bin/free                                                source=promise
default:paths.getfacl                    /usr/bin/getfacl                                             source=promise
default:paths.git                        /var/cfengine/bin/git                                        source=promise
default:paths.grep                       /bin/grep                                                    source=promise
default:paths.groupadd                   /usr/sbin/groupadd                                           source=promise
default:paths.groupdel                   /usr/sbin/groupdel                                           source=promise
default:paths.hostname                   /bin/hostname                                                source=promise
default:paths.ifconfig                   /sbin/ifconfig                                               source=promise
default:paths.init                       /sbin/init                                                   source=promise
default:paths.ip                         /sbin/ip                                                     source=promise
default:paths.iptables                   /sbin/iptables                                               source=promise
default:paths.iptables_save              /sbin/iptables-save                                          source=promise
default:paths.logger                     /usr/bin/logger                                              source=promise
default:paths.ls                         /bin/ls                                                      source=promise
default:paths.lsattr                     /usr/bin/lsattr                                              source=promise
default:paths.lsof                       /usr/sbin/lsof                                               source=promise
default:paths.netstat                    /bin/netstat                                                 source=promise
default:paths.nologin                    /sbin/nologin                                                source=promise
default:paths.npm                        /usr/bin/npm                                                 source=promise
default:paths.path[awk]                  /bin/awk                                                     source=promise
default:paths.path[bc]                   /usr/bin/bc                                                  source=promise
default:paths.path[cat]                  /bin/cat                                                     source=promise
default:paths.path[chkconfig]            /sbin/chkconfig                                              source=promise
default:paths.path[cksum]                /usr/bin/cksum                                               source=promise
default:paths.path[createrepo]           /usr/bin/createrepo                                          source=promise
default:paths.path[crontab]              /usr/bin/crontab                                             source=promise
default:paths.path[crontabs]             /var/spool/cron                                              source=promise
default:paths.path[curl]                 /usr/bin/curl                                                source=promise
default:paths.path[cut]                  /bin/cut                                                     source=promise
default:paths.path[dc]                   /usr/bin/dc                                                  source=promise
default:paths.path[df]                   /bin/df                                                      source=promise
default:paths.path[diff]                 /usr/bin/diff                                                source=promise
default:paths.path[dig]                  /usr/bin/dig                                                 source=promise
default:paths.path[domainname]           /bin/domainname                                              source=promise
default:paths.path[echo]                 /bin/echo                                                    source=promise
default:paths.path[egrep]                /bin/egrep                                                   source=promise
default:paths.path[env]                  /bin/env                                                     source=promise
default:paths.path[ethtool]              /usr/sbin/ethtool                                            source=promise
default:paths.path[find]                 /usr/bin/find                                                source=promise
default:paths.path[free]                 /usr/bin/free                                                source=promise
default:paths.path[getfacl]              /usr/bin/getfacl                                             source=promise
default:paths.path[git]                  /var/cfengine/bin/git                                        source=promise
default:paths.path[grep]                 /bin/grep                                                    source=promise
default:paths.path[groupadd]             /usr/sbin/groupadd                                           source=promise
default:paths.path[groupdel]             /usr/sbin/groupdel                                           source=promise
default:paths.path[hostname]             /bin/hostname                                                source=promise
default:paths.path[ifconfig]             /sbin/ifconfig                                               source=promise
default:paths.path[init]                 /sbin/init                                                   source=promise
default:paths.path[ip]                   /sbin/ip                                                     source=promise
default:paths.path[iptables]             /sbin/iptables                                               source=promise
default:paths.path[iptables_save]        /sbin/iptables-save                                          source=promise
default:paths.path[logger]               /usr/bin/logger                                              source=promise
default:paths.path[ls]                   /bin/ls                                                      source=promise
default:paths.path[lsattr]               /usr/bin/lsattr                                              source=promise
default:paths.path[lsof]                 /usr/sbin/lsof                                               source=promise
default:paths.path[netstat]              /bin/netstat                                                 source=promise
default:paths.path[nologin]              /sbin/nologin                                                source=promise
default:paths.path[npm]                  /usr/bin/npm                                                 source=promise
default:paths.path[perl]                 /usr/bin/perl                                                source=promise
default:paths.path[ping]                 /usr/bin/ping                                                source=promise
default:paths.path[pip]                  /usr/bin/pip                                                 source=promise
default:paths.path[printf]               /usr/bin/printf                                              source=promise
default:paths.path[realpath]             /usr/bin/realpath                                            source=promise
default:paths.path[rpm]                  /bin/rpm                                                     source=promise
default:paths.path[sed]                  /bin/sed                                                     source=promise
default:paths.path[service]              /sbin/service                                                source=promise
default:paths.path[shadow]               /etc/shadow                                                  source=promise
default:paths.path[sort]                 /bin/sort                                                    source=promise
default:paths.path[svc]                  /sbin/service                                                source=promise
default:paths.path[sysctl]               /sbin/sysctl                                                 source=promise
default:paths.path[systemctl]            /bin/systemctl                                               source=promise
default:paths.path[tar]                  /bin/tar                                                     source=promise
default:paths.path[test]                 /usr/bin/test                                                source=promise
default:paths.path[tr]                   /usr/bin/tr                                                  source=promise
default:paths.path[useradd]              /usr/sbin/useradd                                            source=promise
default:paths.path[userdel]              /usr/sbin/userdel                                            source=promise
default:paths.path[virtualenv]           /usr/bin/virtualenv                                          source=promise
default:paths.path[wc]                   /usr/bin/wc                                                  source=promise
default:paths.path[wget]                 /usr/bin/wget                                                source=promise
default:paths.path[yum]                  /usr/bin/yum                                                 source=promise
default:paths.perl                       /usr/bin/perl                                                source=promise
default:paths.ping                       /usr/bin/ping                                                source=promise
default:paths.pip                        /usr/bin/pip                                                 source=promise
default:paths.printf                     /usr/bin/printf                                              source=promise
default:paths.realpath                   /usr/bin/realpath                                            source=promise
default:paths.rpm                        /bin/rpm                                                     source=promise
default:paths.sed                        /bin/sed                                                     source=promise
default:paths.service                    /sbin/service                                                source=promise
default:paths.shadow                     /etc/shadow                                                  source=promise
default:paths.sort                       /bin/sort                                                    source=promise
default:paths.svc                        /sbin/service                                                source=promise
default:paths.sys#workdir                /var/cfengine                                                source=agent
default:paths.sysctl                     /sbin/sysctl                                                 source=promise
default:paths.systemctl                  /bin/systemctl                                               source=promise
default:paths.tar                        /bin/tar                                                     source=promise
default:paths.test                       /usr/bin/test                                                source=promise
default:paths.tr                         /usr/bin/tr                                                  source=promise
default:paths.useradd                    /usr/sbin/useradd                                            source=promise
default:paths.userdel                    /usr/sbin/userdel                                            source=promise
default:paths.virtualenv                 /usr/bin/virtualenv                                          source=promise
default:paths.wc                         /usr/bin/wc                                                  source=promise
default:paths.wget                       /usr/bin/wget                                                source=promise
default:paths.yum                        /usr/bin/yum                                                 source=promise
default:pip_knowledge.call_pip           /usr/bin/pip                                                 source=promise
default:pip_knowledge.paths#path[pip]    /usr/bin/pip                                                 source=agent
default:pip_knowledge.pip_installed_regex ^([[:alnum:]-_]+\s\([\d.]+\))                                source=promise
default:pip_knowledge.pip_list_name_regex ^([[:alnum:]-_]+)\s\([\d.]+\)                                source=promise
default:pip_knowledge.pip_list_version_regex ^[[:alnum:]-_]+\s\(([\d.]+)\)                                source=promise
default:redhat_knowledge.call_rpmvercmp  /var/cfengine/bin/rpmvercmp                                  source=promise
default:redhat_knowledge.call_yum        /usr/bin/yum                                                 source=promise
default:redhat_knowledge.check_update_postproc <non-printable>                                              source=promise
default:redhat_knowledge.default_arch    x86_64                                                       source=promise
default:redhat_knowledge.patch_arch_regex ^\S+\.([^\s.]+)\s+\S+\s+\S+\s*$                              source=promise
default:redhat_knowledge.patch_name_regex ^(\S+)\.[^\s.]+\s+\S+\s+\S+\s*$                              source=promise
default:redhat_knowledge.patch_version_regex ^\S+\.[^\s.]+\s+(\S+)\s+\S+\s*$                              source=promise
default:redhat_knowledge.paths#path[yum] /usr/bin/yum                                                 source=agent
default:redhat_knowledge.paths#sed       /bin/sed                                                     source=agent
default:redhat_knowledge.rpm_compare_equal /var/cfengine/bin/rpmvercmp \'$(v1)\' eq \'$(v2)\'           source=promise
default:redhat_knowledge.rpm_compare_less /var/cfengine/bin/rpmvercmp  \'$(v1)\' lt \'$(v2)\'          source=promise
default:redhat_knowledge.sys#arch        x86_64                                                       source=agent
default:redhat_knowledge.sys#bindir      /var/cfengine/bin                                            source=agent
default:redhat_knowledge.yum_offline_options --quiet -C                                                   source=promise
default:redhat_knowledge.yum_options     --quiet                                                      source=promise
default:report_access_rules.query_types   {'delta','rebase','full'}                                   source=promise
default:rpm_knowledge.call_rpm           /bin/rpm                                                     source=promise
default:rpm_knowledge.paths#rpm          /bin/rpm                                                     source=agent
default:rpm_knowledge.rpm2_arch_regex    ^\S+?\s\S+?\s(\S+)$                                          source=promise
default:rpm_knowledge.rpm2_name_regex    ^(\S+?)\s\S+?\s\S+$                                          source=promise
default:rpm_knowledge.rpm2_output_format %{name} %{version}-%{release} %{arch}\n                      source=promise
default:rpm_knowledge.rpm2_version_regex ^\S+?\s(\S+?)\s\S+$                                          source=promise
default:rpm_knowledge.rpm3_arch_regex    \S+\s+(\S+).*                                                source=promise
default:rpm_knowledge.rpm3_name_regex    (\S+).*                                                      source=promise
default:rpm_knowledge.rpm3_output_format %{name} %{arch} %{version}-%{release}\n                      source=promise
default:rpm_knowledge.rpm3_version_regex \S+\s+\S+\s+(\S+).*                                          source=promise
default:rpm_knowledge.rpm_arch_regex     [^|]+\|[^|]+\|[^|]+\|[^|]+\|\s+([^\s]+).*                    source=promise
default:rpm_knowledge.rpm_name_regex     [^|]+\|[^|]+\|\s+([^\s|]+).*                                 source=promise
default:rpm_knowledge.rpm_output_format  i | repos | %{name} | %{version}-%{release} | %{arch}\n      source=promise
default:rpm_knowledge.rpm_version_regex  [^|]+\|[^|]+\|[^|]+\|\s+([^\s|]+).*                          source=promise
default:services_autorun.bundles          {'autorun'}                                                 source=promise
default:services_autorun.found_inputs     {'/var/cfengine/inputs/services/autorun/copy_from_unless_file_exists.cf','/var/cfengine/inputs/services/autorun/hello.cf','/var/cfengine/inputs/services/autorun/inventory_policy.cf'} source=promise
default:services_autorun.inputs           {'lib/3.7/autorun.cf'}                                      source=promise
default:services_autorun.sys#cf_version_major 3                                                            source=agent
default:services_autorun.sys#cf_version_minor 7                                                            source=agent
default:services_common.inputs            {'/var/cfengine/inputs/lib/3.7/common.cf','/var/cfengine/inputs/lib/3.7/paths.cf'} source=promise
default:set_config_values_matching_meta.tags  {'deprecated=3.6.0','deprecation-reason=Generic reimplementation','replaced-by=set_line_based'} source=promise
default:set_config_values_meta.tags       {'deprecated=3.6.0','deprecation-reason=Generic reimplementation','replaced-by=set_line_based'} source=promise
default:set_line_based_meta.tags          {'replaces=set_config_values','replaces=set_config_values_matching','replaces=set_variable_values','replaces=set_quoted_values','replaces=maintain_key_values'} source=promise
default:set_quoted_values_meta.tags       {'deprecated=3.6.0','deprecation-reason=Generic reimplementation','replaced-by=set_line_based'} source=promise
default:set_variable_values_meta.tags     {'deprecated=3.6.0','deprecation-reason=Generic reimplementation','replaced-by=set_line_based'} source=promise
default:solaris_knowledge.admin_nocheck  <non-printable>                                              source=promise
default:solaris_knowledge.call_pkgadd    $(paths.path[pkgadd])                                        source=promise
default:solaris_knowledge.call_pkginfo   $(paths.path[pkginfo])                                       source=promise
default:solaris_knowledge.call_pkgrm     $(paths.path[pkgrm])                                         source=promise
default:standard_services.call_systemctl /bin/systemctl --no-ask-password --global --system           source=promise
default:standard_services.init           /etc/init.d/$(service)                                       source=promise
default:standard_services.paths#systemctl /bin/systemctl                                               source=agent
default:stdlib_common.input[bundles]     /var/cfengine/inputs/lib/3.7/bundles.cf                      source=promise
default:stdlib_common.input[cfe_internal] /var/cfengine/inputs/lib/3.7/cfe_internal.cf                 source=promise
default:stdlib_common.input[cfe_internal_hub] /var/cfengine/inputs/lib/3.7/cfe_internal_hub.cf             source=promise
default:stdlib_common.input[cfengine_enterprise_hub_ha] /var/cfengine/inputs/lib/3.7/cfengine_enterprise_hub_ha.cf   source=promise
default:stdlib_common.input[commands]    /var/cfengine/inputs/lib/3.7/commands.cf                     source=promise
default:stdlib_common.input[common]      /var/cfengine/inputs/lib/3.7/common.cf                       source=promise
default:stdlib_common.input[databases]   /var/cfengine/inputs/lib/3.7/databases.cf                    source=promise
default:stdlib_common.input[edit_xml]    /var/cfengine/inputs/lib/3.7/edit_xml.cf                     source=promise
default:stdlib_common.input[files]       /var/cfengine/inputs/lib/3.7/files.cf                        source=promise
default:stdlib_common.input[guest_environments] /var/cfengine/inputs/lib/3.7/guest_environments.cf           source=promise
default:stdlib_common.input[monitor]     /var/cfengine/inputs/lib/3.7/monitor.cf                      source=promise
default:stdlib_common.input[packages]    /var/cfengine/inputs/lib/3.7/packages.cf                     source=promise
default:stdlib_common.input[paths]       /var/cfengine/inputs/lib/3.7/paths.cf                        source=promise
default:stdlib_common.input[processes]   /var/cfengine/inputs/lib/3.7/processes.cf                    source=promise
default:stdlib_common.input[services]    /var/cfengine/inputs/lib/3.7/services.cf                     source=promise
default:stdlib_common.input[storage]     /var/cfengine/inputs/lib/3.7/storage.cf                      source=promise
default:stdlib_common.input[users]       /var/cfengine/inputs/lib/3.7/users.cf                        source=promise
default:stdlib_common.inputs              {'/var/cfengine/inputs/lib/3.7/packages.cf','/var/cfengine/inputs/lib/3.7/edit_xml.cf','/var/cfengine/inputs/lib/3.7/cfe_internal.cf','/var/cfengine/inputs/lib/3.7/monitor.cf','/var/cfengine/inputs/lib/3.7/cfe_internal_hub.cf','/var/cfengine/inputs/lib/3.7/users.cf','/var/cfengine/inputs/lib/3.7/bundles.cf','/var/cfengine/inputs/lib/3.7/cfengine_enterprise_hub_ha.cf','/var/cfengine/inputs/lib/3.7/paths.cf','/var/cfengine/inputs/lib/3.7/databases.cf','/var/cfengine/inputs/lib/3.7/commands.cf','/var/cfengine/inputs/lib/3.7/files.cf','/var/cfengine/inputs/lib/3.7/storage.cf','/var/cfengine/inputs/lib/3.7/processes.cf','/var/cfengine/inputs/lib/3.7/common.cf','/var/cfengine/inputs/lib/3.7/guest_environments.cf','/var/cfengine/inputs/lib/3.7/services.cf'} source=promise
default:suse_knowledge.call_zypper       $(paths.zypper)                                              source=promise
default:suse_knowledge.default_arch      x86_64                                                       source=promise
default:suse_knowledge.sys#arch          x86_64                                                       source=agent
default:sys.arch                         x86_64                                                       inventory,source=agent,attribute_name=Architecture
default:sys.bindir                       /var/cfengine/bin                                            source=agent
default:sys.cdate                        Tue_Jul_26_01_10_51_2016                                     time_based,source=agent
default:sys.cf_agent                     "/var/cfengine/bin/cf-agent"                                 cfe_internal,source=agent
default:sys.cf_execd                     "/var/cfengine/bin/cf-execd"                                 cfe_internal,source=agent
default:sys.cf_hub                       "/var/cfengine/bin/cf-hub"                                   cfe_internal,source=agent
default:sys.cf_key                       "/var/cfengine/bin/cf-key"                                   cfe_internal,source=agent
default:sys.cf_monitord                  "/var/cfengine/bin/cf-monitord"                              cfe_internal,source=agent
default:sys.cf_promises                  "/var/cfengine/bin/cf-promises"                              cfe_internal,source=agent
default:sys.cf_runagent                  "/var/cfengine/bin/cf-runagent"                              cfe_internal,source=agent
default:sys.cf_serverd                   "/var/cfengine/bin/cf-serverd"                               cfe_internal,source=agent
default:sys.cf_twin                      "/var/cfengine/bin/cf-twin"                                  cfe_internal,source=agent
default:sys.cf_version                   3.7.3                                                        inventory,source=agent,attribute_name=CFEngine version
default:sys.cf_version_major             3                                                            source=agent
default:sys.cf_version_minor             7                                                            source=agent
default:sys.cf_version_patch             3                                                            source=agent
default:sys.class                        linux                                                        inventory,source=agent,attribute_name=OS type
default:sys.cpus                         2                                                            inventory,source=agent,attribute_name=CPU logical cores
default:sys.crontab                      /var/spool/cron/root                                         source=agent
default:sys.date                         Tue Jul 26 01:10:51 2016                                     time_based,source=agent
default:sys.doc_root                     /var/www/html                                                source=agent
default:sys.domain                                                                                    source=agent
default:sys.enterprise_version           3.7.3                                                        source=agent
default:sys.exports                      /etc/exports                                                 source=agent
default:sys.failsafe_policy_path         /var/cfengine/inputs/failsafe.cf                             source=agent
default:sys.flavor                       centos_6                                                     inventory,source=agent,attribute_name=none
default:sys.flavour                      centos_6                                                     source=agent
default:sys.fqhost                       hub                                                          inventory,source=agent,attribute_name=Host name
default:sys.fstab                        /etc/fstab                                                   source=agent
default:sys.hardware_addresses            {'08:00:27:9a:98:53','08:00:27:fb:e6:85'}                   inventory,source=agent,attribute_name=MAC addresses
default:sys.hardware_flags                {'up loopback running','up broadcast running multicast','up broadcast running multicast'} source=agent
default:sys.hardware_mac[eth0]           08:00:27:9a:98:53                                            source=agent
default:sys.hardware_mac[eth1]           08:00:27:fb:e6:85                                            source=agent
default:sys.host                         hub                                                          inventory,source=agent,attribute_name=none
default:sys.inputdir                     /var/cfengine/inputs                                         source=agent
default:sys.interface                    eth1                                                         source=agent
default:sys.interface_flags[eth0]        up broadcast running multicast                               source=agent
default:sys.interface_flags[eth1]        up broadcast running multicast                               source=agent
default:sys.interface_flags[lo]          up loopback running                                          source=agent
default:sys.interfaces                    {'eth0','eth1'}                                             inventory,source=agent,attribute_name=Interfaces
default:sys.ip_addresses                  {'127.0.0.1','10.0.2.15','192.168.33.2'}                    source=agent
default:sys.ipv4                         10.0.2.15                                                    inventory,source=agent,attribute_name=none
default:sys.ipv4[eth0]                   10.0.2.15                                                    source=agent
default:sys.ipv4[eth1]                   192.168.33.2                                                 source=agent
default:sys.ipv4[lo]                     127.0.0.1                                                    source=agent
default:sys.ipv4_1[eth0]                 10                                                           source=agent
default:sys.ipv4_1[eth1]                 192                                                          source=agent
default:sys.ipv4_1[lo]                   127                                                          source=agent
default:sys.ipv4_2[eth0]                 10.0                                                         source=agent
default:sys.ipv4_2[eth1]                 192.168                                                      source=agent
default:sys.ipv4_2[lo]                   127.0                                                        source=agent
default:sys.ipv4_3[eth0]                 10.0.2                                                       source=agent
default:sys.ipv4_3[eth1]                 192.168.33                                                   source=agent
default:sys.ipv4_3[lo]                   127.0.0                                                      source=agent
default:sys.key_digest                   SHA=30017fd4f85914d0fa2d8c733958b5508d8383363d937e6385a41629e06ca1ca inventory,source=agent,attribute_name=CFEngine ID
default:sys.last_policy_update           Mon Jul 25 19:13:41 2016                                     source=agent
default:sys.libdir                       /var/cfengine/inputs/lib/3.7                                 source=agent
default:sys.local_libdir                 lib/3.7                                                      source=agent
default:sys.logdir                       /var/cfengine                                                source=agent
default:sys.long_arch                    linux_x86_64_2_6_32_431_el6_x86_64__1_SMP_Fri_Nov_22_03_15_09_UTC_2013 source=agent
default:sys.maildir                      /var/spool/mail                                              source=agent
default:sys.masterdir                    /var/cfengine/masterfiles                                    source=agent
default:sys.nova_version                 3.7.3                                                        deprecated,source=agent
default:sys.os                           linux                                                        source=agent
default:sys.ostype                       linux_x86_64                                                 source=agent
default:sys.piddir                       /var/cfengine                                                source=agent
default:sys.policy_hub                   192.168.33.2                                                 source=bootstrap
default:sys.release                      2.6.32-431.el6.x86_64                                        inventory,source=agent,attribute_name=OS kernel
default:sys.resolv                       /etc/resolv.conf                                             source=agent
default:sys.statedir                     /var/cfengine/state                                          source=agent
default:sys.sysday                       17008                                                        time_based,source=agent
default:sys.systime                      1469495451                                                   time_based,source=agent
default:sys.update_policy_path           /var/cfengine/inputs/update.cf                               source=agent
default:sys.uptime                       635                                                          inventory,time_based,source=agent,attribute_name=Uptime minutes
default:sys.uqhost                       hub                                                          inventory,source=agent,attribute_name=none
default:sys.version                      #1 SMP Fri Nov 22 03:15:09 UTC 2013                          source=agent
default:sys.workdir                      /var/cfengine                                                source=agent
default:url_ping.const#n                 <non-printable>                                              source=agent
default:url_ping.const#r                 <non-printable>                                              source=agent
```

