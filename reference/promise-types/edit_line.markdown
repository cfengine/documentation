---
layout: default
title: bundle edit_line
categories: [Reference, Promise Types, files, edit_line]
published: true
alias: reference-promise-types-files-edit_line.html
tags: [reference, bundle agent, bundle edit_line, files promises, file editing]
---

Line based editing is a simple model for editing files. Before XML, and
later JSON, most configuration files were line based. The line-based
editing offers a powerful environment for model-based editing and
templating.

### File editing in CFEngine 3

File editing is not just a single kind of promise but a whole range of
'promises within files'. It is therefore not merely a body to a single
kind of promise, but a bundle of sub-promises. After all, inside each
file are new objects that can make promises, quite separate from files'
external attributes.

A typical file editing stanza has the elements in the following example:

```cf3
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

```

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

```cf3
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
```

****

## Attributes

### select_region

**Type**: `body select_region`

#### include_start_delimiter

**Description**: Whether to include the section delimiter

In a sectioned file, the line that marks the opening of a section is not
normally included in the defined region (that is, it is recognized as a
delimiter, but it is not included as one of the lines available for
editing). Setting this option to true makes it included.

**Type**: (menu option)

**Allowed input range**:   

```cf3
    true
    false
    yes
    no
    on
    off
```

**Default value:** false

**Example**:

```cf3
     body select_region MySection(x)
     {
       select_start => "\[$(x)\]";
       select_end => "\[.*\]";
       include_start_delimiter => "true";
     }
```

Input file:

```cf3
     [My section]
     one
     two
     three
```

In this example, the section does not normally include the line [My
section]. By setting `include_start_delimiter` to `true` it would be
possible for example, to delete the entire section, including the
section header. If however `include_start_delimiter` is false, the
*contents* of the section could be deleted, but the header would be
unaffected by any `delete_lines` promises. See the next section on
`include_start_delimiter` for further details.

**History**: This attribute was introduced in CFEngine version 3.0.5
(2010)   

#### include_end_delimiter

**Description**: Whether to include the section delimiter

In a sectioned file, the line that marks the end of a section is not
normally included in the defined region; that is, it is recognized as a
delimiter, but it is not included as one of the lines available for
editing. Setting this option to true makes it included.

**Type**: (menu option)

**Allowed input range**:   

```cf3
    true
    false
    yes
    no
    on
    off
```

**Default value:** false

**Example**:

```cf3
     body select_region BracketSection(x)
     {
     select_start => "$(x) \{";
     select_end => "}";
     include_end_delimiter => "true";
     }
```

Input file:

```cf3
     /var/log/mail.log {
         monthly
         missingok
         notifempty
         rotate 7
         }
```

The section does not normally include the line containing }. By setting
`include_end_delimiter` to `true` it would be possible for example, to
delete the entire section, including the section trailer. If however
`include_end_delimiter` is false, the *contents* of the section could be
deleted, but the header would be unaffected by any `delete_lines`
promises.

The use of `include_start_delimiter` and `include_end_delimiter` depend
on the type of sections you are dealing with, and what you want to do
with them. Note that sections can be bounded at both the start and end
(as in the example above) or just at the start (as in the sample shown
in `include_start_delimiter`).

**History**: This attribute was introduced in CFEngine version 3.0.5
(2010)   

#### select_start

**Description**: Regular expression matching start of edit region

See also `select_end`. These delimiters mark out the region of a file to
be edited.

**Type**: `string`

**Allowed input range**: `.*`

**Example**:

```cf3
     body select_region example(x)
     {
       select_start => "\[$(x)\]";
       select_end => "\[.*\]";
     }
```

#### select_end

**Description**: Regular expression matches end of edit region from start

See also `select_start`. These delimiters mark out the region of a file
to be edited.

**Type**: `string`

**Allowed input range**: `.*`

**Example**:

```cf3
     body select_region example(x)
     {
     select_start => "\[$(x)\]";
     select_end => "\[.*\]";
     }
```

If you want to match from a starting location to the end of the file
(even if there are other lines matching `select_start` intervening),
then just omit the `select_end` promise and the selected region will run
to the end of the file.
