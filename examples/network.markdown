---
layout: default
title: Network Examples 
published: true
sorting: 9
tags: [Examples]
---

* [Find MAC address][Network#Find MAC address]
* [Client-server example][Network#Client-server example]
* [Read from a TCP socket][Network#Read from a TCP socket]
* [Set up a PXE boot server][Network#Set up a PXE boot server]
* [Resolver management][Network#Resolver management]
* [Mount NFS filesystem][Basic File and Directory Examples#Mount NFS filesystem]
* [Unmount NFS filesystem][Basic File and Directory Examples#Unmount NFS filesystem]
* Find the MAC address
* Mount NFS filesystem

## Find MAC address

Finding the ethernet address can be hard, but on Linux it is straightforward.

```cf3
bundle agent test
{
vars:

linux::
 "interface" string => execresult("/sbin/ifconfig eth0","noshell");

solaris::
 "interface" string => execresult("/usr/sbin/ifconfig bge0","noshell");

freebsd::
 "interface" string => execresult("/sbin/ifconfig le0","noshell");

darwin::
 "interface" string => execresult("/sbin/ifconfig en0","noshell");

classes:

 linux::

   "ok" expression => regextract(
                                ".*HWaddr ([^\s]+).*(\n.*)*",
                                "$(interface)",
                                "mac"
                                );

 solaris::

   "ok" expression => regextract(
                                ".*ether ([^\s]+).*(\n.*)*",
                                "$(interface)",
                                "mac"
                                );

 freebsd::

   "ok" expression => regextract(
                                ".*ether ([^\s]+).*(\n.*)*",
                                "$(interface)",
                                "mac"
                                );

 darwin::

   "ok" expression => regextract(
                                "(?s).*ether ([^\s]+).*(\n.*)*",
                                "$(interface)",
                                "mac"
                                );

reports:

ok::

  "MAC address is $(mac[1])";

}
```

## Client-server example

```cf3

########################################################

#

# Simple test copy from server connection to cfServer

#

########################################################


 #

 # run this as follows:

 #

 # cf-serverd -f runtest_1.cf [-v]

 # cf-agent   -f runtest_2.cf

 #

 # Notice that the same file configures all parts of cfengine



########################################################


body common control
{
bundlesequence  => { "testbundle" };
version => "1.2.3";
#fips_mode => "true";

}

########################################################


bundle agent testbundle
{
files: 

  "/home/mark/tmp/testcopy" 
        comment  => "test copy promise",
    copy_from    => mycopy("/home/mark/LapTop/words","127.0.0.1"),
    perms        => system,
    depth_search => recurse("inf"),
    classes      => satisfied("copy_ok");

  "/home/mark/tmp/testcopy/single_file" 

        comment  => "test copy promise",
    copy_from    => mycopy("/home/mark/LapTop/Cfengine3/trunk/README","127.0.0.1"),
    perms        => system;

reports:

  copy_ok::

    "Files were copied..";
}

#########################################################


body perms system

{
mode  => "0644";
}

#########################################################


body depth_search recurse(d)

{
depth => "$(d)";
}

#########################################################


body copy_from mycopy(from,server)

{
source      => "$(from)";
servers     => { "$(server)" };
compare     => "digest";
encrypt     => "true";
verify      => "true";
copy_backup => "true";                  #/false/timestamp
purge       => "false";
type_check  => "true";
force_ipv4  => "true";
trustkey => "true";
}

#########################################################


body classes satisfied(x)
{
promise_repaired => { "$(x)" };
persist_time => "0";
}

#########################################################

# Server config

#########################################################


body server control

{
allowconnects         => { "127.0.0.1" , "::1" };
allowallconnects      => { "127.0.0.1" , "::1" };
trustkeysfrom         => { "127.0.0.1" , "::1" };
# allowusers

}

#########################################################


bundle server access_rules()

{

access:

  "/home/mark/LapTop"

    admit   => { "127.0.0.1" };
}
```

## Read from a TCP socket

```cf3
body common control

{
bundlesequence  => { "example" };
}

###########################################################


bundle agent example

{     
vars:

  "my80" string => readtcp("research.iu.hio.no","80","GET /index.php HTTP/1.1$(const.r)$(const.n)Host: research.iu.hio.no$(const.r)$(const.n)$(const.r)$(const.n)",20);

classes:

  "server_ok" expression => regcmp(".*200 OK.*\n.*","$(my80)");

reports:

  server_ok::

    "Server is alive";

  !server_ok::

    "Server is not responding - got $(my80)";
}
```

## Set up a PXE boot server

Use CFEngine to set up a PXE boot server.

```cf3
body common control
{
 bundlesequence => { "pxe" };
 inputs => { "/var/cfengine/inputs/cfengine_stdlib.cf" };
}


#

# PXE boot server

#



bundle agent pxe
{
vars:

  "software" slist => {
                      "atftp",
                      "dhcp-server",
                      "syslinux",
                      "apache2"
                      };


   "dirs" slist => {
                   "/tftpboot",
                   "/tftpboot/CFEngine/rpm",
                   "/tftpboot/CFEngine/inputs",
                   "/tftpboot/pxelinux.cfg",
                   "/tftpboot/kickstart",
                   "/srv/www/repos"
                   };

   "tmp_location"    string => "/tftpboot/CFEngine/inputs";

   # Distros that we can install



   "rh_distros" slist => { "4.7", "5.2" };
   "centos_distros" slist => { "5.2" }; 

   # File contents of atftp configuration



   "atftpd_conf" string =>
       "
###########################################


### This file is protected by CFEngine. ###


### Whatever you do, it will be changed ###


###     back to a promising state.      ###


###########################################



ATFTPD_OPTIONS=\"--daemon \"
ATFTPD_USE_INETD=\"no\"
ATFTPD_DIRECTORY=\"/tftpboot\"
ATFTPD_BIND_ADDRESSES=\"\"
       ";

   # File contents of DHCP configuration



   "dhcpd" string =>
       "
###########################################


### This file is protected by CFEngine. ###


### Whatever you do, it will be changed ###


###     back to a promising state.      ###


###########################################



DHCPD_INTERFACE=\"eth0\"
DHCPD_RUN_CHROOTED=\"yes\"
DHCPD_CONF_INCLUDE_FILES=\"\"
DHCPD_RUN_AS=\"dhcpd\"
DHCPD_OTHER_ARGS=\"\"
DHCPD_BINARY=\"\"
       ";

   "dhcpd_conf" string =>
       "
###########################################


### This file is protected by CFEngine. ###


### Whatever you do, it will be changed ###


###     back to a promising state.      ###


###########################################



allow booting;
allow bootp;
ddns-update-style none; ddns-updates off;
 subnet 192.168.0.0 netmask 255.255.255.0 {
   range 192.168.0.20 192.168.0.254;
   default-lease-time 3600;
   max-lease-time 4800;
   option routers 192.168.0.1;
   option domain-name \"test.CFEngine.com\";
   option domain-name-servers 192.168.0.1;
   next-server 192.168.0.1;
   filename \"pxelinux.0\";
 }
 group {
   host node1 {
     # Dummy machine


     hardware ethernet 00:0F:1F:94:FE:07;
     fixed-address 192.168.0.11;
     option host-name \"node1\";
   }
   host node2 {
     # Dell Inspiron 1150


     hardware ethernet 00:0F:1F:0E:70:E7;
     fixed-address 192.168.0.12;
     option host-name \"node2\";
   }
 }
        ";

   # File contains of Apache2 HTTP configuration



   "httpd_conf" string =>
        "
# Repository for RHEL5


<Directory /srv/www/repos>
Options Indexes 
AllowOverride None 
</Directory> 
Alias /repos /srv/www/repos

# PXE boot server


<Directory /tftpboot/distro/RHEL/5.2>
Options Indexes  
AllowOverride None  
</Directory>  
Alias /distro/rhel/5.2 /tftpboot/distro/RHEL/5.2

<Directory /tftpboot/distro/RHEL/4.7>
Options Indexes   
AllowOverride None   
</Directory>   
Alias /distro/rhel/4.7 /tftpboot/distro/RHEL/4.7

<Directory /tftpboot/distro/CentOS/5.2>
Options Indexes    
AllowOverride None    
</Directory>    
Alias /distro/centos/5.2 /tftpboot/distro/CentOS/5.2    

<Directory /tftpboot/kickstart>
Options Indexes     
AllowOverride None     
</Directory>     
Alias /kickstart /tftpboot/kickstart

<Directory /tftpboot/CFEngine>
Options Indexes      
AllowOverride None      
</Directory>      
Alias /CFEngine /tftpboot/CFEngine
        ";

   # File contains of Kickstart for RHEL5 configuration



   "kickstart_rhel5_conf" string =>
        "
###########################################


### This file is protected by CFEngine. ###


### Whatever you do, it will be changed ###


###     back to a promissing state.     ###


###########################################


	
auth  --useshadow  --enablemd5 
bootloader --location=mbr
clearpart --all --initlabel 
graphical
firewall --disabled
firstboot --disable
key 77244a6377a8044a
keyboard no
lang en_US
logging --level=info
url --url=http://192.168.0.1/distro/rhel/5.2
network --bootproto=dhcp --device=eth0 --onboot=on
reboot
rootpw --iscrypted $1$eOnXdDPF$279sQ//zry6rnQktkATeM0
selinux --disabled
timezone --isUtc Europe/Oslo
install
part swap --bytes-per-inode=4096 --fstype=\"swap\" --recommended
part / --bytes-per-inode=4096 --fstype=\"ext3\" --grow --size=1

%packages
@core
@base
db4-devel
openssl-devel
gcc
flex
bison
libacl-devel
libselinux-devel
pcre-devel
#httpd


device-mapper-multipath
-sysreport

%post
cd /root
rpm -i http://192.168.0.1/CFEngine/rpm/CFEngine-3.0.1b1-1.el5.i386.rpm
#/sbin/chkconfig httpd on


cd /etc/yum.repos.d
wget http://192.168.0.1/repos/RHEL5.Base.repo
rpm --import /etc/pki/rpm-gpg/*
yum clean all
yum update
mkdir -p /root/CFEngine_init
cd /root/CFEngine_init
wget -nd -r http://192.168.0.1/CFEngine/inputs/
/usr/local/sbin/cf-agent -B
/usr/local/sbin/cf-agent
        ";

   # File contains of PXElinux boot menu



   "pxelinux_boot_menu" string =>
        "
###########################################


### This file is protected by CFEngine. ###


### Whatever you do, it will be changed ###


###     back to a promissing state.     ###


###########################################



boot options:
     rhel5   - install 32 bit i386 RHEL 5.2             (MANUAL)
     rhel5w  - install 32 bit i386 RHEL 5.2             (AUTO)
     rhel4   - install 32 bit i386 RHEL 4.7 AS          (MANUAL)    
     centos5 - install 32 bit i386 CentOS 5.2 (Desktop) (MANUAL)
        ";
   # File contains of PXElinux default configuration



   "pxelinux_default" string =>
        "
###########################################


### This file is protected by CFEngine. ###


### Whatever you do, it will be changed ###


###     back to a promissing state.     ###


###########################################


	
default rhel5
timeout 300
prompt 1
display pxelinux.cfg/boot.msg
F1 pxelinux.cfg/boot.msg

# install i386 RHEL 5.2


label rhel5
   kernel vmlinuz-RHEL5U2
   append initrd=initrd-RHEL5U2 load_ramdisk=1 ramdisk_size=16384 install=http://192.168.0.1/distro/rhel/5.2

# install i386 RHEL 5.2 using Kickstart


label rhel5w
   kernel vmlinuz-RHEL5U2
   append initrd=initrd-RHEL5U2 load_ramdisk=1 ramdisk_size=16384 ks=http://192.168.0.1/kickstart/kickstart-RHEL5U2.cfg

# install i386 RHEL 4.7


label rhel4
   kernel vmlinuz-RHEL4U7
   append initrd=initrd-RHEL4U7 load_ramdisk=1 ramdisk_size=16384 install=http://192.168.0.1/distro/rhel/4.7

# install i386 CentOS 5.2


label centos5
   kernel vmlinuz-CentOS5.2
   append initrd=initrd-CentOS5.2 load_ramdisk=1 ramdisk_size=16384 install=http://192.168.0.1/distro/centos/5.2
        ";

   # File contains of specified PXElinux default to be a RHEL5 webserver



   "pxelinux_rhel5_webserver" string =>
        "
###########################################


### This file is protected by CFEngine. ###


### Whatever you do, it will be changed ###


###     back to a promissing state.     ###


###########################################



# install i386 RHEL 5.2 using Kickstart


default rhel5w
label rhel5w
   kernel vmlinuz-RHEL5U2
   append initrd=initrd-RHEL5U2 load_ramdisk=1 ramdisk_size=16384 ks=http://192.168.0.1/kickstart/kickstart-RHEL5U2.cfg
        ";

   # File contains of a local repository for RHEL5



   "rhel5_base_repo" string =>
        "
###########################################


### This file is protected by CFEngine. ###


### Whatever you do, it will be changed ###


###     back to a promissing state.     ###


###########################################



# Local Repository


[Server]
name=Server
baseurl=http://192.168.0.1/repos/rhel5/Server/
enable=1
[VT]
name=VT
baseurl=http://192.168.0.1/repos/rhel5/VT/
enable=1
[Cluster]
name=Cluster
baseurl=http://192.168.0.1/repos/rhel5/Cluster/
enable=1
[ClusterStorage]
name=Cluster Storage
baseurl=http://192.168.0.1/repos/rhel5/ClusterStorage/
enable=1
        ";
#####################################################




files:

 packages_ok::

  # Create files/dirs and edit the new files



  "/tftpboot/distro/RHEL/$(rh_distros)/."
       create => "true";

  "/tftpboot/distro/CentOS/$(centos_distros)/."
       create => "true";

  "$(dirs)/."   
       create => "true";

  "/tftpboot/pxelinux.cfg/boot.msg"
       create => "true",
       perms => mo("644","root"),
       edit_line => append_if_no_line("$(pxelinux_boot_menu)"),
       edit_defaults => empty;

  "/tftpboot/pxelinux.cfg/default"
       create => "true",
       perms => mo("644","root"),
       edit_line => append_if_no_line("$(pxelinux_default)"),
       edit_defaults => empty;

  "/tftpboot/pxelinux.cfg/default.RHEL5.webserver"
       create => "true",
       perms => mo("644","root"),
       edit_line => append_if_no_line("$(pxelinux_rhel5_webserver)"),
       edit_defaults => empty;
  
  "/tftpboot/kickstart/kickstart-RHEL5U2.cfg"
       create => "true",
       perms => mo("644","root"),
       edit_line => append_if_no_line("$(kickstart_rhel5_conf)"),
       edit_defaults => empty;

  "/srv/www/repos/RHEL5.Base.repo"
       create => "true",
       perms => mo("644","root"),
       edit_line => append_if_no_line("$(rhel5_base_repo)"),
       edit_defaults => empty;

  # Copy files



  "/tftpboot"

    copy_from => local_cp("/usr/share/syslinux"),
    depth_search => recurse("inf"),
    file_select => pxelinux_files,
    action => immediate;

  "$(tmp_location)"

    perms => m("644"),
    copy_from => local_cp("/var/cfengine/inputs"),
    depth_search => recurse("inf"),
    file_select => input_files,
    action => immediate;

  # Edit atftp, dhcp and apache2 configurations



  "/etc/sysconfig/atftpd"
     edit_line => append_if_no_line("$(atftpd_conf)"),
     edit_defaults => empty,
     classes => satisfied("atftpd_ready");

  "/etc/sysconfig/dhcpd"
     edit_line => append_if_no_line("$(dhcpd)"),
     edit_defaults => empty;

  "/etc/dhcpd.conf"
     edit_line => append_if_no_line("$(dhcpd_conf)"),
     edit_defaults => empty,
     classes => satisfied("dhcpd_ready");

  "/etc/apache2/httpd.conf"
     edit_line => append_if_no_line("$(httpd_conf)"),
     edit_defaults => std_defs,
     classes => satisfied("apache2_ok");

  # Make a static link



  "/tftpboot/pxelinux.cfg/C0A8000C"
     link_from => mylink("/tftpboot/pxelinux.cfg/default.RHEL5.webserver");

  # Hash comment some lines for apaches



  apache2_ok::
  "/etc/apache2/httpd.conf"
     edit_line => comment_lines_matching_apache2("#"),
     classes => satisfied("apache2_ready");

commands:

  # Restart services


  atftpd_ready::
  "/etc/init.d/atftpd restart";

  dhcpd_ready::
  "/etc/init.d/dhcpd restart";

  apache2_ready::
  "/etc/init.d/apache2 restart";


#####################################################



packages:
  
 ipv4_192_168_0_1::
 # Only the PXE boot server



 "$(software)"

     package_policy => "add",
     package_method => zypper,
     classes => satisfied("packages_ok");

}

#####################################################


########### *** Bodies are here *** #################


#####################################################



body file_select pxelinux_files

{
leaf_name => { "pxelinux.0" };

file_result => "leaf_name";
}

#####################################################



body copy_from mycopy_local(from,server)

{
source      => "$(from)";
compare     => "digest";
}

#########################################################



body link_from mylink(x)
{
source => "$(x)";
link_type => "symlink";
}

#######################################################



body classes satisfied(new_class)

{
promise_kept => { "$(new_class)"};
promise_repaired => { "$(new_class)"};
}

#######################################################



bundle edit_line comment_lines_matching_apache2(comment)
  {
  
  vars:
   "regex" slist => { "\s.*Options\sNone", "\s.*AllowOverride\sNone", "\s.*Deny\sfrom\sall" };

  replace_patterns:

   "^($(regex))$"
      replace_with => comment("$(comment)");
  }

#######################################################


body file_select input_files
{
 leaf_name => { ".*.cf",".*.dat",".*.txt" };
 file_result => "leaf_name";
}

#######################################################
```

## Resolver management

```cf3
#######################################################

#

# Resolve conf

#

#######################################################


bundle common g # globals
{
vars:

 "searchlist"  slist => { 
                        "search iu.hio.no", 
                        "search cfengine.com" 
                        };

 "nameservers" slist => { 
                        "128.39.89.10", 
                        "128.39.74.16",
                        "192.168.1.103"
                        };
classes:

  "am_name_server" expression => reglist("@(nameservers)","$(sys.ipv4[eth1])");
}

#######################################################


body common control

{
any::

  bundlesequence  => {
                     "g",
                     resolver(@(g.searchlist),@(g.nameservers))
                     };   

  domain => "iu.hio.no";
}

#######################################################


bundle agent resolver(s,n)

{
files:

  # When passing parameters down, we have to refer to

  # a source context


  "$(sys.resolv)"  # test on "/tmp/resolv.conf" #

      create        => "true",
      edit_line     => doresolv("@(this.s)","@(this.n)"),
      edit_defaults => reconstruct;
 # or edit_defaults => modify

}

#######################################################

# For the library

#######################################################


bundle edit_line doresolv(s,n)

{
vars:

 "line" slist => { @(s), @(n) };

insert_lines:

  "$(line)";

}

#######################################################


body edit_defaults reconstruct
{
empty_file_before_editing => "true";
edit_backup => "false";
max_file_size => "100000";
}

#######################################################


body edit_defaults modify
{
empty_file_before_editing => "false";
edit_backup => "false";
max_file_size => "100000";
}
```

## Mount NFS filesystem

```cf3
#

# cfengine 3

#

# cf-agent -f ./cftest.cf -K

#


body common control

{
bundlesequence => { "mounts" };
}

#


bundle agent mounts

{
storage:

  "/mnt" mount  => nfs("slogans.iu.hio.no","/home");

}

######################################################################


body mount nfs(server,source)

{
mount_type => "nfs";
mount_source => "$(source)";
mount_server => "$(server)";
#mount_options => { "rw" };

edit_fstab => "true";
unmount => "true";
}
```

## Unmount NFS filesystem

```cf3
#####################################################################
# Mount NFS

#####################################################################


body common control

{
bundlesequence => { "mounts" };
}

#####################################################################


bundle agent mounts

{
storage:

  # Assumes the filesystem has been exported


  "/mnt" mount  => nfs("server.example.org","/home");
}

######################################################################


body mount nfs(server,source)

{
mount_type => "nfs";
mount_source => "$(source)";
mount_server => "$(server)";
edit_fstab => "true";
unmount => "true";
}
```
