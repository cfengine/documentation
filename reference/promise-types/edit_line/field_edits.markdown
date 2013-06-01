---
layout: default
title: field_edits
categories: [Reference, Promise Types, files, edit_line, field_edits]
published: true
alias: reference-promise-types-files-edit_line-field_edits.html
tags: [reference, bundles, agent, field_edits, edit_line, files promises]
---

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

```cf3
     
     field_edits:
     
         "regex matching line"
     
                   edit_field = body;
     
```

  

```cf3
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
```

  

Field editing allows us to edit tabular files in a unique way, adding
and removing data from addressable fields. The passwd and group files
are classic examples of tabular files, but there are many ways to use
this feature. For example, editing a string:

```cf3
VARIABLE="one two three"
```

View this line as a tabular line separated by " and with sub-separator
given by the space.

-   [edit\_field in field\_edits](#edit_005ffield-in-field_005fedits)

#### `edit_field` (body template)

**Type**: (ext body)

`allow_blank_fields`

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

Setting `allow_blank_fields` defines how blank fields in a line are handled.
   
When editing a file using the field or column model, blank fields, especially at the start and end are generally discarded. If `allow_blank_fields` is set to true, CFEngine will retain the blank fields and print the appropriate number of field separators. 

**Example**:

```cf3
     
     body edit_field example
     {
     # ...
     allow_blank_fields => "true";
     }
     
```



`extend_fields`

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

Setting `extend_fields` can add new fields, to avoid triggering an error.

If a user specifies a field that does not exist, because there are not so many fields, this allows the number of fields to be extended. Without
this setting, CFEngine will issue an error if a non-existent field is referenced. Blank fields in a tabular file can be eliminated or kept depending in this setting. If in doubt, set this to true. 

**Example**:

```cf3
     
     body edit_field example
     {
     extend_fields => "true";
     }
     
```

 `field_operation`

**Type**: (menu option)

**Allowed input range**:   

```cf3
                    prepend
                    append
                    alphanum
                    delete
                    set
```

**Default value**: append 

Menu option policy for editing subfields is determined by setting `field_operation`.

The method by which to edit a field in multi-field/column editing of tabular files. The methods mean:

append - append the specified value to the end of the field/column, separating (potentially) multiple values with value\_separator

prepend - prepend the specified value at the beginning of the field/column, separating (potentially) multiple values with value\_separator

alphanum - insert the specified value into the field/column, keeping all the values (separated by value\_separator) in alphanumerically sorted
order

set - replace the entire field/column with the specified value

delete - delete the specified value (if present) in the specified field/column

**Example**:

```cf3
     
     body edit_field example
     {
     field_operation => "append";
     }
     
```

`field_separator`

**Type**: `string`

**Allowed input range**: `.*`

**Description**: The regular expression used to separate fields in a line

**Default value:** none

Most tabular files are separated by simple characters, but by allowing a
general regular expression one can make creative use of this model to
edit all kinds of line-based text files.   

**Example**:

```cf3
     
     body edit_field example
     {
     field_separator => ":";
     }
     
```

`field_value`

**Type**: `string`

**Allowed input range**: `.*`

  Set a field to a constant value. For example, reset the value to a
constant default, empty the field, or set it fixed list.   

**Example**:

```cf3
     
     body edit_field example(s)
     {
     field_value => "$(s)";
     }
     
```


`select_field`

**Type**: `int`

**Allowed input range**: `0,99999999`

Setting `select_field` determines the index of the field required 0..n (default starts
from 1). 

**Example**:

```cf3
     
     body field_edits example
     {
     select_field => "5";
     }
```



`start_fields_from_zero`

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

**History**: Version 3.1.0b1,Nova 2.0.0b1 (2010)

The numbering of fields is a matter for consistency and convention. Arrays are usually thought to start with first index equal to zero (0),
but the first column in a file would normally be 1. By setting this option, you can tell CFEngine that the first column should be understood
as number 0 instead, for consistency with other array functions.   

**Example**:

```cf3
     
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
     
```

`value_separator`

**Type**: `string`

**Allowed input range**: `^.$`

**Default value:** none

Setting `value_separator` defines the character separator for subfields inside the selected field. For example, elements in the group file are separated by a colon (':'), but the lists of users in these fields are separated by a comma (',').

**Example**:

```cf3
     
     body field_edit example
     {
     value_separator => ",";
     }
     
```


