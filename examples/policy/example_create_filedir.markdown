---
layout: default
title: Create files and directories
categories: [Examples, Policy, Create files and directories]
published: true
alias: examples-policy-create-files-and-directories.html
tags: [Examples, Policy, create, files and directories]
---

The following is a standalone policy that will create the file
`/home/mark/tmp/test_plain` and the directory `/home/mark/tmp/test_dir/`
and set permissions on both.

```cf3
body common control
{
bundlesequence  => { "example"  };
}


bundle agent example
{
files:

  "/home/mark/tmp/test_plain"  # Path and name of the file we wish to create

       perms => system,        # Set the permissions of the file as defined in the body "system" below
       create => "true";       # Make sure the file exists, create if not

  "/home/mark/tmp/test_dir/."  # Note the trailing "/." (this tells CFEngine it's a directory)

       perms => system,        # Set the permissions of the directory as defined in the body "system" below
       create => "true";       # Make sure the directory exists, create if not
}


body perms system
{
mode  => "0640";               # Set permissions to "0640"
}
```

This policy can be found in `/var/cfengine/share/doc/examples/unit_create_filedir.cf`.

Example output:

```
# cf-agent -f unit_create_filedir.cf -I
2013-06-08T14:56:26-0700     info: /example/files/'/home/mark/tmp/test_plain': Created file '/home/mark/tmp/test_plain', mode 0640
2013-06-08T14:56:26-0700     info: /example/files/'/home/mark/tmp/test_dir/.': Created directory '/home/mark/tmp/test_dir/.'
2013-06-08T14:56:26-0700     info: /example/files/'/home/mark/tmp/test_dir/.': Object '/home/mark/tmp/test_dir' had permission 0755, changed it to 0750
# 
```
