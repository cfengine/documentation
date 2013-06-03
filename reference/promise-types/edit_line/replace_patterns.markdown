---
layout: default
title: replace_patterns
categories: [Reference, Promise Types, files, edit_line, replace_patterns]
published: true
alias: reference-promise-types-files-edit_line-replace_patterns.html
tags: [reference, bundles, agent, replace_patterns, edit_line, files promises]
---

This promise refers to arbitrary text patterns in a file. The pattern is
expressed as a PCRE regular expression.

```cf3
     
       replace_patterns:
     
        "search pattern"
     
           replace_with = replace_body,
           ...;
     
```

  

```cf3
bundle edit_line upgrade_cfexecd
{
  replace_patterns:

    "cfexecd" replace_with => value("cf-execd");
}

########################################

body replace_with value(x)  # defined in cfengine_stdlib.cf
{
replace_value => "$(x)";
occurrences => "all";
}
```

  

This is a straightforward search and replace function. Only the portion
of the line that matches the pattern in the promise will be replaced;
the remainder of the line will not be affected. You can also use PCRE
lookbehind and lookahead patterns to restrict the lines upon which the
pattern will match.

**NOTE:** In `replace_patterns` promises, the regular expression may
match a line fragment, that is, it is unanchored.

See: [Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)

-   [replace\_with in
    replace\_patterns](#replace_005fwith-in-replace_005fpatterns)

### replace_with

**Type**: `body replace_with`

#### occurrences

**Type**: (menu option)

**Allowed input range**:   

```cf3
                    all
                    first
```

**Description**: Menu option to replace all occurrences or just first (NB
the latter is non-convergent)

**Default value:** all

**Example**:

```cf3
     
     body replace_with example
     {
     occurrences => "first";        # Warning! Using "first" is non-convergent
     }
     
```

**Notes**:
A policy for string replacement.

Using "first" is generally unwise, as it will change a different
matching string each time the promise is executed, and may not "catch
up" with whatever external action is altering the text the promise
applies to.   

#### replace_value

**Type**: `string`

**Allowed input range**: `.*`

**Description**: Value used to replace regular expression matches in search

**Example**:

```cf3
     
     body replace_with example(s)
     {
     replace_value => "$(s)";
     }
     
```

**Notes**:  
   
