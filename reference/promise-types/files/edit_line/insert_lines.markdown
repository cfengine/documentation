---
layout: default
title: insert_lines
published: true
tags: [reference, bundle agent, edit_line, files promises, file editing, insert_lines]
---

This promise type is part of the line-editing model. It inserts lines into
the file at a specified location. The location is determined by
body-attributes. The promise object referred to can be a literal line or
a file-reference from which to read lines.

```cf3
      insert_lines:

        "literal line or file reference"

           location => location_body,
           ...;
```

By parameterizing the editing bundle, one can make generic and reusable
editing bundles.

Note: When inserting multiple lines [anchored][anchored] to a particular place in a
file, be careful with your intuition. If your intention is to insert a
set of lines in a given order after a marker, then the following is
incorrect:

```cf3
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
```

This will reverse the order of the lines and will not converge, since
the anchoring after the marker applies independently for each new line.
This is not a bug in CFEngine, but an error of logic in the policy itself.

To add multiple ordered lines after the marker, a single correlated promise
should be used:

```cf3
    bundle edit_line x
    {
    insert_lines:

     "line one$(const.n)line two" location => myloc;
    }
```

Or:

```cf3
    bundle edit_line x
    {
    insert_lines:

      "line one
    line two"
      location => myloc;
    }
```

****

## Attributes ##

### expand_scalars

**Description:** Expand any unexpanded variables

This is a way of incorporating templates with variable expansion into file
operations. Variables should be named and scoped appropriately for the
bundle in which this promise is made. In other words, you should qualify
the variables with the bundle in which they are defined. For example:

```cf3
    $(bundle.variable)
    $(sys.host)
    $(mon.www_in)
```

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
bundle agent testbundle
{
files:

  "/home/mark/tmp/file_based_on_template"

       create    => "true",
       edit_line => ExpandMeFrom("/tmp/source_template");
}

bundle edit_line ExpandMeFrom(template)
{
insert_lines:
   "$(template)"

          insert_type => "file",
       expand_scalars => "true";
}
```

### insert_type

**Description:** Type of object the promiser string refers to

The default is to treat the promiser as a literal string of convergent
lines.

**Type:** (menu option)

**Allowed input range:**

* `literal` or `string`

Treat the promiser as a literal string of convergent lines.

* file

The string should be interpreted as a filename from which to import lines.

* `preserve_block`

The default behavior assumes that multi-line entries are not ordered
specifically. They should be treated as a collection of lines of text,
and not as a single unbroken object.

If the option `preserve_block` is used, then CFEngine will not break up
multiple lines into individual, non-ordered objects, so that the block
of text will be preserved. Even if some of the lines in the block
already exist, they will be added again as a coherent block. Thus if you
suspect that some stray / conflicting lines might be present they should
be cleaned up with `delete_lines` first.

* `preserve_all_lines`

Disables idempotency during the insertion of a block of text so that
multiple identical lines may be inserted.

This means that the text will be inserted to the file even if it is already
present. To avoid that the file grows, use this together with
`empty_file_before_editing`.

* `file_preserve_block`

Interpret the string as a filename, and assume `preserve_block` semantics.
This was added in CFEngine 3.5.x.

**Default value:** literal

**Example:**

```cf3
    bundle edit_line lynryd_skynyrd
    {
     vars:
        "keepers" slist => { "Won't you give me", "Gimme three steps" };

     insert_lines:

         "And you'll never see me no more"
           insert_type => "literal";    # the default

         "/song/lyrics"
           insert_type => "file",  # read selected lines from /song/lyrics
           insert_select => keep("@{keepers}");
    }

    body insert_select keep(s)
    {
    insert_if_startwith_from_list => { "@(s)" };
    }
```

This will ensure that the following lines are inserted into the promised
file:

```cf3
    And you'll never see me no more
    Gimme three steps, Mister
    Gimme three steps towards the door
    Gimme three steps
```

### insert_select

**Type:** `body insert_select`

**See also:** [Common Body Attributes][Promise Types#Common Body Attributes]

#### insert_if_startwith_from_list

**Description:** Insert line if it starts with a string in the list

The list contains literal strings to search for in the secondary file
(the file being read via the `insert_type` attribute, not the main file
being edited). If a string with matching starting characters is found,
then that line from the secondary file will be inserted at the present
location in the primary file.

`insert_if_startswith_from_list` is ignored unless `insert_type` is
`file`, or the promiser is a multi-line block.

**Type:** `slist`

**Allowed input range:** `.*`

**Example:**

```cf3
     body insert_select example
     {
     insert_if_startwith_from_list => { "find_me_1", "find_me_2" };
     }
```

#### insert_if_not_startwith_from_list

**Description:** Insert line if it DOES NOT start with a string in the list

The complement of `insert_if_startwith_from_list`. If the start of a
line does *not* match one of the strings, that line is inserted into the
file being edited.

`insert_if_not_startswith_from_list` is ignored unless `insert_type` is
`file` or the promiser is a multi-line block.

**Type:** `slist`

**Allowed input range:** `.*`

**Example:**

```cf3
     body insert_select example
     {
     insert_if_not_startwith_from_list => { "find_me_1", "find_me_2" };
     }
```

#### insert_if_match_from_list

**Description:** Insert line if it fully matches a regex in the list

The list contains literal strings to search for in the secondary file
(the file being read via the `insert_type` attribute, not the main file
being edited). If the regex matches a *complete* line of the file, that
line from the secondary file will be inserted at the present location in
the primary file. That is, the regex's in the list are [anchored][anchored].

`insert_if_match_from_list` is ignored unless `insert_type` is `file`,
or the promiser is a multi-line block.

**Type:** `slist`

**Allowed input range:** `.*`

**Example:**

```cf3
     body insert_select example
     {
     insert_if_match_from_list => { ".*find_.*_1.*", ".*find_.*_2.*" };
     }
```

#### insert_if_not_match_from_list

**Description:** Insert line if it DOES NOT fully match a regex in the list

The complement of `insert_if_match_from_list`. If the line does *not*
match a line in the secondary file, it is inserted into the file being
edited.

`insert_if_not_match_from_list` is ignored unless `insert_type` is
`file`, or the promiser is a multi-line block.

**Type:** `slist`

**Allowed input range:** `.*`

**Example:**

```cf3
     body insert_select example
     {
     insert_if_not_match_from_list => { ".*find_.*_1.*", ".*find_.*_2.*" };
     }
```

#### insert_if_contains_from_list

**Description:** Insert line if a regex in the list match a line fragment.

The list contains literal strings to search for in the secondary file;
in other words, the file being read via the `insert_type` attribute, not
the main file being edited. If the string is found in a line of the
file, that line from the secondary file will be inserted at the present
location in the primary file.

`insert_if_contains_from_list` is ignored unless `insert_type` is
`file`, or the promiser is a multi-line block.

**Type:** `slist`

**Allowed input range:** `.*`

**Example:**

```cf3
     body insert_select example
     {
     insert_if_contains_from_list => { "find_me_1", "find_me_2" };
     }
```

#### insert_if_not_contains_from_list

**Description:** Insert line if a regex in the list DOES NOT match a line
fragment.

The complement of `insert_if_contains_from_list`. If the line is *not*
found in the secondary file, it is inserted into the file being edited.

`insert_if_not_contains_from_list` is ignored unless `insert_type` is
`file`, or the promiser is a multi-line block.

**Type:** `slist`

**Allowed input range:** `.*`

**Example:**

```cf3
     body insert_select example
     {
     insert_if_not_contains_from_list => { "find_me_1", "find_me_2" };
     }
```

### location

**Type:** `body location`

**See also:** [Common Body Attributes][Promise Types#Common Body Attributes], [`location` bodies in the standard library](reference-standard-library-files.html#location-bodies), [`start` location body in the standard library](reference-standard-library-files.html#location-bodies), [`before(srt)` location body in the standard library](reference-standard-library-files.html#before), [`after(srt)` location body in the standard library](reference-standard-library-files.html#after)

#### before_after

**Description:** Menu option, point cursor before of after matched line

Determines whether an edit will occur before or after the currently
matched line.

**Type:** (menu option)

**Allowed input range:**

```
    before
    after
```

**Default value:** after

**Example:**

```cf3
     body location append
     {
     before_after => "before";
     }
```

#### first_last

**Description:** Choose first or last occurrence of match in file.

In multiple matches, decide whether the first or last occurrence of the
matching pattern in the case affected by the change. In principle this
could be generalized to more cases but this seems like a fragile quality
to evaluate, and only these two cases are deemed of reproducible
significance.

**Type:** (menu option)

**Allowed input range:**

```
    first
    last
```

**Default value:** last

**Example:**

```cf3
     body location example
     {
     first_last => "last";
     }
```

#### select_line_matching

**Description:** Regular expression for matching file line location

The expression must match a whole line, not a fragment within a line;
that is, it is [anchored][anchored].


**Type:** `string`

**Allowed input range:** `.*`

**Example:**

```cf3
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
```

**Notes:**

* This attribute is mutually exclusive of `select_line_number`.
* This attribute can not match a multiple line pattern (`(?m)` has no effect).

### select_region

**Description:** Constrains `edit_line` operations to region identified by matching regular expressions.

This body applies to all promise types within `edit_line` bundles.

**See also:** [```select_region``` with `edit_line` operations][edit_line#select_region], [```select_region``` in `delete_lines`][delete_lines#select_region], [```select_region``` in `field_edits`][field_edits#select_region], [```select_region``` in `replace_patterns`][replace_patterns#select_region]

### whitespace_policy

**Description:** Criteria for matching and recognizing existing lines

The white space matching policy applies only to `insert_lines`, as a
convenience. It works by rewriting the insert string as a regular
expression when *matching* lines (that is, when determining if the line
is already in the file), but leaving the string as specified when
actually inserting it.

Simply put, the 'does this line exist' test will be changed to a regexp
match. The line being tested will optionally have `\s*` prepended or
appended if `ignore_leading` or `ignore_trailing` is specified, and if
`ignore_imbedded` is used then all embedded white spaces are replaced
with `\s+`. Since `whitespace_policy` is additive you may specify more
than one.

Any regular expression meta-characters that exist in your input line
will be escaped. In this way, it is possible to safely insert a line
such as `authpriv.* /var/log/something` into a syslog config file.

**Type:** (option list)

**Allowed input range:**

```cf3
    ignore_leading
    ignore_trailing
    ignore_embedded
    exact_match
```

**Default value:** `exact_match`

**Example:**

```cf3
bundle edit_line Insert(service, filename)
{
insert_lines:

  "$(service).* $(filename)"

      whitespace_policy => { "ignore_trailing", "ignore_embedded" };
}
```

**History:** This attribute was introduced in CFEngine version 3.0.5
(2010)
