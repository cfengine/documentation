---
layout: default
title: field_005fedits-in-edit_005fline-promises
categories: [Bundles-for-agent,field_005fedits-in-edit_005fline-promises]
published: true
alias: Bundles-for-agent-field_005fedits-in-edit_005fline-promises.html
tags: [Bundles-for-agent,field_005fedits-in-edit_005fline-promises]
---

### `field_edits` promises in edit\_line

\

Certain types of text files (e.g. the passwd and group files in Unix)
are tabular in nature, with field separators (e.g. : or ,). This promise
assumes a parameterizable model for editing the fields of such files,
using a regular expression to separate major fields and a character to
separate sub-fields. First you match the line with a regular expression.
The regular expression must match the entire line; that is, it is
anchored (see [Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). Then a
`field_edits` body describes the separators for fields and one level of
sub-fields, along with policies for editing these fields, ordering the
items within them.

~~~~ {.smallexample}
     
     field_edits:
     
         "regex matching line"
     
                   edit_field = body;
     
~~~~

\

~~~~ {.verbatim}
bundle agent example

{
vars:

 "userset" slist => { "one-x", "two-x", "three-x" };

files:

  "/tmp/passwd"

       create    => "true",
       edit_line => SetUserParam("mark","6","/set/this/shell");

  "/tmp/group"

       create    => "true",
       edit_line => AppendUserParam("root","4","@(userset)");
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
~~~~

\

Field editing allows us to edit tabular files in a unique way, adding
and removing data from addressable fields. The passwd and group files
are classic examples of tabular files, but there are many ways to use
this feature. For example, editing a string:

~~~~ {.verbatim}
VARIABLE="one two three"
~~~~

View this line as a tabular line separated by " and with sub-separator
given by the space.

-   [edit\_field in field\_edits](#edit_005ffield-in-field_005fedits)

#### `edit_field` (body template)

**Type**: (ext body)

`allow_blank_fields`

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

**Synopsis**: true/false allow blank fields in a line (do not purge)

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body edit_field example
     {
     # ...
     allow_blank_fields => "true";
     }
     
~~~~

**Notes**:\
 \

When editing a file using the field or column model, blank fields,
especially at the start and end are generally discarded. If this is set
to true, CFEngine will retain the blank fields and print the appropriate
number of field separators. \

`extend_fields`

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

**Synopsis**: true/false add new fields at end of line if necessary to
complete edit

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body edit_field example
     {
     extend_fields => "true";
     }
     
~~~~

**Notes**:\
 \

If a user specifies a field that does not exist, because there are not
so many fields, this allows the number of fields to be extended. Without
this setting, CFEngine will issue an error if a non-existent field is
referenced. Blank fields in a tabular file can be eliminated or kept
depending in this setting. If in doubt, set this to true. \

`field_operation`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
                    prepend
                    append
                    alphanum
                    delete
                    set
~~~~

**Synopsis**: Menu option policy for editing subfields

**Default value:** none

**Example**:\
 \

~~~~ {.verbatim}
     
     body edit_field example
     {
     field_operation => "append";
     }
     
~~~~

**Notes**:\
 \

The method by which to edit a field in multi-field/column editing of
tabular files. The methods mean:

append - append the specified value to the end of the field/column,
separating (potentially) multiple values with value\_separator

prepend - prepend the specified value at the beginning of the
field/column, separating (potentially) multiple values with
value\_separator

alphanum - insert the specified value into the field/column, keeping all
the values (separated by value\_separator) in alphanumerically sorted
order

set - replace the entire field/column with the specified value

delete - delete the specified value (if present) in the specified
field/column

**Default value**: append \

`field_separator`

**Type**: string

**Allowed input range**: `.*`

**Synopsis**: The regular expression used to separate fields in a line

**Default value:** none

**Example**:\
 \

~~~~ {.verbatim}
     
     body edit_field example
     {
     field_separator => ":";
     }
     
~~~~

**Notes**:\
 \

Most tabular files are separated by simple characters, but by allowing a
general regular expression one can make creative use of this model to
edit all kinds of line-based text files. \

`field_value`

**Type**: string

**Allowed input range**: `.*`

**Synopsis**: Set field value to a fixed value

**Example**:\
 \

~~~~ {.verbatim}
     
     body edit_field example(s)
     {
     field_value => "$(s)";
     }
     
~~~~

**Notes**:\
 \

Set a field to a constant value. For example, reset the value to a
constant default, empty the field, or set it fixed list. \

`select_field`

**Type**: int

**Allowed input range**: `0,99999999`

**Synopsis**: Integer index of the field required 0..n (default starts
from 1)

**Example**:\
 \

~~~~ {.verbatim}
     
     body field_edits example
     {
     select_field => "5";
     }
~~~~

**Notes**:\
 \

Numbering starts from 1 (not from 0). \

`start_fields_from_zero`

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

**Synopsis**: If set, the default field numbering starts from 0

**Example**:\
 \

~~~~ {.verbatim}
     
     body edit_field col(split,col,newval,method)
     
     {
     field_separator    => "$(split)";
     select_field       => "$(col)";
     value_separator    => ",";
     field_value        => "$(newval)";
     field_operation    => "$(method)";
     extend_fields      => "true";
     allow_blank_fields => "true";
     start_fields_from_zero => "true";
     }
     
~~~~

**Notes**:\
 \

*History*: Was introduced in version 3.1.0b1,Nova 2.0.0b1 (2010)

The numbering of fields is a matter for consistency and convention.
Arrays are usually thought to start with first index equal to zero (0),
but the first column in a file would normally be 1. By setting this
option, you can tell CFEngine that the first column should be understood
as number 0 instead, for consistency with other array functions. \

`value_separator`

**Type**: string

**Allowed input range**: `^.$`

**Synopsis**: Character separator for subfields inside the selected
field

**Default value:** none

**Example**:\
 \

~~~~ {.verbatim}
     
     body field_edit example
     {
     value_separator => ",";
     }
     
~~~~

**Notes**:\
 \

For example, elements in the group file are separated by :, but the
lists of users in these fields are separated by ,.
