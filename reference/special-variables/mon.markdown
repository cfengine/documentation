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

#### Variable mon.listening\_udp4\_ports

List variable containing an observational measure collected every 2.5
minutes from cf-monitord. Description: port numbers that were observed
to be set up to receive connections on the host concerned.

#### Variable mon.listening\_tcp4\_ports

List variable containing an observational measure collected every 2.5
minutes from cf-monitord. Description: port numbers that were observed
to be set up to receive connections on the host concerned.

#### Variable mon.listening\_udp6\_ports

List variable containing an observational measure collected every 2.5
minutes from cf-monitord. Description: port numbers that were observed
to be set up to receive connections on the host concerned.

#### Variable mon.listening\_tcp6\_ports

List variable containing an observational measure collected every 2.5
minutes from cf-monitord. Description: port numbers that were observed
to be set up to receive connections on the host concerned.

#### Variable mon.value\_users

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Users with active processes, including system users.

#### Variable mon.av\_users

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Users with active processes, including system users.

#### Variable mon.dev\_users

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Users with active processes, including system users.

#### Variable mon.value\_rootprocs

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Sum privileged system processes.

#### Variable mon.av\_rootprocs

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Sum privileged system processes.

#### Variable mon.dev\_rootprocs

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Sum privileged system processes.

#### Variable mon.value\_otherprocs

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Sum non-privileged process.

#### Variable mon.av\_otherprocs

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Sum non-privileged process.

#### Variable mon.dev\_otherprocs

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Sum non-privileged process.

#### Variable mon.value\_diskfree

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Free disk on / partition.

#### Variable mon.av\_diskfree

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Free disk on / partition.

#### Variable mon.dev\_diskfree

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Free disk on / partition.

#### Variable mon.value\_loadavg

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Kernel load average utilization (sum over cores).

#### Variable mon.av\_loadavg

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Kernel load average utilization (sum over cores).

#### Variable mon.dev\_loadavg

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Kernel load average utilization (sum over cores).

#### Variable mon.value\_netbiosns\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: netbios name lookups (in).

#### Variable mon.av\_netbiosns\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: netbios name lookups (in).

#### Variable mon.dev\_netbiosns\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: netbios name lookups (in).

#### Variable mon.value\_netbiosns\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: netbios name lookups (out).

#### Variable mon.av\_netbiosns\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: netbios name lookups (out).

#### Variable mon.dev\_netbiosns\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: netbios name lookups (out).

#### Variable mon.value\_netbiosdgm\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: netbios name datagrams (in).

#### Variable mon.av\_netbiosdgm\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: netbios name datagrams (in).

#### Variable mon.dev\_netbiosdgm\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: netbios name datagrams (in).

#### Variable mon.value\_netbiosdgm\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: netbios name datagrams (out).

#### Variable mon.av\_netbiosdgm\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: netbios name datagrams (out).

#### Variable mon.dev\_netbiosdgm\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: netbios name datagrams (out).

#### Variable mon.value\_netbiosssn\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Samba/netbios name sessions (in).

#### Variable mon.av\_netbiosssn\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Samba/netbios name sessions (in).

#### Variable mon.dev\_netbiosssn\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Samba/netbios name sessions (in).

#### Variable mon.value\_netbiosssn\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Samba/netbios name sessions (out).

#### Variable mon.av\_netbiosssn\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Samba/netbios name sessions (out).

#### Variable mon.dev\_netbiosssn\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Samba/netbios name sessions (out).

#### Variable mon.value\_imap\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: imap mail client sessions (in).

#### Variable mon.av\_imap\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: imap mail client sessions (in).

#### Variable mon.dev\_imap\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: imap mail client sessions (in).

#### Variable mon.value\_imap\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: imap mail client sessions (out).

#### Variable mon.av\_imap\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: imap mail client sessions (out).

#### Variable mon.dev\_imap\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: imap mail client sessions (out).

#### Variable mon.value\_cfengine\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: cfengine connections (in).

#### Variable mon.av\_cfengine\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: cfengine connections (in).

#### Variable mon.dev\_cfengine\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: cfengine connections (in).

#### Variable mon.value\_cfengine\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: cfengine connections (out).

#### Variable mon.av\_cfengine\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: cfengine connections (out).

#### Variable mon.dev\_cfengine\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: cfengine connections (out).

#### Variable mon.value\_nfsd\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: nfs connections (in).

#### Variable mon.av\_nfsd\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: nfs connections (in).

#### Variable mon.dev\_nfsd\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: nfs connections (in).

#### Variable mon.value\_nfsd\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: nfs connections (out).

#### Variable mon.av\_nfsd\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: nfs connections (out).

#### Variable mon.dev\_nfsd\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: nfs connections (out).

#### Variable mon.value\_smtp\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: smtp connections (in).

#### Variable mon.av\_smtp\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: smtp connections (in).

#### Variable mon.dev\_smtp\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: smtp connections (in).

#### Variable mon.value\_smtp\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: smtp connections (out).

#### Variable mon.av\_smtp\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: smtp connections (out).

#### Variable mon.dev\_smtp\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: smtp connections (out).

#### Variable mon.value\_www\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: www connections (in).

#### Variable mon.av\_www\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: www connections (in).

#### Variable mon.dev\_www\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: www connections (in).

#### Variable mon.value\_www\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: www connections (out).

#### Variable mon.av\_www\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: www connections (out).

#### Variable mon.dev\_www\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: www connections (out).

#### Variable mon.value\_ftp\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: ftp connections (in).

#### Variable mon.av\_ftp\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: ftp connections (in).

#### Variable mon.dev\_ftp\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: ftp connections (in).

#### Variable mon.value\_ftp\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: ftp connections (out).

#### Variable mon.av\_ftp\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: ftp connections (out).

#### Variable mon.dev\_ftp\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: ftp connections (out).

#### Variable mon.value\_ssh\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: ssh connections (in).

#### Variable mon.av\_ssh\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: ssh connections (in).

#### Variable mon.dev\_ssh\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: ssh connections (in).

#### Variable mon.value\_ssh\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: ssh connections (out).

#### Variable mon.av\_ssh\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: ssh connections (out).

#### Variable mon.dev\_ssh\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: ssh connections (out).

#### Variable mon.value\_wwws\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: wwws connections (in).

#### Variable mon.av\_wwws\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: wwws connections (in).

#### Variable mon.dev\_wwws\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: wwws connections (in).

#### Variable mon.value\_wwws\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: wwws connections (out).

#### Variable mon.av\_wwws\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: wwws connections (out).

#### Variable mon.dev\_wwws\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: wwws connections (out).

#### Variable mon.value\_icmp\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: ICMP packets (in).

#### Variable mon.av\_icmp\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: ICMP packets (in).

#### Variable mon.dev\_icmp\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: ICMP packets (in).

#### Variable mon.value\_icmp\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: ICMP packets (out).

#### Variable mon.av\_icmp\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: ICMP packets (out).

#### Variable mon.dev\_icmp\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: ICMP packets (out).

#### Variable mon.value\_udp\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: UDP dgrams (in).

#### Variable mon.av\_udp\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: UDP dgrams (in).

#### Variable mon.dev\_udp\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: UDP dgrams (in).

#### Variable mon.value\_udp\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: UDP dgrams (out).

#### Variable mon.av\_udp\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: UDP dgrams (out).

#### Variable mon.dev\_udp\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: UDP dgrams (out).

#### Variable mon.value\_dns\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: DNS requests (in).

#### Variable mon.av\_dns\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: DNS requests (in).

#### Variable mon.dev\_dns\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: DNS requests (in).

#### Variable mon.value\_dns\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: DNS requests (out).

#### Variable mon.av\_dns\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: DNS requests (out).

#### Variable mon.dev\_dns\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: DNS requests (out).

#### Variable mon.value\_tcpsyn\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP sessions (in).

#### Variable mon.av\_tcpsyn\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP sessions (in).

#### Variable mon.dev\_tcpsyn\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP sessions (in).

#### Variable mon.value\_tcpsyn\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP sessions (out).

#### Variable mon.av\_tcpsyn\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP sessions (out).

#### Variable mon.dev\_tcpsyn\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP sessions (out).

#### Variable mon.value\_tcpack\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP acks (in).

#### Variable mon.av\_tcpack\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP acks (in).

#### Variable mon.dev\_tcpack\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP acks (in).

#### Variable mon.value\_tcpack\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP acks (out).

#### Variable mon.av\_tcpack\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP acks (out).

#### Variable mon.dev\_tcpack\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP acks (out).

#### Variable mon.value\_tcpfin\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP finish (in).

#### Variable mon.av\_tcpfin\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP finish (in).

#### Variable mon.dev\_tcpfin\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP finish (in).

#### Variable mon.value\_tcpfin\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP finish (out).

#### Variable mon.av\_tcpfin\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP finish (out).

#### Variable mon.dev\_tcpfin\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP finish (out).

#### Variable mon.value\_tcpmisc\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP misc (in).

#### Variable mon.av\_tcpmisc\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP misc (in).

#### Variable mon.dev\_tcpmisc\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP misc (in).

#### Variable mon.value\_tcpmisc\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP misc (out).

#### Variable mon.av\_tcpmisc\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP misc (out).

#### Variable mon.dev\_tcpmisc\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: TCP misc (out).

#### Variable mon.value\_webaccess

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Webserver hits.

#### Variable mon.av\_webaccess

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Webserver hits.

#### Variable mon.dev\_webaccess

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Webserver hits.

#### Variable mon.value\_weberrors

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Webserver errors.

#### Variable mon.av\_weberrors

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Webserver errors.

#### Variable mon.dev\_weberrors

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Webserver errors.

#### Variable mon.value\_syslog

Observational measure collected every 2.5 minutes from cf-monitord.
Description: New log entries (Syslog).

#### Variable mon.av\_syslog

Observational measure collected every 2.5 minutes from cf-monitord.
Description: New log entries (Syslog).

#### Variable mon.dev\_syslog

Observational measure collected every 2.5 minutes from cf-monitord.
Description: New log entries (Syslog).

#### Variable mon.value\_messages

Observational measure collected every 2.5 minutes from cf-monitord.
Description: New log entries (messages).

#### Variable mon.av\_messages

Observational measure collected every 2.5 minutes from cf-monitord.
Description: New log entries (messages).

#### Variable mon.dev\_messages

Observational measure collected every 2.5 minutes from cf-monitord.
Description: New log entries (messages).

#### Variable mon.value\_temp0

Observational measure collected every 2.5 minutes from cf-monitord.
Description: CPU Temperature 0.

#### Variable mon.av\_temp0

Observational measure collected every 2.5 minutes from cf-monitord.
Description: CPU Temperature 0.

#### Variable mon.dev\_temp0

Observational measure collected every 2.5 minutes from cf-monitord.
Description: CPU Temperature 0.

#### Variable mon.value\_temp1

Observational measure collected every 2.5 minutes from cf-monitord.
Description: CPU Temperature 1.

#### Variable mon.av\_temp1

Observational measure collected every 2.5 minutes from cf-monitord.
Description: CPU Temperature 1.

#### Variable mon.dev\_temp1

Observational measure collected every 2.5 minutes from cf-monitord.
Description: CPU Temperature 1.

#### Variable mon.value\_temp2

Observational measure collected every 2.5 minutes from cf-monitord.
Description: CPU Temperature 2.

#### Variable mon.av\_temp2

Observational measure collected every 2.5 minutes from cf-monitord.
Description: CPU Temperature 2.

#### Variable mon.dev\_temp2

Observational measure collected every 2.5 minutes from cf-monitord.
Description: CPU Temperature 2.

#### Variable mon.value\_temp3

Observational measure collected every 2.5 minutes from cf-monitord.
Description: CPU Temperature 3.

#### Variable mon.av\_temp3

Observational measure collected every 2.5 minutes from cf-monitord.
Description: CPU Temperature 3.

#### Variable mon.dev\_temp3

Observational measure collected every 2.5 minutes from cf-monitord.
Description: CPU Temperature 3.

#### Variable mon.value\_cpu

Observational measure collected every 2.5 minutes from cf-monitord.
Description: %CPU utilization (all).

#### Variable mon.av\_cpu

Observational measure collected every 2.5 minutes from cf-monitord.
Description: %CPU utilization (all).

#### Variable mon.dev\_cpu

Observational measure collected every 2.5 minutes from cf-monitord.
Description: %CPU utilization (all).

#### Variable mon.value\_cpu0

Observational measure collected every 2.5 minutes from cf-monitord.
Description: %CPU utilization 0.

#### Variable mon.av\_cpu0

Observational measure collected every 2.5 minutes from cf-monitord.
Description: %CPU utilization 0.

#### Variable mon.dev\_cpu0

Observational measure collected every 2.5 minutes from cf-monitord.
Description: %CPU utilization 0.

#### Variable mon.value\_cpu1

Observational measure collected every 2.5 minutes from cf-monitord.
Description: %CPU utilization 1.

#### Variable mon.av\_cpu1

Observational measure collected every 2.5 minutes from cf-monitord.
Description: %CPU utilization 1.

#### Variable mon.dev\_cpu1

Observational measure collected every 2.5 minutes from cf-monitord.
Description: %CPU utilization 1.

#### Variable mon.value\_cpu2

Observational measure collected every 2.5 minutes from cf-monitord.
Description: %CPU utilization 2.

#### Variable mon.av\_cpu2

Observational measure collected every 2.5 minutes from cf-monitord.
Description: %CPU utilization 2.

#### Variable mon.dev\_cpu2

Observational measure collected every 2.5 minutes from cf-monitord.
Description: %CPU utilization 2.

#### Variable mon.value\_cpu3

Observational measure collected every 2.5 minutes from cf-monitord.
Description: %CPU utilization 3.

#### Variable mon.av\_cpu3

Observational measure collected every 2.5 minutes from cf-monitord.
Description: %CPU utilization 3.

#### Variable mon.dev\_cpu3

Observational measure collected every 2.5 minutes from cf-monitord.
Description: %CPU utilization 3.

#### Variable mon.value\_microsoft\_ds\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Samba/MS\_ds name sessions (in).

#### Variable mon.av\_microsoft\_ds\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Samba/MS\_ds name sessions (in).

#### Variable mon.dev\_microsoft\_ds\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Samba/MS\_ds name sessions (in).

#### Variable mon.value\_microsoft\_ds\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Samba/MS\_ds name sessions (out).

#### Variable mon.av\_microsoft\_ds\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Samba/MS\_ds name sessions (out).

#### Variable mon.dev\_microsoft\_ds\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Samba/MS\_ds name sessions (out).

#### Variable mon.value\_www\_alt\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Alternative web service connections (in).

#### Variable mon.av\_www\_alt\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Alternative web service connections (in).

#### Variable mon.dev\_www\_alt\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Alternative web service connections (in).

#### Variable mon.value\_www\_alt\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Alternative web client connections (out).

#### Variable mon.av\_www\_alt\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Alternative web client connections (out).

#### Variable mon.dev\_www\_alt\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Alternative web client connections (out).

#### Variable mon.value\_imaps\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: encrypted imap mail service sessions (in).

#### Variable mon.av\_imaps\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: encrypted imap mail service sessions (in).

#### Variable mon.dev\_imaps\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: encrypted imap mail service sessions (in).

#### Variable mon.value\_imaps\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: encrypted imap mail client sessions (out).

#### Variable mon.av\_imaps\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: encrypted imap mail client sessions (out).

#### Variable mon.dev\_imaps\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: encrypted imap mail client sessions (out).

#### Variable mon.value\_ldap\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: LDAP directory service service sessions (in).

#### Variable mon.av\_ldap\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: LDAP directory service service sessions (in).

#### Variable mon.dev\_ldap\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: LDAP directory service service sessions (in).

#### Variable mon.value\_ldap\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: LDAP directory service client sessions (out).

#### Variable mon.av\_ldap\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: LDAP directory service client sessions (out).

#### Variable mon.dev\_ldap\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: LDAP directory service client sessions (out).

#### Variable mon.value\_ldaps\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: LDAP directory service service sessions (in).

#### Variable mon.av\_ldaps\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: LDAP directory service service sessions (in).

#### Variable mon.dev\_ldaps\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: LDAP directory service service sessions (in).

#### Variable mon.value\_ldaps\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: LDAP directory service client sessions (out).

#### Variable mon.av\_ldaps\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: LDAP directory service client sessions (out).

#### Variable mon.dev\_ldaps\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: LDAP directory service client sessions (out).

#### Variable mon.value\_mongo\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Mongo database service sessions (in).

#### Variable mon.av\_mongo\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Mongo database service sessions (in).

#### Variable mon.dev\_mongo\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Mongo database service sessions (in).

#### Variable mon.value\_mongo\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Mongo database client sessions (out).

#### Variable mon.av\_mongo\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Mongo database client sessions (out).

#### Variable mon.dev\_mongo\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Mongo database client sessions (out).

#### Variable mon.value\_mysql\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: MySQL database service sessions (in).

#### Variable mon.av\_mysql\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: MySQL database service sessions (in).

#### Variable mon.dev\_mysql\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: MySQL database service sessions (in).

#### Variable mon.value\_mysql\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: MySQL database client sessions (out).

#### Variable mon.av\_mysql\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: MySQL database client sessions (out).

#### Variable mon.dev\_mysql\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: MySQL database client sessions (out).

#### Variable mon.value\_postgres\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: PostgreSQL database service sessions (in).

#### Variable mon.av\_postgres\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: PostgreSQL database service sessions (in).

#### Variable mon.dev\_postgres\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: PostgreSQL database service sessions (in).

#### Variable mon.value\_postgres\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: PostgreSQL database client sessions (out).

#### Variable mon.av\_postgres\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: PostgreSQL database client sessions (out).

#### Variable mon.dev\_postgres\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: PostgreSQL database client sessions (out).

#### Variable mon.value\_ipp\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Internet Printer Protocol (in).

#### Variable mon.av\_ipp\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Internet Printer Protocol (in).

#### Variable mon.dev\_ipp\_in

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Internet Printer Protocol (in).

#### Variable mon.value\_ipp\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Internet Printer Protocol (out).

#### Variable mon.av\_ipp\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Internet Printer Protocol (out).

#### Variable mon.dev\_ipp\_out

Observational measure collected every 2.5 minutes from cf-monitord.
Description: Internet Printer Protocol (out).
