---
layout: default
title: mon
published: true
tags: [reference, variables, mon, cf-monitord, monitoring]
---

The variables discovered by `cf-monitord` are placed in this monitoring
context. Monitoring variables are expected to be changing rapidly - values are
typically updated or added every 2.5 minutes.

In CFEngine Enterprise, custom defined monitoring targets also become
variables in this context, named by the handle of the promise that defined
them.

### mon.listening_udp4_ports

Port numbers that were observed to be set up to receive connections on the
host concerned.

### mon.listening_tcp4_ports

Port numbers that were observed to be set up to receive connections on the
host concerned.

### mon.listening_udp6_ports

Port numbers that were observed to be set up to receive connections on the
host concerned.

### mon.listening_tcp6_ports

port numbers that were observed
to be set up to receive connections on the host concerned.

### mon.value_users

Users with active processes, including system users.

### mon.av_users

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Users with active processes, including system users.

### mon.dev_users

Users with active processes, including system users.

### mon.value_rootprocs

Sum privileged system processes.

### mon.av_rootprocs

Sum privileged system processes.

### mon.dev_rootprocs

Sum privileged system processes.

### mon.value_otherprocs

Sum non-privileged process.

### mon.av_otherprocs

Sum non-privileged process.

### mon.dev_otherprocs

Sum non-privileged process.

### mon.value_diskfree

Last checked percentage Free disk on / partition.

### mon.av_diskfree

Average percentage Free disk on / partition.

### mon.dev_diskfree

Standard deviation of percentage Free disk on / partition.

### mon.value_loadavg

Kernel load average utilization (sum over cores).

### mon.av_loadavg

Kernel load average utilization (sum over cores).

### mon.dev_loadavg

Kernel load average utilization (sum over cores).

### mon.value_netbiosns_in

netbios name lookups (in).

### mon.av_netbiosns_in

netbios name lookups (in).

### mon.dev_netbiosns_in

netbios name lookups (in).

### mon.value_netbiosns_out

netbios name lookups (out).

### mon.av_netbiosns_out

netbios name lookups (out).

### mon.dev_netbiosns_out

netbios name lookups (out).

### mon.value_netbiosdgm_in

netbios name datagrams (in).

### mon.av_netbiosdgm_in

netbios name datagrams (in).

### mon.dev_netbiosdgm_in

netbios name datagrams (in).

### mon.value_netbiosdgm_out

netbios name datagrams (out).

### mon.av_netbiosdgm_out

netbios name datagrams (out).

### mon.dev_netbiosdgm_out

netbios name datagrams (out).

### mon.value_netbiosssn_in

Samba/netbios name sessions (in).

### mon.av_netbiosssn_in

Samba/netbios name sessions (in).

### mon.dev_netbiosssn_in

Samba/netbios name sessions (in).

### mon.value_netbiosssn_out

Samba/netbios name sessions (out).

### mon.av_netbiosssn_out

Samba/netbios name sessions (out).

### mon.dev_netbiosssn_out

Samba/netbios name sessions (out).

### mon.value_imap_in

imap mail client sessions (in).

### mon.av_imap_in

imap mail client sessions (in).

### mon.dev_imap_in

imap mail client sessions (in).

### mon.value_imap_out

imap mail client sessions (out).

### mon.av_imap_out

imap mail client sessions (out).

### mon.dev_imap_out

imap mail client sessions (out).

### mon.value_cfengine_in

cfengine connections (in).

### mon.av_cfengine_in

cfengine connections (in).

### mon.dev_cfengine_in

cfengine connections (in).

### mon.value_cfengine_out

cfengine connections (out).

### mon.av_cfengine_out

cfengine connections (out).

### mon.dev_cfengine_out

cfengine connections (out).

### mon.value_nfsd_in

nfs connections (in).

### mon.av_nfsd_in

nfs connections (in).

### mon.dev_nfsd_in

nfs connections (in).

### mon.value_nfsd_out

nfs connections (out).

### mon.av_nfsd_out

nfs connections (out).

### mon.dev_nfsd_out

nfs connections (out).

### mon.value_smtp_in

smtp connections (in).

### mon.av_smtp_in

smtp connections (in).

### mon.dev_smtp_in

smtp connections (in).

### mon.value_smtp_out

smtp connections (out).

### mon.av_smtp_out

smtp connections (out).

### mon.dev_smtp_out

smtp connections (out).

### mon.value_www_in

www connections (in).

### mon.av_www_in

www connections (in).

### mon.dev_www_in

www connections (in).

### mon.value_www_out

www connections (out).

### mon.av_www_out

www connections (out).

### mon.dev_www_out

www connections (out).

### mon.value_ftp_in

ftp connections (in).

### mon.av_ftp_in

ftp connections (in).

### mon.dev_ftp_in

ftp connections (in).

### mon.value_ftp_out

ftp connections (out).

### mon.av_ftp_out

ftp connections (out).

### mon.dev_ftp_out

ftp connections (out).

### mon.value_ssh_in

ssh connections (in).

### mon.av_ssh_in

ssh connections (in).

### mon.dev_ssh_in

ssh connections (in).

### mon.value_ssh_out

ssh connections (out).

### mon.av_ssh_out

ssh connections (out).

### mon.dev_ssh_out

ssh connections (out).

### mon.value_wwws_in

wwws connections (in).

### mon.av_wwws_in

wwws connections (in).

### mon.dev_wwws_in

wwws connections (in).

### mon.value_wwws_out

wwws connections (out).

### mon.av_wwws_out

wwws connections (out).

### mon.dev_wwws_out

wwws connections (out).

### mon.value_icmp_in

ICMP packets (in).

### mon.av_icmp_in

ICMP packets (in).

### mon.dev_icmp_in

ICMP packets (in).

### mon.value_icmp_out

ICMP packets (out).

### mon.av_icmp_out

ICMP packets (out).

### mon.dev_icmp_out

ICMP packets (out).

### mon.value_udp_in

UDP dgrams (in).

### mon.av_udp_in

UDP dgrams (in).

### mon.dev_udp_in

UDP dgrams (in).

### mon.value_udp_out

UDP dgrams (out).

### mon.av_udp_out

UDP dgrams (out).

### mon.dev_udp_out

UDP dgrams (out).

### mon.value_dns_in

DNS requests (in).

### mon.av_dns_in

DNS requests (in).

### mon.dev_dns_in

DNS requests (in).

### mon.value_dns_out

DNS requests (out).

### mon.av_dns_out

DNS requests (out).

### mon.dev_dns_out

DNS requests (out).

### mon.value_tcpsyn_in

TCP sessions (in).

### mon.av_tcpsyn_in

TCP sessions (in).

### mon.dev_tcpsyn_in

TCP sessions (in).

### mon.value_tcpsyn_out

TCP sessions (out).

### mon.av_tcpsyn_out

TCP sessions (out).

### mon.dev_tcpsyn_out

TCP sessions (out).

### mon.value_tcpack_in

TCP acks (in).

### mon.av_tcpack_in

TCP acks (in).

### mon.dev_tcpack_in

TCP acks (in).

### mon.value_tcpack_out

TCP acks (out).

### mon.av_tcpack_out

TCP acks (out).

### mon.dev_tcpack_out

TCP acks (out).

### mon.value_tcpfin_in

TCP finish (in).

### mon.av_tcpfin_in

TCP finish (in).

### mon.dev_tcpfin_in

TCP finish (in).

### mon.value_tcpfin_out

TCP finish (out).

### mon.av_tcpfin_out

TCP finish (out).

### mon.dev_tcpfin_out

TCP finish (out).

### mon.value_tcpmisc_in

TCP misc (in).

### mon.av_tcpmisc_in

TCP misc (in).

### mon.dev_tcpmisc_in

TCP misc (in).

### mon.value_tcpmisc_out

TCP misc (out).

### mon.av_tcpmisc_out

TCP misc (out).

### mon.dev_tcpmisc_out

TCP misc (out).

### mon.value_webaccess

Webserver hits.

### mon.av_webaccess

Webserver hits.

### mon.dev_webaccess

Webserver hits.

### mon.value_weberrors

Webserver errors.

### mon.av_weberrors

Webserver errors.

### mon.dev_weberrors

Webserver errors.

### mon.value_syslog

New log entries (Syslog).

### mon.av_syslog

New log entries (Syslog).

### mon.dev_syslog

New log entries (Syslog).

### mon.value_messages

New log entries (messages).

### mon.av_messages

New log entries (messages).

### mon.dev_messages

New log entries (messages).

### mon.value_temp0

CPU Temperature 0.

### mon.av_temp0

CPU Temperature 0.

### mon.dev_temp0

CPU Temperature 0.

### mon.value_temp1

CPU Temperature 1.

### mon.av_temp1

CPU Temperature 1.

### mon.dev_temp1

CPU Temperature 1.

### mon.value_temp2

CPU Temperature 2.

### mon.av_temp2

CPU Temperature 2.

### mon.dev_temp2

CPU Temperature 2.

### mon.value_temp3

CPU Temperature 3.

### mon.av_temp3

CPU Temperature 3.

### mon.dev_temp3

CPU Temperature 3.

### mon.value_cpu

%CPU utilization (all).

### mon.av_cpu

%CPU utilization (all).

### mon.dev_cpu

%CPU utilization (all).

### mon.value_cpu0

%CPU utilization 0.

### mon.av_cpu0

%CPU utilization 0.

### mon.dev_cpu0

%CPU utilization 0.

### mon.value_cpu1

%CPU utilization 1.

### mon.av_cpu1

%CPU utilization 1.

### mon.dev_cpu1

%CPU utilization 1.

### mon.value_cpu2

%CPU utilization 2.

### mon.av_cpu2

%CPU utilization 2.

### mon.dev_cpu2

%CPU utilization 2.

### mon.value_cpu3

%CPU utilization 3.

### mon.av_cpu3

%CPU utilization 3.

### mon.dev_cpu3

%CPU utilization 3.

### mon.value_microsoft_ds_in

Samba/MS_ds name sessions (in).

### mon.av_microsoft_ds_in

Samba/MS_ds name sessions (in).

### mon.dev_microsoft_ds_in

Samba/MS_ds name sessions (in).

### mon.value_microsoft_ds_out

Samba/MS_ds name sessions (out).

### mon.av_microsoft_ds_out

Samba/MS_ds name sessions (out).

### mon.dev_microsoft_ds_out

Samba/MS_ds name sessions (out).

### mon.value_www_alt_in

Alternative web service connections (in).

### mon.av_www_alt_in

Alternative web service connections (in).

### mon.dev_www_alt_in

Alternative web service connections (in).

### mon.value_www_alt_out

Alternative web client connections (out).

### mon.av_www_alt_out

Alternative web client connections (out).

### mon.dev_www_alt_out

Alternative web client connections (out).

### mon.value_imaps_in

encrypted imap mail service sessions (in).

### mon.av_imaps_in

encrypted imap mail service sessions (in).

### mon.dev_imaps_in

encrypted imap mail service sessions (in).

### mon.value_imaps_out

encrypted imap mail client sessions (out).

### mon.av_imaps_out

encrypted imap mail client sessions (out).

### mon.dev_imaps_out

encrypted imap mail client sessions (out).

### mon.value_ldap_in

LDAP directory service service sessions (in).

### mon.av_ldap_in

LDAP directory service service sessions (in).

### mon.dev_ldap_in

LDAP directory service service sessions (in).

### mon.value_ldap_out

LDAP directory service client sessions (out).

### mon.av_ldap_out

LDAP directory service client sessions (out).

### mon.dev_ldap_out

LDAP directory service client sessions (out).

### mon.value_ldaps_in

LDAP directory service service sessions (in).

### mon.av_ldaps_in

LDAP directory service service sessions (in).

### mon.dev_ldaps_in

LDAP directory service service sessions (in).

### mon.value_ldaps_out

LDAP directory service client sessions (out).

### mon.av_ldaps_out

LDAP directory service client sessions (out).

### mon.dev_ldaps_out

LDAP directory service client sessions (out).

### mon.value_mongo_in

Mongo database service sessions (in).

### mon.av_mongo_in

Mongo database service sessions (in).

### mon.dev_mongo_in

Mongo database service sessions (in).

### mon.value_mongo_out

Mongo database client sessions (out).

### mon.av_mongo_out

Mongo database client sessions (out).

### mon.dev_mongo_out

Mongo database client sessions (out).

### mon.value_mysql_in

MySQL database service sessions (in).

### mon.av_mysql_in

MySQL database service sessions (in).

### mon.dev_mysql_in

MySQL database service sessions (in).

### mon.value_mysql_out

MySQL database client sessions (out).

### mon.av_mysql_out

MySQL database client sessions (out).

### mon.dev_mysql_out

MySQL database client sessions (out).

### mon.value_postgres_in

PostgreSQL database service sessions (in).

### mon.av_postgres_in

PostgreSQL database service sessions (in).

### mon.dev_postgres_in

PostgreSQL database service sessions (in).

### mon.value_postgres_out

PostgreSQL database client sessions (out).

### mon.av_postgres_out

PostgreSQL database client sessions (out).

### mon.dev_postgres_out

PostgreSQL database client sessions (out).

### mon.value_ipp_in

Internet Printer Protocol (in).

### mon.av_ipp_in

Internet Printer Protocol (in).

### mon.dev_ipp_in

Internet Printer Protocol (in).

### mon.value_ipp_out

Internet Printer Protocol (out).

### mon.av_ipp_out

Internet Printer Protocol (out).

### mon.dev_ipp_out

Internet Printer Protocol (out).
