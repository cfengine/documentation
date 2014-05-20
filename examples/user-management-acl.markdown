---
layout: default
title: User Management and ACL Examples 
published: true
sorting: 15
tags: [Examples,User Management,ACL]
---

* [Manage users][User Management and ACL Examples#Manage users]
* [Add users][User Management and ACL Examples#Add users]
* [Remove users][User Management and ACL Examples#Remove users]
* [Add users to passwd and group][User Management and ACL Examples#Add users to passwd and group]
* [ACL file example][User Management and ACL Examples#ACL file example]
* [ACL generic example][User Management and ACL Examples#ACL generic example]
* [ACL secret example][User Management and ACL Examples#ACL secret example]
* [Active directory example][User Management and ACL Examples#Active directory example]
* [Active list users directory example][User Management and ACL Examples#Active list users directory example]
* [Active directory show users example][User Management and ACL Examples#Active directory show users example]
* [Get a list of users][User Management and ACL Examples#Get a list of users]
* [LDAP interactions][User Management and ACL Examples#LDAP interactions]

## Manage users

There are many approaches to managing users. You can edit system files like /etc/passwd directly, or you can use commands on some systems like ‘useradd’ or ‘adduser’. In all cases it is desirable to make this a data-driven process.

    Add users
    Remove users

### Add users

A simple approach which adds new users to the password file, and to a group called ‘users’ in the group file. Is shown below. This example does not edit the shadow file. A simple pattern that can be modified for use is shown below.

Note that, although this is a simple minded approach, it is the most efficient of the approaches shown here as all operations can be carried out in a single operation for each file.

```cf3
bundle agent addusers
{
vars:

  # Add some users


  "pw[mark]" string => "mark:x:1000:100:Mark Burgess:/home/mark:/bin/bash";
  "pw[fred]" string => "fred:x:1001:100:Right Said:/home/fred:/bin/bash";
  "pw[jane]" string => "jane:x:1002:100:Jane Doe:/home/jane:/bin/bash";

  "users" slist => getindices("pw");

files:

  "/etc/passwd"
     edit_line => append_users_starting("addusers.pw");

#  "/etc/shadow"

#     edit_line => append_users_starting("$(users):defaultpasswd:::::::");


  "/etc/group"
       edit_line => append_user_field("users","4","@(addusers.users)");

  "/home/$(users)/."

     create => "true",
      perms => mog("755","$(users)","users");
}
```

A second approach is to use the shell commands supplied by some operating systems; this assumes that suitable defaults have been set up manually. Also the result is not repairable in a simple convergent manner. The command needs to edit multiple files for each user, and is quite inefficient.

```cf3
bundle agent addusers
{
vars:

  "users" slist => { "mark", "fred", "jane" };

commands:

   "/usr/sbin/useradd $(users)";
}
```

An alternative approach is to use a method to wrap around the handling of a user. Although this looks nice, it is less efficient than the first method because it must edit the files multiple times.

```cf3
bundle agent addusers
{
vars:

  # Add some users


  "pw[mark]" string => "mark:x:1000:100:Mark Burgess:/home/mark:/bin/bash";
  "pw[fred]" string => "fred:x:1001:100:Right Said:/home/fred:/bin/bash";
  "pw[jane]" string => "jane:x:1002:100:Jane Doe:/home/jane:/bin/bash";

  "users" slist => getindices("pw");

methods:

  "any" usebundle => user_add("$(users)","$(pw[$(users)])");

}

bundle agent user_add(x,pw)
{
files:

  "/etc/passwd"
     edit_line => append_users_starting("addusers.pw");

#  "/etc/shadow"

#     edit_line => append_users_starting("$(users):defaultpasswd:::::::");


  "/etc/group"
       edit_line => append_user_field("users","4","@(addusers.users)");

  "/home/$(users)/."

     create => "true",
      perms => mog("755","$(users)","users");
}
```

### Remove users

```cf3
```

## Add users to passwd and group ##

Add lines to the password file, and users to group if they are not already there.

```cf3
body common control
{
bundlesequence => { "addpasswd" };
inputs => { "cf_std_library.cf" };
}

bundle agent addpasswd
{
vars:

  # want to set these values by the names of their array keys


  "pwd[mark]" string => "mark:x:1000:100:Mark Burgess:/home/mark:/bin/bash";
  "pwd[fred]" string => "fred:x:1001:100:Right Said:/home/fred:/bin/bash";
  "pwd[jane]" string => "jane:x:1002:100:Jane Doe:/home/jane:/bin/bash";

  "users" slist => getindices("pwd");

files:

  "/etc/passwd"

        create => "true",
     edit_line => append_users_starting("addpasswd.pwd");

  "/etc/group"

       edit_line => append_user_field("users","4","@(addpasswd.users)");

}
```

## ACL file example

```cf3
body common control
{
bundlesequence => { "acls" };
}

#########################################


bundle agent acls

{
files:

  "/media/flash/acl/test_dir"
 
    depth_search => include_base,
    acl => template;
}

#########################################


body acl template

{
acl_method => "overwrite";
acl_type => "posix";
acl_directory_inherit => "parent";
aces => { "user:*:r(wwx),-r:allow", "group:*:+rw:allow", "mask:x:allow", "all:r"};
}

#########################################


body acl win

{
acl_method => "overwrite";
acl_type => "ntfs";
acl_directory_inherit => "nochange";
aces => { "user:Administrator:rw", "group:Bad:rwx(Dpo):deny" };
}

#########################################


body depth_search include_base

{
include_basedir => "true";
}
```

## ACL generic example

```cf3
body common control
{
bundlesequence => { "acls" };
}

#########################################


bundle agent acls

{
files:

  "/media/flash/acl/test_dir"
   
    depth_search => include_base,
    acl => test;
}

#########################################


body acl test

{
acl_type => "generic";
aces => {"user:bob:rwx", "group:staff:rx", "all:r"};
}

#########################################


body depth_search include_base

{
include_basedir => "true";
}
```

## ACL secret example

```cf3
body common control
{
bundlesequence => { "acls" };
}

#########################################


bundle agent acls

{
files:

 windows::

  "c:\Secret"
    acl => win,
    depth_search => include_base,
    comment => "Secure the secret directory from unauthorized access";
}

#########################################


body acl win

{
acl_method => "overwrite";
aces => { "user:Administrator:rwx" };
}

#########################################


body depth_search include_base

{
include_basedir => "true";
}
```

## Active directory example

```cf3
#########################################################################

#   active_directory.cf - Extract Data From Windows Domain Controllers

#

#   NOTE: Since we don't supply any credentials in this policy file,

#         the Domain Controller must allow anonymous bind. Also,

#         the user "NT AUTHORITY\ANONYMOUS LOGON" must be granted access

#         to the resources we want to read.

#

#########################################################################


bundle agent active_directory
{
vars:
# NOTE: Edit this to your domain, e.g. "corp", may also need more DC's after it

  "domain_name" string => "cftesting";

  "user_name"    string => "Guest";


  
# NOTE: We can also extract data from remote Domain Controllers


dummy.DomainController::
  "domain_controller"  string => "localhost";


  "userlist"    slist => ldaplist(
                                  "ldap://$(domain_controller)",
                                  "CN=Users,DC=$(domain_name),DC=com",
                                  "(objectClass=user)",
                                  "sAMAccountName",
                                  "subtree",
                                  "none");

classes:

dummy.DomainController::

   "gotuser" expression => ldaparray(
                                    "userinfo",
                                    "ldap://$(domain_controller)",
                                    "CN=$(user_name),CN=Users,DC=$(domain_name),DC=com",
                                    "(name=*)",
                                    "subtree",
                                    "none");

								  
reports:
dummy.DomainController::
  "Username is \"$(userlist)\"";

dummy.gotuser::
  "Got user data; $(userinfo[name]) has logged on $(userinfo[logonCount]) times";

}
```

## Active list users directory example

```cf3
# List users from Active Directory through LDAP

# Note: Anonymous LDAP binding must be allowed, and the Anonymous user

# must have read access to CN=Users


bundle agent ldap
{
vars:
   "userlist" slist => ldaplist(
                                    "ldap://cf-win2003",
                                    "CN=Users,DC=domain,DC=cf-win2003",
                                    "(objectClass=user)",
                                    "sAMAccountName",
                                    "subtree",
                                    "none");
reports:
Yr2010::
  "Username: \"$(userlist)\"";
}
```

## Active directory show users example

```cf3
# List users from Active Directory through LDAP

# Note: Anonymous LDAP binding must be allowed, and the Anonymous user

# must have read access to CN=Users and CN=theusername

# Run the agent in verbose mode to see the data


bundle agent ldap
{
classes:
   "gotdata" expression => ldaparray(
                                    "myarray",
                                    "ldap://cf-win2003",
                                    "CN=Test Pilot,CN=Users,DC=domain,DC=cf-win2003",
                                    "(name=*)",
                                    "subtree",
                                    "none");
reports:
gotdata::
  "Got user data";
!gotdata::
  "Did not get user data";
}
```

## Get a list of users

```cf3
#######################################################

#

# GetUsers

#

#######################################################


body common control

{
any::

  bundlesequence  => {
                     test
                     };   
}

#######################################################


bundle agent test

{
vars:

  "allusers" slist => getusers("zenoss,mysql,at","12,0");

reports:

 linux::

  "Found user $(allusers)";

}
```

## LDAP interactions

```cf3
#


body common control
{
bundlesequence => { "ldap" , "followup"};
}

###################################################################################################

#  NOTE!! relying on LDAP or other network data without validation is EXTREMELY dangerous. 

#         You could destroy a system by assuming that the service will respond with a 

#         sensible result. Cfengine does not recommend reliance on network services in configuration.

###################################################################################################


bundle agent ldap
{
vars:

   # Get the first matching value for "uid"


  "value" string => ldapvalue("ldap://eternity.iu.hio.no","dc=cfengine,dc=com","(sn=User)","uid","subtree","none");

   # Geta all matching values for "uid" - should be a single record match


  "list" slist =>  ldaplist("ldap://eternity.iu.hio.no","dc=cfengine,dc=com","(sn=User)","uid","subtree","none");

classes:

   "gotdata" expression => ldaparray("myarray","ldap://eternity.iu.hio.no","dc=cfengine,dc=com","(uid=mark)","subtree","none");

   "found" expression => regldap("ldap://eternity.iu.hio.no","dc=cfengine,dc=com","(sn=User)","uid","subtree","jon.*","none");

reports:

 linux::

   "LDAP VALUE $(value) found";
   "LDAP LIST VALUE $(list)";

 gotdata::

   "Found specific entry data  ...$(ldap.myarray[uid]),$(ldap.myarray[gecos]), etc";

  found::

    "Matched regex";

}

bundle agent followup

{
reports:

 linux::

"Different bundle ...$(ldap.myarray[uid]),$(ldap.myarray[gecos]),

}
```