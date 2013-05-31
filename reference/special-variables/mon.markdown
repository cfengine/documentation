---
layout: default
title: Variable context mon
categories: [Reference, Special Variables, Variable context mon]
published: true
alias: reference-special-variables-variable-context-mon.html
tags: [reference, variables, variable context mon, cf-monitord, monitoring]
---

The variables discovered by `cf-monitord` are placed in this monitoring
context. Monitoring variables are expected to be changing rapidly.

In CFEngine Enterprise, custom defined monitoring targets also become 
variables in this context, named by the handle of the promise that defined 
them.

### mon.listening\_udp4\_ports

List variable containing an observational measure collected every 2.5
minutes from `cf-monitord`. Description: port numbers that were observed
to be set up to receive connections on the host concerned.

### mon.listening\_tcp4\_ports

List variable containing an observational measure collected every 2.5
minutes from `cf-monitord`. Description: port numbers that were observed
to be set up to receive connections on the host concerned.

### mon.listening\_udp6\_ports

List variable containing an observational measure collected every 2.5
minutes from `cf-monitord`. Description: port numbers that were observed
to be set up to receive connections on the host concerned.

### mon.listening\_tcp6\_ports

List variable containing an observational measure collected every 2.5
minutes from `cf-monitord`. Description: port numbers that were observed
to be set up to receive connections on the host concerned.

### mon.value\_users

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Users with active processes, including system users.

### mon.av\_users

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Users with active processes, including system users.

### mon.dev\_users

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Users with active processes, including system users.

### mon.value\_rootprocs

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Sum privileged system processes.

### mon.av\_rootprocs

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Sum privileged system processes.

### mon.dev\_rootprocs

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Sum privileged system processes.

### mon.value\_otherprocs

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Sum non-privileged process.

### mon.av\_otherprocs

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Sum non-privileged process.

### mon.dev\_otherprocs

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Sum non-privileged process.

### mon.value\_diskfree

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Free disk on / partition.

### mon.av\_diskfree

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Free disk on / partition.

### mon.dev\_diskfree

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Free disk on / partition.

### mon.value\_loadavg

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Kernel load average utilization (sum over cores).

### mon.av\_loadavg

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Kernel load average utilization (sum over cores).

### mon.dev\_loadavg

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Kernel load average utilization (sum over cores).

### mon.value\_netbiosns\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: netbios name lookups (in).

### mon.av\_netbiosns\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: netbios name lookups (in).

### mon.dev\_netbiosns\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: netbios name lookups (in).

### mon.value\_netbiosns\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: netbios name lookups (out).

### mon.av\_netbiosns\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: netbios name lookups (out).

### mon.dev\_netbiosns\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: netbios name lookups (out).

### mon.value\_netbiosdgm\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: netbios name datagrams (in).

### mon.av\_netbiosdgm\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: netbios name datagrams (in).

### mon.dev\_netbiosdgm\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: netbios name datagrams (in).

### mon.value\_netbiosdgm\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: netbios name datagrams (out).

### mon.av\_netbiosdgm\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: netbios name datagrams (out).

### mon.dev\_netbiosdgm\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: netbios name datagrams (out).

### mon.value\_netbiosssn\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Samba/netbios name sessions (in).

### mon.av\_netbiosssn\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Samba/netbios name sessions (in).

### mon.dev\_netbiosssn\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Samba/netbios name sessions (in).

### mon.value\_netbiosssn\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Samba/netbios name sessions (out).

### mon.av\_netbiosssn\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Samba/netbios name sessions (out).

### mon.dev\_netbiosssn\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Samba/netbios name sessions (out).

### mon.value\_imap\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: imap mail client sessions (in).

### mon.av\_imap\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: imap mail client sessions (in).

### mon.dev\_imap\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: imap mail client sessions (in).

### mon.value\_imap\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: imap mail client sessions (out).

### mon.av\_imap\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: imap mail client sessions (out).

### mon.dev\_imap\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: imap mail client sessions (out).

### mon.value\_cfengine\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: cfengine connections (in).

### mon.av\_cfengine\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: cfengine connections (in).

### mon.dev\_cfengine\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: cfengine connections (in).

### mon.value\_cfengine\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: cfengine connections (out).

### mon.av\_cfengine\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: cfengine connections (out).

### mon.dev\_cfengine\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: cfengine connections (out).

### mon.value\_nfsd\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: nfs connections (in).

### mon.av\_nfsd\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: nfs connections (in).

### mon.dev\_nfsd\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: nfs connections (in).

### mon.value\_nfsd\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: nfs connections (out).

### mon.av\_nfsd\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: nfs connections (out).

### mon.dev\_nfsd\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: nfs connections (out).

### mon.value\_smtp\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: smtp connections (in).

### mon.av\_smtp\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: smtp connections (in).

### mon.dev\_smtp\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: smtp connections (in).

### mon.value\_smtp\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: smtp connections (out).

### mon.av\_smtp\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: smtp connections (out).

### mon.dev\_smtp\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: smtp connections (out).

### mon.value\_www\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: www connections (in).

### mon.av\_www\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: www connections (in).

### mon.dev\_www\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: www connections (in).

### mon.value\_www\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: www connections (out).

### mon.av\_www\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: www connections (out).

### mon.dev\_www\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: www connections (out).

### mon.value\_ftp\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: ftp connections (in).

### mon.av\_ftp\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: ftp connections (in).

### mon.dev\_ftp\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: ftp connections (in).

### mon.value\_ftp\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: ftp connections (out).

### mon.av\_ftp\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: ftp connections (out).

### mon.dev\_ftp\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: ftp connections (out).

### mon.value\_ssh\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: ssh connections (in).

### mon.av\_ssh\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: ssh connections (in).

### mon.dev\_ssh\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: ssh connections (in).

### mon.value\_ssh\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: ssh connections (out).

### mon.av\_ssh\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: ssh connections (out).

### mon.dev\_ssh\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: ssh connections (out).

### mon.value\_wwws\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: wwws connections (in).

### mon.av\_wwws\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: wwws connections (in).

### mon.dev\_wwws\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: wwws connections (in).

### mon.value\_wwws\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: wwws connections (out).

### mon.av\_wwws\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: wwws connections (out).

### mon.dev\_wwws\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: wwws connections (out).

### mon.value\_icmp\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: ICMP packets (in).

### mon.av\_icmp\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: ICMP packets (in).

### mon.dev\_icmp\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: ICMP packets (in).

### mon.value\_icmp\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: ICMP packets (out).

### mon.av\_icmp\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: ICMP packets (out).

### mon.dev\_icmp\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: ICMP packets (out).

### mon.value\_udp\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: UDP dgrams (in).

### mon.av\_udp\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: UDP dgrams (in).

### mon.dev\_udp\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: UDP dgrams (in).

### mon.value\_udp\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: UDP dgrams (out).

### mon.av\_udp\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: UDP dgrams (out).

### mon.dev\_udp\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: UDP dgrams (out).

### mon.value\_dns\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: DNS requests (in).

### mon.av\_dns\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: DNS requests (in).

### mon.dev\_dns\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: DNS requests (in).

### mon.value\_dns\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: DNS requests (out).

### mon.av\_dns\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: DNS requests (out).

### mon.dev\_dns\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: DNS requests (out).

### mon.value\_tcpsyn\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP sessions (in).

### mon.av\_tcpsyn\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP sessions (in).

### mon.dev\_tcpsyn\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP sessions (in).

### mon.value\_tcpsyn\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP sessions (out).

### mon.av\_tcpsyn\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP sessions (out).

### mon.dev\_tcpsyn\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP sessions (out).

### mon.value\_tcpack\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP acks (in).

### mon.av\_tcpack\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP acks (in).

### mon.dev\_tcpack\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP acks (in).

### mon.value\_tcpack\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP acks (out).

### mon.av\_tcpack\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP acks (out).

### mon.dev\_tcpack\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP acks (out).

### mon.value\_tcpfin\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP finish (in).

### mon.av\_tcpfin\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP finish (in).

### mon.dev\_tcpfin\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP finish (in).

### mon.value\_tcpfin\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP finish (out).

### mon.av\_tcpfin\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP finish (out).

### mon.dev\_tcpfin\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP finish (out).

### mon.value\_tcpmisc\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP misc (in).

### mon.av\_tcpmisc\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP misc (in).

### mon.dev\_tcpmisc\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP misc (in).

### mon.value\_tcpmisc\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP misc (out).

### mon.av\_tcpmisc\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP misc (out).

### mon.dev\_tcpmisc\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: TCP misc (out).

### mon.value\_webaccess

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Webserver hits.

### mon.av\_webaccess

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Webserver hits.

### mon.dev\_webaccess

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Webserver hits.

### mon.value\_weberrors

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Webserver errors.

### mon.av\_weberrors

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Webserver errors.

### mon.dev\_weberrors

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Webserver errors.

### mon.value\_syslog

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: New log entries (Syslog).

### mon.av\_syslog

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: New log entries (Syslog).

### mon.dev\_syslog

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: New log entries (Syslog).

### mon.value\_messages

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: New log entries (messages).

### mon.av\_messages

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: New log entries (messages).

### mon.dev\_messages

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: New log entries (messages).

### mon.value\_temp0

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: CPU Temperature 0.

### mon.av\_temp0

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: CPU Temperature 0.

### mon.dev\_temp0

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: CPU Temperature 0.

### mon.value\_temp1

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: CPU Temperature 1.

### mon.av\_temp1

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: CPU Temperature 1.

### mon.dev\_temp1

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: CPU Temperature 1.

### mon.value\_temp2

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: CPU Temperature 2.

### mon.av\_temp2

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: CPU Temperature 2.

### mon.dev\_temp2

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: CPU Temperature 2.

### mon.value\_temp3

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: CPU Temperature 3.

### mon.av\_temp3

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: CPU Temperature 3.

### mon.dev\_temp3

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: CPU Temperature 3.

### mon.value\_cpu

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: %CPU utilization (all).

### mon.av\_cpu

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: %CPU utilization (all).

### mon.dev\_cpu

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: %CPU utilization (all).

### mon.value\_cpu0

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: %CPU utilization 0.

### mon.av\_cpu0

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: %CPU utilization 0.

### mon.dev\_cpu0

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: %CPU utilization 0.

### mon.value\_cpu1

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: %CPU utilization 1.

### mon.av\_cpu1

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: %CPU utilization 1.

### mon.dev\_cpu1

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: %CPU utilization 1.

### mon.value\_cpu2

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: %CPU utilization 2.

### mon.av\_cpu2

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: %CPU utilization 2.

### mon.dev\_cpu2

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: %CPU utilization 2.

### mon.value\_cpu3

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: %CPU utilization 3.

### mon.av\_cpu3

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: %CPU utilization 3.

### mon.dev\_cpu3

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: %CPU utilization 3.

### mon.value\_microsoft\_ds\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Samba/MS\_ds name sessions (in).

### mon.av\_microsoft\_ds\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Samba/MS\_ds name sessions (in).

### mon.dev\_microsoft\_ds\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Samba/MS\_ds name sessions (in).

### mon.value\_microsoft\_ds\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Samba/MS\_ds name sessions (out).

### mon.av\_microsoft\_ds\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Samba/MS\_ds name sessions (out).

### mon.dev\_microsoft\_ds\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Samba/MS\_ds name sessions (out).

### mon.value\_www\_alt\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Alternative web service connections (in).

### mon.av\_www\_alt\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Alternative web service connections (in).

### mon.dev\_www\_alt\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Alternative web service connections (in).

### mon.value\_www\_alt\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Alternative web client connections (out).

### mon.av\_www\_alt\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Alternative web client connections (out).

### mon.dev\_www\_alt\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Alternative web client connections (out).

### mon.value\_imaps\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: encrypted imap mail service sessions (in).

### mon.av\_imaps\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: encrypted imap mail service sessions (in).

### mon.dev\_imaps\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: encrypted imap mail service sessions (in).

### mon.value\_imaps\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: encrypted imap mail client sessions (out).

### mon.av\_imaps\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: encrypted imap mail client sessions (out).

### mon.dev\_imaps\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: encrypted imap mail client sessions (out).

### mon.value\_ldap\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: LDAP directory service service sessions (in).

### mon.av\_ldap\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: LDAP directory service service sessions (in).

### mon.dev\_ldap\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: LDAP directory service service sessions (in).

### mon.value\_ldap\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: LDAP directory service client sessions (out).

### mon.av\_ldap\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: LDAP directory service client sessions (out).

### mon.dev\_ldap\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: LDAP directory service client sessions (out).

### mon.value\_ldaps\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: LDAP directory service service sessions (in).

### mon.av\_ldaps\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: LDAP directory service service sessions (in).

### mon.dev\_ldaps\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: LDAP directory service service sessions (in).

### mon.value\_ldaps\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: LDAP directory service client sessions (out).

### mon.av\_ldaps\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: LDAP directory service client sessions (out).

### mon.dev\_ldaps\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: LDAP directory service client sessions (out).

### mon.value\_mongo\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Mongo database service sessions (in).

### mon.av\_mongo\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Mongo database service sessions (in).

### mon.dev\_mongo\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Mongo database service sessions (in).

### mon.value\_mongo\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Mongo database client sessions (out).

### mon.av\_mongo\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Mongo database client sessions (out).

### mon.dev\_mongo\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Mongo database client sessions (out).

### mon.value\_mysql\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: MySQL database service sessions (in).

### mon.av\_mysql\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: MySQL database service sessions (in).

### mon.dev\_mysql\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: MySQL database service sessions (in).

### mon.value\_mysql\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: MySQL database client sessions (out).

### mon.av\_mysql\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: MySQL database client sessions (out).

### mon.dev\_mysql\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: MySQL database client sessions (out).

### mon.value\_postgres\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: PostgreSQL database service sessions (in).

### mon.av\_postgres\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: PostgreSQL database service sessions (in).

### mon.dev\_postgres\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: PostgreSQL database service sessions (in).

### mon.value\_postgres\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: PostgreSQL database client sessions (out).

### mon.av\_postgres\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: PostgreSQL database client sessions (out).

### mon.dev\_postgres\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: PostgreSQL database client sessions (out).

### mon.value\_ipp\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Internet Printer Protocol (in).

### mon.av\_ipp\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Internet Printer Protocol (in).

### mon.dev\_ipp\_in

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Internet Printer Protocol (in).

### mon.value\_ipp\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Internet Printer Protocol (out).

### mon.av\_ipp\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Internet Printer Protocol (out).

### mon.dev\_ipp\_out

Observational measure collected every 2.5 minutes from `cf-monitord`.
Description: Internet Printer Protocol (out).
