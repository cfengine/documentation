---
layout: default
title: bundle edit_line
published: true
tags: [reference, bundle agent, bundle edit_line, files promises, file editing]
---

Line based editing is a simple model for editing files. Before XML, and
later JSON, most configuration files were line based. The line-based
editing offers a powerful environment for model-based editing and
templating.

## File editing in CFEngine 3

File editing is not just a single kind of promise but a whole range of
'promises within files'. It is therefore not merely a body to a single
kind of promise, but a bundle of promises. After all, inside each
file are new objects that can make promises, quite separate from files'
external attributes.

A typical file editing stanza has the elements in the following example:

```cf3
body common control
{
  version => "1.2.3";
  bundlesequence  => { "outerbundle"  };
}

bundle agent outerbundle
{
files:

  "/home/mark/tmp/cf3_test"
       create    => "true",     # Like autocreate in cf2
       edit_line => inner_bundle;
}

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
      "This is file $(edit.filename)";
}

body replace_with C_comment
{
  replace_value => "/* $(match.1) */"; # backreference
  occurrences => "all";          # first, last all
}

body select_region MySection(x)
{
  select_start => "\[$(x)\]";
  select_end => "\[.*\]";
}

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
-   On Windows, a text file may be stored stored either with CRLF line
    endings (Windows style), or LF line endings (Unix style). CFEngine
    will respect the existing line ending type and make modifications
    using the same type. New files will get CRLF line ending type.

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

body changes lay_a_tripwire
{
  hash           => "md5";
  report_changes => "content";
  update         => "yes";
}
```

