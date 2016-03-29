---
layout: default
title: User Management and ACL Examples
published: true
sorting: 15
tags: [Examples,User Management,ACL]
---

* [Manage users][User Management and ACL Examples#Manage users]
* [Add users][User Management and ACL Examples#Add users]
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


[%CFEngine_include_snippet(add_users.cf, .* )%]

A second approach is to use the shell commands supplied by some operating systems; this assumes that suitable defaults have been set up manually. Also the result is not repairable in a simple convergent manner. The command needs to edit multiple files for each user, and is quite inefficient.


[%CFEngine_include_snippet(add_users_1.cf, .* )%]

An alternative approach is to use a method to wrap around the handling of a user. Although this looks nice, it is less efficient than the first method because it must edit the files multiple times.


[%CFEngine_include_snippet(add_users_1.cf, .* )%]

## Add users to passwd and group ##

Add lines to the password file, and users to group if they are not already there.


[%CFEngine_include_snippet(add_users_to_passwd_and_group.cf, .* )%]

## ACL file example


[%CFEngine_include_snippet(acl_file_example.cf, .* )%]

## ACL generic example


[%CFEngine_include_snippet(acl_generic_example.cf, .* )%]

## ACL secret example


[%CFEngine_include_snippet(acl_secret_example.cf, .* )%]

## Active directory example


[%CFEngine_include_snippet(active_directory_example.cf, .* )%]

## Active list users directory example


[%CFEngine_include_snippet(active_list_users_directory_example.cf, .* )%]

## Active directory show users example


[%CFEngine_include_snippet(active_directory_show_users_example.cf, .* )%]

## Get a list of users


[%CFEngine_include_snippet(get_a_list_of_users.cf, .* )%]

## LDAP interactions

[%CFEngine_include_snippet(ldap_interactions.cf, .* )%]
