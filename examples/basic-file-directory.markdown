---
layout: default
title: File and Directory Examples
published: true
sorting: 6
tags: [Examples,Files,Directories]
---

* [Create files and directories][File and Directory Examples#Create files and directories]
* [Copy single files][File and Directory Examples#Copy single files]
* [Copy directory trees][File and Directory Examples#Copy directory trees]
* [Disabling and rotating files][File and Directory Examples#Disabling and rotating files]
* [Add lines to a file][File and Directory Examples#Add lines to a file]
* [Check file or directory permissions][File and Directory Examples#Check file or directory permissions]
* [Commenting lines in a file][File and Directory Examples#Commenting lines in a file]
* [Copy files][File and Directory Examples#Copy files]
* [Copy and flatten directory][File and Directory Examples#Copy and flatten directory]
* [Copy then edit a file convergently][File and Directory Examples#Copy then edit a file convergently]
* [Creating files and directories][File and Directory Examples#Creating files and directories]
* [Deleting lines from a file][File and Directory Examples#Deleting lines from a file]
* [Deleting lines exception][File and Directory Examples#Deleting lines exception]
* [Editing files][File and Directory Examples#Editing files]
* [Editing tabular files][File and Directory Examples#Editing tabular files]
* [Inserting lines in a file][File and Directory Examples#Inserting lines in a file]
* [Back references in filenames][File and Directory Examples#Back references in filenames]
* [Add variable definitions to a file][File and Directory Examples#Add variable definitions to a file]
* [Linking files][File and Directory Examples#Linking files]
* [Listing files-pattern in a directory][File and Directory Examples#Listing files-pattern in a directory]
* [Locate and transform files][File and Directory Examples#Locate and transform files]
* [BSD flags][File and Directory Examples#BSD flags]
* [Search and replace text][File and Directory Examples#Search and replace text]
* [Selecting a region in a file][File and Directory Examples#Selecting a region in a file]
* [Warn if matching line in file][File and Directory Examples#Warn if matching line in file]
* Copy single files
* Create files and directories
* Change detection

## Create files and directories ##

Create files and directories and set permissions.

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

## Copy single files ##

Copy single files, locally (local_cp) or from a remote site (secure_cp). The Community Open Promise-Body Library (COPBL; cfengine_stdlib.cf) should be included in the /var/cfengine/inputs/ directory and input as below.

```cf3
body common control
{
bundlesequence  => { "mycopy" };
inputs => { "cfengine_stdlib.cf" };
}

bundle agent mycopy
{
files:

  "/home/mark/tmp/test_plain"

    copy_from => local_cp("$(sys.workdir)/bin/file");

  "/home/mark/tmp/test_remote_plain"

    copy_from => secure_cp("$(sys.workdir)/bin/file","serverhost");
}
```

## Copy directory trees ##

Copy directory trees, locally (local_cp) or from a remote site (secure_cp). (depth_search => recurse("")) defines the number of sublevels to include, ("inf") gets entire tree.

```cf3
body common control
{
bundlesequence  => { "my_recursive_copy" };
inputs => { "cfengine_stdlib.cf" };
}

bundle agent my_recursive_copy
{
files:

  "/home/mark/tmp/test_dir"

      copy_from => local_cp("$(sys.workdir)/bin/."),
   depth_search => recurse("inf");

  "/home/mark/tmp/test_dir"

      copy_from => secure_cp("$(sys.workdir)/bin","serverhost"),
   depth_search => recurse("inf");

}
```

## Disabling and rotating files ##

Use the following simple steps to disable and rotate files. See the Community Open Promise-Body Library if you wish more details on what disable and rotate does.

```cf3
body common control
{
bundlesequence  => { "my_disable" };
inputs => { "cfengine_stdlib.cf" };
}

bundle agent my_disable
{

files:

  "/home/mark/tmp/test_create"
      rename => disable;
 
 "/home/mark/tmp/rotate_my_log"
      rename => rotate("4");

}
```

## Add lines to a file ##

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

## Back references in filenames

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

## Add variable definitions to a file

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

## BSD flags ##

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