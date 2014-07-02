---
layout: default
title: File Comparison
published: true
sorting: 100
tags: [examples, tutorials, file]
---

1. Add the [policy contents][File Comparison#Full Policy] to /var/cfengine/masterfiles/file_test.cf.
2. Run the following commands on the command line:

	```console
	export AOUT_BIN="a.out"
	export GCC_BIN="/usr/bin/gcc"
	export RM_BIN="/bin/rm"
	export WORK_DIR=$HOME
	export CFE_FILE1="test_plain_1.txt"
	export CFE_FILE2="test_plain_2.txt"

	/var/cfengine/bin/cf-agent --no-lock --file /var/cfengine/masterfiles/file_test.cf --bundlesequence global_vars,packages,create_aout_source_file,create_aout,test_delete,do_files_exist,testbundle,outer_bundle_1,copy_a_file,do_files_exist_2,list_file_1,stat,outer_bundle_2,list_file_2
	```

Here is the order in which bundles are called in the command line above (some other support bundles are contained within file_test.cf but are not included here):
	
1. **global_vars**

	Sets up some global variables that are used frequently by other bundles.
	
	```cf3
	bundle agent global_vars
	{	
		vars:

		  "gccexec" string => getenv("GCC_BIN",255);
		  "rmexec" string => getenv("RM_BIN",255);
		  
		  "aoutbin" string => getenv("AOUT_BIN",255);
		  "workdir" string => getenv("WORK_DIR",255);
		  
		  "aoutexec" string => "$(workdir)/$(aoutbin)";
		  
		  "file1name" string => getenv("CFE_FILE1",255);
		  "file2name" string => getenv("CFE_FILE2",255);
		  
		  "file1" string => "$(workdir)/$(file1name)";
		  "file2" string => "$(workdir)/$(file2name)";
		   
	}
	```
	
2. **packages**

	Ensures that the gcc package is installed, for later use by the create_aout bundle.
	
	```cf3
	bundle agent packages
	{
	  vars:

		  "match_package" slist => {
			"gcc"
		  };

	  packages:
		  "$(match_package)"
		  package_policy => "add",
		  package_method => yum;
		  
	}
	```
	
3. **create_aout_source_file**

	Creates the c source file that will generate a binary application in create_aout.
	
	```cf3
	bundle agent create_aout_source_file
	{

	  # This bundle creates the source file that will be compiled in bundle agent create_aout.
	  # See that bundle's comments for more information.
	  
	  vars:
	  
		# An slist is used here instead of a straight forward string because it doesn't seem possible to create
		# line endings using \n when using a string to insert text into a file.
		
		"c" slist => {"#include <stdlib.h>","#include <stdio.h>","#include <sys/stat.h>","void main()","{char file1[255];strcpy(file1,\"$(global_vars.file1)\");char file2[255];strcpy(file2,\"$(global_vars.file2)\");struct stat time1;int i = lstat(file1, &time1);struct stat time2;int j = lstat(file2, &time2);if (time1.st_mtime < time2.st_mtime){printf(\"Newer\");}else{if(time1.st_mtim.tv_nsec < time2.st_mtim.tv_nsec){printf(\"Newer\");}else{printf(\"Not newer\");}}}"};

	  files:
		  "$(global_vars.workdir)/a.c"
		  perms => system,
		  create => "true",
		  edit_line => Insert("@(c)");

	  reports:
		"$(global_vars.workdir)/a.c has been created";
		
	}
	```
	
4. **create_aout**

	This bundle creates a binary application from the source in  create_aout_source_file that uses the stat library to compare two files, determine if the modified times are different, nd whether the second file is newer than the first.
	
	The difference between this application and using CFEngine's built in support for getting file stats is that normally the accuracy is only to the second of the modified file time but in order to better compare two files requires parts of a second as well. The stat library provides the extra support for retrieving the additional information required.	
	
	```cf3
	bundle agent create_aout
	{

	  # This bundle creates a binary application from the source in  create_aout_source_file
	  # that uses the stat library to compare two files, determine if the modified times are different, 
	  # and whether the second file is newer than the first.
	  
	  # The difference between this application and using CFEngine's built in support for
	  # getting file stats is that normally the accuracy is only to the second of the modified file time
	  # but in order to better compare two files requires parts of a second as well. The stat library
	  # provides the extra support for retrieving the additional information required.
	  
	  vars:
		# Removes any previous binary
		"rmaout" string => execresult("$(global_vars.rmexec) $(global_vars.aoutexec)","noshell");
		"compilestr" string => "$(global_vars.gccexec) $(global_vars.workdir)/a.c -o $(global_vars.aoutexec)";
		"gccaout" string => execresult("$(compilestr)","noshell");
		
	  reports:
		  "rm output: $(rmaout)";
		  "gcc output: $(gccaout)";
		  "Creating aout using $(compilestr)";

	}
	```
	
5. **test_delete**

	Deletes any previous copy of the test files used in the example.
	
	```cf3
	bundle agent test_delete
	{

	  files:
		  "$(global_vars.file1)"
		  delete => tidy;
	}
	```
	
6. **do_files_exist**

	Verifies whether the test files exist or not.
	
	```cf3
	bundle agent do_files_exist
	{
	  vars:

		  "mylist" slist => { "$(global_vars.file1)", "$(global_vars.file2)" };

	  classes:

		  "exists" expression => filesexist("@(mylist)");

	  reports:

		exists::

		  "$(global_vars.file1) and $(global_vars.file2) files exist";

		!exists::

		  "$(global_vars.file1) and $(global_vars.file2) files do not exist";
		  
	}
	```
	
7. **testbundle**

	Creates the first test file, as an empty file.
	
	```cf3
	bundle agent testbundle
	{

	  files:
		  "$(global_vars.file1)"
		  perms => system,
		  create => "true";

	  reports:
		"$(global_vars.file1) has been created";
	}
	```
	
8. **outer_bundle_1**

	Adds some text to the first test file.
	
	```cf3
	bundle agent outer_bundle_1
	{
		files:

		   "$(global_vars.file1)"
		   create    => "false",
		   edit_line => inner_bundle_1;
	}
	```
	
9. **copy_a_file**

	Makes a copy of the test file.
	
	```cf3
	bundle agent copy_a_file
	{
	  files:

		  "$(global_vars.file2)"
		  copy_from => local_cp("$(global_vars.file1)");

	  reports:
		 "$(global_vars.file1) has been copied to $(global_vars.file2)";
	}
	```
	
10. **do_files_exist_2**

	Verifies that both test files exist.
	
	```cf3
	bundle agent do_files_exist_2
	{
	  vars:

		  "mylist" slist => { "$(global_vars.file1)", "$(global_vars.file2)" };
		  "file" string => "$(global_vars.file1)";
		  "file2" string => "$(global_vars.file2)";

		  "filestat1" string => filestat("$(global_vars.file1)","mtime");
		  "filestat2" string => filestat("$(global_vars.file2)","mtime");

	  classes:

		  "exists" expression => filesexist("@(mylist)");

	  reports:

		exists::

		  "$(global_vars.file1) and $(global_vars.file2) files both exist. $(global_vars.file1) Last Modified Time = $(filestat1). $(global_vars.file2) Last Modified Time = $(filestat2)";

		!exists::

		  "$(global_vars.file1) and $(global_vars.file2) files do not exist";
	}
	```
	
11. **list_file_1**

	Reports the contents of each test file.
	
	```cf3
	bundle agent list_file_1
	{

	  vars:
		  "ls1" slist => lsdir("$(global_vars.workdir)","$(global_vars.file1name)","true");
		  "ls2" slist => lsdir("$(global_vars.workdir)","$(global_vars.file2name)","true");

		  "file_content_1" string => readfile( "$(global_vars.file1)" , "0" );
		  "file_content_2" string => readfile( "$(global_vars.file2)" , "0" );
	  reports:
		  "Contents of $(global_vars.file1) = $(file_content_1). Contents of $(global_vars.file2) = $(file_content_2)";

	}
	```
	
12. **stat**

	Compares the modified time of each test file using the binary application compiled in create_aout to see if it is newer.
	
	```cf3
	bundle agent stat
	{

	  # This bundle uses the binary application stat to compare two files,
	  # determine if the modified times are different, and whether the second file is newer than
	  # the first. 
	  
	  # The difference between this application and using CFEngine's built in support for
	  # getting file stats is that normally the accuracy is only to the second of the modified file time
	  # but in order to better compare two files requires parts of a second as well. The stat command
	  # provides this additional information, but it must be extracted from the middle of a string.

	  vars:
		"file1" string => "$(global_vars.file1)";
		"file2" string => "$(global_vars.file2)";
		"aoutexec" string => getenv("AOUT_EXEC",255);

		"aout" string => execresult("$(aoutexec)","noshell");

		"file1_stat" string => execresult("/usr/bin/stat -c \"%y\" $(file1)","noshell");
		"file1_split1" slist => string_split($(file1_stat)," ",3);
		"file1_split2" string => nth("file1_split1",1);
		"file1_split3" slist => string_split($(file1_split2),"\.",3);
		"file1_split4" string => nth("file1_split3",1);

		"file2_stat" string => execresult("/usr/bin/stat -c \"%y\" $(file2)","noshell");
		"file2_split1" slist => string_split($(file2_stat)," ",3);
		"file2_split2" string => nth("file2_split1",1);
		"file2_split3" slist => string_split($(file2_split2),"\.",3);
		"file2_split4" string => nth("file2_split3",1);

	  commands:
		#"/bin/sleep 1";

	  reports:
		"$(file1_split4) $(file1_stat)";
		"$(file2_split4) $(file2_stat)";
		"Executable output: $(aout)";

	}
	```
	
13. **outer_bundle_2**

	Modifies the text in the second file.
	
	```cf3
	bundle agent outer_bundle_2
	{
		files:

		   "$(global_vars.file2)"
		   create    => "false",
		   edit_line => inner_bundle_2;
	}
	```
	
14. **list_file_2**

	Uses `filestat` and `isnewerthan` to compare the two test files to see if the second one is newer. Sometimes the modifications
	already performed, such as copy and modifying text, happen too quickly and filestat and isnewerthan may both report that the
	second test file is not newer than the first, while the more accurate stat based checks in the stat bundle (see step 12) will
	recognize the difference.
	
	```cf3
	bundle agent list_file_2
	{

	  vars:
		  "ls1" slist => lsdir("$(global_vars.workdir)","$(global_vars.file1name)","true");
		  "ls2" slist => lsdir("$(global_vars.workdir)","$(global_vars.file2name)","true");
		  "file_content_1" string => readfile( "$(global_vars.file1)" , "0" );
		  "file_content_2" string => readfile( "$(global_vars.file2)" , "0" );

		  "file3" string => filestat("$(global_vars.file2)","mtime");
		  "file4" string => filestat("$(global_vars.file2)","mtime");

	  classes:

		  "ok" expression => isgreaterthan($(file4),$(file3));
		  "newer" expression => isnewerthan("$(global_vars.file1)","$(global_vars.file2)");

	  reports:
		  "Contents of $(global_vars.file1) = $(file_content_1). Last Modified Time = $(file3). Contents of $(global_vars.file2) = $(file_content_2) Last Modified Time = $(file4)";

		  ok::
			 "Was modified later";

		  !ok::
			 "Was not modified later";
		  newer::
			 "Is newer";
		  !newer::
			 "Is not newer";

	}
	```
	
	
## Full Policy ##

```cf3
body common control {

    inputs => {
       "libraries/cfengine_stdlib.cf",
    };
	
}

bundle agent global_vars
{	
	vars:

	  "gccexec" string => getenv("GCC_BIN",255);
	  "rmexec" string => getenv("RM_BIN",255);
	  
	  "aoutbin" string => getenv("AOUT_BIN",255);
	  "workdir" string => getenv("WORK_DIR",255);
	  
	  "aoutexec" string => "$(workdir)/$(aoutbin)";
	  
	  "file1name" string => getenv("CFE_FILE1",255);
	  "file2name" string => getenv("CFE_FILE2",255);
	  
	  "file1" string => "$(workdir)/$(file1name)";
	  "file2" string => "$(workdir)/$(file2name)";
	   
}

bundle agent packages
{
  vars:

      "match_package" slist => {
        "gcc"
      };

  packages:
      "$(match_package)"
      package_policy => "add",
      package_method => yum;
	  
}

bundle agent create_aout_source_file
{

  # This bundle creates the source file that will be compiled in bundle agent create_aout.
  # See that bundle's comments for more information.
  
  vars:
  
    # An slist is used here instead of a straight forward string because it doesn't seem possible to create
	# line endings using \n when using a string to insert text into a file.
	
    "c" slist => {"#include <stdlib.h>","#include <stdio.h>","#include <sys/stat.h>","void main()","{char file1[255];strcpy(file1,\"$(global_vars.file1)\");char file2[255];strcpy(file2,\"$(global_vars.file2)\");struct stat time1;int i = lstat(file1, &time1);struct stat time2;int j = lstat(file2, &time2);if (time1.st_mtime < time2.st_mtime){printf(\"Newer\");}else{if(time1.st_mtim.tv_nsec < time2.st_mtim.tv_nsec){printf(\"Newer\");}else{printf(\"Not newer\");}}}"};

  files:
      "$(global_vars.workdir)/a.c"
      perms => system,
      create => "true",
      edit_line => Insert("@(c)");

  reports:
    "$(global_vars.workdir)/a.c has been created";
	
}

bundle edit_line Insert(name)
{
   insert_lines:
      "$(name)";
}

bundle agent create_aout
{

  # This bundle creates a binary application from the source in  create_aout_source_file
  # that uses the stat library to compare two files, determine if the modified times are different, 
  # and whether the second file is newer than the first.
  
  # The difference between this application and using CFEngine's built in support for
  # getting file stats is that normally the accuracy is only to the second of the modified file time
  # but in order to better compare two files requires parts of a second as well. The stat library
  # provides the extra support for retrieving the additional information required.
  
  vars:
    # Removes any previous binary
    "rmaout" string => execresult("$(global_vars.rmexec) $(global_vars.aoutexec)","noshell");
	"compilestr" string => "$(global_vars.gccexec) $(global_vars.workdir)/a.c -o $(global_vars.aoutexec)";
    "gccaout" string => execresult("$(compilestr)","noshell");
	
  reports:
	  "rm output: $(rmaout)";
	  "gcc output: $(gccaout)";
	  "Creating aout using $(compilestr)";

}

bundle agent test_delete
{

  files:
      "$(global_vars.file1)"
      delete => tidy;
}

bundle agent do_files_exist
{
  vars:

      "mylist" slist => { "$(global_vars.file1)", "$(global_vars.file2)" };

  classes:

      "exists" expression => filesexist("@(mylist)");

  reports:

    exists::

      "$(global_vars.file1) and $(global_vars.file2) files exist";

    !exists::

      "$(global_vars.file1) and $(global_vars.file2) files do not exist";
	  
}

bundle agent testbundle
{

  files:
      "$(global_vars.file1)"
      perms => system,
      create => "true";

  reports:
    "$(global_vars.file1) has been created";
}


bundle agent outer_bundle_1
{
    files:

       "$(global_vars.file1)"
       create    => "false",
       edit_line => inner_bundle_1;
}

# Copies file
bundle agent copy_a_file
{
  files:

      "$(global_vars.file2)"
      copy_from => local_cp("$(global_vars.file1)");

  reports:
     "$(global_vars.file1) has been copied to $(global_vars.file2)";
}

bundle agent do_files_exist_2

{
  vars:

      "mylist" slist => { "$(global_vars.file1)", "$(global_vars.file2)" };
      "file" string => "$(global_vars.file1)";
      "file2" string => "$(global_vars.file2)";

      "filestat1" string => filestat("$(global_vars.file1)","mtime");
      "filestat2" string => filestat("$(global_vars.file2)","mtime");

  classes:

      "exists" expression => filesexist("@(mylist)");

  reports:

    exists::

      "$(global_vars.file1) and $(global_vars.file2) files both exist. $(global_vars.file1) Last Modified Time = $(filestat1). $(global_vars.file2) Last Modified Time = $(filestat2)";

    !exists::

      "$(global_vars.file1) and $(global_vars.file2) files do not exist";
}

bundle agent list_file_1
{

  vars:
      "ls1" slist => lsdir("$(global_vars.workdir)","$(global_vars.file1name)","true");
      "ls2" slist => lsdir("$(global_vars.workdir)","$(global_vars.file2name)","true");

      "file_content_1" string => readfile( "$(global_vars.file1)" , "0" );
      "file_content_2" string => readfile( "$(global_vars.file2)" , "0" );
  reports:
      "Contents of $(global_vars.file1) = $(file_content_1). Contents of $(global_vars.file2) = $(file_content_2)";

}

bundle agent stat
{

  # This bundle uses the binary application stat to compare two files,
  # determine if the modified times are different, and whether the second file is newer than
  # the first. 
  
  # The difference between this application and using CFEngine's built in support for
  # getting file stats is that normally the accuracy is only to the second of the modified file time
  # but in order to better compare two files requires parts of a second as well. The stat command
  # provides this additional information, but it must be extracted from the middle of a string.

  vars:
    "file1" string => "$(global_vars.file1)";
    "file2" string => "$(global_vars.file2)";
    "aoutexec" string => getenv("AOUT_EXEC",255);

    "aout" string => execresult("$(aoutexec)","noshell");

    "file1_stat" string => execresult("/usr/bin/stat -c \"%y\" $(file1)","noshell");
    "file1_split1" slist => string_split($(file1_stat)," ",3);
    "file1_split2" string => nth("file1_split1",1);
    "file1_split3" slist => string_split($(file1_split2),"\.",3);
    "file1_split4" string => nth("file1_split3",1);

    "file2_stat" string => execresult("/usr/bin/stat -c \"%y\" $(file2)","noshell");
    "file2_split1" slist => string_split($(file2_stat)," ",3);
    "file2_split2" string => nth("file2_split1",1);
    "file2_split3" slist => string_split($(file2_split2),"\.",3);
    "file2_split4" string => nth("file2_split3",1);

  commands:
    #"/bin/sleep 1";

  reports:
    "$(file1_split4) $(file1_stat)";
    "$(file2_split4) $(file2_stat)";
    "Executable output: $(aout)";

}

bundle agent outer_bundle_2
{
    files:

       "$(global_vars.file2)"
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
    "inserted $(msg) into $(global_vars.file1)";

}

bundle edit_line inner_bundle_2
{
   replace_patterns:

   "Helloz to World!"
      replace_with => hello_world;

   reports:
      "Text in $(global_vars.file2) has been replaced";

}

body replace_with hello_world
{
   replace_value => "Hello World";
   occurrences => "all";
}

bundle agent list_file_2
{

  vars:
      "ls1" slist => lsdir("$(global_vars.workdir)","$(global_vars.file1name)","true");
      "ls2" slist => lsdir("$(global_vars.workdir)","$(global_vars.file2name)","true");
      "file_content_1" string => readfile( "$(global_vars.file1)" , "0" );
      "file_content_2" string => readfile( "$(global_vars.file2)" , "0" );

      "file3" string => filestat("$(global_vars.file2)","mtime");
      "file4" string => filestat("$(global_vars.file2)","mtime");

  classes:

      "ok" expression => isgreaterthan($(file4),$(file3));
      "newer" expression => isnewerthan("$(global_vars.file1)","$(global_vars.file2)");

  reports:
      "Contents of $(global_vars.file1) = $(file_content_1). Last Modified Time = $(file3). Contents of $(global_vars.file2) = $(file_content_2) Last Modified Time = $(file4)";

      ok::
         "Was modified later";

      !ok::
         "Was not modified later";
      newer::
         "Is newer";
      !newer::
         "Is not newer";

}

body perms system
{
      mode  => "0640";
}

```

