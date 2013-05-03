---
layout: default
title: insert_005flines-in-edit_005fline-promises
categories: [Bundles-for-agent,insert_005flines-in-edit_005fline-promises]
published: true
alias: Bundles-for-agent-insert_005flines-in-edit_005fline-promises.html
tags: [Bundles-for-agent,insert_005flines-in-edit_005fline-promises]
---

### `insert_lines` promises in edit\_line

\

This promise is part of the line-editing model. It inserts lines into
the file at a specified location. The location is determined by
body-attributes. The promise object referred to can be a literal line of
a file-reference from which to read lines.

~~~~ {.smallexample}
     
      insert_lines:
     
        "literal line or file reference"
     
           location = location_body,
           ...;
     
~~~~

\

~~~~ {.verbatim}
body common control

{
any::

  bundlesequence  => {
                     example
                     };   
}

#######################################################

bundle agent example

{
files:

  "/var/spool/cron/crontabs/root"

     edit_line => addline;
}

#######################################################
# For the library
#######################################################

bundle edit_line addline

{
insert_lines:

 "0,5,10,15,20,25,30,35,40,45,50,55 * * * * /var/cfengine/bin/cf-execd -F";

}
~~~~

\

By parameterizing the editing bundle, one can make generic and reusable
editing bundles.

Note: When inserting multiple lines anchored to a particular place in a
file, be careful with your intuition. If your intention is to insert a
set of lines in a given order after a marker, then the following is
incorrect:

~~~~ {.verbatim}
bundle edit_line x
{
insert_lines:

  "line one" location => myloc;
  "line two" location => myloc;
}

body location myloc

{
select_line_matching => "# Right here.*";
before_after => "after";
}
~~~~

This will reverse the order of the lines and will not converge, since
the anchoring after the marker applies independently for each new line.
This is not a bug, but an error of logic.

What was probably intended was to add multiple ordered lines after the
marker, which should be a single correlated promise.

~~~~ {.verbatim}
bundle edit_line x
{
insert_lines:
 
 "line one$(const.n)line two" location => myloc;

}
~~~~

Or:

~~~~ {.verbatim}
bundle edit_line x
{
insert_lines:
 
  "line one
line two" location => myloc;

}
~~~~

-   [expand\_scalars in
    insert\_lines](#expand_005fscalars-in-insert_005flines)
-   [insert\_type in
    insert\_lines](#insert_005ftype-in-insert_005flines)
-   [insert\_select in
    insert\_lines](#insert_005fselect-in-insert_005flines)
-   [location in insert\_lines](#location-in-insert_005flines)
-   [whitespace\_policy in
    insert\_lines](#whitespace_005fpolicy-in-insert_005flines)

#### `expand_scalars`

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

**Synopsis**: Expand any unexpanded variables

**Example**:\
 \

~~~~ {.verbatim}
body common control

{
bundlesequence  => { "testbundle"  };
}

########################################################

bundle agent testbundle

{
files:

  "/home/mark/tmp/file_based_on_template"

       create    => "true",
       edit_line => ExpandMeFrom("/tmp/source_template");


}

########################################################

bundle edit_line ExpandMeFrom(template)
{
insert_lines:

   "$(template)"

          insert_type => "file",
       expand_scalars => "true";
}
~~~~

**Notes**:\
 \

A way of incorporating templates with variable expansion into file
operations. Variables should be named and scoped appropriately for the
bundle in which this promise is made. In other words, you should qualify
the variables with the bundle in which they are defined. For example:

~~~~ {.verbatim}
$(bundle.variable)
$(sys.host)
$(mon.www_in)
~~~~

In CFEngine 2 `editfiles` this was called ExpandVariables.

#### `insert_type`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               literal
               string
               file
               file_preserve_block
               preserve_block
~~~~

**Default value:** literal

**Synopsis**: Type of object the promiser string refers to

**Example**:\
 \

~~~~ {.verbatim}
bundle edit_line lynryd_skynyrd
{
 vars:
    "keepers" slist => { "Won't you give me", "Gimme three steps" };

 insert_lines:

     "And you'll never see me no more"
       insert_type => "literal";    # the default

     "/song/lyrics"
       insert_type => "file",       # read selected lines from /song/lyrics
       insert_select => keep("@{keepers}");
}

body insert_select keep(s)
{
insert_if_startwith_from_list => { "@(s)" };
}
~~~~

This will ensure that the following lines are inserted into the promised
file:

~~~~ {.verbatim}
And you'll never see me no more
Gimme three steps, Mister
Gimme three steps towards the door
Gimme three steps
~~~~

**Notes**:\
 \

The default is to treat the promiser as a literal string of convergent
lines (the values `literal` and `string` are synonymous).

The default behaviour assumes that multi-line entries are not ordered
specifically. They should be treated as a collection of lines of text,
and not as a single unbroken object.

If the option preserve\_block is used, then CFEngine will not break up
multiple lines into individual, non-ordered objects, so that the block
of text will be preserved. Even if some of the lines in the block
already exist, they will be added again as a coherent block. Thus if you
suspect that some stray / conflicting lines might be present they should
be cleaned up with `delete_lines` first.

The value `file` is used to tell CFEngine that the string is non-literal
and should be interpreted as a filename from which to import lines.

See: [insert\_select](#insert_005fselect-in-insert_005flines).

Inserted files assume non-preserve\_block semantics. An equivalent file
setting that does preserve the ordering of lines in the file is called
`file_preserve_block`. This was added in CFEngine Core 3.5.x.

#### `insert_select` (body template)

**Type**: (ext body)

`insert_if_startwith_from_list`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: Insert line if it starts with a string in the list

**Example**:\
 \

~~~~ {.verbatim}
     
     body insert_select example
     {
     insert_if_startwith_from_list => { "find_me_1", "find_me_2" };
     }
     
~~~~

**Notes**:\
 \
 The list contains literal strings to search for in the secondary file
(the file being read via the `insert_type` attribute, not the main file
being edited). If a string with matching starting characters is found,
then that line from the secondary file will be inserted at the present
location in the primary file.

`insert_if_startswith_from_list` is ignored unless `insert_type` is
`file` (see [insert\_type in
insert\_lines](#insert_005ftype-in-insert_005flines)), or the promiser
is a multi-line block. \

`insert_if_not_startwith_from_list`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: Insert line if it DOES NOT start with a string in the list

**Example**:\
 \

~~~~ {.verbatim}
     
     body insert_select example
     {
     insert_if_not_startwith_from_list => { "find_me_1", "find_me_2" };
     }
     
~~~~

**Notes**:\
 \

The complement of `insert_if_startwith_from_list`. If the start of a
line does *not* match one of the strings, that line is inserted into the
file being edited.

`insert_if_not_startswith_from_list` is ignored unless `insert_type` is
`file` or the promiser is a multi-line block.

See: [insert\_type in
insert\_lines](#insert_005ftype-in-insert_005flines) \

`insert_if_match_from_list`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: Insert line if it fully matches a regex in the list

**Example**:\
 \

~~~~ {.verbatim}
     
     body insert_select example
     {
     insert_if_match_from_list => { ".*find_.*_1.*", ".*find_.*_2.*" };
     }
     
~~~~

**Notes**:\
 \
 The list contains literal strings to search for in the secondary file
(the file being read via the `insert_type` attribute, not the main file
being edited). If the regex matches a *complete* line of the file, that
line from the secondary file will be inserted at the present location in
the primary file. That is, the regex's in the list are anchored.

See: [Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)

`insert_if_match_from_list` is ignored unless `insert_type` is `file`,
or the promiser is a multi-line block.

See [insert\_type in
insert\_lines](#insert_005ftype-in-insert_005flines) \

`insert_if_not_match_from_list`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: Insert line if it DOES NOT fully match a regex in the list

**Example**:\
 \

~~~~ {.verbatim}
     
     body insert_select example
     {
     insert_if_not_match_from_list => { ".*find_.*_1.*", ".*find_.*_2.*" };
     }
     
~~~~

**Notes**:\
 \

The complement of `insert_if_match_from_list`. If the line does *not*
match a line in the secondary file, it is inserted into the file being
edited.

`insert_if_not_match_from_list` is ignored unless `insert_type` is
`file`, or the promiser is a multi-line block.

See: [insert\_type in
insert\_lines](#insert_005ftype-in-insert_005flines) \

`insert_if_contains_from_list`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: Insert line if a regex in the list match a line fragment

**Example**:\
 \

~~~~ {.verbatim}
     
     body insert_select example
     {
     insert_if_contains_from_list => { "find_me_1", "find_me_2" };
     }
     
~~~~

**Notes**:\
 \

The list contains literal strings to search for in the secondary file;
in other words, the file being read via the `insert_type` attribute, not
the main file being edited. If the string is found in a line of the
file, that line from the secondary file will be inserted at the present
location in the primary file.

`insert_if_contains_from_list` is ignored unless `insert_type` is
`file`, or the promiser is a multi-line block.

See: [insert\_type in
insert\_lines](#insert_005ftype-in-insert_005flines) \

`insert_if_not_contains_from_list`

**Type**: slist

**Allowed input range**: `.*`

**Synopsis**: Insert line if a regex in the list DOES NOT match a line
fragment

**Example**:\
 \

~~~~ {.verbatim}
     
     body insert_select example
     {
     insert_if_not_contains_from_list => { "find_me_1", "find_me_2" };
     }
     
~~~~

**Notes**:\
 \

The complement of `insert_if_contains_from_list`. If the line is *not*
found in the secondary file, it is inserted into the file being edited.

`insert_if_not_contains_from_list` is ignored unless `insert_type` is
`file`, or the promiser is a multi-line block.

See: [insert\_type in
insert\_lines](#insert_005ftype-in-insert_005flines)

#### `location` (body template)

**Type**: (ext body)

`before_after`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    before
                    after
~~~~

**Synopsis**: Menu option, point cursor before of after matched line

**Default value:** after

**Example**:\
 \

~~~~ {.verbatim}
     
     body location append
     
     {
     #...
     before_after => "before";
     }
     
~~~~

**Notes**:\
 \

Determines whether an edit will occur before or after the currently
matched line. \

`first_last`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    first
                    last
~~~~

**Synopsis**: Menu option, choose first or last occurrence of match in
file

**Default value:** last

**Example**:\
 \

~~~~ {.verbatim}
     
     body location example
     {
     first_last => "last";
     }
     
~~~~

**Notes**:\
 \

In multiple matches, decide whether the first or last occurrence of the
matching pattern in the case affected by the change. In principle this
could be generalized to more cases but this seems like a fragile quality
to evaluate, and only these two cases are deemed of reproducible
significance. \

`select_line_matching`

**Type**: string

**Allowed input range**: `.*`

**Synopsis**: Regular expression for matching file line location

**Example**:\
 \

~~~~ {.verbatim}
     
     # Editing
     
     body location example
     {
     select_line_matching => "Expression match.* whole line";
     }
     
     # Measurement promises
     
     body match_value example
     {
     select_line_matching => "Expression match.* whole line";
     }
     
~~~~

**Notes**:\
 \

The expression must match a whole line, not a fragment within a line;
that is, it is anchored.

See: [Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)

This attribute is mutually exclusive of `select_line_number`.

#### `whitespace_policy`

**Type**: (option list)

**Allowed input range**: \

~~~~ {.example}
               ignore_leading
               ignore_trailing
               ignore_embedded
               exact_match
~~~~

**Synopsis**: Criteria for matching and recognizing existing lines

**Default value**: `exact_match`

**Example**:\
 \

~~~~ {.verbatim}
bundle edit_line Insert(service, filename)
{
insert_lines:

  "$(service).* $(filename)"

      whitespace_policy => { "ignore_trailing", "ignore_embedded" };

}
~~~~

**Notes**:\
 \

The white space matching policy applies only to `insert_lines`, as a
convenience. It works by rewriting the insert string as a regular
expression when *matching* lines (that is, when determining if the line
is already in the file), but leaving the string as specified when
actually inserting it.

Simply put, the \`does this line exist' test will be changed to a regexp
match. The line being tested will optionally have "\\s\*" prepended or
appended if `ignore_leading` or `ignore_trailing` is specified, and if
`ignore_imbedded` is used then all embedded white spaces are replaced
with \\s+. Since `whitespace_policy` is additive you may specify more
than one.

Any regular expression meta-characters that exist in your input line
will be escaped. In this way, it is possible to safely insert a line
such as "authpriv.\* /var/log/something" into a syslog config file.

Unless you use this new attribute, your `insert_line` promises should
behave as before.

**History**: This attribute was introduced in CFEngine version 3.0.5
(2010)
