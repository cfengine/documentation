---
layout: default
title: field_edits
categories: [Reference, Promise Types, files, edit_line, field_edits]
published: true
alias: reference-promise-types-files-edit_line-field_edits.html
tags: [reference, bundle agent, bundle edit_line, files promises, file editing, field_edits]
---

Certain types of text files are tabular in nature, with field separators (e.g. 
`:` or `,`). The `passwd` and group files are classic examples of tabular 
files, but there are many ways to use this  feature. For example, editing a 
string:

```cf3
    VARIABLE="one two three"
```

View this line as a tabular line separated by " and with sub-separator
given by the space.

Field editing allows us to edit tabular files in a unique way, adding and 
removing data from addressable fields.

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
```

The promise in this example assumes a parameterizable model for editing the 
fields of such files.

```
    bundle edit_line SetUserParam(user,field,val)
    {
      field_edits:

       "$(user):.*"

          # Set field of the file to parameter

          edit_field => col(":","$(field)","$(val)","set");
    }

    bundle edit_line AppendUserParam(user,field,allusers)
    {
      vars:

        "val" slist => { @(allusers) };

      field_edits:

       "$(user):.*"

          # Set field of the file to parameter

          edit_field => col(":","$(field)","$(val)","alphanum");
    }
```

First you match the line with a regular expression. The regular expression 
must match the entire line; that is, it is [anchored][anchored].

```cf3
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

Then a `field_edits` body describes the separators for fields and 
one level of sub-fields, along with policies for editing these fields, 
ordering the items within them.

***

## Attributes

### edit_field

**Type:** `body edit_field`

**Example:**

```cf3
     body edit_field col(split, col, newval, method)
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

#### allow_blank_fields

**Description:** Setting `allow_blank_fields` defines how blank fields in a line are handled.
   
When editing a file using the field or column model, blank fields, especially 
at the start and end, are generally discarded. If `allow_blank_fields` is set 
to true, CFEngine will retain the blank fields and print the appropriate 
number of field separators. 

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
     body edit_field example
     {
     allow_blank_fields => "true";
     }
```

#### extend_fields

**Description:** Setting `extend_fields` can add new fields, to avoid 
triggering an error.

If a user specifies a field that does not exist, because there are not so many 
fields, this allows the number of fields to be extended. Without this setting, 
CFEngine will issue an error if a non-existent field is referenced. Blank 
fields in a tabular file can be eliminated or kept depending  in this setting. 
If in doubt, set this to true. 

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
     body edit_field example
     {
     extend_fields => "true";
     }
```

#### field_operation

**Description:** Menu option policy for editing subfields.

The method by which to edit a field in multi-field/column editing of tabular 
files.

**Type:** (menu option)

**Allowed input range:**   

* `append`

Append the specified value to the end of the field/column, separating 
(potentially) multiple values with `value_separator`

* `prepend`

Prepend the specified value at the beginning of the field/column, separating 
(potentially) multiple values with `value_separator`

* `alphanum`

Insert the specified value into the field/column, keeping all the values 
(separated by `value_separator`) in alphanumerically sorted order

* `set`

Replace the entire field/column with the specified value.

* `delete`

Delete the specified value (if present) in the specified field/column.

**Default value:** append 

**Example:**

```cf3
     body edit_field example
     {
     field_operation => "append";
     }
```

#### field_separator

**Description:** The regular expression used to separate fields in a line.

Most tabular files are separated by simple characters, but by allowing a
general regular expression one can make creative use of this model to
edit all kinds of line-based text files.   

**Type:** `string`

**Allowed input range:** `.*`

**Default value:** none

**Example:**

```cf3
     body edit_field example
     {
     field_separator => ":";
     }
```

#### field_value

**Description:** Set a field to a constant value.

For example, reset the value to a constant default, empty the field, or set it 
fixed list.   

**Type:** `string`

**Allowed input range:** `.*`

**Example:**

```cf3
     body edit_field example(s)
     {
     field_value => "$(s)";
     }
```

#### select_field

**Description**: Sets the index of the field required, see also `start_fields_from_zero`.

**Type:** `int`

**Allowed input range:** `0,99999999`

**Example:**

```cf3
     body field_edits example
     {
     select_field => "5";
     }
```

#### start_fields_from_zero

**Description:** The numbering of fields is a matter for consistency and 
convention. Arrays are usually thought to start with first index equal to zero 
(0), but the first column in a file would normally be 1. By setting this 
option, you can tell CFEngine that the first column should be understood as 
number 0 instead, for consistency with other array functions.   

**Type:** [`boolean`][boolean]

**History:** Version 3.1.0b1,Nova 2.0.0b1 (2010)

#### value_separator

**Description:** Defines the character separator for subfields inside the 
selected field.

For example, elements in the group file are separated by a colon (':'), but 
the lists of users in these fields are separated by a comma (',').

**Type:** `string`

**Allowed input range:** `^.$`

**Default value:** none

**Example:**

```cf3
     body field_edit example
     {
     value_separator => ",";
     }
```

