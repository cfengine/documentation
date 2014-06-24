---
layout: default
title: Create, Modify, and Delete Files
sorting: 10
published: false
tags: [Examples, Tutorials]
---

## List Files ##

```cf3
bundle agent list_file
{

  vars:
      "ls" slist => lsdir("/home/user","test_plain.txt","true");

  reports:
      "ls: $(ls)";

}
```

1. ls /home/user/test_plain.txt

/var/cfengine/bin/cf-agent --no-lock --file ./file_test.cf --bundlesequence list_file

touch /home/user/test_plain.txt

/var/cfengine/bin/cf-agent --no-lock --file ./file_test.cf --bundlesequence list_file

ls /home/user/test_plain.txt

rm /home/user/test_plain.txt


## Create a File ##

```cf3
bundle agent testbundle
{

  files:
      "/home/user/test_plain.txt"
      perms => system,
      create => "true";
}

bundle agent list_file
{

  vars:
      "ls" slist => lsdir("/home/user","test_plain.txt","true");

  reports:
      "ls: $(ls)";

}


bundle agent list_file_2
{

  vars:
      "ls" slist => lsdir("/home/user","test_plain.txt","true");

  reports:
      "ls: $(ls)";

}



body perms system
{
      mode  => "0640";
}
```

ls /home/user/test_plain.txt

/var/cfengine/bin/cf-agent --no-lock --file ./file_test.cf --bundlesequence list_file,testbundle,list_file_2

/var/cfengine/bin/cf-agent --no-lock --file ./file_test.cf --bundlesequence list_file,list_file_2

ls /home/user/test_plain.txt

rm /home/user/test_plain.txt


## Delete a File ##

```cf3
body common control {

    inputs => {
       "libraries/cfengine_stdlib.cf",
    };
}

bundle agent testbundle
{

  files:
      "/home/user/test_plain.txt"
      perms => system,
      create => "true";
}

bundle agent test_delete
{

  files:
      "/home/user/test_plain.txt"
      delete => tidy;
}


bundle agent list_file
{

  vars:
      "ls" slist => lsdir("/home/user","test_plain.txt","true");

  reports:
      "ls: $(ls)";

}


bundle agent list_file_2
{

  vars:
      "ls" slist => lsdir("/home/user","test_plain.txt","true");

  reports:
      "ls: $(ls)";

}



body perms system
{
      mode  => "0640";
}
```

rm /home/user/test_plain.txt

ls /home/user/test_plain.txt

/var/cfengine/bin/cf-agent --no-lock --file ./file_test.cf --bundlesequence list_file,testbundle,list_file_2

/var/cfengine/bin/cf-agent --no-lock --file ./file_test.cf --bundlesequence list_file,list_file_2

/var/cfengine/bin/cf-agent --no-lock --file ./file_test.cf --bundlesequence list_file,test_delete,list_file_2

ls /home/user/test_plain.txt

rm /home/user/test_plain.txt

(last command will throw an error because the file doesn't exist!)

## Modify a File ##

rm /home/user/test_plain.txt

ls /home/user/test_plain.txt

/var/cfengine/bin/cf-agent --no-lock --file ./file_test.cf --bundlesequence list_file,testbundle,list_file_2

/var/cfengine/bin/cf-agent --no-lock --file ./file_test.cf --bundlesequence list_file,list_file_2


```cf3
body common control {

    inputs => {
       "libraries/cfengine_stdlib.cf",
    };
}

bundle agent testbundle
{

  files:
      "/home/user/test_plain.txt"
      perms => system,
      create => "true";
}

bundle agent test_delete
{

  files:
      "/home/user/test_plain.txt"
      delete => tidy;
}


bundle agent list_file
{

  vars:
      "ls" slist => lsdir("/home/user","test_plain.txt","true");

  reports:
      "ls: $(ls)";

}


bundle agent list_file_2
{

  vars:
      "ls" slist => lsdir("/home/user","test_plain.txt","true");

  reports:
      "ls: $(ls)";

}

# Finds the file, if exists calls bundle to edit line

bundle agent outer_bundle_1
{
    files:

       "/home/user/test_plain.txt"
       create    => "false",
       edit_line => inner_bundle_1;
}

# Finds the file, if exists calls bundle to edit line

bundle agent outer_bundle_2
{
    files:

       "/home/user/test_plain.txt"
       create    => "false",
       edit_line => inner_bundle_2;
}

# Inserts lines

bundle edit_line inner_bundle_1
{
  vars:

    "msg" string => "Helloz to World!";

  insert_lines:
    "$(msg)";

}

# Replaces lines

bundle edit_line inner_bundle_2
{
   replace_patterns:

   "Helloz to World!"
      replace_with => hello_world;

}

body replace_with hello_world
{
   replace_value => "Hello World";
   occurrences => "all";
}


body perms system
{
      mode  => "0640";
}
```



/var/cfengine/bin/cf-agent --no-lock --file ./file_test.cf --bundlesequence list_file,test_delete,list_file_2

ls /home/user/test_plain.txt

rm /home/user/test_plain.txt
