---
layout: default
title: CFEngine Advanced Examples 
published: true
sorting: 3
tags: [Examples]
---


* [Aborting execution][CFEngine Advanced Examples#Aborting execution]
* [ACL file example][CFEngine Advanced Examples#ACL file example]
* [ACL generic example][CFEngine Advanced Examples#ACL generic example]
* [ACL secret example][CFEngine Advanced Examples#ACL secret example]
* [Active directory example][CFEngine Advanced Examples#Active directory example]
* [Active list users directory example][CFEngine Advanced Examples#Active list users directory example]
* [Active directory show users example][CFEngine Advanced Examples#Active directory show users example]
* [Add lines to a file][CFEngine Advanced Examples#Add lines to a file]
* [Add users to passwd and group][CFEngine Advanced Examples#Add users to passwd and group]
* [Add software packages to the system][CFEngine Advanced Examples#Add software packages to the system]
* [Add variable definitions to a file][CFEngine Advanced Examples#Add variable definitions to a file]
* [Application baseline][CFEngine Advanced Examples#Application baseline]
* [Array example][CFEngine Advanced Examples#Array example]
* [Back references in filenames][CFEngine Advanced Examples#Back references in filenames]
* [BSD flags][CFEngine Advanced Examples#BSD flags]
* [Change directory for command][CFEngine Advanced Examples#Change directory for command]
* [Check file or directory permissions][CFEngine Advanced Examples#Check file or directory permissions]
* [Class match example][CFEngine Advanced Examples#Class match example]
* [Client-server example][CFEngine Advanced Examples#Client-server example]
* [Commands example][CFEngine Advanced Examples#Commands example]
* [Commenting lines in a file][CFEngine Advanced Examples#Commenting lines in a file]
* [Copy files][CFEngine Advanced Examples#Copy files]
* [Copy and flatten directory][CFEngine Advanced Examples#Copy and flatten directory]
* [Copy then edit][CFEngine Advanced Examples#Copy then edit]
* [Creating files and directories][CFEngine Advanced Examples#Creating files and directories]
* [Database creation][CFEngine Advanced Examples#Database creation]
* [Deleting lines from a file][CFEngine Advanced Examples#Deleting lines from a file]
* [Deleting lines exception][CFEngine Advanced Examples#Deleting lines exception]
* [Editing files][CFEngine Advanced Examples#Editing files]
* [Editing tabular files][CFEngine Advanced Examples#Editing tabular files]
* [Environment (virtual)][CFEngine Advanced Examples#Environment (virtual)]
* [Environment variables][CFEngine Advanced Examples#Environment variables]
* [Execresult example][CFEngine Advanced Examples#Execresult example]
* [Inserting lines in a file][CFEngine Advanced Examples#Inserting lines in a file]
* [Get a list of users][CFEngine Advanced Examples#Get a list of users]
* [Global classes][CFEngine Advanced Examples#Global classes]
* [Hello world][CFEngine Advanced Examples#Hello world]
* [LDAP interactions][CFEngine Advanced Examples#LDAP interactions]
* [Linking files][CFEngine Advanced Examples#Linking files]
* [Listing files-pattern in a directory][CFEngine Advanced Examples#Listing files-pattern in a directory]
* [Locate and transform files][CFEngine Advanced Examples#Locate and transform files]
* [Logging][CFEngine Advanced Examples#Logging]
* [Measurements][CFEngine Advanced Examples#Measurements]
* [Methods][CFEngine Advanced Examples#Methods]
* [Method validation][CFEngine Advanced Examples#Method validation]
* [Mount NFS filesystem][CFEngine Advanced Examples#Mount NFS filesystem]
* [Ordering promises][CFEngine Advanced Examples#Ordering promises]
* [Process management][CFEngine Advanced Examples#Process management]
* [Read from a TCP socket][CFEngine Advanced Examples#Read from a TCP socket]
* [Resolver management][CFEngine Advanced Examples#Resolver management]
* [Search and replace text][CFEngine Advanced Examples#Search and replace text]
* [Selecting a region in a file][CFEngine Advanced Examples#Selecting a region in a file]
* [Service management (windows)][CFEngine Advanced Examples#Service management (windows)]
* [Set up a PXE boot server][CFEngine Advanced Examples#Set up a PXE boot server]
* [Tidying garbage files][CFEngine Advanced Examples#Tidying garbage files]
* [Software distribution][CFEngine Advanced Examples#Software distribution]
* [Trigger classes][CFEngine Advanced Examples#Trigger classes]
* [Unmount NFS filesystem][CFEngine Advanced Examples#Unmount NFS filesystem]
* [Web server modules][CFEngine Advanced Examples#Web server modules]
* [Warn if matching line in file][CFEngine Advanced Examples#Warn if matching line in file]
* [Windows registry][CFEngine Advanced Examples#Windows registry]
* [unit_registry_cache.cf][CFEngine Advanced Examples#unit_registry_cache.cf]
* [unit_registry.cf][CFEngine Advanced Examples#unit_registry.cf]

## Aborting execution

```cf3
body common control

{
bundlesequence  => { "testbundle"  };

version => "1.2.3";
}

###########################################


body agent control

{
abortbundleclasses => { "invalid.Hr16" };
}

###########################################


bundle agent testbundle
{
vars:

 "userlist" slist => { "xyz", "mark", "jeang", "jonhenrik", "thomas", "eben" };

methods:

 "any" usebundle => subtest("$(userlist)");

}

###########################################


bundle agent subtest(user)

{
classes:

  "invalid" not => regcmp("[a-z][a-z][a-z][a-z]","$(user)");

reports:

 !invalid::

  "User name $(user) is valid at 4 letters";

 invalid::

  "User name $(user) is invalid";
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

## Add lines to a file

There are numerous approaches to adding lines to a file. Often the order of a configuration file is unimportant, we just need to ensure settings within it. A simple way of adding lines is show below.

```cf3
body common control

{
any::

  bundlesequence  => { "insert" };   
}

#######################################################


bundle agent insert

{
vars:

  "lines" string => 
                "
                One potato
                Two potato
                Three potatoe
                Four
                ";
 
files:

  "/tmp/test_insert"

            create => "true",
         edit_line => append_if_no_line("$(insert.lines)");

}
```

Also you could write this using a list variable:

```cf3
body common control

{
any::

  bundlesequence  => { "insert" };   
}

#######################################################


bundle agent insert

{
vars:

  "lines" slist => { "One potato", "Two potato",
                "Three potatoe", "Four" };
 
files:

  "/tmp/test_insert"

            create => "true",
         edit_line => append_if_no_line("@(insert.lines)");

}
```

## Add users to passwd and group

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


## Add software packages to the system

```cf3

#
# Package managment

#


body common control
{
bundlesequence => { "packages" };
}

#############################################


bundle agent packages
{
vars:

 "match_package" slist => { 
                          "apache2", 
                          "apache2-mod_php5",
                          "apache2-prefork",
                          "php5" 
                          };
packages:

 solaris::

  "$(match_package)"

     package_policy => "add",
     package_method => solaris;

 redhat|SuSE::

  "$(match_package)"

     package_policy => "add",
     package_method => yum;

}
```

Note you can also arrange to hide all the differences between package managers on an OS basis, but since some OSs have multiple managers, this might not be 100 percent correct.


## Add variable definitions to a file e.g. /etc/system

```cf3

body common control
{
bundlesequence => { "setvars" };
inputs => { "cf_std_library.cf" };
}


bundle agent setvars
{
vars:

  # want to set these values by the names of their array keys


  "rhs[lhs1]" string => " Mary had a little pig";
  "rhs[lhs2]" string => "Whose Fleece was white as snow";
  "rhs[lhs3]" string => "And everywhere that Mary went";

  # oops, now change pig -> lamb


files:

  "/tmp/system"

        create => "true",
     edit_line => set_variable_values("setvars.rhs");

}
```

Results in:

lhs1= Mary had a little pig
lhs2=Whose Fleece was white as snow
lhs3=And everywhere that Mary went

An example of this would be to add variables to /etc/sysctl.conf on Linux:

```cf3
body common control
{
bundlesequence => { "setvars" };
inputs => { "cf_std_library.cf" };
}


bundle agent setvars
{
vars:

  # want to set these values by the names of their array keys


  "rhs[net/ipv4/tcp_syncookies]" string => "1";
  "rhs[net/ipv4/icmp_echo_ignore_broadcasts]" string => "1";
  "rhs[net/ipv4/ip_forward]" string => "1";

  # oops, now change pig -> lamb


files:

  "/etc/sysctl"

        create => "true",
     edit_line => set_variable_values("setvars.rhs");

}

    Application baseline
    Array example
    Back references in filenames
    BSD flags
    Change directory for command
```

## Application baseline

```cf3
#########################################################################

#

#   app_baseline.cf - Verify Existence of Applications

#

#   NOTE: Sometimes applications are not correctly installed even

#         though the native package manager reports them to be.

#         Cfengine can check for application-specific configuration

#         and act upon or report any anomalies.

#

#########################################################################



bundle agent app_baseline
{

methods:
windows::
"any" usebundle => detect_adobereader;


}

###


bundle agent detect_adobereader
{
vars:

windows::
  "value1" string => registryvalue("HKEY_LOCAL_MACHINE\SOFTWARE\Adobe\Acrobat Reader\9.0\Installer", "ENU_GUID");
  "value2" string => registryvalue("HKEY_LOCAL_MACHINE\SOFTWARE\Adobe\Acrobat Reader\9.0\Installer", "VersionMax");
  "value3" string => registryvalue("HKEY_LOCAL_MACHINE\SOFTWARE\Adobe\Acrobat Reader\9.0\Installer", "VersionMin");
 
classes:

windows::
  "is_correct" and => { 
                       strcmp("$(value1)", "{AC76BA86-7AD7-1033-7B44-A93000000001}"),
                       strcmp("$(value2)", "90003"),
                       islessthan("$(value3)", "10001" )
                      };
 
 reports:

windows.!is_correct::
 "Adobe Reader is not correctly deployed - got \"$(value1)\", \"$(value2)\", \"$(value3)\"";
}
```

## Array example

```cf3
body common control
{
bundlesequence => { "array" };
}


bundle common g
{
vars:

  "array[1]" string => "one"; 
  "array[2]" string => "two"; 
}

bundle agent array
{
vars:

  "localarray[1]" string => "one"; 
  "localarray[2]" string => "two"; 

reports:

 linux::

   "Global $(g.array[1]) and $(localarray[2])";
}
```


## Backreferences in filenames

```cf3

######################################################################

#

# File editing - back reference

#

######################################################################



body common control

{
version => "1.2.3";
bundlesequence  => { "testbundle"  };
}

########################################################


bundle agent testbundle

{
files:

  # The back reference in a path only applies to the last link

  # of the pathname, so the (tmp) gets ignored


  "/tmp/(cf3)_(.*)"

       edit_line => myedit("second $(match.2)");


  # but ...


#  "/tmp/cf3_test"

#       create    => "true",

#       edit_line => myedit("second $(match.1)");



}

########################################################


bundle edit_line myedit(parameter)
  {
  vars:

   "edit_variable" string => "private edit variable is $(parameter)"; 

  insert_lines:

     "$(edit_variable)";
  
  }
```

## BSD flags

```cf3
body common control
{
bundlesequence => { "test" };
}

bundle agent test
{
files:

 freebsd::

   "/tmp/newfile"

       create => "true",
       perms => setbsd;

}


body perms setbsd
{
bsdflags => { "+uappnd","+uchg", "+uunlnk", "-nodump" };
}
```

## Change directory for command

```cf3
body common control

{
bundlesequence  => { "example" };
}

###########################################################


body contain cd(dir)
{
chdir => "${dir}";
useshell => "true";
}

bundle agent example
{
commands:

   "/bin/pwd"
       contain => cd("/tmp");
}
```

## Check file or directory permissions

```cf3
bundle agent check_perms
{
vars:

  "ns_files" slist => {
                      "/local/iu/logs/admin",
                      "/local/iu/logs/security",
                      "/local/iu/logs/updates",
                      "/local/iu/logs/xfer"
                      };
files:

   NameServers::

    "/local/dns/pz"

            perms => mo("644","dns")
     depth_search => recurse("1"),
      file_select => exclude("secret_file");

    "/local/iu/dns/pz/FixSerial"

            perms => m("755"),
      file_select => plain;

    "$(ns_files)"

            perms => mo("644","dns"),
      file_select => plain;


    "$(ftp)/pub"      
             perms => mog("644","root","other");

    "$(ftp)/pub"      
             perms => m("644"),
      depth_search => recurse("inf");

    "$(ftp)/etc"        perms => mog("111","root","other");
    "$(ftp)/usr/bin/ls" perms => mog("111","root","other");
    "$(ftp)/dev"        perms => mog("555","root","other");
    "$(ftp)/usr"        perms => mog("555","root","other");
}
```

    Class match example
    Client-server example
    Commands example
    Commenting lines in a file


## Class match example

```cf3

body common control

{
bundlesequence  => { "example" };
}

###########################################################


bundle agent example

{     
classes:

  "do_it" and => { classmatch(".*_3"), "linux" }; 

reports:

  do_it::

    "Host matches pattern";

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


## Commands example

```cf3
body common control
{
bundlesequence  => { "my_commands" };
inputs => { "cfengine_stdlib.cf" };
}


bundle agent my_commands
{
commands:

 Sunday.Hr04.Min05_10.myhost::

  "/usr/bin/update_db";

 any::

  "/etc/mysql/start"

      contain => setuid("mysql");

}
```

## Commenting lines in a file

```cf3
######################################################################

#

# File editing

#

# Normal ordering:

# - delete

# - replace | colum_edit

# - insert

# 

######################################################################



body common control

{
version => "1.2.3";
bundlesequence  => { "testbundle"  };
}

########################################################


bundle agent testbundle

{

files:

  "/home/mark/tmp/cf3_test"

       create    => "true",
       edit_line => myedit("second");
}

########################################################


bundle edit_line myedit(parameter)
  {
  vars:

   "edit_variable" string => "private edit variable is $(parameter)"; 

  
  replace_patterns:

  # replace shell comments with C comments


   "#(.*)"

      replace_with => C_comment,
     select_region => MySection("New section");

  }

########################################

# Bodies

########################################


body replace_with C_comment

{
replace_value => "/* $(match.1) */"; # backreference 0
occurrences => "all";  # first, last all
}

########################################################


body select_region MySection(x)

{
select_start => "\[$(x)\]";
select_end => "\[.*\]";
}

######################################################################

#

# Comment lines

#

######################################################################


body common control

{
version => "1.2.3";
bundlesequence  => { "testbundle"  };
}

########################################################


bundle agent testbundle

{
files:

  "/home/mark/tmp/comment_test"

       create    => "true",
       edit_line => comment_lines_matching;
}

########################################################


bundle edit_line comment_lines_matching
  {
  vars:

    "regexes" slist => { "one.*", "two.*", "four.*" };

  replace_patterns:

   "^($(regexes))$"
      replace_with => comment("# ");
  }

########################################

# Bodies

########################################


body replace_with comment(c)

{
replace_value => "$(c) $(match.1)";
occurrences => "all";
}

######################################################################

#

# Uncomment lines

#

######################################################################


body common control

{
version => "1.2.3";
bundlesequence  => { "testbundle"  };
}

# try this on some test data like


# one

# two

# mark one

#mark two


########################################################


bundle agent testbundle

{
files:

  "/home/mark/tmp/comment_test"

       create    => "true",
       edit_line => uncomment_lines_matching("\s*mark.*","#");
}

########################################################


bundle edit_line uncomment_lines_matching(regex,comment)
{
replace_patterns:

 "#($(regex))$" replace_with => uncomment;
}

########################################################


body replace_with uncomment
{
replace_value => "$(match.1)";
occurrences => "all";
}
```

## Copy files

```cf3
files:

  "/var/cfengine/inputs" 

    handle => "update_policy",
    perms => m("600"),
    copy_from => u_scp("$(master_location)",@(policy_server)),
    depth_search => recurse("inf"),
    file_select => input_files,
    action => immediate;

  "/var/cfengine/bin" 

    perms => m("700"),
    copy_from => u_scp("/usr/local/sbin","localhost"),
    depth_search => recurse("inf"),
    file_select => cf3_files,
    action => immediate,
    classes => on_change("reload");

```


    Copy and flatten directory 

## Copy and flatten directory

```cf3

########################################################

#

# Simple test copy from server connection to cfServer

#

########################################################


 #

 # run this as follows:

 #

 # cf-serverd -f runtest_1.cf [-d2]

 # cf-agent   -f runtest_2.cf

 #

 # Notice that the same file configures all parts of cfengine


########################################################


body common control

{
bundlesequence  => { "testbundle" };
version => "1.2.3";
}

########################################################


bundle agent testbundle

{
files:

  "/home/mark/tmp/testflatcopy" 

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
verify      => "true";
copy_backup => "true";                  #/false/timestamp
purge       => "false";
type_check  => "true";
force_ipv4  => "true";
trustkey => "true";
collapse_destination_dir => "true";
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
}

#########################################################


bundle server access_rules()

{
access:

  "/home/mark/LapTop"

    admit   => { "127.0.0.1" };
}
```

## Copy then edit a file convergently

To convergently chain a copy followed by edit, you need a staging file. First you copy to the staging file. Then you edit the final file and insert the staging file into it as part of the editing. This is convergent with respect to both stages of the process.

```cf3
bundle agent master
{
files:

  "$(final_destination)"

         create => "true",
     edit_line => fix_file("$(staging_file)"),
 edit_defaults => empty,
         perms => mo("644","root"),
        action => ifelapsed("60");
}

#


bundle edit_line fix_file(f)
{
insert_lines:

  "$(f)"
 
     # insert this into an empty file to reconstruct

 
     insert_type => "file";

replace_patterns:

    "searchstring"

          replace_with => With("replacestring");
}
```

    Creating files and directories
    Database creation
    Deleting lines from a file
    Deleting lines exception


## Creating files and directories

```cf3

########################################################

#

# Simple test create files

#

########################################################


body common control

{
bundlesequence  => { "testbundle"  };
}

########################################################


bundle agent testbundle

{
files:

  "/home/mark/tmp/test_plain" 

       perms => system,
       create => "true";

  "/home/mark/tmp/test_dir/." 

       perms => system,
       create => "true";

}

#########################################################


body perms system

{
mode  => "0640";
}

#########################################################
```


## Database creation

```cf3
body common control
{
bundlesequence => { "dummy" };
}

body knowledge control

{
#sql_database => "postgres";

sql_owner => "postgres";
sql_passwd => ""; # No passwd
sql_type => "postgres";
}

bundle knowledge dummy
{
topics:
}


body common control
{
bundlesequence => { "databases" };
}

bundle agent databases

{
#commands:


#  "/usr/bin/createdb cf_topic_maps",


#        contain => as_user("mysql");


databases:

  "knowledge_bank/topics"

    database_operation => "create",
    database_type => "sql",
    database_columns => { 
                        "topic_name,varchar,256",
                        "topic_comment,varchar,1024",
                        "topic_id,varchar,256",
                        "topic_type,varchar,256",
                        "topic_extra,varchar,26" 
                        },

    database_server => myserver;



}

################################################


body database_server myserver
{
none::
 db_server_owner => "postgres";
 db_server_password => "";
 db_server_host => "localhost";
 db_server_type => "postgres";
 db_server_connection_db => "postgres";
any::
 db_server_owner => "root";
 db_server_password => "";
 db_server_host => "localhost";
 db_server_type => "mysql";
 db_server_connection_db => "mysql";
}

body contain as_user(x)
{
exec_owner => "$(x)";
}
```

## Deleting lines from a file

```cf3
body common control
{
bundlesequence => { "test" };
}



bundle agent test
{
files:

  "/tmp/resolv.conf"  # test on "/tmp/resolv.conf" #

     create        => "true",
     edit_line     => resolver,
     edit_defaults => def;

}


#######################################################

# For the library

#######################################################


bundle edit_line resolver

{
vars:

 "search" slist => { "search iu.hio.no cfengine.com", "nameserver 128.39.89.10" };

delete_lines:

  "search.*";

insert_lines:

  "$(search)" location => end;
}

#######################################################


body edit_defaults def
{
empty_file_before_editing => "false";
edit_backup => "false";
max_file_size => "100000";
}

########################################################


body location start

{
# If not line to match, applies to whole text body

before_after => "before";
}

########################################################


body location end

{
# If not line to match, applies to whole text body

before_after => "after";
}
```

## Deleting lines exception

```cf3
########################################################

#

# Simple test editfile

#

########################################################


#

# This assumes a file format like:

#

# [section 1]

#

# lines....

#

# [section 2]

#

# lines... etc



body common control

{
bundlesequence  => { "testbundle" };
}

########################################################


bundle agent testbundle

{
files:

  "/tmp/passwd_excerpt"

       create    => "true",
       edit_line => MarkNRoot;
}

########################################################


bundle edit_line MarkNRoot
  {
  delete_lines:

       "mark.*|root.*" not_matching => "true";

  }
```

## Editing files

This is a huge topic. See also See Add lines to a file, See Editing tabular files, etc. Editing a file can be complex or simple, depending on needs.

Here is an example of how to comment out lines matching a number of patterns:

```cf3
######################################################################
#

# Comment lines

#

######################################################################


body common control

{
version         =>   "1.2.3";
bundlesequence  => { "testbundle"  };
inputs          => { "cf_std_library.cf" };
}

########################################################


bundle agent testbundle

{
vars:

  "patterns" slist => { "finger.*", "echo.*", "exec.*", "rstat.*", 
                                               "uucp.*", "talk.*" };

files:

  "/etc/inetd.conf"

      edit_line => comment_lines_matching("@(testbundle.patterns)","#");
}
```


## Editing tabular files

```cf3
######################################################################

#

# File editing

#

# Normal ordering:

# - delete

# - replace | colum_edit

# - insert

# 

######################################################################



body common control

{
version => "1.2.3";
bundlesequence  => { "testbundle"  };
}

########################################################


bundle agent testbundle

{
vars:

 "userset" slist => { "one-x", "two-x", "three-x" };

files:

  # Make a copy of the password file


  "/home/mark/tmp/passwd"

       create    => "true",
       edit_line => SetUserParam("mark","6","/set/this/shell");

  "/home/mark/tmp/group"

       create    => "true",
       edit_line => AppendUserParam("root","4","@(userset)");

commands:

  "/bin/echo" args => "$(userset)";

}

########################################################


bundle edit_line SetUserParam(user,field,val)
  {
  field_edits:

   "$(user):.*"

      # Set field of the file to parameter


      edit_field => col(":","$(field)","$(val)","set");
  }

########################################################


bundle edit_line AppendUserParam(user,field,allusers)
  {
  vars:

    "val" slist => { @(allusers) };

  field_edits:

   "$(user):.*"

      # Set field of the file to parameter


      edit_field => col(":","$(field)","$(val)","alphanum");

  }

########################################

# Bodies

########################################


body edit_field col(split,col,newval,method)

{
field_separator => "$(split)";
select_field    => "$(col)";
value_separator  => ",";
field_value     => "$(newval)";
field_operation => "$(method)";
extend_fields => "true";
}
```

    Environment (virtual)
    Environment variables
    Execresult example
    Inserting lines in a file
    Get a list of users
    Global classes
    Hello world
    LDAP interactions
    Linking files
    Listing files-pattern in a directory
    Locate and transform files
    Logging
    Measurements
    Methods
    Method validation
    Mount NFS filesystem


## Environments (virtual)

```cf3

#######################################################

#

# Virtual environments

#

#######################################################


body common control

{
bundlesequence  => { "my_vm_cloud" };   
}

#######################################################


bundle agent my_vm_cloud

{
vars:

  "vms[atlas]" slist => { "guest1", "guest2", "guest3" };

environments:

 scope||any::  # These should probably be in class "any" to ensure uniqueness

   "$(vms[$(sys.host)])"

       environment_resources => virt_xml("$(xmlfile[$(this.promiser)])"),
       environment_interface => vnet("eth0,192.168.1.100/24"),
       environment_type      => "test",
       environment_host      => "atlas";

      # default environment_state => "create" on host, and "suspended elsewhere"

}

#######################################################


body environment_resources virt_xml(specfile)
{
env_spec_file => "$(specfile)";
}

#######################################################


body environment_interface vnet(primary)
{
env_name      => "$(this.promiser)";
env_addresses => { "$(primary)" };

host1::

  env_network => "default_vnet1";

host2::

  env_network => "default_vnet2";

}
```

## Environment variables

```cf3
#######################################################

#

# Virtual environments

#

#######################################################


body common control

{
bundlesequence  => { "my_vm_cloud" };   
}

#######################################################


bundle agent my_vm_cloud

{
environments:

   "centos5"

       environment_resources => virt_xml,
       environment_type      => "xen",
       environment_host      => "ursa-minor";

      # default environment_state => "create" on host, and "suspended elsewhere"

}

#######################################################


body environment_resources virt_xml
{
env_spec_file => "/srv/xen/centos5-libvirt-create.xml";
}
```

## Execresult example

```cf3
body common control

{
bundlesequence  => { "example" };
}

###########################################################


bundle agent example

{     
vars:

  "my_result" string => execresult("/bin/ls /tmp","noshell");

reports:

  linux::

    "Variable is $(my_result)";

}
```

## Inserting lines in a file

```cf3
#######################################################

#

# Insert a number of lines with vague whitespace

#

#######################################################


body common control

{
any::

  bundlesequence  => { "insert" };   
}


#######################################################


bundle agent insert

{
vars:

  "v" string => "  One potato";
 
files:

  "/tmp/test_insert"

            create => "true",
         edit_line => Insert("$(insert.v)");

}

#######################################################

# For the library

#######################################################


bundle edit_line Insert(name)

{
insert_lines:

  "  $(name)"

      whitespace_policy => { "ignore_leading", "ignore_embedded" };

}

#######################################################


body edit_defaults empty

{
empty_file_before_editing => "true";
}


#######################################################

#

# Insert a number of lines

#

#######################################################


body common control

{
any::

  bundlesequence  => { "insert" };   
}


#######################################################


bundle agent insert

{
vars:

  "v" string => "
                One potato
                Two potato
                Three potatoe
                Four
                ";
 
files:

  "/tmp/test_insert"

            create => "true",
         edit_line => Insert("$(insert.v)"),
     edit_defaults => empty;

}

#######################################################

# For the library

#######################################################


bundle edit_line Insert(name)

{
insert_lines:

  "Begin$(const.n)$(name)$(const.n)End";

}

#######################################################


body edit_defaults empty

{
empty_file_before_editing => "false";
}


#######################################################

#

# Insert a number of lines

#

#######################################################


body common control

{
any::

  bundlesequence  => { "insert" };   
}


#######################################################


bundle agent insert

{
vars:

  "v" slist => {
                "One potato",
                "Two potato",
                "Three potatoe",
                "Four"    
               };
 
files:

  "/tmp/test_insert"

            create => "true",
         edit_line => Insert("@(insert.v)");
   #  edit_defaults => empty;


}

#######################################################

# For the library

#######################################################


bundle edit_line Insert(name)

{
insert_lines:

  "$(name)";

}

#######################################################


body edit_defaults empty

{
empty_file_before_editing => "true";
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

## Global classes

```cf3
body common control
{
bundlesequence => { "g","tryclasses_1", "tryclasses_2" };

}

#################################


bundle common g
{
classes:

  "one" expression => "any";

  "client_network" expression => iprange("128.39.89.0/24");
}

#################################


bundle agent tryclasses_1
{
classes:

  "two" expression => "any";
}

#################################


bundle agent tryclasses_2
{
classes:

  "three" expression => "any";

reports:

  one.three.!two::

    "Success";
}


#################################
```

## Hello world

```cf3
# Hard promises


body common control
{
bundlesequence => { "hello" };
}

# soft promises


bundle agent hello
{
reports:

 linux::

   "Hello world!";
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

## Linking files

```cf3
######################################################################

#

# File editing

#

# Normal ordering:

# - delete

# - replace | colum_edit

# - insert

# 

######################################################################



body common control

{
version => "1.2.3";
bundlesequence  => { "testbundle"  };
}

########################################################


bundle agent testbundle

{
files:

  # Make a copy of the password file


  "/home/mark/tmp/passwd"

       link_from     => linkdetails("/etc/passwd"),
       move_obstructions => "true";


  "/home/mark/tmp/linktest"

       link_from     => linkchildren("/usr/local/sbin");


#child links

}

#########################################################


body link_from linkdetails(tofile)

{
source        => "$(tofile)";
link_type     => "symlink";
when_no_source  => "force";      # kill
}

#########################################################


body link_from linkchildren(tofile)

{
source        => "$(tofile)";
link_type     => "symlink";
when_no_source  => "force";      # kill
link_children => "true";
when_linking_children => "if_no_such_file"; # "override_file";
}


Removing deadlinks from a directory:

#######################################################

#

# Test dead link removal

#

#######################################################


body common control
   {
   any::

      bundlesequence  => { 
"testbundle"  
                         };
   }


############################################


bundle agent testbundle

{
files:

  "/home/mark/tmp/test_to" -> "someone"

      depth_search => recurse("inf"),
      perms => modestuff,
      action => tell_me;

}

############################################


body depth_search recurse(d)

{
rmdeadlinks => "true";
depth => "$(d)";
}

############################################


body perms modestuff

{
mode => "o-w";
}

############################################


body action tell_me

{
report_level => "inform";
}
```

## Listing files-pattern in a directory

```cf3
body common control

{
bundlesequence  => { "example" };
}

###########################################################


bundle agent example

{     
vars:

  "ls" slist => lsdir("/etc","p.*","true");

reports:

  !sdfkjh::

    "ls: $(ls)";

}
```

## Locate and transform files

```cf3
#######################################################

#

# Compressing files

#

#######################################################


body common control
   {
   any::

      bundlesequence  => { 
"testbundle"  
                         };

   version => "1.2.3";
   }

############################################


bundle agent testbundle

{
files:

  "/home/mark/tmp/testcopy" 

    file_select => pdf_files,
    transformer => "/usr/bin/gzip $(this.promiser)",
    depth_search => recurse("inf");

}

############################################


body file_select pdf_files

{
leaf_name => { ".*.pdf" , ".*.fdf" };
file_result => "leaf_name";
}

############################################


body depth_search recurse(d)

{
depth => "$(d)";
}
```

## Logging

```cf3
body common control
{
bundlesequence => { "test" };
}

bundle agent test
{
vars:

  "software" slist => { "/root/xyz", "/tmp/xyz" };

files:

  "$(software)"

    create => "true",
     action => logme("$(software)");

}

#


body action logme(x)
{
log_kept => "/tmp/private_keptlog.log";
log_failed => "/tmp/private_faillog.log";
log_repaired => "/tmp/private_replog.log";
log_string => "$(sys.date) $(x) promise status";
}


body common control
{
bundlesequence => { "one" };
}



bundle agent one
{
files:

  "/tmp/xyz"

       create => "true",
       action => log;

}

body action log
{
log_level => "inform";
}
```

## Measurements

```cf3
#cop measurements,example


#######################################################

#

# Test file:

#

# First line

# Blonk blonk bnklkygsuilnm

#

#######################################################


body common control
{
bundlesequence => { "report" };
}

#######################################################


body monitor control
{
forgetrate => "0.7";
histograms => "true";
}

#######################################################


bundle agent report
{
reports:

 cfengine_3::

   "
   Free memory read at $(mon.av_free_memory_watch)
   cf_monitord read $(mon.value_monitor_self_watch)   
   ";
}

#######################################################


bundle monitor watch
{
measurements:

  # Test 1 - extract string matching


  "/home/mark/tmp/testmeasure"

      handle => "blonk_watch",
      stream_type => "file",
      data_type => "string",
      history_type => "weekly",
      units => "blonks",
      match_value => find_blonks,
      action => sample_min("10");

  # Test 2 - follow a special process over time

  # using cfengine's process cache to avoid resampling


   "/var/cfengine/state/cf_rootprocs"

      handle => "monitor_self_watch",
      stream_type => "file",
      data_type => "int",
      history_type => "static",
      units => "kB",
      match_value => proc_value(".*cf-monitord.*",
                                "root\s+[0-9.]+\s+[0-9.]+\s+[0-9.]+\s+[0-9.]+\s+([0-9]+).*");

  # Test 3, discover disk device information


  "/bin/df"

      handle => "free_disk_watch",
      stream_type => "pipe",
      data_type => "slist",
      history_type => "static",
      units => "device",
      match_value => file_system;
      # Update this as often as possible


  # Test 4


   "/tmp/file"

         handle => "line_counter",
    stream_type => "file",
      data_type => "counter",
    match_value => scanlines("MYLINE.*"),
   history_type => "log";

}

##########################################################


body match_value scanlines(x)
{
select_line_matching => "^$(x)$";
}

##########################################################


body action sample_min(x)
{
ifelapsed => "$(x)";
expireafter => "$(x)";
}

##########################################################


body match_value find_blonks
{
select_line_number => "2";
extraction_regex => "Blonk blonk ([blonk]+).*";
}

##########################################################


body match_value free_memory
{
select_line_matching => "MemFree:.*";
extraction_regex => "MemFree:\s+([0-9]+).*";
}

##########################################################


body match_value proc_value(x,y)
{
select_line_matching => "$(x)";
extraction_regex => "$(y)";
}

##########################################################


body match_value file_system
{
select_line_matching => "/.*";
extraction_regex => "(.*)";
}
```

## Methods

```cf3
body common control

{
bundlesequence  => { "testbundle"  };

version => "1.2.3";
}

###########################################


bundle agent testbundle
{
vars:

 "userlist" slist => { "mark", "jeang", "jonhenrik", "thomas", "eben" };

methods:

 "any" usebundle => subtest("$(userlist)");

}

###########################################


bundle agent subtest(user)

{
commands:

 "/bin/echo Fix $(user)";

reports:

 linux::

  "Finished doing stuff for $(user)";
}
```

## Method validation

```cf3
body common control

{
bundlesequence  => { "testbundle"  };

version => "1.2.3";
}

###########################################


body agent control

{
abortbundleclasses => { "invalid" };
}

###########################################


bundle agent testbundle
{
vars:

 "userlist" slist => { "xyz", "mark", "jeang", "jonhenrik", "thomas", "eben" };

methods:

 "any" usebundle => subtest("$(userlist)");

}

###########################################


bundle agent subtest(user)

{
classes:

  "invalid" not => regcmp("[a-z][a-z][a-z][a-z]","$(user)");

reports:

 !invalid::

  "User name $(user) is valid at 4 letters";

 invalid::

  "User name $(user) is invalid";
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

## Ordering promises

This counts to five by default. If we change ‘/bin/echo one’ to ‘/bin/echox one’, then the command will fail, causing us to skip five and go to six instead.

This shows how dependencies can be chained in spite of the order of promises in the bundle.

Normally the order of promises in a bundle is followed, within each promise type, and the types are ordered according to normal ordering.

```cf3
##################################################################

#

# cfengine 3 - ordering promises into dependent chains

#

##

#

# cf-agent -f ./cftest.cf -K

#

##################################################################


body common control

{
bundlesequence => { "order" };
}

##################################################################


bundle agent order

{
vars:

 "list" slist => { "three", "four" };

commands:

 ok_later::

   "/bin/echo five";

 otherthing::

   "/bin/echo six";

 any::


  "/bin/echo one"     classes => d("ok_later","otherthing");
  "/bin/echo two";
  "/bin/echo $(list)";

 preserved_class::

  "/bin/echo seven";

}

############################################


body classes d(if,else)

{
promise_repaired => { "$(if)" };
repair_failed => { "$(else)" };
persist_time => "0";
}
```

    Process management
    Read from a TCP socket
    Resolver management
    Search and replace text
    Selecting a region in a file
    Service management (windows)


## Process management

```cf3	
body common control
{
bundlesequence => { "test" };
}



bundle agent test
{
processes:

 "sleep"

   signals => { "term", "kill" };

}

########################################################

#

# Simple test processes 

#

########################################################


body common control

{
bundlesequence  => { "testbundle"  };
}

########################################################


bundle agent testbundle

{
processes:

 "sleep"

    process_count   => up("sleep");

reports:

 sleep_out_of_control::

   "Out of control";
}

########################################################


body process_count up(s)

{
match_range => "5,10"; # or irange("1","10");
out_of_range_define => { "$(s)_out_of_control" };
}

########################################################

#

# Simple test processes 

#

########################################################


body common control

{
bundlesequence  => { "testbundle"  };
}

########################################################


bundle agent testbundle

{
processes:

 ".*"

    process_select  => proc_finder("a.*"),
    process_count   => up("cfservd");
}

########################################################


body process_count up(s)

{
match_range => "1,10"; # or irange("1","10");
out_of_range_define => { "$(s)_out_of_control" };
}

########################################################


body process_select proc_finder(p)

{
stime_range => irange(ago("0","0","0","2","0","0"),now);
process_result => "stime";
}


########################################################

#

# Simple test processes 

#

########################################################


body common control

{
bundlesequence  => { "testbundle"  };
}

########################################################


bundle agent testbundle

{
processes:

 ".*"

    process_select  => proc_finder("a.*"),
    process_count   => up("cfservd");
}

########################################################


body process_count up(s)

{
match_range => "1,10"; # or irange("1","10");
out_of_range_define => { "$(s)_out_of_control" };
}

########################################################


body process_select proc_finder(p)

{
process_owner  => { "avahi", "bin" };
command        => "$(p)";
pid            => "100,199";
vsize          => "0,1000";
process_result => "command.(process_owner|vsize)";
}


body common control
{
bundlesequence => { "process_restart" };
}

#########################################################


bundle agent process_restart
{
processes:

  "/usr/bin/daemon" 
        restart_class => "launch";

commands:

  launch::

   "/usr/bin/daemon";

}

body common control
{
bundlesequence => { "process_restart" };
}

#########################################################


bundle agent process_restart
{
vars:

  "component" slist => {
                       "cf-monitord", 
                       "cf-serverd", 
                       "cf-execd" 
                       };
processes:

  "$(component)" 
        restart_class => canonify("start_$(component)");

commands:

   "/var/cfengine/bin/$(component)"
       ifvarclass => canonify("start_$(component)");

}

########################################################

#

# Simple test process restart

#

########################################################


body common control

{
bundlesequence  => { "testbundle"  };
}

########################################################


bundle agent testbundle

{
processes:

 "cfservd"

        process_count   => up("cfservd");

 cfservd_out_of_control::

   "cfservd"

        signals         => { "stop" , "term" },
        restart_class   => "start_cfserv";


commands:

  start_cfserv::

    "/usr/local/sbin/cfservd";

}

########################################################


body process_count up(s)

{
match_range => "1,10"; # or irange("1","10");
out_of_range_define => { "$(s)_out_of_control" };
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

## Search and replace text

```cf3
######################################################################

#

# File editing

#

# Normal ordering:

# - delete

# - replace | colum_edit

# - insert

# 

######################################################################



body common control

{
version => "1.2.3";
bundlesequence  => { "testbundle"  };
}

########################################################


bundle agent testbundle

{

files:

  "/tmp/replacestring"

       create    => "true",
       edit_line => myedit("second");
}

########################################################


bundle edit_line myedit(parameter)
  {
  vars:

   "edit_variable" string => "private edit variable is $(parameter)"; 

  
  replace_patterns:

  # replace shell comments with C comments


   "puppet"

      replace_with => With("cfengine 3");

  }

########################################

# Bodies

########################################


body replace_with With(x)

{
replace_value => "$(x)";
occurrences => "first";
}

########################################


body select_region MySection(x)

{
select_start => "\[$(x)\]";
select_end => "\[.*\]";
}
```

## Selecting a region in a file

```cf3
body common control

{
version => "1.2.3";
bundlesequence  => { "testbundle"  };
}

########################################################


bundle agent testbundle

{

files:

  "/tmp/testfile"

       create    => "true",
       edit_line => myedit("second");
}

########################################################


bundle edit_line myedit(parameter)
  {
  vars:

   "edit_variable" string => "private edit variable is $(parameter)"; 

  
  replace_patterns:

  # comment out lines after start


   "([^#].*)"

      replace_with => comment,
     select_region => ToEnd("Start.*");

  }

########################################

# Bodies

########################################


body replace_with comment

{
replace_value => "# $(match.1)"; # backreference 0
occurrences => "all";  # first, last all
}

########################################################


body select_region ToEnd(x)

{
select_start => "$(x)";
}
```

## Service management (windows)

```cf3
body common control

{
bundlesequence  => { "winservice" };
}

###########################################################


bundle agent winservice

{
vars:

  "bad_services" slist => { "Alerter",  "ClipSrv" };

services:

 windows::

  "$(bad_services)"

       service_policy => "disable",
       comment => "Disable services that create security issues";
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


## Tidying garbage files

Emulating the `tidy' feature of CFEngine 2.

```cf3
#######################################################
#

# Deleting files, like cf2 tidy age=0 r=inf

#

#######################################################


body common control

{
 any::

  bundlesequence  => { "testbundle" };   
}

############################################


bundle agent testbundle

{
files:

  "/tmp/test" 

    delete => tidyfiles,
    file_select => zero_age,
    depth_search => recurse("inf");
}

#########################################################


body depth_search recurse(d)

{
#include_basedir => "true";

depth => "$(d)";
}

#########################################################


body delete tidy

{
dirlinks => "delete";
rmdirs   => "false"; 
}

#########################################################


body file_select zero_age

#

# we can build old "include", "exclude", and "ignore" 

# from these as standard patterns - these bodies can

# form a library of standard patterns

#


{
mtime     => irange(ago(1,0,0,0,0,0),now);  
file_result => "mtime"; 
}

    Software distribution
    Trigger classes
```
	
## Software distribution

```cf3
#########################################################################

#

#   software_local.cf - Application Deployment From Directory Repository

#

#   NOTE: Windows needs to support WMI queries about installed msi files

#         in order for Cfengine to detect them. On Windows 2003,

#         go to Control Panel -> Add/Remove Programs -> 

#         Windows Components -> Mgmnt and Monitoring Tools and check

#         WMI Windows Installer Provider.

#

#   NOTE: Naming conventions are important when updating packages.

#         By default, Cfengine expects "name-version-arch.msi" 

#         on Windows, where name is lowercase, and arch is 

#         i686 or x86_64. No spaces should be included in the filename.

#         The Caption and Version fields inside the msi package

#         are important. They must correspond to the file name as 

#         follows: name = lowercase(spacetodash(Caption)), 

#         version = Version. For any msi-file, use InstEd 

#         (www.instedit.com) to check/modify the 

#         Caption and Version fields 

#         (Tables->Property->ProductName/ProductVersion).

#

#         For example, ProductName "CFEngine Nova" with ProductVersion

#         "1.1.2" for 32-bit Windows will correspond to the filename

#         "cfengine-nova-1.1.2-i686.msi".

#

#########################################################################


bundle agent check_software
{
vars:

# software to install if not installed

 "include_software" slist => {
                             "7-zip-4.50-$(sys.arch).msi"
                             };

# this software gets updated if it is installed

 "autoupdate_software" slist => { 
                               "7-zip"
                               };							 

# software to uninstall if it is installed

 "exclude_software" slist => {
                             "7-zip-4.65-$(sys.arch).msi"
                             };

methods:
#  "any" usebundle => add_software( "@(check_software.include_software)", "$(sys.policy_hub)" );

#  "any" usebundle => update_software( "@(check_software.autoupdate_software)", "$(sys.policy_hub)" );

#  "any" usebundle => remove_software( "@(check_software.exclude_software)", "$(sys.policy_hub)" );

}

#########################################################################


bundle agent add_software(pkg_name,
{
vars:
# dir to install from locally - can also check multiple directories

 "local_software_dir" string => "C:\Program Files\Cfengine\software\add";

 
files:

  "$(local_software_dir)"
       copy_from => remote_cp("/var/cfengine/master_software_updates/$(sys.flavour)_$(sys.arch)/add", "$(srv)"),

    depth_search => recurse("1"),

         classes => if_repaired("got_newpkg"),

		 comment => "Copy software from remote repository";



packages:

# When to check if the package is installed ?

 got_newpkg|any::
  "$(pkg_name)"
    package_policy           => "add",

    package_method           => msi_implicit( "$(local_software_dir)" ),

    classes                  => if_else("add_success", "add_fail" ),

    comment                  => "Install new software, if not already present";


reports::
 add_fail::
   "Failed to install one or more packages";
}

#########################################################################


bundle agent update_software(sw_names,
{
vars:
# dir to install from locally - can also check multiple directories

 "local_software_dir" string => "C:\Program Files\Cfengine\software\update";

 
files:

  "$(local_software_dir)"
       copy_from => remote_cp("/var/cfengine/master_software_updates/$(sys.flavour)_$(sys.arch)/update", "$(srv)"),

    depth_search => recurse("1"),

         classes => if_repaired("got_newpkg"),

		 comment => "Copy software updates from remote repository";

 
 
packages:

# When to check if the package is updated ?

 got_newpkg|any::
  "$(sw_names)"
    package_policy           => "update",

    package_select           => ">=",                 # picks the newest update available

    package_architectures    => { "$(sys.arch)" },    # install 32 or 64 bit package ?
    package_version          => "1.0",                # at least version 1.0

    package_method           => msi_explicit( "$(local_software_dir)" ),

    classes                  => if_else("update_success", "update_fail");


	
reports::
 update_fail::
   "Failed to update one or more packages";
}

#########################################################################


bundle agent remove_software(pkg_name,
{
vars:
# dir to install from locally - can also check multiple directories

 "local_software_dir" string => "C:\Program Files\Cfengine\software\remove";

 
files:

  "$(local_software_dir)"
       copy_from => remote_cp("/var/cfengine/master_software_updates/$(sys.flavour)_$(sys.arch)/remove", "$(srv)"),

    depth_search => recurse("1"),

         classes => if_repaired("got_newpkg"),

         comment => "Copy removable software from remote repository";


packages:
got_newpkg::
  "$(pkg_name)"
    package_policy           => "delete",

    package_method           => msi_implicit( "$(local_software_dir)" ),

    classes                  => if_else("remove_success", "remove_fail" ),

    comment                  => "Remove software, if present";


reports::
 remove_fail::
   "Failed to remove one or more packages";
}
```

## Trigger classes

```cf3
#######################################################

#

# Insert a number of lines and trigger a followup if edited

#

#######################################################


body common control

{
any::

  bundlesequence  => { "insert" };   
}


#######################################################


bundle agent insert

{
vars:

  "v" string => "
                One potato
                Two potato
                Three potahto
                Four
                ";
 
files:

  "/tmp/test_insert"

     edit_line => Insert("$(insert.v)"),
     edit_defaults => empty,
     classes => trigger("edited");

commands:

 edited::

  "/bin/echo make bananas";

reports:

  edited::

    "The potatoes are bananas";

}

#######################################################

# For the library

#######################################################


bundle edit_line Insert(name)

{
insert_lines:

  "Begin$(const.n) $(name)$(const.n)End";

}

#######################################################


body edit_defaults empty

{
empty_file_before_editing => "true";
}

#######################################################


body classes trigger(x)

{
promise_repaired => { "$(x)" };
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

## Web server modules

The problem of editing the correct modules into the list of standard modules for the Apache web server. This example is based on the standard configuration deployment of SuSE Linux. Simply provide the list of modules you want and another list that you don't want.

```cf3
#######################################################
#

# Apache 2 reconfig - modelled on SuSE

#

#######################################################


body common control

{
any::

  bundlesequence  => {
                     apache
                     };   
}

#######################################################


bundle agent apache

{
files:

 SuSE::

  "/etc/sysconfig/apache2" 

     edit_line => fixapache;
}

#######################################################

# For the library

#######################################################


bundle edit_line fixapache

{ 
vars:

 "add_modules"     slist => { 
                            "dav", 
                            "dav_fs", 
                            "ssl", 
                            "php5", 
                            "dav_svn",
                            "xyz",
                            "superduper"
                            };

 "del_modules"     slist => { 
                            "php3",
                            "jk",
                            "userdir",
                            "imagemap",
                            "alias"
                            };

insert_lines:

 "APACHE_CONF_INCLUDE_FILES=\"/site/masterfiles/local-http.conf\"";

field_edits:

 #####################################################################

 # APACHE_MODULES="authz_host actions alias ..."

 #####################################################################


    # Values have the form NAME = "quoted space separated list"


   "APACHE_MODULES=.*"

      # Insert module "columns" between the quoted RHS 

      # using space separators


      edit_field => quotedvar("$(add_modules)","append");

   "APACHE_MODULES=.*"

      # Delte module "columns" between the quoted RHS 

      # using space separators


      edit_field => quotedvar("$(del_modules)","delete");

   # if this line already exists, edit it  


}
```

    Warn if matching line in file
    Windows registry
    unit_registry_cache.cf
    unit_registry.cf

## Warn if matching line in file

```cf3
########################################################

#

# Warn if line matched

#

########################################################


body common control

{
bundlesequence  => { "testbundle" };
}

########################################################


bundle agent testbundle

{
files:

  "/var/cfengine/inputs/.*"

       edit_line => DeleteLinesMatching(".*cfenvd.*"),
       action => WarnOnly;
}

########################################################


bundle edit_line DeleteLinesMatching(regex)
  {
  delete_lines:

    "$(regex)" action => WarnOnly;

  }

########################################################


body action WarnOnly
{
action_policy => "warn";
}
```

## Windows registry

```cf3
body common control
{
bundlesequence => { "reg" };
}

bundle agent reg
{
vars:

  "value" string => registryvalue("HKEY_LOCAL_MACHINE\SOFTWARE\Cfengine AS\Cfengine","value3");

reports:

  windows::

   "Value extracted: $(value)";

}
```

## unit_registry_cache.cf

```cf3
body common control
{
 bundlesequence => {
#                   "registry_cache"

#                   "registry_restore"

                   };
}

#########################################


bundle agent registry_cache
{
 databases:
  windows::

     "HKEY_LOCAL_MACHINE\SOFTWARE\Adobe"
        database_operation => "cache",
        database_type      => "ms_registry",
        comment => "Save correct registry settings for Adobe products";
}

#########################################


bundle agent registry_restore
{
 databases:
  windows::

     "HKEY_LOCAL_MACHINE\SOFTWARE\Adobe"
        database_operation => "restore",
        database_type      => "ms_registry",
        comment => "Make sure Adobe products have correct registry settings";
}
```

## unit_registry.cf

```cf3
body common control
{
 
bundlesequence => { "databases" };
}


bundle agent databases

{
databases:

 windows::

  # Regsitry has (value,data) pairs in "keys" which are directories


#  "HKEY_LOCAL_MACHINE\SOFTWARE\Cfengine AS"


#    database_operation => "create", 

#    database_type     => "ms_registry";


#  "HKEY_LOCAL_MACHINE\SOFTWARE\Cfengine AS\Cfengine"


#    database_operation => "create", 

#    database_rows => { "value1,REG_SZ,new value 1", "value2,REG_SZ,new val 2"} ,

#    database_type     => "ms_registry";



  "HKEY_LOCAL_MACHINE\SOFTWARE\Cfengine AS\Cfengine"

    database_operation => "delete", 
    database_columns => { "value1", "value2" } ,
    database_type => "ms_registry";


# "HKEY_LOCAL_MACHINE\SOFTWARE\Cfengine AS\Cfengine"


#    database_operation => "cache",   # cache,restore


#    registry_exclude => { ".*Windows.*CurrentVersion.*", ".*Touchpad.*", ".*Capabilities.FileAssociations.*", ".*Rfc1766.*" , ".*Synaptics.SynTP.*", ".*SupportedDevices.*8086", ".*Microsoft.*ErrorThresholds" },


#    database_type     => "ms_registry";


"HKEY_LOCAL_MACHINE\SOFTWARE\Cfengine AS"

   database_operation => "restore",
   database_type      => "ms_registry";

}
```
