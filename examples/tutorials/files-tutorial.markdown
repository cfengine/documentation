---
layout: default
title: Create, Modify, and Delete Files
sorting: 10
published: true
tags: [Examples, Tutorials]
---

## Prerequisites ##

* Read the tutorial [Tutorial for Running Examples][Examples and Tutorials#Tutorial for Running Examples]
* Ensure you have read and understand the section on [how to make an example stand alone][Examples and Tutorials#Make the Example Stand Alone]
* Ensure you have read the note at the end of that section regarding modification of the body common control to the following:

```cf3
body common control {

    inputs => {
       "libraries/cfengine_stdlib.cf",
    };
}
```

Note: This change is not necessary for supporting each of the examples in this tutorial. It will be included only in those examples that require it.

## List Files ##

Note: The following workflow assumes the directory /home/user already exists. If it does not either create the directory or adjust the example to a path of your choosing.

1. Create a file /var/cfengine/masterfiles/file_test.cf that includes the following text:

	```cf3

	bundle agent list_file
	{

	  vars:
		  "ls" slist => lsdir("/home/user","test_plain.txt","true");

	  reports:
		  "ls: $(ls)";

	}
	```

2. Run the following command to remove any existing test file at the location we wish to use for testing this example:

	```console
	rm /home/user/test_plain.txt
	```

3. Test to ensure there is no file /home/user/test_plain.txt, using the following command (the expected result is that there should be no file listed at the location /home/user/test_plain.txt):

	```console
	ls /home/user/test_plain.txt
	```

5. Run the following command to instruct CFEngine to see if the file exists (the expected result is that no report will be generated (because the file does not exist):

	```console
	/var/cfengine/bin/cf-agent --no-lock --file /var/cfengine/masterfiles/file_test.cf --bundlesequence list_file
	```

6. Create a file for testing the example, using the following command:

	```console
	touch /home/user/test_plain.txt
	```

7. Run the following command to instruct CFEngine to search for the file (the expected result is that a report will be generated, because the file exists):

	```console
	/var/cfengine/bin/cf-agent --no-lock --file /var/cfengine/masterfiles/file_test.cf --bundlesequence list_file
	```

8. Double check the file exists, using the following command (the expected result is that there will be a file listed at the location /home/user/test_plain.txt):

	```console
	ls /home/user/test_plain.txt
	```

9. Run the following command to remove the file:

	```console
	rm /home/user/test_plain.txt
	```

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

## Copy a File and Edit its Text##

```cf3

body common control {

    inputs => {
       "libraries/cfengine_stdlib.cf",
    };
}

bundle agent testbundle
{

  files:
      "/home/ichien/test_plain.txt"
      perms => system,
      create => "true";

  reports:
    "test_plain.txt has been created";
}

bundle agent test_delete
{

  files:
      "/home/ichien/test_plain.txt"
      delete => tidy;
}

bundle agent do_files_exist

{
  vars:

      "mylist" slist => { "/home/ichien/test_plain.txt", "/home/ichien/test_plain_2.txt" };

  classes:

      "exists" expression => filesexist("@(mylist)");

  reports:

    exists::

      "test_plain.txt and test_plain_2.txt files exist";

    !exists::

      "test_plain.txt and test_plain_2.txt files do not exist";
}



bundle agent do_files_exist_2

{
  vars:

      "mylist" slist => { "/home/ichien/test_plain.txt", "/home/ichien/test_plain_2.txt" };

  classes:

      "exists" expression => filesexist("@(mylist)");

  reports:

    exists::

      "test_plain.txt and test_plain_2.txt files both exist";

    !exists::

      "test_plain.txt and test_plain_2.txt files do not exist";
}



bundle agent list_file_1
{

  vars:
      "ls1" slist => lsdir("/home/ichien","test_plain.txt","true");
      "ls2" slist => lsdir("/home/ichien","test_plain_2.txt","true");

      "file_content_1" string => readfile( "/home/ichien/test_plain.txt" , "33" );
      "file_content_2" string => readfile( "/home/ichien/test_plain_2.txt" , "33" );
  reports:
      #"ls1: $(ls1)";
      #"ls2: $(ls2)";

      "Contents of /home/ichien/test_plain.txt = $(file_content_1)";
      "Contents of /home/ichien/test_plain_2.txt = $(file_content_2)";
}


bundle agent list_file_2
{

  vars:
      "ls1" slist => lsdir("/home/ichien","test_plain.txt","true");
      "ls2" slist => lsdir("/home/ichien","test_plain_2.txt","true");
      "file_content_1" string => readfile( "/home/ichien/test_plain.txt" , "33" );
      "file_content_2" string => readfile( "/home/ichien/test_plain_2.txt" , "33" );

  reports:
      #"ls1: $(ls1)";
      #"ls2: $(ls2)";
      "Contents of /home/ichien/test_plain.txt = $(file_content_1)";
      "Contents of /home/ichien/test_plain_2.txt = $(file_content_2)";

}

bundle agent outer_bundle_1
{
    files:

       "/home/ichien/test_plain.txt"
       create    => "false",
       edit_line => inner_bundle_1;
}

# Copies file
bundle agent copy_a_file
{
  files:

      "/home/ichien/test_plain_2.txt"
      copy_from => local_cp("/home/ichien/test_plain.txt");

  reports:
     "test_plain.txt has been copied to test_plain_2.txt";
}

bundle agent outer_bundle_2
{
    files:

       "/home/ichien/test_plain_2.txt"
       create    => "false",
       edit_line => inner_bundle_2;
}


bundle edit_line inner_bundle_1
{
  vars:

    "msg" string => "Helloz to World!";

  insert_lines:
    "$(msg)";

  reports:
    "inserted $(msg) into test_plain.txt";

}

bundle edit_line inner_bundle_2
{
   replace_patterns:

   "Helloz to World!"
      replace_with => hello_world;

   reports:
      "Text in test_plain_2.txt has been replaced";

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

```console
/var/cfengine/bin/cf-agent --no-lock --file ./file_test.cf --bundlesequence test_delete,do_files_exist,testbundle,outer_bundle_1,copy_a_file,do_files_exist_2,list_file_1,outer_bundle_2,list_file_2
```