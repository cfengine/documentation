---
layout: default
title: replace_patterns
published: true
tags: [reference, bundle agent, edit_line, files promises, file editing]
---

This promise refers to arbitrary text patterns in a file. The pattern is
expressed as a PCRE regular expression.

```cf3
       replace_patterns:

        "search pattern"

           replace_with => replace_body,
           ...;
```

In `replace_patterns` promises, the regular expression may
match a line fragment, that is, it is [unanchored][unanchored].

```cf3
    bundle edit_line upgrade_cfexecd
    {
      replace_patterns:

        "cfexecd" replace_with => value("cf-execd");
    }

    body replace_with value(x)  # defined in cfengine_stdlib.cf
    {
    replace_value => "$(x)";
    occurrences => "all";
    }
```

This is a straightforward search and replace function. Only the portion
of the line that matches the pattern in the promise will be replaced;
the remainder of the line will not be affected. You can also use PCRE
look-behind and look-ahead patterns to restrict the lines upon which the
pattern will match.

****

## Attributes ##

### replace_with

**Type:** `body replace_with`

**See also:** [Common Body Attributes][Promise Types and Attributes#Common Body Attributes]

#### occurrences

**Description:** Defines which occurrences should be replaced.

Using "first" is generally unwise, as it will change a different
matching string each time the promise is executed, and may not "catch
up" with whatever external action is altering the text the promise
applies to.

**Type:** (menu option)

**Allowed input range:**

* `all`

Replace all occurrence.

* `first`

Replace only the first occurrence. Note: this is non-convergent.

**Default value:** all

**Example:**

```cf3
     body replace_with example
     {
     occurrences => "first";        # Warning! Using "first" is non-convergent
     }
```

#### replace_value

**Description:** Value used to replace regular expression matches in search

**Type:** `string`

**Allowed input range:** `.*`

**Example:**

```cf3
     body replace_with example(s)
     {
     replace_value => "$(s)";
     }
```

### select_region

**Description:** Constrains `edit_line` operations to region identified by matching regular expressions.

This body applies to all promise types within `edit_line` bundles.

**See Also:** [```select_region``` with `edit_line` operations][edit_region#select_region], [```select_region``` in `delete_lines`][delete_lines#select_region], [```select_region``` in `field_edits`][field_edits#select_region], [```select_region``` in `insert_lines`][insert_lines#select_region]

