---
layout: default
title: Pattern Matching and Referencing
published: true
sorting: 80
tags: [manuals, language, syntax, concepts, pattern, regexp, matching]
---

One of the strengths of CFEngine 3 is the ability to recognize and exploit
patterns. All string patterns in CFEngine 3 are matched using PCRE regular
expressions.

CFEngine has the ability to extract back-references from pattern matches. This
makes sense in two cases. Back references are fragments of a string that match
parenthetic expressions. For instance, suppose we have the string:

    Mary had a little lamb ...

and apply the regular expression


    "Mary ([^l]+)little (.*)"

The pattern matches the entire string, and it contains two parenthesized
subexpressions, which respectively match the fragments `had a ` and `lamb
...`. The regular expression libraries assign three matches to this result,
labelled 0, 1 and 2.

The zeroth value is the entire string matched by the total expression. The
first value is the fragment matched by the first parenthesis, and so on.

Each time CFEngine matches a string, these values are assigned to a special
variable context `$(match.n)`. The fragments can be referred to in the remainder
of the promise. There are two places where this makes sense. One is in pattern
replacement during file editing, and the other is in searching for files.

Consider the examples below:

```cf3

    bundle agent testbundle
    {
    files:

      # This might be a dangerous pattern - see explanation in the next section

      # on "Runaway change warning"


      "/home/mark/tmp/cf([23])?_(.*)"
           edit_line => myedit("second backref: $(match.2)");
    }
```

There are other filenames that could match this pattern, but if, for example,
there were to exist a file `/home/mark/tmp/cf3_test`, then we would have:

    ‘$(match.0)’
    equal to `/home/mark/tmp/cf3_test'
    ‘$(match.1)’
    equal to `3'
    ‘$(match.2)’
    equal to `test'

Note that because the pattern allows for an optional '2' or '3' to follow the
letters `cf`, it is possible that `$(match.1)` would contain the empty string.
For example, if there was a file named `/home/mark/tmp/cf_widgets`, then we
would have

    ‘$(match.0)’
    equal to `/home/mark/tmp/cf_widgets'
    ‘$(match.1)’
    equal to `'
    ‘$(match.2)’
    equal to `widgets'

Now look at the edit bundle. This takes a parameter (which is the
back-reference from the filename match), but it also uses back references to
replace shell comment lines with C comment lines (the same approach is used to
hash-comment lines in files). The back-reference variables `$(match.n)` refer
to the most recent pattern match, and so in the `C_comment` body, they do not
refer to the filename components, but instead to the hash-commented line in
the `replace_patterns` promise.

```cf3
    bundle edit_line myedit(parameter)
    {
      vars:

       "edit_variable" string => "private edit variable is $(parameter)";

      insert_lines:

         "$(edit_variable)";

      replace_patterns:

      # replace shell comments with C comments

       "#(.*)"

          replace_with => C_comment,
         select_region => MySection("New section");
      }

    ########################################
    # Bodies
    ########################################

    body replace_with C_comment
    {
    replace_value => "/* $(match.1) */"; # backreference from replace_patterns
    occurrences => "all";  # first, last, or all
    }

    ########################################################

    body select_region MySection(x)
    {
        select_start => "\[$(x)\]";
        select_end => "\[.*\]";
    }
```	

Try this example on the file

    [First section]
    one
    two
    three

    [New section]
    four
    #five

    six

    [final]
    seven
    eleven


The resulting file is edited like this:

    [First section]

    one
    two
    three

    [New section]

    four
    /* five */
    six

    [final]

    seven
    eleven

    private edit variable is second backref: test

### Runaway change warning

Be careful when using patterns to search for files that are altered by
CFEngine if you are not using a file repository. Each time CFEngine makes a
change it saves an old file into a copy like `cf3_test.cf-before-edit`. These
new files then get matched by the same expression above – because it ends in
the `generic.*`), or does not specify a tail for the expression. Thus CFEngine
will happily edit backups of the edit file too, and generate a recursive
process, resulting in something like the following:

     cf3_test                  cf3_test.cf-before-edit
     cf3_test~                 cf3_test~.cf-before-edit.cf-before-edit
     cf3_test~.cf-before-edit  cf3_test~.cf-before-edit.cf-before-edit.cf-before-edit

Always try to be as specific as possible when specifying patterns. A lazy
approach will often come back to haunt you.

### Commenting lines

The following example shows how you would hash-comment lines in a file using
CFEngine.

```cf3
    ######################################################################
    #
    # HashCommentLines implemented in CFEngine 3
    #
    ######################################################################


    body common control
    {
        version => "1.2.3";
        bundlesequence  => { "testbundle"  };
    }

    ########################################################

    bundle agent testbundle
    {
    files:
      "/home/mark/tmp/comment_test"
           create    => "true",
           edit_line => comment_lines_matching;
    }

    ########################################################


    bundle edit_line comment_lines_matching
      {
      vars:

        "regexes" slist => { "one.*", "two.*", "four.*" };

      replace_patterns:

       "^($(regexes))$"
          replace_with => comment("# ");
      }

    ########################################
    # Bodies
    ########################################


    body replace_with comment(c)
    {
        replace_value => "$(c) $(match.1)";
        occurrences => "all";
    }
```

### Regular expressions in paths

When applying regular expressions in paths, the path will first be split at
the path separators, and each element matched independently. For example, this
makes it possible to write expressions like `/home/.*/file` to match a single
file inside a lot of directories — the `.*` does not eat the whole string.

Note that whenever regular expressions are used in paths, the `/` is always
used as the path separator, even on Windows. However, on Windows, if the
pathname is interpreted literally (no regular expressions), then the backslash
is also recognized as the path separator. This is because the backslash has a
special (and potentially ambiguous) meaning in regular expressions (a `\d`
means the same as `[0-9]`, but on Windows it could also be a path separator
and a directory named `d`).

The `pathtype` attribute allows you to force a specific behavior when
interpreting pathnames. By default, CFEngine looks at your pathname and makes
an educated guess as to whether your pathname contains a regular expression.
The values `literal` and `regex` explicitly force CFEngine to interpret the
pathname either one way or another. (see the `pathtype` attribute).

```cf3
    body common control
    {
        bundlesequence => { "wintest" };
    }

    ########################################


    bundle agent wintest
    {
    files:
      "c:/tmp/file/f.*"		# "best guess" interpretation
        delete => nodir;


      "c:\tmp\file"
        delete => nodir,
        pathtype => "literal";	# force literal string interpretation


      "C:/windows/tmp/f\d"
        delete => nodir,
        pathtype => "regex";	# force regular expression interpretation
    }

    ########################################


    body delete nodir
    {
        rmdirs => "false";
    }
```

Note that the path `/tmp/gar.*` will only match filenames like `/tmp/gar`,
`/tmp/garbage` and `/tmp/garden`. It will not match filename like
`/tmp/gar/baz` (because even though the `.*` in a regular expression means
"zero or more of any character", CFEngine restricts that to mean "zero or more
of any character in a path component"). Correspondingly, CFEngine also
restricts where you can use the `/` character (you can't use it in a character
class like `[^/]` or in a parenthesized or repeated regular expression
component.

This means that regular expressions which include "optional directory
components" won't work. You can't have a files promise to tidy the directory
`(/usr)?/tmp`. Instead, you need to be more verbose and specify
`/usr/tmp|/tmp`, or even better, think declaratively and create an `slist`
that contains both the strings `/tmp` and `/usr/tmp`, and then allow CFEngine
to iterate over the list!

This also means that the path `/tmp/.*/something` will match files like
`/tmp/abc/something` or `/tmp/xyzzy/something`. However, even though the
pattern `.*` means "zero or more of any character (except `/`)", CFEngine
matches files bounded by directory separators. So even though the pathname
`/tmp//something` is technically the same as the pathname `/tmp/something`,
the regular expression `/tmp/.*/something` will not match on the degenerate
case of `/tmp//something` (or `/tmp/something`).

### Anchored vs. unanchored regular expressions

CFEngine uses the full power of regular expressions, but there are two
“flavors” of regex. Because they behave somewhat differently (while still
utilizing the same syntax), it is important to know which one is used for a
particular component of CFEngine:

An “anchored” regular expression will only successfully match an entire
string, from start to end. An anchored regular expression behaves as if it
starts with `^` and ends with `$`, whether you specify them yourself or not.
Furthermore, an anchored regular expression cannot have these automatic
anchors removed.

An “unanchored” regular expression may successfully match anywhere in a
string. An unanchored regex may use anchors (such as `^`, `$`, `\A`, `\Z`,
`\b`, etc.) to restrict where in the string it may match. That is, an
unanchored regular expression may be easily converted into a partially- or
fully-anchored regex.

For example, the comment parameter in [`readstringarray()`][readstringarray]
is an unanchored regex. If you specify the regular expression as `#.*`, then
on any line which contains a pound sign, everything from there until the end
of the line will be removed as a comment. However, if you specify the regular
expression as `^#.*` (note the `^` anchor at the start of the regex), then
only lines which start with a `#` will be removed as a comment! If you want to
ignore C-style comment in a multi-line string, then you have to a bit more
clever, and use this regex: `(?s)/\*.*?\*/`

Conversely, `delete_lines` promises use anchored regular expressions to delete
lines. If our promise uses `bob:\d*` as a line-matching regex, then only the
second line of this file will be deleted (because only the second line starts
with `bob:` and is then followed exclusively by digits, all the way to the end
of the string).

    bobs:your:uncle
    bob:111770
    thingamabob:1234
    robert:bob:xyz
    i:am:not:bob

If CFEngine expects an unanchored regular expression, then finding every line
that contains the letters `bob` is easy. You just use the regex `bob`. But if
CFEngine expects an anchored regular expression, then you must use `.*bob.*`.

If you want to find every line that has a field which is exactly `bob` with no
characters before or after, then it is only a little more complicated if
CFEngine expects an unanchored regex: `(^|:)bob(:|$)`. But if CFEngine expects
an anchored regular expression, then it starts getting ugly, and you'd need to
use `bob:.*|.*:bob:.*|.*:bob`.


### Special topics on Regular Expressions

Regular expressions are a complicated subject, and really are beyond the scope
of this document. However, it is worth mentioning a couple of special topics
that you might want to know of when using regular expressions.

The first is how to not get a back reference. If you want to have a
parenthesized expression that does not generate a back reference, there is a
special PCRE syntax to use. Instead of using `()` to bracket the piece of a
regular expression, use `(?:)` instead. For example, this will match the
filenames foolish, foolishly, bearish, bearishly, garish, and garishly in the
`/tmp` directory. The variable `$match.0` will contain the full filename, and
`$match.1` will either contain the string `ly` or the empty string. But the
`(?:expression)` which matches foo, bear, or gar does not create a
back-reference:

```cf3
    files:
        "/tmp/(?:foo|bear|gar)ish(ly)?"
```

Note that sometimes multi-line strings are subject to be matched by regular
expressions. CFEngine internally matches all regular expressions using
PCRE_DOTALL option, so `.` matches newlines. If you want to match any
character except newline you could use `\N` escape sequence.

Another thing you might want to do is ignore capitalization. CFEngine is
case-sensitive (in all things), so the files promise `/tmp/foolish` will not
match the files `/tmp/Foolish` or `/tmp/fOoLish`, etc. There are two ways to
achieve case-insensitivity. The first is to use character classes:

```cf3
    files:
        "/tmp/[Ff][Oo][Oo][Ll][Ii][Ss][Hh]"
```

While this is certainly correct, it can also lead to unreadability. The PCRE
patterns in CFEngine have another way of introducing case-insensitivity into a
pattern:

```cf3
    files:
        "/tmp/(?i:foolish)"
```

The `(?i:)` brackets impose case-insensitive matching on the text that it
surrounds, without creating a sub-expression. You could also write the regular
expression like this (but be aware that the two expressions are different, and
work slightly differently, so check the documentation for the specifics):

```cf3
    files:
        "/tmp/(?i)foolish"
```

The `/s`, `/m`, and `/x` switches from PCRE are also available, but use them
with great care!

