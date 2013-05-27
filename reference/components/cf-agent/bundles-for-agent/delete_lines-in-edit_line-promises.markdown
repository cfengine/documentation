---
layout: default
title: delete_lines
categories: [Reference, Promise Types, edit_line, delete_lines]
published: true
alias: reference-promise-types-files-edit_line-delete_lines.html
tags: [reference, bundles, agent, delete_lines, edit_line, files promises]
---

This promise assures that certain lines exactly matching regular
expression patterns will not be present in a text file. If the lines are
found, the default promise is to remove them (this behavior may be
modified with further pattern matching in `delete_select` and/or changed
with `not_matching`).

  

```cf3
bundle edit_line example
  {
  delete_lines:

    "olduser:.*";

  }
```

Note that typically, only a single line is specified in each
`delete_lines` promise. However, you may of course have multiple
promises that each delete a line.

It is also possible to specify multi-line `delete_lines` promises.
However, these promises will only delete those lines if *all* the lines
are present in the file *in exactly the same order* as specified in the
promise (with no intervening lines). That is, all the lines must match
as a unit for the `delete_lines` promise to be kept.

If the promiser contains multiple lines, then CFEngine assumes that all
of the lines must exist as a contiguous block in order to be deletes.
This gives preserve\_block semantics to any multiline `delete_lines`
promise.

-   [delete\_select in
    delete\_lines](#delete_005fselect-in-delete_005flines)
-   [not\_matching in
    delete\_lines](#not_005fmatching-in-delete_005flines)

#### `delete_select` (body template)

**Type**: (ext body)

`delete_if_startwith_from_list`

**Type**: slist

**Allowed input range**: `.*`

**Notes**:  
   

Delete lines from a file if they begin with the sub-strings listed. Note
that this determination is made only on promised lines (that is, this
attribute modifies the selection criteria, it does not make the initial
selection). 

**Example**:  
   

```cf3
     
     body delete_select example(s)
     {
     delete_if_startwith_from_list => { @(s) };
     }
     
```

If the file contains the following lines, then the following promise initially selects the four lines containing
alpha, but is moderated by the `delete_select` attribute.

```cf3
     start alpha igniter
     start beta igniter
     init alpha burner
     init beta burner
     stop beta igniter
     stop alpha igniter
     stop alpha burner
```

Thus, the promise will delete only the first and third lines of the file:

```cf3
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
```

`delete_if_not_startwith_from_list`

**Type**: slist

**Allowed input range**: `.*`

Delete lines from a file unless they start with the sub-strings in the list given. Note that this determination is made only on promised lines.
In other words, this attribute modifies the selection criteria, it does not make the initial selection.   

**Example**:  
   

```cf3
     
     body delete_select example(s)
     {
     delete_if_not_startwith_from_list => { @(s) };
     }
     
```

`delete_if_match_from_list`

**Type**: slist

**Allowed input range**: `.*`

Delete lines from a file if the lines *completely* match any of the regular expressions listed. In other words, the regular expression is
anchored (see [Anchored vs. unanchored regular expressions](#Anchored-vs_002e-unanchored-regular-expressions)).

Note that this attribute modifies the selection criteria, it does not make the initial selection, and the match determination is made only on
promised lines.   

**Example**:  
   

```cf3
     
     body delete_select example(s)
     {
     delete_if_match_from_list => { @(s) };
     }
     
```

`delete_if_not_match_from_list`

**Type**: slist

**Allowed input range**: `.*`

Delete lines from a file unless the lines *completely* match any of the regular expressions listed. In other words, the regular expressions are
anchored (see [Anchored vs. unanchored regular expressions](#Anchored-vs_002e-unanchored-regular-expressions)).

Note that this attribute modifies the selection criteria, it does not make the initial selection, and the match determination is made only on
promised lines.   

**Example**:  
   

```cf3
     
     body delete_select example(s)
     {
     delete_if_not_match_from_list => { @(s) };
     }
     
```

`delete_if_contains_from_list`

**Type**: slist

**Allowed input range**: `.*`

Delete lines from a file if they contain the sub-strings listed.

Note that this attribute modifies the selection criteria, it does not make the initial selection, and the match determination is made only on
promised lines.   

**Example**:  
   

```cf3
     
     body delete_select example(s)
     {
     delete_if_contains_from_list => { @(s) };
     }
     
```

`delete_if_not_contains_from_list`

**Type**: slist

**Allowed input range**: `.*`

Delete lines from the file which do not contain the sub-strings listed.

Note that this attribute modifies the selection criteria, it does not
make the initial selection, and the match determination is made only on
promised lines.

**Example**:  
   

```cf3
     
     body delete_select discard(s)
     {
     delete_if_not_contains_from_list => { "substring1", "substring2" };
     }
     
```

#### `not_matching`

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

When this option is true, it negates the pattern match of the promised lines.

**NOTE** that this does not negate any condition expressed in `delete_select`. It only negates the match of the initially promised
lines.

Note, this makes no sense for multi-line deletions, and is therefore disallowed. Either a multi-line promiser matches and it should be
removed (i.e. `not_matching` is false), or it does not match the whole thing and the ordered lines have no meaning anymore as an entity. In
this case, the lines can be separately stated.

**Example**:  
   

```cf3
delete_lines:

  # edit /etc/passwd - account names that are not "mark" or "root"

  "(mark|root):.*" not_matching => "true";
```

