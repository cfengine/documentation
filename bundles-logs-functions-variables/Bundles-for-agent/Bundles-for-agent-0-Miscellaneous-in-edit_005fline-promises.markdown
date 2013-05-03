---
layout: default
title: Miscellaneous-in-edit_005fline-promises
categories: [Bundles-for-agent,Miscellaneous-in-edit_005fline-promises]
published: true
alias: Bundles-for-agent-Miscellaneous-in-edit_005fline-promises.html
tags: [Bundles-for-agent,Miscellaneous-in-edit_005fline-promises]
---

### Miscelleneous in `edit_line` promises

\

Line based editing is a simple model for editing files. Before XML, and
later JSON, most configuration files were line based. The line-based
editing offers a powerful environment for model-based editing and
templating.

-   [select\_region in \*](#select_005fregion-in-_002a)

#### `select_region` (body template)

**Type**: (ext body)

`include_start_delimiter`

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

**Synopsis**: Whether to include the section delimiter

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body select_region MySection(x)
     {
     select_start => "\[$(x)\]";
     select_end => "\[.*\]";
     include_start_delimiter => "true";
     }
     
~~~~

**Notes**:\
 \

In a sectioned file, the line that marks the opening of a section is not
normally included in the defined region (that is, it is recognized as a
delimiter, but it is not included as one of the lines available for
editing). Setting this option to true makes it included. For example:

~~~~ {.verbatim}
     [My section]
     one
     two
     three
~~~~

In the example above, the section does not normally include the line [My
section]. By setting `include_start_delimiter` to trueit would be
possible for example, to delete the entire section, including the
section header. If however `include_start_delimiter` is false, the
*contents* of the section could be deleted, but the header would be
unaffected by any `delete_lines` promises. See the next section on
`include_start_delimiter` for further details.

**History**: This attribute was introduced in CFEngine version 3.0.5
(2010) \

`include_end_delimiter`

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

**Synopsis**: Whether to include the section delimiter

**Default value:** false

**Example**:\
 \

~~~~ {.verbatim}
     
     body select_region BracketSection(x)
     {
     select_start => "$(x) \{";
     select_end => "}";
     include_end_delimiter => "true";
     }
     
~~~~

**Notes**:\
 \

In a sectioned file, the line that marks the end of a section is not
normally included in the defined region; that is, it is recognized as a
delimiter, but it is not included as one of the lines available for
editing. Setting this option to true makes it included. For example:

~~~~ {.verbatim}
     /var/log/mail.log {
         monthly
         missingok
         notifempty
         rotate 7
         }
~~~~

The section does not normally include the line containing }. By setting
`include_end_delimiter` to trueit would be possible for example, to
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
(2010) \

`select_start`

**Type**: string

**Allowed input range**: `.*`

**Synopsis**: Regular expression matching start of edit region

**Example**:\
 \

~~~~ {.verbatim}
     
     body select_region example(x)
     
     {
     select_start => "\[$(x)\]";
     select_end => "\[.*\]";
     }
     
~~~~

**Notes**:\
 \

See also `select_end`. These delimiters mark out the region of a file to
be edited. In the example, it is assumed that the file has section
markers.

~~~~ {.smallexample}
          [section 1]
          
          lines.
          lines...
          
          
          [section 2]
          
          lines ....
          etc..
          
~~~~

The start marker includes the first matched line. \

`select_end`

**Type**: string

**Allowed input range**: `.*`

**Synopsis**: Regular expression matches end of edit region from start

**Example**:\
 \

~~~~ {.verbatim}
     
     body select_region example(x)
     
     {
     select_start => "\[$(x)\]";
     select_end => "\[.*\]";
     }
     
~~~~

**Notes**:\
 \

See also `select_start`. These delimiters mark out the region of a file
to be edited. In this example, it is assumed that the file has section
markers:

~~~~ {.smallexample}
          [section 1]
          
          lines.
          lines...
          
          
          [section 2]
          
          lines ....
          etc..
          
~~~~

If you want to match from a starting location to the end of the file
(even if there are other lines matching `select_start` intervening),
then just omit the `select_end` promise and the selected region will run
to the end of the file.
