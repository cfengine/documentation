---
layout: default
title: Distribute ssh keys
published: true
tags: [Examples, Policy, ssh, distribution]
reviewed: 2013-06-08
reviewed-by: atsaloli
---

Let's say we have a list of users that are trusted
to login to a set of servers managed by CFEngine.

We are going to implement this trust relationship
by ensuring the users' accounts on managed servers
have a .ssh/authorized_keys file with each user's
public key.

Let's assume we collected all users' public keys
into a single directory on the server and that
users exist on the clients (and have corresponding
home directory).  The following CFEngine policy
distributes the keys from /var/cfengine/masterfiles/ssh_keys
on the policy server to /var/cfengine/inputs/ssh_keys
on the managed servers and from there each user's
key will go to each user's .ssh/authorized_keys file.

Note: special variable $(sys.policy_hub) contains
the hostname of the policy server.


You have to adapt this policy in the mentioned places for it to work in your environment.

```cf3

body common control {
bundlesequence => { "distribute_ssh_keys" };
inputs => { "libraries/cfengine_stdlib.cf" };
}

bundle agent distribute_ssh_keys
{
vars:

    "users"             slist => { "user1", "user2" };   # List of users to be included in key distribution.
                                                         # Modify to include actual users.
    "source_server"    string => "$(sys.policy_hub)";         # Server where keys are stored
    "source_directory" string => "/var/cfengine/masterfiles/ssh_keys"; # Source directory of key files
    "local_cache"      string => "/var/cfengine/inputs/ssh_keys";      # Local cache of key files

files:

   "$(local_cache)/$(users).pub"

       comment => "Copy public keys from an authorized source into a cache on localhost",
         perms => mo("600","root"),
     copy_from => remote_cp("$(source_directory)/$(users).pub","$(source_server)"),
        action => if_elapsed("60");  # wait 60 min before checking this promise again

  # Ensure that authorized_keys file exists and has permissions 600 and call a file editing promise

   "/home/$(users)/.ssh/authorized_keys"

     comment => "Edit the authorized keys into the user's personal keyring",
      create => "true",
       perms => m("600"),
   edit_line => insert_file_if_no_line_matching("$(users)","$(local_cache)/$(users).pub"),
      action => if_elapsed("60");
}

#####

bundle edit_line insert_file_if_no_line_matching(user,file)
{

# Check if user exists in the authorized_keys file
classes:

  "have_user"
    expression => regline("$(user).*","$(this.promiser)");

# Insert the content of the key file into authorized_keys if the user's key is not already there
insert_lines:

  !have_user::

    "$(file)"
      insert_type => "file";
}
```

Example run:

First, let's setup for the run. Put users' SSH keys into the key distribution point on the policy hub:

```
policy_hub# ls /var/cfengine/masterfiles/ssh_keys/*pub
/var/cfengine/masterfiles/ssh_keys/user1.pub  /var/cfengine/masterfiles/ssh_keys/user2.pub
policy_hub#
```

There are no authorized_keys files on the managed servers, but the home (and .ssh) directories exist:

```
# ls -d /home/user*/.ssh
/home/user1/.ssh  /home/user2/.ssh
# ls /home/user?/.ssh/authorized_keys
ls: cannot access /home/user?/.ssh/authorized_keys: No such file or directory
#
```

Run CFEngine on one of the managed servers to create
and populate /var/cfengine/inputs/ssh_keys from source
(policy_hub:/var/cfengine/masterfiles/ssh_keys)
and then install each user's key into that user's
authorized_keys file:

```
# cf-agent -f ssh.cf
2013-06-08T15:49:29-0700    error: Failed to chdir into '/var/cfengine/inputs/ssh_keys'
#
```
Note: the above error only happens on the first run.  Then /var/cfengine/inputs/ssh_keys
is created and this error does not recur.

The local cache now contains the users' public keys:

```
ls /var/cfengine/inputs/ssh_keys/
user1.pub
user2.pub
#
```

CFEngine created authorized_keys files:

```
# ls /home/user?/.ssh/auth*keys
/home/user1/.ssh/authorized_keys
/home/user2/.ssh/authorized_keys
#
```

CFEngine installed the user's keys:

```
# more /home/user?/.ssh/auth*keys
::::::::::::::
/home/user1/.ssh/authorized_keys
::::::::::::::
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCjtmJf9QfME2KIV19C96EyRg1dizxKMTjLRsPtwsmC2fRyA3fRFvpUVKApigDTNxF5nDqfgGtY9
0KhnuqjhOgYWnpm4dmiTdFXJ5XHuNPCc4JpsXBeyMy2f8e1aobb/dN5UhSSZmYb84FkYwbI/EkxJ46CmmOpOi6C5AjYfqwzshIGNgJS39hbtsUimc
qBAOYTHzVpm5+KfHbNryZ9ORWEVcPvnchKtEfNu8iuDdecOxmWWUPhEyhUz7/SfZ4cPs7692JcIX2XQCsvsGWS5JPiVXGDPCcLz7WNI2A7rohoC9f
vpE11CBigl7zTlB0M7nQYzpjaf7qS3AvOXw5CLUPD user1@examplehost
::::::::::::::
/home/user2/.ssh/authorized_keys
::::::::::::::
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDhaBkZg7t63kNXqduU1LzLH+8DEkTGAhOjharGf6TMWL9fkWXS+Xjj2iD7KZgT2VBC9Hf8o+HhL
al5kyHYH8qRxtPXMm5UVhIHnq8hxDQQPo/jW62wwxB0N2pF8oU4sMzMzCANJYE3C6H0rjIzgloiCIkBwL21WoFhxZ145z7VoKTEf0ICRk2+xmCc2W
hX1pQVJzs5GlKlWEsJUp8Skqt+OuJTtIS4R3nJALvo7zindvum12DcbWfsrV5oW3gl89GkyDAdi1mWaqBmGX5qF5b19KaP4qdth61foUTR7NyHuCs
C/hNB84Loy+2nMU8QpKJ7Ha6UyBtU2YrzDxL3YPgJ user2@examplehost
#
```
