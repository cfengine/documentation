---
layout: default
title: files-in-agent-promises
categories: [Bundles-for-agent,files-in-agent-promises]
published: true
alias: Bundles-for-agent-files-in-agent-promises.html
tags: [Bundles-for-agent,files-in-agent-promises]
---

### `files` promises in agent

\

Files promises are an umbrella for attributes of files. Operations fall
basically into three categories: create, delete and edit.

~~~~ {.smallexample}
     
      files:
     
        "/path/file_object"
     
            perms = perms_body,
            ... ;
     
~~~~

Prior to version 3, file promises were scattered into many different
types, including `files`, `tidy`, `copy`, and `links`. File handling in
CFEngine 3 uses regular expressions everywhere for pattern matching. The
old \`wildcard/globbing' expressions \* and ? are deprecated, and
everything is based consistently on Perl Compatible Regular Expressions.

There is a natural ordering in file processing that obviates the need
for the actionsequence. For example, the trick of using multiple
actionsequence items with different classes.

~~~~ {.verbatim}
 actionsequence = ( ... files.one  ..  files.two )
~~~~

can now be handled more elegantly using bundles. The natural ordering
uses that fact that some operations are mutually exclusive and that some
operations do not make sense in reverse order. For example, editing a
file and then copying onto it would be nonsense. Similarly, you cannot
both remove a file and rename it.

**File copying**

One of the first things users of CFEngine 2 will notice is that copying
is now \`backwards'. Instead of the default object being source and the
option being the destination, in CFEngine 3 the destination is paramount
and the source is an option. This is because the model of voluntary
cooperation tells us that it is the object that is changed, which is the
agent making the promise. One cannot force change onto a destination
with CFEngine, one can only invite change from a source.

**Normal ordering of promise attributes**

CFEngine 3 no longer has an \`action sequence'. Ordering of operations
has, in most cases, a natural ordering that is assumed by the agent. For
example, \`delete then create' (normal ordering) makes sense, but
\`create then delete' does not. This sort of principle can be extended
to deal with all aspects of file promises.

The diagram below shows the ordering. Notice that the same ordering
applies regardless of file type (plain-file or directory). Note also
that file editing is done "atomically".

See: \`File editing in CFEngine 3'

![The normal ordering of file operators in CFEngine 3](filelogic.png)

The pseudo-code for this logic is shown in the diagram and below:

~~~~ {.verbatim}
 for each file promise-object
    {
    if (depth_search) 
      do 
        DepthSearch (HandleLeaf)
      else 
        (HandleLeaf)
      done
    }

 HandleLeaf()
   {
   Does leaf-file exist?

     NO:  create
     YES: rename,delete,touch, 

     do
      for all servers in {localhost, @(servers)}
         {
         if (server-will-provide)
            do
              if (depth_search)
                 embedded source-depth-search (use file source)
                 break
              else
                 (use file source)
                 break
              done
            done
         }
     done
      
   Do all links (always local)

   Check Permissions

   Do edits
   }
~~~~

**Depth searches (formerly known as 'recursion') during searches**

In CFEngine 2 there was the concept of recursion during file searches.
Recursion is now called "depth-search". In addition, it was possible to
specify wildcards in the base-path for this search. CFEngine 3 replaces
the \`globbing' symbols with standard regular expressions:

~~~~ {.verbatim}
      CFEngine 2               CFEngine 3

/one/*/two/thr*/four    /one/.*/two/thr.*/four
~~~~

Note: When searching for hidden files (files with names starting with a
\`.') or files with specific extensions, you should take care to escape
the dot (e.g., `\.cshrc` or `.*\.txt`) when you wish it to mean a
literal character and not the any character interpretation provided by
regular expression interpretation.

Note: When doing a recursive search, the files '.' and '..' are never
included in the matched files, even if the regular expression in the
leaf\_name specifically allows them.

Note: The filename /dir/ect/ory/. is a special case used with the create
attribute to indicate the directory named /dir/ect/ory and not any of
the files under it. If you really want to specify a regular expression
that matches any single-character filename, use /dir/ect/ory/[\\w\\W] as
your promise regular expression (you can't use /dir/ect/ory[\^/], see
below for an explanation.

Depth search refers to a search for file objects that starts from the
one or more matched base-paths as shown in the example above.

**Filenames and regular expressions**

CFEngine allows regular expressions within filenames, but only after
first doing some sanity checking to prevent some readily avoidable
problems. The biggest rule you need to know about filenames and regular
expressions is that *all* regular expressions in filenames are bounded
by directory separators, and that each component expression is anchored
between the directory separators. In other words, CFEngine splits up any
file paths into its component parts, and then it evaluates any regular
expressions at a component-level.

See: [Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions).

What this means is that the path /tmp/gar.\* will only match filenames
like /tmp/gar, /tmp/garbage and /tmp/garden. It will *not* match
filename like /tmp/gar/baz; because even though the .\* in a regular
expression means "zero or more of any character", CFEngine restricts
that to mean "zero or more of any character *in a path component*".

Correspondingly, CFEngine also restricts where you can use the /
character. For example, you cannot use it in a character class like
[\^/] or in a parenthesized or repeated regular expression component.

This means that regular expressions that include "optional directory
components" will not work. You cannot have a files promise to tidy the
directory (/usr)?/tmp. Instead, you need to be more verbose and specify
/usr/tmp|/tmp. Potentially more efficient would be a declarative
approach. First, create an *slist* that contains both the strings /tmp
and /usr/tmp; and then allow CFEngine to iterate over the list.

This also means that the path /tmp/.\*/something will match files such
as /tmp/abc/something or /tmp/xyzzy/something. However, even though the
pattern .\* means "zero or more of any character (except /)", CFEngine
matches files bounded by directory separators. So even though the
pathname /tmp//something is technically the same as the pathname
/tmp/something, the regular expression /tmp/.\*/something will *not*
match on the case of /tmp//something (or /tmp/something).

**Promises involving regular expressions**

CFEngine can only keep (or repair, or fail to keep) a promise on files
which actually exist. If you make a promise based on a wildcard match,
then the promise is only ever attempted if the match succeeds. However,
if you make a promise containing a recursive search that includes a
wildcard match, then the promise can be kept or repaired, provided that
the directory specified in the promise exists. Consider the following
two examples, which assumethat there first exist files named /tmp/gar,
/tmp/garbage and /tmp/garden. Initially, the two promises look like they
should do the same thing; but there is a subtle difference:

~~~~ {.verbatim}
bundle agent foobaz           bundle agent foobaz
{                   {
files:                  files:
 "/tmp/gar.*"                "/tmp"
    delete => tidy,             delete => tidy,
    classes => if_ok("done");           depth_search => recurse("0"),
                        file_select => gars,
                        classes => if_ok("done");
                    }

                    body file_select gars
                    {
                    leaf_name => { "gar.*" };
                    file_result => "leaf_name";
                    }

body classes if_ok(x)           body classes if_ok(x)
{                   {
promise_repaired => { "$(x)" };     promise_repaired => { "$(x)" };
promise_kept => { "$(x)" };     promise_kept => { "$(x)" };
}                   }
~~~~

In the first example, when the configuration containing this promise is
first executed, any file starting with "gar" that exists in the /tmp
directory will be removed, and the done class will be set. However, when
the configuration is executed a second time, the pattern /tmp/gar.\*
will not match any files, and that promise will not even be *attempted*
(and, consequently the done class will *not* be set).

In the second example, when the configuration containing this promise is
first executed, any file starting with "gar" that exists in the /tmp
directory will also be removed, and the done class will also be set. The
second time the configuration is executed, however, the promise on the
/tmp directory will still be executed (because /tmp of course still
exists), and the done class *will* be set, because all files matching
the file\_select attribute have been deleted from that directory.

**Local and remote searches**

There are two distinct kinds of depth search:

-   A local search over promiser agents.
-   A remote search over provider agents.

When we are *copying* or *linking* to a file source, it is the search
over the *remote* source that drives the content of a promise (the
promise is a promise to use what the remote source provides). In
general, the sources are on a different device to the images that make
the promises. For all other promises, we search over existing local
objects.

If we specify depth search together with copy of a directory, then the
implied remote source search is assumed, and it is made after the search
over local base-path objects has been made. If you mix complex promise
body operations in a single promise, this could lead to confusion about
the resulting behaviour, and a warning is issued. In general it is not
recommended to mix searches without a full understanding of the
consequences, but this might occasionally be useful.

Depth search is not allowed with `edit_line` promises.

**File editing in CFEngine 3**

CFEngine 2 assumed that all files were line-edited, because it was based
on Unix traditions. Since then many new file formats have emerged,
including XML. CFEngine 3 opens up the possibility for multiple models
of file editing. Line based editing still exists, but is now more
powerful and has been simplified compared with previous versions.

File editing is not just a single kind of promise but a whole range of
\`promises within files'. It is therefore not merely a body to a single
kind of promise, but a bundle of sub-promises. After all, inside each
file are new objects that can make promises, quite separate from files'
external attributes.

A typical file editing stanza has the elements in the following example:

~~~~ {.verbatim}
######################################################################
#
# File editing
#
######################################################################

body common control

{
version => "1.2.3";
bundlesequence  => { "outerbundle"  };
}

########################################################

bundle agent outerbundle

{
files:

  "/home/mark/tmp/cf3_test"

       create    => "true",     # Like autocreate in cf2
       edit_line => inner_bundle;
}

########################################################

bundle edit_line inner_bundle
  {
  vars:

   "who" string => "SysAdmin John"; # private variable in bundle

  insert_lines:
    "/* This file is maintained by CFEngine (see $(who) for details) */",
    location => first_line;
  
  replace_patterns:

   # replace shell comments with C comments

   "#(.*)"

      replace_with => C_comment,
     select_region => MySection("New section");

  reports:

    someclass::

      "This is file $(edit.filename)";
  }

########################################
# Bodies for the library ...
########################################

body replace_with C_comment

{
replace_value => "/* $(match.1) */"; # backreference
occurrences => "all";          # first, last all
}

########################################################

body select_region MySection(x)

{
select_start => "\[$(x)\]";
select_end => "\[.*\]";
}

########################################################

body location first_line

{
before_after => "before";
first_last => "first";
select_line_matching => ".*";
}

~~~~

There are several things to notice:

-   The line-editing promises are all convergent promises about patterns
    within the file. They have bodies, just like other attributes do and
    these allow us to make simple templates about file editing while
    extending the power of the basic primitives.
-   All file edits specified in a single `edit_line` bundle are handled
    "atomically". CFEngine edits files like this:
    -   CFEngine makes a copy of the file you you want to edit.
    -   CFEngine makes all the edits in the **copy** of the file. The
        filename is the same as your original file with the extension
        .cf-after-edit appended.
    -   After all edits are complete (the `delete_lines`, `field_edits`,
        `insert_lines`, and finally `replace_patterns` promises),
        CFEngine checks to see if the new file is the same as the
        original one. If there are no differences, the promises have
        converged, so it deletes the copy, and the original is left
        completely unmodified.
    -   If there are any differences, CFEngine makes a copy of your
        original file with the extension .cf-before-edit (so you always
        have the most recent backup available), and then renames the
        edited version to your original filename.

    Because file rename is an atomic operation (guaranteed by the
    operating system), any application program will either see the old
    version of the file or the new one. There is no "window of
    opportunity" where a partially edited file can be seen (unless an
    application intentionally looks for the .cf-after-edit file).
    Problems during editing (such as disk-full or permission errors) are
    likewise detected, and CFEngine will not rename a partial file over
    your original.
-   All pattern matching is through Perl Compatible Regular Expressions
-   Editing takes place within a marked region (which defaults to the
    whole file if not otherwise specified).
-   Search/replace functions now allow back-references.
-   The line edit model now contains a field or column model for dealing
    with tabular files such as Unix passwd and group files. We can now
    apply powerful convergent editing operations to single fields inside
    a table, to append, order and delete items from lists inside fields.
-   The special variable `$(edit.filename)` contains the name of the
    file being edited within an edit bundle.

In the example above, back references are used to allow conversion of
comments from shell-style to C-style.

Another example of files promises is to look for changes in files. The
following example reports on all recent changes to files in a directory
by maintaining the most recent version of the `md5` hash of the file
contents. Similar checks can be used to examine metadata or both the
contents and metadata, as well as using different difference checks. The
Community Edition only reports that changes were found, but Enterprise
versions of CFEngine can also report on what exactly the significant
changes were.

~~~~ {.verbatim}
bundle agent example
{
files:

  "/home/mark/tmp" -> "Security team"

       changes      => lay_a_tripwire,
       depth_search => recurse("inf"),
       action       => background;
}

#########################################################

body changes lay_a_tripwire

{
hash           => "md5";
report_changes => "content";
update         => "yes";
}
~~~~

\

-   [acl in files](#acl-in-files)
-   [changes in files](#changes-in-files)
-   [copy\_from in files](#copy_005ffrom-in-files)
-   [create in files](#create-in-files)
-   [delete in files](#delete-in-files)
-   [depth\_search in files](#depth_005fsearch-in-files)
-   [edit\_defaults in files](#edit_005fdefaults-in-files)
-   [edit\_line in files](#edit_005fline-in-files)
-   [edit\_template in files](#edit_005ftemplate-in-files)
-   [edit\_xml in files](#edit_005fxml-in-files)
-   [file\_select in files](#file_005fselect-in-files)
-   [link\_from in files](#link_005ffrom-in-files)
-   [move\_obstructions in files](#move_005fobstructions-in-files)
-   [pathtype in files](#pathtype-in-files)
-   [perms in files](#perms-in-files)
-   [rename in files](#rename-in-files)
-   [repository in files](#repository-in-files)
-   [touch in files](#touch-in-files)
-   [transformer in files](#transformer-in-files)

#### `acl` (body template)

**Type**: (ext body)

`aces`

**Type**: slist

**Allowed input range**:
`((user|group):[^:]+:[-=+,rwx()dtTabBpcoD]*(:(allow|deny))?)|((all|mask):[-=+,rwx()]*(:(allow|deny))?)`

**Synopsis**: Native settings for access control entry

**Example**:\
 \

~~~~ {.verbatim}
     
     body acl template
     
     {
     acl_method => "overwrite";
     acl_type => "posix";
     acl_directory_inherit => "parent";
     
     aces => { 
             "user:*:r(wwx),-r:allow", 
             "group:*:+rw:allow", 
             "mask:x:allow", 
             "all:r"
             };
     }
     
~~~~

**Notes**:\
 \

POSIX ACL are available in CFEngine Community starting with 3.4.0. NTFS
ACL are available with CFEngine Nova or above. Form of the permissions
is:

~~~~ {.smallexample}
                aces = {
                        "user:uid:mode[:perm_type]", ...,
                        "group:gid:mode[:perm_type]", ...,
                        "all:mode[:perm_type]"
                        };
~~~~

-   `user` indicates that the line applies to a user specified by the
    user identifier `uid`. `mode` is the permission mode string.
-   `group` indicates that the line applies to a group specified by the
    group identitfier `gid`. `mode` is the permission mode string.
-   `all` indicates that the line applies to every user. `mode` is the
    permission mode string.
-   `uid` is a valid user identifier for the system and cannot be empty.
    However, `uid` can be set to \* as a synonym for the entity that
    owns the file system object (e.g. user:\*:r).
-   `gid` is a valid group identifier for the system and cannot be
    empty. However, in some ACL types, `gid` can be set to \* to
    indicate a special group (e.g. in POSIX this refers to the file
    group).
-   `mode` is one or more strings `op`|`perms`|(`nperms`); a
    concatenation of `op`, `perms` and optionally (`nperms`) separated
    with commas (e.g. +rx,-w(s) ). `mode` is parsed from left to right.
-   `op` specifies the operation on any existing permissions, if the
    defined ACE already exists. `op` can be =, empty, + or -. = or empty
    sets the permissions to the ACE as stated. + adds and - removes the
    permissions from any existing ACE.
-   `nperms` (optional) specifies file system specific (native)
    permissions. Only valid if `acl_type` is defined. `nperms` will only
    be enforced if the file object is stored on a file system supporting
    the ACL type set in `acl_type`. For example, `nperms` will be
    ignored if `acl_type:``ntfs` and the object is stored on a file
    system not supporting NTFS ACLs. Valid values for `nperms` varies
    with different ACL types, and is defined in subsequent sections.
-   `perm_type` (optional) can be set to either `allow` or `deny`, and
    defaults to `allow`. `deny` is only valid if `acl_type` is set to an
    ACL type that support deny permissions. A `deny` ACE will only be
    enforced if the file object is stored on a file system supporting
    the acl type set in `acl_type`.

`gperms` (generic permissions) is a concatenation of zero or more of the
characters shown in the table below. If left empty, none of the
permissions are set.

Flag

Description

Semantics on file

Semantics on directory

\

`r`

Read

Read data, permissions, attributes

Read directory contents, permissions, attributes \

`w`

Write

Write data

Create, delete, rename subobjects \

`x`

Execute

Execute file

Access subobjects \

Note that the `r` permission is not necessary to read an object's
permissions and attributes in all file systems. For example, in POSIX,
having `x` on its containing directory is sufficient. \

`acl_directory_inherit`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    nochange
                    parent
                    specify
                    clear
~~~~

**Synopsis**: Access control list type for the affected file system

**Example**:\
 \

~~~~ {.verbatim}
     
     body acl template
     
     {
     acl_method => "overwrite";
     acl_type => "posix";
     acl_directory_inherit => "parent";
     
     aces => {
             "user:*:rwx:allow",
             "group:*:+rw:allow",
             "mask:rx:allow",
             "all:r"
             };
     }
     
~~~~

**Notes**:\
 \

Directories have ACLs associated with them, but they also have the
ability to inherit an ACL to sub-objects created within them. POSIX
calls the former ACL type "access ACL" and the latter "default ACL", and
we will use the same terminology.

The constraint `acl_directory_inherit` gives control over the default
ACL of directories. The default ACL can be left unchanged (`nochange`),
empty (`clear`), or be explicitly specified (`specify`). In addition,
the default ACL can be set equal to the directory's access ACL
(`parent`). This has the effect that child objects of the directory gets
the same access ACL as the directory. \

`acl_method`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    append
                    overwrite
~~~~

**Synopsis**: Editing method for access control list

**Example**:\
 \

~~~~ {.verbatim}
     
     body acl template
     
     {
     acl_method => "overwrite";
     acl_type => "posix";
     aces => { "user:*:rw:allow", "group:*:+r:allow", "all:"};
     }
     
~~~~

**Notes**:\
 \

When defining an ACL, we can either use an existing ACL as the starting
point, or state all entries of the ACL. If we just care about one entry,
say that the superuser has full access, the `method` constraint can be
set to `append`, which is the default. This has the effect that all the
existing ACL entries that are not mentioned will be left unchanged. On
the other hand, if `method` is set to `overwrite`, the resulting ACL
will only contain the mentioned entries. When doing this, it is
important to check that all the required ACL entries are set. For
example, owning user, group and all in POSIX ACLs. \

`acl_type`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    generic
                    posix
                    ntfs
~~~~

**Synopsis**: Access control list type for the affected file system

**Example**:\
 \

~~~~ {.verbatim}
     
     body acl template
     
     {
     acl_type => "ntfs";
     aces => { "user:Administrator:rwx(po)", "user:Auditor:r(o)"};
     }
     
~~~~

**Notes**:\
 \

ACLs are supported on multiple platforms, which may have different sets
of available permission flags. By using the constraint `acl_type`, we
can specify which platform, or ACL API, we are targeting with the ACL.
The default, `generic`, is designed to work on all supported platforms.
However, if very specific permission flags are required, like Take
Ownership on the NTFS platform, we must set `acl_type` to indicate the
target platform. Currently, the supported values are `posix` and `ntfs`.
\

`specify_inherit_aces`

**Type**: slist

**Allowed input range**:
`((user|group):[^:]+:[-=+,rwx()dtTabBpcoD]*(:(allow|deny))?)|((all|mask):[-=+,rwx()]*(:(allow|deny))?)`

**Synopsis**: Native settings for access control entry

**Example**:\
 \

~~~~ {.verbatim}
     body acl template
     {
     specify_inherit_aces => {  "all:r" };
     }
~~~~

**Notes**:\
 \

`specify_inherit_aces` (optional) is a list of access control entries
that are set on child objects. It is also parsed from left to right and
allows multiple entries with same entity-type and id. Only valid if
`acl_directory_inherit` is set to `specify`.

This is an ACL which makes explicit setting for the acl inherited by new
objects within a directory. It is included for those implementations
that do not have a clear inheritance policy.

#### `changes` (body template)

**Type**: (ext body)

`hash`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    md5
                    sha1
                    sha224
                    sha256
                    sha384
                    sha512
                    best
~~~~

**Synopsis**: Hash files for change detection

**Example**:\
 \

~~~~ {.verbatim}
     
     body changes example
     {
     hash => "md5";
     }
     
~~~~

**Notes**:\
 \

The `best` option cross correlates the best two available algorithms
known in the OpenSSL library. \

`report_changes`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    all
                    stats
                    content
                    none
~~~~

**Synopsis**: Specify criteria for change warnings

**Example**:\
 \

~~~~ {.verbatim}
     
     body changes example
     {
     report_changes => "content";
     }
     
~~~~

**Notes**:\
 \

Files can change in permissions and contents, i.e. external or internal
attributes. If all is chosen all attributes are checked. \

`update_hashes`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: Update hash values immediately after change warning

**Example**:\
 \

~~~~ {.verbatim}
     
     body changes example
     {
     update_hashes => "true";
     }
     
~~~~

**Notes**:\
 \

If this is positive, file hashes should be updated as soon as a change
is registered so that multiple warnings are not given about a single
change. This applies to addition and removal too. \

`report_diffs`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: Generate reports summarizing the major differences between
individual text files

**Example**:\
 \

~~~~ {.verbatim}
     
     body changes example
     {
     report_diffs => "true";
     }
     
~~~~

**Notes**:\
 \

*This feature is available only in enterprise levels Nova and above.*

If true, CFEngine will log a \`diff' summary of major changes to the
files. It is not permitted to combine this promise with a depth search,
since this would consume a dangerous amount of resources and would lead
to unreadable reports.

The feature is intended as a informational summary, not as a version
control function suitable for transaction control. If you want to do
versioning on system files, you should keep a single repository for them
and use CFEngine to synchronize changes from the repository source.
Repositories should not be used to attempt to capture random changes of
the system.

#### `copy_from` (body template)

**Type**: (ext body)

`source`

**Type**: string

**Allowed input range**: `.+`

**Synopsis**: Reference source file from which to copy

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from example
     {
     source => "/path/to/source";
     }
     
     # or
     
     body link_from example
     {
     source => "/path/to/source";
     }
     
~~~~

**Notes**:\
 \

For remote copies this refers to the file name on the remote server. \

`servers`

**Type**: slist

**Allowed input range**: `[A-Za-z0-9_.:-]+`

**Synopsis**: List of servers in order of preference from which to copy

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from example
     {
     servers => { "primary.example.org", "secondary.example.org", 
                      "tertiary.other.domain" };
     }
     
~~~~

**Notes**:\
 \

The servers are tried in order until one of them succeeds. \

`collapse_destination_dir`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: Place files in subdirectories into the root destination
directory during copy

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from mycopy(from,server)
     
     {
     source      => "$(from)";
     servers     => { "$(server)" };
     collapse_destination_dir => "true";
     }
     
~~~~

**Notes**:\
 \

Under normal operations, recursive copies cause CFEngine to track
subdirectories of files. So, for instance, if we copy recursively from
src to dest, then src/subdir/file will map to dest/subdir/file.

By setting this option to true, the promiser destination directory
promises to aggregate files searched from all subdirectories into
itself; in other words, a single destination directory. \

`compare`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    atime
                    mtime
                    ctime
                    digest
                    hash
                    exists
                    binary
~~~~

**Synopsis**: Menu option policy for comparing source and image file
attributes

**Default value:** mtime or ctime differs

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from example
     
     {
     compare => "digest";
     }
     
~~~~

**Notes**:\
 \

The default copy method is mtime (modification time), meaning that the
source file is copied to the destination (promiser) file, if the source
file has been modified more recently than the destination.

The different options are:

-   `mtime` CFEngine copies the file if the modification time of the
    source file is more recent than that of the promised file
-   `ctime` CFEngine copies the file if the creation time of the source
    file is more recent than that of the promised file
-   `atime` CFEngine copies the file if the modification time or
    creation time of the source file is more recent than that of the
    promised file. If the times are equal, a byte-for-bye comparison is
    done on the files to determine if it needs to be copied.
-   `exists` CFEngine copies the file if the promised file does not
    already exist.
-   `binary` CFEngine copies the file if they are both plain files and a
    byte-for-byte comparison determines that they are different. If both
    are not plain files, CFEngine reverts to comparing the `mtime` and
    `ctime` of the files. If the source file is on a different machine
    (e.g. network copy), then `hash` is used instead to reduce network
    bandwidth.
-   `hash` CFEngine copies the file if they are both plain files and a
    message digest comparison indicates that the files are different. In
    Enterprise versions of CFEngine version 3.1.0 and later, SHA256 is
    used as a message digest hash to conform with FIPS; in older
    Enterprise versions of CFEngine and all Community versions, MD5 is
    used.
-   `digest` a synonym for `hash`

\

`copy_backup`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    timestamp
~~~~

**Synopsis**: Menu option policy for file backup/version control

**Default value:** true

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from example
     {
     copy_backup => "timestamp";
     }
     
~~~~

**Notes**:\
 \

Determines whether a backup of the previous version is kept on the
system. This should be viewed in connection with the system repository,
since a defined repository affects the location at which the backup is
stored.

See: [default\_repository](#default_005frepository-in-agent) and
[repository](#repository-in-files) for further details. \

`encrypt`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false use encrypted data stream to connect to remote
host

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from example
     {
     servers  => { "remote-host.example.org" };
     encrypt => "true";
     }
     
~~~~

**Notes**:\
 \

Client connections are encrypted with using a Blowfish randomly
generated session key. The initial connection is encrypted using the
public/private keys for the client and server hosts. \

`check_root`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false check permissions on the root directory when
depth\_search

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from example
     {
     check_root => "true";
     }
     
~~~~

**Notes**:\
 \

When copying files recursively (by depth search), this flag determines
whether the permissions of the root directory should be set from the
root of the source. The default is to check only copied file objects and
subdirectories within this root (false). \

`copylink_patterns`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of patterns matching files that should be copied
instead of linked

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from example
     {
     copylink_patterns => { "special_node1", "other_node.*" };
     }
     
~~~~

**Notes**:\
 \

The matches are performed on the last node of the filename; in other
words, the file without its path. As Windows does not support symbolic
links, this feature is not available there. \

`copy_size`

**Type**: irange [int,int]

**Allowed input range**: `0,inf`

**Synopsis**: Integer range of file sizes that may be copied

**Default value:** any size range

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from example
     {
     copy_size => irange("0","50000");
     } 
     
~~~~

**Notes**:\
 \

The use of the irange function is optional. Ranges may also be specified
as a comma separated numbers. \

`findertype`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    MacOSX
~~~~

**Synopsis**: Menu option for default finder type on MacOSX

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from example
     {
     findertype => "MacOSX";
     }
     
~~~~

**Notes**:\
 \

This applies only to the Mac OS X variants. \

`linkcopy_patterns`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of patterns matching files that should be replaced
with symbolic links

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from mycopy(from)
     
     {
     source            => "$(from)";
     linkcopy_patterns => { ".*" };
     }
     
~~~~

**Notes**:\
 \

The pattern matches the last node filename; in other words, without the
absolute path. Windows only supports hard links.

See: `link_type`. \

`link_type`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    symlink
                    hardlink
                    relative
                    absolute
~~~~

**Synopsis**: Menu option for type of links to use when copying

**Default value:** symlink

**Example**:\
 \

~~~~ {.verbatim}
     
     body link_from example
     {
     link_type => "symlink";
     source => "/tmp/source";
     }
     
~~~~

**Notes**:\
 \

Users are advised to be wary of \`hard links' (see Unix manual pages for
the ln command). The behaviour of non-symbolic links is often precarious
and unpredictable. However, hard links are the only supported type by
Windows.

Note that symlink is synonymous with absolute links, which are different
from relative links. Although all of these are symbolic links, the
nomenclature here is defined such that symlink and absolute are
equivalent . When verifying a link, choosing \`relative' means that the
link *must* be relative to the source, so relative and absolute links
are mutually exclusive. \

`force_update`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false force copy update always

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from example
     {
     force_update => "true";
     }
     
~~~~

**Notes**:\
 \

Warning: this is a non-convergent operation. Although the end point
might stabilize in content, the operation will never quiesce. Use of
this feature is not recommended except in exceptional circumstances
since it creates a busy-dependency. If the copy is a network copy, the
system will be disturbed by network disruptions. \

`force_ipv4`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false force use of ipv4 on ipv6 enabled network

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from example
     {
     force_ipv4 => "true";
     }
     
~~~~

**Notes**:\
 \

IPv6 should be harmless to most users unless you have a partially or
mis-configured setup. \

`portnumber`

**Type**: int

**Allowed input range**: `1024,99999`

**Synopsis**: Port number to connect to on server host

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from example
     {
     portnumber => "5308";
     }
     
~~~~

**Notes**:\
 \

The standard or registered port number is tcp/5308. CFEngine does not
presently use its registered udp port with the same number, but this
could change in the future. \

`preserve`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false whether to preserve file permissions on copied
file

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from example
     {
     preserve => "true";
     }
     
~~~~

**Notes**:\
 \

Ensures the destination file (promiser) gets the same Unix mode as the
source. This also applies to remote copies.

*History*: Was introduced in version 3.1.0b3,Nova 2.0.0b1 (2010) \

`purge`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false purge files on client that do not match files
on server when a depth\_search is used

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from example
     {
     purge => "true";
     }
     
~~~~

**Notes**:\
 \

Purging files is a potentially dangerous matter during a file copy it
implies that any promiser (destination) file which is not matched by a
source will be deleted. Since there is no source, this means the file
will be irretrievable. Great care should be exercised when using this
feature.

Note that purging will also delete backup files generated during the
file copying if `copy_backup` is set to true. \

`stealth`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false whether to preserve time stamps on copied file

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from example
     {
     stealth => "true";
     }
     
~~~~

**Notes**:\
 \

Preserves file access and modification times on the promiser files. \

`timeout`

**Type**: int

**Allowed input range**: `1,3600`

**Synopsis**: Connection timeout, seconds

**Example**:\
 \

~~~~ {.verbatim}
     
     body runagent control
     {
     timeout => "10";
     }
     
~~~~

**Notes**:\
 \

Timeout in seconds. \

`trustkey`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false trust public keys from remote server if
previously unknown

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from example
     {
     trustkey => "true";
     }
     
~~~~

**Notes**:\
 \

If the server's public key has not already been trusted, trustkey
provides automated key-exchange.

Note that, as a simple security precaution, trustkey should normally be
set to false. Even though the risks to the client low, it is a good
security practice to avoid key exchange with a server one is not one
hundred percent sure about. On the server-side however, trust is often
granted to many clients or to a whole network in which possibly
unauthorized parties might be able to obtain an IP address. Thus the
trust issue is most important on the server side.

As soon as a public key has been exchanged, the trust option has no
effect. A machine that has been trusted remains trusted until its key is
manually revoked by a system administrator. Keys are stored in
WORKDIR/ppkeys. \

`type_check`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false compare file types before copying and require
match

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from example
     {
     type_check => "false";
     }
     
~~~~

**Notes**:\
 \

File types at source and destination should normally match in order for
updates to overwrite them. This option allows this checking to be
switched off. \

`verify`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false verify transferred file by hashing after copy
(resource penalty)

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from example
     {
     verify => "true";
     }
     
~~~~

**Notes**:\
 \

This is a highly resource intensive option, not recommended for large
file transfers.

#### `create`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               true
               false
               yes
               no
               on
               off
~~~~

**Default value:** false

**Synopsis**: true/false whether to create non-existing file

**Example**:\
 \

~~~~ {.verbatim}
files:

  "/path/plain_file"

     create =>   "true";

  "/path/dir/."
  
     create =>   "true";
~~~~

**Notes**:\
 \

Directories are created by using the /. to signify a directory type.
Note that, if no permissions are specified, mode 600 is chosen for a
file, and mode 755 is chosen for a directory. If you cannot accept these
defaults, you *should* specify permissions.

Note that technically, /. is a regular expression. However, it is used
as a special case meaning "directory". See **filenames and regular
expressions** near the beginning of the section on [files
promises](#files-in-agent-promises) for a more complete discussion.

**Note:** In general, you should not use `create` with
[copy\_from](#copy_005ffrom-in-files) or
[link\_from](#link_005ffrom-in-files) in files promises. These latter
attributes automatically create the promised file, and using `create`
may actually prevent the copy or link promise from being kept (since
`create` acts first, which may affect file comparison or linking
operations).

#### `delete` (body template)

**Type**: (ext body)

`dirlinks`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    delete
                    tidy
                    keep
~~~~

**Synopsis**: Menu option policy for dealing with symbolic links to
directories during deletion

**Example**:\
 \

~~~~ {.verbatim}
     
     body delete example
     {
     dirlinks => "keep";
     }
     
~~~~

**Notes**:\
 \

Links to directories are normally removed just like any other link or
file objects. By keeping directory links, you preserve the logical
directory structure of the file system, so that a link to a directory is
not removed but is treated as a directory to be descended into.

The value `keep` instructs CFEngine not to remove directory links. The
values `delete` and `tidy` are synonymous, and instruct CFEngine to
remove directory links.

**Default value** (only if body is present):\
 \

The default value only has significance if there is a `delete` body
present. If there is no `delete` body then files (and directory links)
are **not** deleted.

`dirlinks = delete` \

`rmdirs`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false whether to delete empty directories during
recursive deletion

**Example**:\
 \

~~~~ {.verbatim}
     
     body delete example
     {
     rmdirs => "true";
     }
     
~~~~

**Notes**:\
 \

Note the parent directory of a search is not deleted in recursive
deletions. In CFEngine 2 there was an option to delete the parent of the
search. In CFEngine 3 you must code a separate promise to delete the
single parent object.

~~~~ {.verbatim}
     
     bundle agent cleanup
     {
     files:
     
       # This will not delete the parent
     
       "/home/mark/tmp/testcopy" 
     
         delete => tidyfiles,
         file_select => changed_within_1_year,
         depth_search => recurse("inf");
     
       # Now delete the parent.
     
       "/home/mark/tmp/testcopy" 
         delete => tidyfiles;
     }
     
     body delete tidyfiles
     {
     dirlinks => "delete";
     rmdirs   => "true";
     }
     
     body file_select changed_within_1_year
     {
     mtime     => irange(ago(1,0,0,0,0,0),now);
     file_result => "mtime";
     }
     
~~~~

**Default value** (only if body is present):\
 \

The default value only has significance if there is a `delete` body
present. If there is no `delete` body then files (and directories) are
**not** deleted.

`rmdirs = true`

#### `depth_search` (body template)

**Type**: (ext body)

`depth`

**Type**: int

**Allowed input range**: `0,99999999999`

**Synopsis**: Maximum depth level for search

**Example**:\
 \

~~~~ {.verbatim}
     
     body depth_search example
     {
     depth => "inf";
     }
     
~~~~

**Notes**:\
 \

This was previously called \`recurse' in earlier versions of CFEngine.
Note that the value inf may be used for an unlimited value.

When searching recursively from a directory, the parent directory is
only the anchor point and is not part of the search. To alter the
parent, a separate non-recursive promise should be made. \

`exclude_dirs`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: List of regexes of directory names NOT to include in depth
search

**Example**:\
 \

~~~~ {.verbatim}
     
     body depth_search
     {
     # no dot directories
     exclude_dirs => { "\..*" };
     }
     
~~~~

**Notes**:\
 \

Directory names are treated specially when searching recursively through
a file system. \

`include_basedir`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false include the start/root dir of the search
results

**Example**:\
 \

~~~~ {.verbatim}
     
     body depth_search example
     {
     include_basedir => "true";
     }
     
~~~~

**Notes**:\
 \

When checking files recursively (with `depth_search`) the promiser is a
directory. This parameter determines whether that initial directory
should be considered part of the promise or simply a boundary that marks
the edge of the search. If true, the promiser directory will also
promise the same attributes as the files inside it. \

`include_dirs`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: List of regexes of directory names to include in depth
search

**Example**:\
 \

~~~~ {.verbatim}
     
     body depth_search example
     {
     include_dirs => { "subdir1", "subdir2", "pattern.*" };
     }
     
~~~~

**Notes**:\
 \

This is the complement of `exclude_dirs`. \

`rmdeadlinks`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false remove links that point to nowhere

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body depth_search example
     {
     rmdeadlinks => "true";
     }
     
~~~~

**Notes**:\
 \

A value of true determines that links pointing to files that do not
exist should be deleted; or kept if set to false. \

`traverse_links`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false traverse symbolic links to directories

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body depth_search example
     {
     traverse_links => "true";
     }
     
~~~~

**Notes**:\
 \

If this is true, `cf-agent` will treat symbolic links to directories as
if they were directories. Normally this is considered a potentially
dangerous assumption and links are not traversed. \

`xdev`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false exclude directories that are on different
devices

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body depth_search example
     {
     xdev => "true";
     }
     
~~~~

**Notes**:\
 \

#### `edit_defaults` (body template)

**Type**: (ext body)

`edit_backup`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    timestamp
                    rotate
~~~~

**Synopsis**: Menu option for backup policy on edit changes

**Default value:** true

**Example**:\
 \

~~~~ {.verbatim}
     
     body edit_defaults example
     {
     edit_backup => "timestamp";
     }
     
~~~~

**Notes**:\
 \
 \

`empty_file_before_editing`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: Baseline memory model of file to zero/empty before
commencing promised edits

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body edit_defaults example
     {
     empty_file_before_editing => "true";
     }
     
~~~~

**Notes**:\
 \

Emptying a file before reconstructing its contents according to a fixed
recipe allows an ordered procedure to be convergent. \

`inherit`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: If true this causes the sub-bundle to inherit the private
classes of its parent

**Example**:\
 \

~~~~ {.verbatim}
     bundle agent name
     {
     methods:
     
       "group name" usebundle => my_method,
                      inherit => "true";
     }
     
     
     body edit_defaults example
     {
     inherit => "true";
     }
~~~~

**Notes**:\
 \

*History*: Was introduced in 3.4.0, Enterprise 3.0.0 (2012)

**Default value**: false

The `inherit` constraint can be added to the CFEngine code in two
places: for `edit_defaults` and in `methods` promises. If set to true,
it causes the child-bundle named in the promise to inherit only the
classes of the parent bundle. Inheriting the variables is unnecessary as
the child can always access the parent's variables by a qualified
reference using its bundle name. For example, \$(bundle.variable). \

`max_file_size`

**Type**: int

**Allowed input range**: `0,99999999999`

**Synopsis**: Do not edit files bigger than this number of bytes

**Example**:\
 \

~~~~ {.verbatim}
     
     body edit_defaults example
     {
     max_file_size => "50K";
     }
     
~~~~

**Notes**:\
 \

max\_file\_size is a local, per-file sanity check to make sure the file
editing is sensible. If this is set to zero, the check is disabled and
any size may be edited. The default value of `max_file_size` is
determined by the global control body setting whose default value is
`100k`.

See: [editfilesize in agent](#editfilesize-in-agent) \

`recognize_join`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: Join together lines that end with a backslash, up to 4kB
limit

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     files:
     
       "/tmp/test_insert"
                 create => "true",
              edit_line => Insert("$(insert.v)"),
          edit_defaults => join;
     }
     
     #
     
     body edit_defaults join
     {
     recognize_join => "true";
     }
~~~~

**Notes**:\
 \

If set to true, this option allows CFEngine to process line based files
with backslash continuation. The default is to not process continuation
backslashes.

Back slash lines will only be concatenated if the file requires editing,
and will not be restored. Restoration of the backslashes is not possible
in a meaningful and convergent fashion. \

`rotate`

**Type**: int

**Allowed input range**: `0,99`

**Synopsis**: How many backups to store if 'rotate' edit\_backup
strategy is selected. Defaults to 1

**Example**:\
 \

~~~~ {.verbatim}
     
     body rename example
     {
     rotate => "4";
     }
     
~~~~

**Notes**:\
 \

Used for log rotation. If the file is named foo and the rotate attribute
is set to 4, as above, then initially foo is copied to foo.1 and the old
file foo is zeroed out. In other words, the inode of the original
logfile does not change, but the original logfile will be empty after
the rotation is complete.

The next time the promise is executed, foo.1 will be renamed foo.2, foo
is again copied to foo.1 and the old file foo is again zeroed out.

A promise may typically be executed as guarded by time-based or
file-size-based classes. Each time the promise is executed the files are
copied/zeroed or rotated (as above) until there are rotate numbered
files, plus the one "main" file. In the example above, the file foo.3
will be renamed foo.4, but the old version of the file foo.4 will be
deleted (that is, it "falls off the end" of the rotation).

#### `edit_line`

**Type**: (ext bundle) (Separate Bundle)

#### `edit_template`

**Type**: string

**Allowed input range**: `"?(/.*)`

**Synopsis**: The name of a special CFEngine template file to expand

**Example**:\
 \

~~~~ {.verbatim}
#This is a template file /templates/input.tmpl

These lines apply to anyone

[%CFEngine solaris.Monday:: %]
Everything after here applies only to solaris on Mondays
until overridden...

[%CFEngine linux:: %]
Everything after here now applies now to linux only.

[%CFEngine BEGIN %]
This is a block of text
That contains list variables: $(some.list)
With text before and after.
[%CFEngine END %]

nameserver $(some.list)
~~~~

For example:

~~~~ {.verbatim}
[%CFEngine any:: %]
VirtualHost $(sys.ipv4[eth0]):80>
        ServerAdmin             $(stage_file.params[apache_mail_address][1])
        DocumentRoot            /var/www/htdocs
        ServerName              $(stage_file.params[apache_server_name][1])
        AddHandler              cgi-script cgi
        ErrorLog                /var/log/httpd/error.log
        AddType                 application/x-x509-ca-cert .crt
        AddType                 application/x-pkcs7-crl    .crl
        SSLEngine               off
        CustomLog               /var/log/httpd/access.log
/VirtualHost>

[%CFEngine webservers_prod:: %]
[%CFEngine BEGIN %]
VirtualHost $(sys.ipv4[$(bundle.interfaces)]):443>                                               
        ServerAdmin             $(stage_file.params[apache_mail_address][1]) 
        DocumentRoot            /var/www/htdocs                                  
        ServerName              $(stage_file.params[apache_server_name][1])            
        AddHandler              cgi-script cgi                                 
        ErrorLog                /var/log/httpd/error.log                  
        AddType                 application/x-x509-ca-cert .crt                
        AddType                 application/x-pkcs7-crl    .crl                
        SSLEngine               on                                             
        SSLCertificateFile      $(stage_file.params[apache_ssl_crt][1])
        SSLCertificateKeyFile   $(stage_file.params[apache_ssl_key][1])
        CustomLog               /var/log/httpd/access.log                      
/VirtualHost>
[%CFEngine END %]
~~~~

**Notes**:\
 \

*History*: Was introduced in 3.3.0, Nova 2.2.0 (2012)

The template format uses inline tags to mark regions and classes. Each
line represents an `insert_lines` promise, unless the promises are
grouped into a block using:

~~~~ {.verbatim}
[%CFEngine BEGIN %]
...
[%CFEngine END %]
~~~~

Variables, scalars and list variables are expanded within each promise.
If lines are grouped into a block, the whole block is repeated when
lists are expanded (see the Special Topics Guide on editing).

If a class-context modified is used:

~~~~ {.verbatim}
[%CFEngine class-expression:: %]
~~~~

then the lines that follow are only inserted if the context matches the
agent's current context. This allows conditional insertion.

#### `edit_xml`

**Type**: (ext bundle) (Separate Bundle)

#### `file_select` (body template)

**Type**: (ext body)

`leaf_name`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of regexes that match an acceptable name

**Example**:\
 \

~~~~ {.verbatim}
     
     body file_select example
     {
     leaf_name => { "S[0-9]+[a-zA-Z]+", "K[0-9]+[a-zA-Z]+" };
     file_result => "leaf_name";
     }
     
~~~~

**Notes**:\
 \

This pattern matches only the node name of the file, not its path. \

`path_name`

**Type**: slist

**Allowed input range**: `"?(/.*)`

**Synopsis**: List of pathnames to match acceptable target

**Example**:\
 \

~~~~ {.verbatim}
     
     body file_select example
     {
     leaf_name => { "prog.pid", "prog.log" };
     path_name => { "/etc/.*", "/var/run/.*" };
     
     file_result => "leaf_name.path_name"
     }
     
~~~~

**Notes**:\
 \

Path name and leaf name can be conveniently tested for separately by use
of appropriate regular expressions. \

`search_mode`

**Type**: slist

**Allowed input range**: `[0-7augorwxst,+-]+`

**Synopsis**: A list of mode masks for acceptable file permissions

**Example**:\
 \

~~~~ {.verbatim}
     
     #######################################################
     #
     # Searching for permissions
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
     
         file_select => by_modes,
         transformer => "/bin/echo DETECTED $(this.promiser)",
         depth_search => recurse("inf");
     
     }
     
     ############################################
     
     body file_select by_modes
     
     {
     search_mode => { "711" , "666" };
     file_result => "mode";
     }
     
     ############################################
     
     body depth_search recurse(d)
     
     {
     depth => "$(d)";
     }
     
~~~~

**Notes**:\
 \

The mode may be specified in symbolic or numerical form with + and -
constraints. Concatenation `ug+s` implies `u` OR `g`, and `u+g,u+s`
implies `u` AND `g`. \

`search_size`

**Type**: irange [int,int]

**Allowed input range**: `0,inf`

**Synopsis**: Integer range of file sizes

**Example**:\
 \

~~~~ {.verbatim}
     
     body file_select example
     {
     search_size => irange("0","20k");
     file_result => "size";
     }
     
~~~~

**Notes**:\
 \
 \

`search_owners`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of acceptable user names or ids for the file, or
regexes to match

**Example**:\
 \

~~~~ {.verbatim}
     
     body file_select example
     {
     search_owners => { "mark", "jeang", "student_.*" };
     file_result => "owner";
     }
     
~~~~

**Notes**:\
 \

A list of regular expressions any of which must match the entire userid
(see [Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). Windows
does not have user ids, only names. \

`search_groups`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of acceptable group names or ids for the file, or
regexes to match

**Example**:\
 \

~~~~ {.verbatim}
     
     body file_select example
     {
     search_groups => { "users", "special_.*" };
     file_result => "group";
     }
     
~~~~

**Notes**:\
 \

A list of regular expressions, any of which must match the entire group
(see [Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). On
Windows, files do not have group associations. \

`search_bsdflags`

**Type**: slist

**Allowed input range**:
`[+-]*[(arch|archived|nodump|opaque|sappnd|sappend|schg|schange|simmutable|sunlnk|sunlink|uappnd|uappend|uchg|uchange|uimmutable|uunlnk|uunlink)]+`

**Synopsis**: String of flags for bsd file system flags expected set

**Example**:\
 \

~~~~ {.verbatim}
     
     body file_select xyz
     {
     search_bsdflags => "archived|dump";
     file_result => "bsdflags";
     }
~~~~

**Notes**:\
 \

Extra BSD file system flags (these have no effect on non-BSD versions of
CFEngine). See the manual page for `chflags` for more details. \

`ctime`

**Type**: irange [int,int]

**Allowed input range**: `0,2147483647`

**Synopsis**: Range of change times (ctime) for acceptable files

**Example**:\
 \

~~~~ {.verbatim}
     
     body files_select example
     {
     ctime => irange(ago(1,0,0,0,0,0),now);
     file_result => "ctime";
     }
     
~~~~

**Notes**:\
 \

The file's change time refers to both modification of content and
attributes, such as permissions. On Windows, `ctime` refers to creation
time. \

`mtime`

**Type**: irange [int,int]

**Allowed input range**: `0,2147483647`

**Synopsis**: Range of modification times (mtime) for acceptable files

**Example**:\
 \

~~~~ {.verbatim}
     
     body files_select example
     
     {
     # Files modified more than one year ago (i.e., not in mtime range)
     mtime => irange(ago(1,0,0,0,0,0),now);
     file_result => "!mtime";
     }
     
~~~~

**Notes**:\
 \

The file's modification time refers to both modification of content but
not other attributes, such as permissions. \

`atime`

**Type**: irange [int,int]

**Allowed input range**: `0,2147483647`

**Synopsis**: Range of access times (atime) for acceptable files

**Example**:\
 \

~~~~ {.verbatim}
     body file_select used_recently
     {
     
     # files accessed within the last hour
     atime     => irange(ago(0,0,0,1,0,0),now);
     file_result => "atime";
     }
     
     
     body file_select not_used_much
     
     {
     # files not accessed since 00:00 1st Jan 2000 (in the local timezime)
     atime     => irange(on(2000,1,1,0,0,0),now);
     file_result => "!atime";
     }
     
~~~~

**Notes**:\
 \

A range of times during which a file was accessed can be specified in a
`file_select` body. This is similar to file filters in CFEngine 2. \

`exec_regex`

**Type**: string

**Allowed input range**: `.*`

**Synopsis**: Matches file if this regular expression matches any full
line returned by the command

**Example**:\
 \

~~~~ {.verbatim}
     
     body file_select example
     {
     exec_regex => "SPECIAL_LINE: .*";
     exec_program => "/path/test_program $(this.promiser)";
     file_result => "exec_program.exec_regex";
     }
     
~~~~

**Notes**:\
 \

The regular expression must be used in conjunction with the
`exec_program` test. In this way the program must both return exit
status 0 and its output must match the regular expression. The entire
output must be matched (see [Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). \

`exec_program`

**Type**: string

**Allowed input range**: `"?(/.*)`

**Synopsis**: Execute this command on each file and match if the exit
status is zero

**Example**:\
 \

~~~~ {.verbatim}
     
     body file_select example
     {
     exec_program => "/path/test_program $(this.promiser)";
     file_result => "exec_program";
     }
     
~~~~

**Notes**:\
 \

This is part of the customizable file search criteria. If the
user-defined program returns exit status 0, the file is considered
matched. \

`file_types`

**Type**: (option list)

**Allowed input range**: \

~~~~ {.example}
                    plain
                    reg
                    symlink
                    dir
                    socket
                    fifo
                    door
                    char
                    block
~~~~

**Synopsis**: List of acceptable file types from menu choices

**Example**:\
 \

~~~~ {.verbatim}
     
     body file_select filter
     {
     file_types => { "plain","symlink" };
     
     file_result => "file_types";
     }
     
~~~~

**Notes**:\
 \

File types vary in details between operating systems. The main POSIX
types are provided here as menu options, with reg being a synonym for
plain. In both cases this means not one of the "special" file types. \

`issymlinkto`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of regular expressions to match file objects

**Example**:\
 \

~~~~ {.verbatim}
     
     body file_select example
     {
     issymlinkto => { "/etc/[^/]*", "/etc/init\.d/[a-z0-9]*" };
     }
     
~~~~

**Notes**:\
 \

A list of regular expressions. If the file is a symbolic link that
points to files matched by one of these expressions, the file will be
selected. Windows does not support symbolic links, so this attribute is
not applicable on that platform. \

`file_result`

**Type**: string

**Allowed input range**:
`[!*(leaf_name|path_name|file_types|mode|size|owner|group|atime|ctime|mtime|issymlinkto|exec_regex|exec_program|bsdflags)[|.]*]*`

**Synopsis**: Logical expression combining classes defined by file
search criteria

**Example**:\
 \

~~~~ {.verbatim}
     
     body file_select year_or_less
     
     {
     mtime       => irange(ago(1,0,0,0,0,0),now);  
     file_result => "mtime"; 
     }
     
     body file_select my_pdf_files_morethan1dayold
     
     {
     mtime         => irange(ago(0,0,1,0,0,0),now);  
     leaf_name     => { ".*\.pdf" , ".*\.fdf" };
     search_owners => { "mark" };
     
     file_result => "owner.leaf_name.!mtime";
     }
     
~~~~

**Notes**:\
 \

Sets the criteria for file selection outcome during file searches. The
syntax is the same as for a class expression, since the file selection
is a classification of the file-search in the same way that system
classes are a classification of the abstract host-search. That is, you
may specify a boolean expression involving any of the file-matching
components. In this way, you may specify arbitrarily complex
file-matching parameters, such as what is shown above, "is owned by
mark, has the extension '.pdf' or '.fdf', and whose modification time is
not between 1 day ago and now"; that is, it is older than 1 day.

Items in the boolean expression in `file_result` must be from the
following list:

-   leaf\_name
-   path\_name
-   file\_types
-   mode
-   size
-   owner
-   group
-   atime
-   ctime
-   mtime
-   issymlinkto
-   exec\_regex
-   exec\_program
-   bsdflags

#### `link_from` (body template)

**Type**: (ext body)

`copy_patterns`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: A set of patterns that should be copied and synchronized
instead of linked

**Example**:\
 \

~~~~ {.verbatim}
     
     body link_from example
     {
     copy_patterns =>  { "special_node1", "/path/special_node2" };
     }
     
~~~~

**Notes**:\
 \

During the linking of files, it is sometimes useful to buffer changes
with an actual copy, especially if the link is to an ephemeral file
system. This list of patterns matches files that arise during a linking
policy. A positive match means that the file should be copied and
updated by modification time. \

`link_children`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false whether to link all directory's children to
source originals

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body link_from example
     {
     link_children => "true";
     }
     
~~~~

**Notes**:\
 \

If the promiser is a directory, instead of copying the children, link
them to the source. \

`link_type`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    symlink
                    hardlink
                    relative
                    absolute
~~~~

**Synopsis**: The type of link used to alias the file

**Default value:** symlink

**Example**:\
 \

~~~~ {.verbatim}
     
     body link_from example
     {
     link_type => "symlink";
     source => "/tmp/source";
     }
     
~~~~

**Notes**:\
 \

This determines what kind of link should be used to link files. Users
are advised to be wary of \`hard links' (see Unix manual pages for the
ln command). The behaviour of non-symbolic links is often precarious and
unpredictable. However, hard links are the only supported type by
Windows.

Note that symlink is synonymous with absolute links, which are different
from relative links. Although all of these are symbolic links, the
nomenclature here is defined such that symlink and absolute are
equivalent . When verifying a link, choosing \`relative' means that the
link *must* be relative to the source, so relative and absolute links
are mutually exclusive. \

`source`

**Type**: string

**Allowed input range**: `.+`

**Synopsis**: The source file to which the link should point

**Example**:\
 \

~~~~ {.verbatim}
     
     body copy_from example
     {
     source => "/path/to/source";
     }
     
     # or
     
     body link_from example
     {
     source => "/path/to/source";
     }
     
~~~~

**Notes**:\
 \

For remote copies this refers to the file name on the remote server. \

`when_linking_children`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    override_file
                    if_no_such_file
~~~~

**Synopsis**: Policy for overriding existing files when linking
directories of children

**Example**:\
 \

~~~~ {.verbatim}
     
     body link_from example
     {
     when_linking_children => "if_no_such_file";
     }
     
~~~~

**Notes**:\
 \

The options refer to what happens if the directory already exists, and
is already partially populated with files. If the directory being copied
from contains a file with the same name as that of a link to be created,
it must be decided whether to override the existing destination object
with a link, or simply omit the automatic linkage for files that already
exist. The latter case can be used to make a copy of one directory with
certain fields overridden. \

`when_no_source`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    force
                    delete
                    nop
~~~~

**Synopsis**: Behaviour when the source file to link to does not exist

**Default value:** nop

**Example**:\
 \

~~~~ {.verbatim}
     
     body link_from example
     {
     when_no_source => "force";
     }
     
~~~~

**Notes**:\
 \

This describes how CFEngine should respond to an attempt to create a
link to a file that does not exist. The options are to force the
creation to a file that does not (yet) exist, delete any existing link,
or do nothing.

#### `move_obstructions`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               true
               false
               yes
               no
               on
               off
~~~~

**Default value:** false

**Synopsis**: true/false whether to move obstructions to file-object
creation

**Example**:\
 \

~~~~ {.verbatim}
files:

  "/tmp/testcopy" 

    copy_from    => mycopy("/tmp/source"),
    move_obstructions => "true",
    depth_search => recurse("inf");
~~~~

**Notes**:\
 \

If we have promised to make file X a link, but it already exists as a
file, or vice-versa, or if a file is blocking the creation of a
directory, then normally CFEngine will report an error. If this is set,
existing objects will be moved aside to allow the system to heal without
intervention. Files and directories are saved/renamed, but symbolic
links are deleted.

Note that symbolic links for directories are treated as directories, not
links. This behaviour can be discussed, but the aim is to err on the
side of caution.

Some operating systems (Solaris) use symbolic links in path names.
Copying to a directory could then result in renaming of the important
link, if the behaviour is different.

#### `pathtype`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               literal
               regex
               guess
~~~~

**Synopsis**: Menu option for interpreting promiser file object

**Example**:\
 \

~~~~ {.verbatim}
files:

   "/var/lib\d"
      pathtype => "guess",  # best guess (default)
         perms => system;

   "/var/lib\d"
      pathtype => "regex",  # force regex interpretation
         perms => system;

   "/var/.*/lib"

      pathtype => "literal",    # force literal interpretation
         perms => system;
~~~~

**Notes**:\
 \
 By default, CFEngine makes an educated guess as to whether the promise
pathname involves a regular expression or not. This guesswork is needed
due to cross-platform differences in filename interpretation.

If CFEngine guesses (or is told) that the pathname uses a regular
expression pattern, it will undertake a file search to find possible
matches. This can consume significant resources, and so the guess option
will always try to optimize this. Guesswork is, however, imperfect, so
you have the option to declare your intention.

If the keyword `literal` is invoked, a path will be treated as a literal
string regardless of what characters it contains. If it is declared
regex, it will be treated as a pattern to match.

Note that CFEngine splits the promiser up into path links before
matching, so that each link in the path chain is matched separately.
Thus it it meaningless to have a / in a regular expression, as the
comparison will never see this character.

In the examples above, at least one case implies an iteration over all
files/directories matching the regular expression, while the last case
means a single literal object with a name composed of dots and stars.

On Windows paths using `regex` must use the forward slash (`/`) as path
separator, since the backward slash has a special meaning in a regular
expression. Literal paths may also use backslash (`\`) as a path
separator.

See [Regular expressions in paths](#Regular-expressions-in-paths), for
more information.

#### `perms` (body template)

**Type**: (ext body)

`bsdflags`

**Type**: slist

**Allowed input range**:
`[+-]*[(arch|archived|nodump|opaque|sappnd|sappend|schg|schange|simmutable|sunlnk|sunlink|uappnd|uappend|uchg|uchange|uimmutable|uunlnk|uunlink)]+`

**Synopsis**: List of menu options for BSD file system flags to set

**Example**:\
 \

~~~~ {.verbatim}
     
     body perms example
     
     {
     bsdflags => { "uappnd","uchg","uunlnk","nodump",
                   "opaque","sappnd","schg","sunlnk" };
     }
     
~~~~

**Notes**:\
 \

The BSD Unices (FreeBSD, OpenBSD, NetBSD) and MacOSX have additional
file system flags which can be set. Refer to the BSD `chflags`
documentation for this. \

`groups`

**Type**: slist

**Allowed input range**: `[a-zA-Z0-9_$.-]+`

**Synopsis**: List of acceptable groups of group ids, first is change
target

**Example**:\
 \

~~~~ {.verbatim}
     body perms example
     {
     groups => { "users", "administrators" };
     }
     
~~~~

**Notes**:\
 \

The first named group in the list is the default that will be configured
if the file does not match an element of the list. The reserved word
none may be used to match files that are not owned by a registered
group. On Windows, files do not have file groups associated with them,
and thus this attribute is ignored.

ACLs may be used in place for this. \

`mode`

**Type**: string

**Allowed input range**: `[0-7augorwxst,+-]+`

**Synopsis**: File permissions (like posix chmod)

**Example**:\
 \

~~~~ {.verbatim}
     
     body perms example
     {
     mode => "a+rx,o+w";
     }
     
~~~~

**Notes**:\
 \

The mode string may be symbolic or numerical, like `chmod`. This is
ignored on Windows, as the permission model uses ACLs. ACLs are
supported by CFEngine Nova. \

`owners`

**Type**: slist

**Allowed input range**: `[a-zA-Z0-9_$.-]+`

**Synopsis**: List of acceptable owners or user ids, first is change
target

**Example**:\
 \

~~~~ {.verbatim}
     
     body perms example
     {
     owners => { "mark", "wwwrun", "jeang" };
     }
     
~~~~

**Notes**:\
 \

The first user is the reference value that CFEngine will set the file to
if none of the list items matches the true state of the file. The
reserved word none may be used to match files that are not owned by a
registered user.

On Windows, users can only take ownership of files, never give it. Thus,
the first user in the list should be the user running the CFEngine
process (usually Administrator). Additionally, some groups may be owners
on Windows (such as the Administrators group). \

`rxdirs`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false add execute flag for directories if read flag
is set

**Example**:\
 \

~~~~ {.verbatim}
     
     body perms rxdirs
     {
     rxdirs => "false";
     }
     
~~~~

**Notes**:\
 \

Default behaviour is to set the x flag on directories automatically if
the r flag is specified when specifying multiple files in a single
promise. This is ignored on Windows, as the permission model uses ACLs.

#### `rename` (body template)

**Type**: (ext body)

`disable`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    true
                    false
                    yes
                    no
                    on
                    off
~~~~

**Synopsis**: true/false automatically rename and remove permissions

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body rename example
     {
     disable => "true"; 
     disable_suffix => ".nuked";
     }
     
~~~~

**Notes**:\
 \

Disabling a file means making it unusable. For executables this means
preventing execution, for an information file it means making the file
unreadable. \

`disable_mode`

**Type**: string

**Allowed input range**: `[0-7augorwxst,+-]+`

**Synopsis**: The permissions to set when a file is disabled

**Example**:\
 \

~~~~ {.verbatim}
     
     body rename example
     {
     disable_mode => "0600"; 
     }
     
~~~~

**Notes**:\
 \

To disable an executable it is not enough to rename it, you should also
remove the executable flag. \

`disable_suffix`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: The suffix to add to files when disabling (.cfdisabled)

**Example**:\
 \

~~~~ {.verbatim}
     
     body rename example
     {
     disable => "true"; 
     disable_suffix => ".nuked";
     }
     
~~~~

**Notes**:\
 \

To disable files in a particular manner, use this string suffix. The
default value is .cf-disabled. \

`newname`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: The desired name for the current file

**Example**:\
 \

~~~~ {.verbatim}
     
     body rename example(s)
     {
     newname => "$(s)";
     }
     
~~~~

**Notes**:\
 \
 \

`rotate`

**Type**: int

**Allowed input range**: `0,99`

**Synopsis**: Maximum number of file rotations to keep

**Example**:\
 \

~~~~ {.verbatim}
     
     body rename example
     {
     rotate => "4";
     }
     
~~~~

**Notes**:\
 \

Used for log rotation. If the file is named foo and the rotate attribute
is set to 4, as above, then initially foo is copied to foo.1 and the old
file foo is zeroed out (that is, the inode of the original logfile does
not change, but the original log file will be empty after the rotation
is complete).

The next time the promise is executed, foo.1 will be renamed foo.2, foo
is again copied to foo.1 and the old file foo is again zeroed out.

Each time the promise is executed (and typically, the promise would be
executed as guarded by time-based or file-size-based classes), the files
are copied/zeroed or rotated as above until there are rotate numbered
files plus the one "main" file. In the example above, the file foo.3
will be renamed foo.4, but the old version of the file foo.4 will be
deleted (that is, it "falls off the end" of the rotation).

#### `repository`

**Type**: string

**Allowed input range**: `"?(/.*)`

**Synopsis**: Name of a repository for versioning

**Example**:\
 \

~~~~ {.verbatim}
files:

 "/path/file"

   copy_from => source,
   repository => "/var/cfengine/repository";
~~~~

**Notes**:\
 \

A local repository for this object, overrides the default.

See [default\_repository](#default_005frepository-in-agent)

Note that when a repository is specified, the files are stored using the
canonified directory name of the original file, concatenated with the
name of the file. So, for example, /usr/local/etc/postfix.conf would
ordinarily be stored in an alternative repository as
\_usr\_local\_etc\_postfix.conf.cfsaved.

#### `touch`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               true
               false
               yes
               no
               on
               off
~~~~

**Synopsis**: true/false whether to touch time stamps on file

**Example**:\
 \

~~~~ {.verbatim}
files:

 "/path/file"

   touch => "true";
~~~~

**Notes**:\
 \

#### `transformer`

**Type**: string

**Allowed input range**: `"?(/.*)`

**Synopsis**: Command (with full path) used to transform current file
(no shell wrapper used)

**Example**:\
 \

~~~~ {.verbatim}
files:
  "/home/mark/tmp/testcopy"

    file_select => pdf_files,
    transformer => "/usr/bin/gzip $(this.promiser)",
    depth_search => recurse("inf");
~~~~

~~~~ {.verbatim}
 classes:
    "do_update" expression => isnewerthan("/etc/postfix/alias",
                                          "/etc/postfix/alias.cdb");

 files:
    "/etc/postfix/alias.cdb"
       create => "true",        # Must have this!
       transformer => "/usr/sbin/postalias /etc/postfix/alias",
       ifvarclass => "do_update";
~~~~

**Notes**:\
 \

A command to execute, usually for the promised file to transform it to
something else (but possibly to create the promised file based on a
different origin file). The examples above show both types of promises.

The promiser file must exist in order to effect the transformer.

In the first example, the promise is made on the file that we wish to
transform. If the promised file exists, the transformer will change the
file to a compressed version (and the next time CFEngine runs, the
promised file will no longer exist, because it now has the .gz
extension).

In the second example, the promise is made on the file *resulting from*
the transformation (and the promise is conditional on the original file
being newer than the result file). In this case, we *must* specify
create = true. If we do not, then if the promised file is removed the
transformer will not be executed.

Note also that if you use the `$(this.promiser)` variable or other
variable in this command, and the file object contains spaces, then you
should quote the variable. For example:

~~~~ {.verbatim}
    transformer => "/usr/bin/gzip \"$(this.promiser)\"",
~~~~

Note also that the transformer does not actually need to change the
file. You can, for example, simply report on the existence of files
with:

~~~~ {.verbatim}
    transformer => "/bin/echo I found a file named $(this.promiser)",
~~~~

The file streams `stdout` and `stderr` are redirected by CFEngine, and
will not appear in any output unless you run `cf-agent` with the -v
switch (or enable `verbose` in an `outputs` promise).

It is possible to set classes based on the return code of a
transformer-command in a very flexible way. See the `kept_returncodes`,
`repaired_returncodes` and `failed_returncodes` attributes.

Finally, you should note that the command is not run in a shell. This
means that you cannot perform file redirection or create pipelines.
