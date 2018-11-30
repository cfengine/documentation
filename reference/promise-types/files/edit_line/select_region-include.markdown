### select_region

**Type:** `body select_region`

**Description:** Constrains `edit_line` operations to region identified by matching regular expressions.

Restrict edits to a specific region of a file based on ```select_start```
and ```select_end``` regular expressions. If the beginning and ending regular
expressions match more than one region only the first region will be
selected for editing.

**Example:**

{%raw%}
[%CFEngine_include_example(select_region.cf)%]
{%endraw%}

**See also:** [Common Body Attributes][Promise Types and Attributes#Common Body Attributes]

#### Scope and lifetime of the select_region

The region selected with `select_region` exists during the lifetime of the promise.
This means that once a promise has been started the selected region will be used regardless
of what the changes are.

There is a down side to this, promise lifetime is shorter than expected. For instance let's
look at the following code example:

```cf3
bundle agent init
{
vars:
    "states" slist => { "actual", "expected" };

    "actual" string =>
"header
header
BEGIN
One potato
Two potato
Three potatoe
Four
END
trailer
trailer";

    "expected" string =>
"header
header
One potato
Two potato
Four
trailer
trailer";

files:
    "testfile.$(states)"
      create => "true",
      edit_line => init_insert("$(init.$(states))"),
      edit_defaults => init_empty;
}

bundle edit_line init_insert(str)
{
insert_lines:
    "$(str)";
}

body edit_defaults init_empty
{
  empty_file_before_editing => "true";
}

#######################################################

bundle agent test
{
vars:
    "tstr" slist => { "BEGIN", "    Three potatoe", "END" };

files:
    "testfile.actual"
      edit_line => test_delete("$(test.tstr)");
}

bundle edit_line test_delete(str)
{
delete_lines:
    "$(str)"
      select_region => test_select;
}

body select_region test_select
{
  select_start => "BEGIN";
  select_end => "END";
  include_start_delimiter => "true";
  include_end_delimiter => "true";
  select_end_match_eof => "true";
}
```

The code generates two files, `testfile.actual` and `testfile.expected`. The idea is that both files will be
equal after the promise is run, since the transformations applied to `testfile.actual` will convert it into
`testfile.equal`.

However due to the lifetime of promises, this is not true. The attribute `select_region` lives as long as the
promise that created it lives and it will be recreated on the next incarnation.

Notice that `tstr` is a `slist` that is used as a parameter for `edit_line`, which uses it to select the strings that
will be removed. The `select_region` body specifies that the `select_start` attribute is "BEGIN", which holds true only
for the first invocation of the promise because during that iteration it will be removed. Once it is removed
the `select_region` body will never be able to match `select_start` again.

In the previous example, it is easy to think that the `select_region` will be kept during the whole iteration of the
`slist`. This is not true, each element in the `slist` will trigger its own invocation of the promise, therefore
`select_region` will only match the first iteration.

The solution to this problem is simple: if the marker for a region needs to be removed, then it cannot be used as a marker.
In the example above it is enough to change the markers from "BEGIN" to "header" and from "END" to "trailer" to obtain the
desired result.

****


#### include\_end\_delimiter

**Description:** Whether to include the section delimiter

In a sectioned file, the line that marks the end of a section is not
normally included in the defined region; that is, it is recognized as a
delimiter, but it is not included as one of the lines available for
editing. Setting this option to true makes it included.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

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

**History:**

- Introduced in CFEngine version 3.0.5 (2010)

#### include\_start\_delimiter

**Description:** Whether to include the section delimiter

In a sectioned file, the line that marks the opening of a section is not
normally included in the defined region (that is, it is recognized as a
delimiter, but it is not included as one of the lines available for
editing). Setting this option to true makes it included.

**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

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

**History:**

- Introduced in CFEngine version 3.0.5 (2010)

#### select\_end

**Description:** [Anchored][anchored] regular expression matches end of edit region from ```select_start```

**Type:** `string`

**Allowed input range:** `.*`

**Example:**

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

**Note:** When a region does not always have an end (like the last section of an
INI formatted file) ```select_end_match_eof``` can be used to allow the end of
the file to be considered the end of the region. The global default can be
modified with [`select_end_match_eof`][cf-agent#select_end_match_eof].

#### select\_end\_match\_eof

**Description:** Allow the end of a file to be considered the end of a region.

When `select_end_match_eof` is set to true `select_end` will consider end of
file as the end region if it is unable to match the end pattern. If the
`select_end` attribute is omitted, the selected region will run to the end of
the file no matter what the value of `select_end_match_eof` is set to.


**Type:** [`boolean`][boolean]

**Default value:** false

**Example:**

```cf3
     body select_region example(x)
     {
     select_start => "\[$(x)\]";
     select_end => "\[.*\]";
     select_end_match_eof => "true";
     }
```

**See Also:** [`select_end_match_eof` in body agent control][cf-agent#select_end_match_eof]

**History:**

- Introduced in CFEngine version 3.9.0 (2016)

#### select\_start

**Description:** [Anchored][anchored] regular expression matching start of edit region

**Type:** `string`

**Allowed input range:** `.*`

**Example:**

```cf3
     body select_region example(x)
     {
       select_start => "\[$(x)\]";
       select_end => "\[.*\]";
     }
```
