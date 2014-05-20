---
layout: default
title: System Security Examples 
published: true
sorting: 10
tags: [Examples,System Security]
---

* [Distribute root passwords][System Security Examples#Distribute root passwords]
* [Distribute ssh keys][System Security Examples#Distribute ssh keys]
* Distribute ssh keys

## Distribute root passwords	
  
```cf3
  
######################################################################
#

# Root password distribution

# 

######################################################################


body common control

{
version => "1.2.3";
bundlesequence  => { "SetRootPassword" };
}

########################################################


bundle common g
{
vars:

  "secret_keys_dir" string => "/tmp";
}

########################################################


bundle agent SetRootPassword

{
files:

  "/var/cfengine/ppkeys/rootpw.txt"

      copy_from => scp("$(sys.fqhost)-root.txt","master_host.example.org");

      # or $(pw_class)-root.txt


  # Or get variables directly from server woth Nova


 "remote-passwd" string => remotescalar("rem_password","127.0.0.1","yes");

  # Test this on a copy


  "/tmp/shadow"

       edit_line => SetRootPw;

}

########################################################


bundle edit_line SetRootPw
  {
  vars:

   # Assume this file contains a single string of the form root:passwdhash:

   # with : delimiters to avoid end of line/file problems


   "pw" int => readstringarray("rpw","$(sys.workdir)/ppkeys/rootpw.txt",
                                                    "#[^\n]*",":","1","200");

  field_edits:

   "root:.*"

      # Set field of the file to parameter


      edit_field => col(":","2","$(rpw[1])","set");
  }

########################################################


bundle server passwords
{
vars:

  # Read a file of format

  #

  # classname: host1,host2,host4,IP-address,regex.*,etc

  #


       "pw_classes" int => readstringarray("acl","$(g.secret_keys_dir)/classes.txt",
                                                       "#[^\n]*",":","100","4000");  
  "each_pw_class" slist => getindices("acl");
 
access:

  "/secret/keys/$(each_pw_class)-root.txt"

        admit   => splitstring("$(acl[$(each_pw_class)][1])" , ":" , "100"),
    ifencrypted => "true";

}
```

## Distribute ssh keys

```cf3
# Assume that we have collected all users' public keys into a single source area
# on the server. First copy the ones we need to localhost, and then edit them into

# the the user's local keyring.


  # vars:

  #

  #  "users" slist => { "user1", "user2", ...};

  #

  # methods:

  #

  #  "any" usebundle => allow_ssh_login_from_authorized_keys(@(users),"sourcehost");

  #


########################################################################


bundle agent allow_ssh_rootlogin_from_authorized_keys(user,sourcehost)
{
vars:

  "local_cache"       string => "/var/cfengine/ssh_cache"; 
  "authorized_source" string => "/master/CFEngine/ssh_keys";

files:

   "$(local_cache)/$(user).pub"

         comment => "Copy public keys from a an authorized cache into a cache on localhost",
           perms => mo("600","root"),
       copy_from => remote_cp("$(authorized_source)/$(user).pub","$(sourcehost)"),
          action => if_elapsed("60");

   "/root/.ssh/authorized_keys" 

         comment => "Edit the authorized keys into the user's personal keyring",
       edit_line => insert_file_if_no_line_matching("$(user)","$(local_cache)/$(user).pub"),
          action => if_elapsed("60");
}

########################################################################


bundle agent allow_ssh_login_from_authorized_keys(user,sourcehost)
{
vars:

  "local_cache"       string => "/var/cfengine/ssh_cache"; 
  "authorized_source" string => "/master/CFEngine/ssh_keys";

files:

   "$(local_cache)/$(user).pub"

         comment => "Copy public keys from a an authorized cache into a cache on localhost",
           perms => mo("600","root"),
       copy_from => remote_cp("$(authorized_source)/$(user).pub","$(sourcehost)"),
          action => if_elapsed("60");

   "/home/$(user)/.ssh/authorized_keys" 

         comment => "Edit the authorized keys into the user's personal keyring",
       edit_line => insert_file_if_no_line_matching("$(user)","$(local_cache)/$(user).pub"),
          action => if_elapsed("60");
}

########################################################################


bundle edit_line insert_file_if_no_line_matching(user,file)
{
classes:

  "have_user" expression => regline("$(user).*","$(this.promiser)");

insert_lines:

  !have_user::

    "$(file)" 
         insert_type => "file";
}

```