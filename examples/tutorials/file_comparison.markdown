---
layout: default
title: File Comparison
published: true
sorting: 100
tags: [examples, tutorials, file]
---

1. Add the [policy contents][File Comparison#Full Policy] (also can be downloaded from <a href="file_compare_test.cf">file_compare_test.cf</a>) to a new file, such as /var/cfengine/masterfiles/file_test.cf.
2. Run the following commands as root on the command line:

	```console
	export AOUT_BIN="a.out"
	export GCC_BIN="/usr/bin/gcc"
	export RM_BIN="/bin/rm"
	export WORK_DIR=$HOME
	export CFE_FILE1="test_plain_1.txt"
	export CFE_FILE2="test_plain_2.txt"

	/var/cfengine/bin/cf-agent /var/cfengine/masterfiles/file_test.cf --bundlesequence robot,global_vars,packages,create_aout_source_file,create_aout,test_delete,do_files_exist_1,create_file_1,outer_bundle_1,copy_a_file,do_files_exist_2,list_file_1,stat,outer_bundle_2,list_file_2

	```

Here is the order in which bundles are called in the command line above (some other support bundles are contained within file_test.cf but are not included here):

1. [robot][#robot] - demonstrates use of `reports`.
2. [global_vars][#global_vars] - sets up some global variables for later use.
3. [packages][#packages] - installs packages that will be used later on.
4. [create_aout_source_file][#create_aout_source_file] - creates a source file.
5. [create_aout][#create_aout] - compiles the source file.
6. [test_delete][#test_delete] - deletes a file.
7. [do_files_exist_1][#do_files_exist_1] - checks the existence of files.
8. [create_file_1][#create_file_1] - creates a file.
9. [outer_bundle_1][#outer_bundle_1] - adds text to a file.
10. [copy_a_file][#copy_a_file] - copies the file.
11. [do_files_exist_2][#do_files_exist_2] - checks the existence of both files.
12. [list_file_1][#list_file_1] - shows the contents of each file.
13. [stat][#stat] - uses the stat command and the aout application to compare modified times of both files.
14. [outer_bundle_2][#outer_bundle_2] - modifies the contents of the second file.
15. [list_file_2][#list_file_2] - shows the contents of both files and uses CFEngine functionality to compare the modified time for each file.

## robot ##

Demonstrates use of `reports`, using an ascii art representation of the CFEngine robot.
	
## global_vars ##

Sets up some global variables that are used frequently by other bundles.
	
```cf3
bundle common global_vars
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

	classes:
	  "gclass" expression => "any";

}
```
	
## packages ##

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

	  reports:

		gclass::
			"Package gcc installed";
			"*********************************";

	}
```
	
## create_aout_source_file ##

Creates the c source file that will generate a binary application in create_aout.
	
```cf3
bundle agent create_aout_source_file
{

  # This bundle creates the source file that will be compiled in bundle agent create_aout.
  # See that bunlde's comments for more information.

  vars:

	# An slist is used here instead of a straight forward string because it doesn't seem possible to create
	# line endings using \n when using a string to insert text into a file.

	"c" slist => {"#include <stdlib.h>","#include <stdio.h>","#include <sys/stat.h>","#include <string.h>","void main()","{char file1[255];strcpy(file1,\"$(global_vars.file1)\");char file2[255];strcpy(file2,\"$(global_vars.file2)\");struct stat time1;int i = lstat(file1, &time1);struct stat time2;int j = lstat(file2, &time2);if (time1.st_mtime < time2.st_mtime){printf(\"Newer\");}else{if(time1.st_mtim.tv_nsec < time2.st_mtim.tv_nsec){printf(\"Newer\");}else{printf(\"Not newer\");}}}"};

  files:
	  "$(global_vars.workdir)/a.c"
	  perms => system,
	  create => "true",
	  edit_line => Insert("@(c)");

  reports:
	"The source file $(global_vars.workdir)/a.c has been created. It will be used to compile the binary a.out, which will provide more accurate file stats to compare two files than the built in CFEngine functionality for comparing file stats, including modification time. This information will be used to determine of the second of the two files being compared is newer or not.";
	"*********************************";

}
```
	
## create_aout ##

This bundle creates a binary application from the source in  create_aout_source_file that uses the stat library to compare two files, determine if the modified times are different, nd whether the second file is newer than the first.
	
The difference between this application and using CFEngine's built in support for getting file stats is that normally the accuracy is only to the second of the modified file time but in order to better compare two files requires parts of a second as well. The stat library provides the extra support for retrieving the additional information required.	
	
```cf3
bundle agent create_aout
{

	classes:

	"doesfileacexist" expression => fileexists("$(global_vars.workdir)/a.c");
	"doesaoutexist" expression => fileexists("$(global_vars.aoutbin)");

  vars:

	# Removes any previous binary
	"rmaout" string => execresult("$(global_vars.rmexec) $(global_vars.aoutexec)","noshell");
	
	doesfileacexist::
	"compilestr" string => "$(global_vars.gccexec) $(global_vars.workdir)/a.c -o $(global_vars.aoutexec)";
	"gccaout" string => execresult("$(compilestr)","noshell");

  reports:
	doesfileacexist::
	  "gcc output: $(gccaout)";
	  "Creating aout using $(compilestr)";
	!doesfileacexist::
	  "Cannot compile a.out, $(global_vars.workdir)/a.c does not exist.";	
	doesaoutexist::
	  "The binary application aout has been compiled from the source in the create_aout_source_file bundle. It uses the stat library to compare two files, determine if the modified times are different, and whether the second file is newer than the first. The difference between this application and using CFEngine's built in support for getting file stats (e.g. filestat, isnewerthan), which provides file modification time accurate to a second. However, in order to better compare two files might sometimes require parts of a second as well. The stat library provides the extra support for retrieving the additional information required to get better accuracy (down to parts of a second), and is utilized by the binary application a.out that is compiled within the create_aout bundle.";
	  "*********************************";

}
```
	
## test_delete ##

Deletes any previous copy of the test files used in the example.
	
```cf3
bundle agent test_delete
{

  files:
	  "$(global_vars.file1)"
	  delete => tidy;
}
```
	
## do_files_exist_1 ##

Verifies whether the test files exist or not.
	
```cf3
bundle agent do_files_exist_1

{

  classes:

	"doesfile1exist" expression => fileexists("$(global_vars.file1)");
	"doesfile2exist" expression => fileexists("$(global_vars.file2)");

  methods:

	doesfile1exist::

	"any" usebundle => delete_file("$(global_vars.file1)");	
	doesfile2exist::
	"any" usebundle => delete_file("$(global_vars.file2)");	
  reports:

	!doesfile1exist::
	  "$(global_vars.file1) does not exist.";
	doesfile1exist::
	  "$(global_vars.file1) did exist. Call to delete it was made.";	
	
	!doesfile2exist::
	  "$(global_vars.file2) does not exist.";
	doesfile2exist::
	  "$(global_vars.file2) did exist. Call to delete it was made.";	

}
```
	
## create_file_1 ##

Creates the first test file, as an empty file.
	
```cf3
bundle agent create_file_1
{

  files:
	  "$(global_vars.file1)"
	  perms => system,
	  create => "true";

  reports:
	"$(global_vars.file1) has been created";
}
```
	
## outer_bundle_1 ##

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
	
## copy_a_file ##

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
	
## do_files_exist_2 ##

Verifies that both test files exist.
	
```cf3
bundle agent do_files_exist_2
{
	methods:

	"any" usebundle => does_file_exist($(global_vars.file1));
	"any" usebundle => does_file_exist($(global_vars.file2));
}
```
	
## list_file_1 ##

Reports the contents of each test file.
	
```cf3
bundle agent list_file_1
{

  methods:	
	"any" usebundle => file_content($(global_vars.file1));
	"any" usebundle => file_content($(global_vars.file2));
  reports:
	"*********************************";

}
```

## exec_aout ##

```cf3
bundle agent exec_aout
{

  classes:
	"doesaoutexist" expression => fileexists("$(global_vars.aoutbin)");

  vars:
	doesaoutexist::
	"aout" string => execresult("$(global_vars.aoutexec)","noshell");

  reports:
	doesaoutexist::
	"*********************************";
	"$(global_vars.aoutbin) determined that $(global_vars.file2) is $(aout) than $(global_vars.file1)";
	"*********************************";
	!doesaoutexist::
	"Executable $(global_vars.aoutbin) does not exist.";

}
```
	
## stat ##

Compares the modified time of each test file using the binary application compiled in create_aout to see if it is newer.
	
```cf3
bundle agent stat
{

  classes:

	"doesfile1exist" expression => fileexists("$(global_vars.file1)");
	"doesfile2exist" expression => fileexists("$(global_vars.file2)");

  vars:

	doesfile1exist::
	
	"file1" string => "$(global_vars.file1)";
	"file2" string => "$(global_vars.file2)";

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
	
  methods:

	  "any" usebundle => exec_aout();

  reports:
	doesfile1exist::
	  "Parts of a second extracted extracted from stat for $(file1): $(file1_split4). Full stat output for $(file1): $(file1_stat)";
	  "Parts of a second extracted extracted from stat for $(file2): $(file2_split4). Full stat output for $(file2): $(file2_stat)";
	  "Using the binary Linux application stat to compare two files can help determine if the modified times between two files are different. The difference between the stat application using its additional flags and using CFEngine's built in support for getting and comparing file stats (e.g. filestat, isnewerthan) is that normally the accuracy is only to the second of the file's modified time. In order to better compare two files requires parts of a second as well, which the stat command can provide with some additional flags. Unfortunately the information must be extracted from the middle of a string, which is what the stat bundle accomplishes using the string_split and nth functions.";
	  "*********************************";
	!doesfile1exist::
	  "stat: $(global_vars.file1) and probably $(global_vars.file2) do not exist.";

}
```
	
## outer_bundle_2 ##

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
	
## list_file_2 ##

Uses `filestat` and `isnewerthan` to compare the two test files to see if the second one is newer. Sometimes the modifications already performed, such as copy and modifying text, happen too quickly and filestat and isnewerthan may both report that the second test file is not newer than the first, while the more accurate stat based checks in the stat bundle (see step 12) will recognize the difference.
	
```cf3
bundle agent list_file_2
{
	
  methods:

	  "any" usebundle => file_content($(global_vars.file1));
	  "any" usebundle => file_content($(global_vars.file2));	

  classes:

	  "ok" expression => isgreaterthan(filestat("$(global_vars.file2)","mtime"),filestat("$(global_vars.file1)","mtime"));
	  "newer" expression => isnewerthan("$(global_vars.file2)","$(global_vars.file1)");

  reports:
	"*********************************";
	  ok::
		 "Using isgreaterthan+filestat determined that $(global_vars.file2) was modified later than $(global_vars.file1).";

	  !ok::
		 "Using isgreaterthan+filestat determined that $(global_vars.file2) was not modified later than $(global_vars.file1).";
	  newer::
		 "Using isnewerthan determined that $(global_vars.file2) was modified later than $(global_vars.file1).";
	  !newer::
		 "Using isnewerthan determined that $(global_vars.file2) was not modified later than $(global_vars.file1).";

}
```
	
	
## Full Policy ##

[%CFEngine_include_snippet(documentation/examples/tutorials/file_compare_test.cf, .* )%]

