---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Bundles-for-agent-0-delete_005flines-in-edit_005fline-promises-6.markdown.html
tags: [xx]
---

### `delete_lines` promises in edit\_line

\

This promise assures that certain lines exactly matching regular
expression patterns will not be present in a text file. If the lines are
found, the default promise is to remove them (this behavior may be
modified with further pattern matching in `delete_select` and/or changed
with `not_matching`).

\

    bundle edit_line example
      {
      delete_lines:

        "olduser:.*";

      }

Note that typically, only a single line is specified in each
`delete_lines` promise. However, you may of course have multiple
promises that each delete a line.

It is also possible to specify multi-line `delete_lines` promises.
However, these promises will only delete those lines if *all* the lines
are present in the file *in exactly the same order* as specified in the
promise (with no intervening lines). That is, all the lines must match
as a unit for the `delete_lines` promise to be kept.

\

If the promiser contains multiple lines, then CFEngine assumes that all
of the lines must exist as a contiguous block in order to be deletes.
This gives preserve\_block semantics to any multiline `delete_lines`
promise.

-   delete\_select in delete\_lines
-   not\_matching in delete\_lines

#### `delete_select` (body template)

**Type**: (ext body)

`delete_if_startwith_from_list`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: Delete line if it starts with a string in the list

**Example**:\
 \

         
         body delete_select example(s)
         {
         delete_if_startwith_from_list => { @(s) };
         }
         

**Notes**:\
 \

Delete lines from a file if they begin with the sub-strings listed. Note
that this determination is made only on promised lines (that is, this
attribute modifies the selection criteria, it does not make the initial
selection). Therefore, if the file contains the following lines:

         start alpha igniter
         start beta igniter
         init alpha burner
         init beta burner
         stop beta igniter
         stop alpha igniter
         stop alpha burner

Then the following promise initially selects the four lines containing
alpha, but is moderated by the `delete_select` attribute. Thus, the
promise will delete only the first and third lines of the file:

         bundle edit_line alpha
         {
         delete_lines:
             ".*alpha.*"
            delete_select => starters;
         }
         
         body delete_select starters
         {
             delete_if_startwith_from_list => { "begin", "start", "init" };
         }

\

`delete_if_not_startwith_from_list`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: Delete line if it DOES NOT start with a string in the list

**Example**:\
 \

         
         body delete_select example(s)
         {
         delete_if_not_startwith_from_list => { @(s) };
         }
         

**Notes**:\
 \

Delete lines from a file unless they start with the sub-strings in the
list given. Note that this determination is made only on promised lines.
In other words, this attribute modifies the selection criteria, it does
not make the initial selection. \

`delete_if_match_from_list`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: Delete line if it fully matches a regex in the list

**Example**:\
 \

         
         body delete_select example(s)
         {
         delete_if_match_from_list => { @(s) };
         }
         

**Notes**:\
 \

Delete lines from a file if the lines *completely* match any of the
regular expressions listed. In other words, the regular expression is
anchored (see Anchored vs. unanchored regular expressions).

Note that this attribute modifies the selection criteria, it does not
make the initial selection, and the match determination is made only on
promised lines. \

`delete_if_not_match_from_list`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: Delete line if it DOES NOT fully match a regex in the list

**Example**:\
 \

         
         body delete_select example(s)
         {
         delete_if_not_match_from_list => { @(s) };
         }
         

**Notes**:\
 \

Delete lines from a file unless the lines *completely* match any of the
regular expressions listed. In other words, the regular expressions are
anchored (see Anchored vs. unanchored regular expressions).

Note that this attribute modifies the selection criteria, it does not
make the initial selection, and the match determination is made only on
promised lines. \

`delete_if_contains_from_list`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: Delete line if a regex in the list match a line fragment

**Example**:\
 \

         
         body delete_select example(s)
         {
         delete_if_contains_from_list => { @(s) };
         }
         

**Notes**:\
 \

Delete lines from a file if they contain the sub-strings listed.

Note that this attribute modifies the selection criteria, it does not
make the initial selection, and the match determination is made only on
promised lines. \

`delete_if_not_contains_from_list`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: Delete line if a regex in the list DOES NOT match a line
fragment

**Example**:\
 \

         
         body delete_select discard(s)
         {
         delete_if_not_contains_from_list => { "substring1", "substring2" };
         }
         

**Notes**:\
 \

Delete lines from the file which do not contain the sub-strings listed.

Note that this attribute modifies the selection criteria, it does not
make the initial selection, and the match determination is made only on
promised lines.

#### `not_matching`

**Type**: (menu option)

**Allowed input range**: \

                   true
                   false
                   yes
                   no
                   on
                   off

**Default value:** false

**Synopsis**: true/false negate match criterion

**Example**:\
 \

    delete_lines:

      # edit /etc/passwd - account names that are not "mark" or "root"

      "(mark|root):.*" not_matching => "true";

**Notes**:\
 \

When this option is true, it negates the pattern match of the promised
lines.

**NOTE** that this does not negate any condition expressed in
`delete_select`. It only negates the match of the initially promised
lines.

Note, this makes no sense for multi-line deletions, and is therefore
disallowed. Either a multi-line promiser matches and it should be
removed (i.e. `not_matching` is false), or it does not match the whole
thing and the ordered lines have no meaning anymore as an entity. In
this case, the lines can be separately stated.
