---
layout: default
title: Markdown Cheatsheet
published: true
sorting: 1
alias: markdown-cheatsheet.html
---

Markdown formatting is simple, and the CFEngine generator adds a few things
to make it even simpler. Here's a list of the most commonly used formats.

## Basic Formatting

```
One
Paragraph

Two
Paragraphs
```

One
Paragraph

Two
Paragraphs


`**Bold**` **Bold**

`*Italic*` *Italic*


## Links

### Link within documentation and to known pages

`[top of the page][Markdown Cheatsheet] and [inside page][Markdown Cheatsheet#Links]`

[top of the page][Markdown Cheatsheet] and [inside page][Markdown Cheatsheet#Links]

**Note:** For known pages, see the 
[_references.markdown](https://github.com/cfengine/documentation-generator/blob/master/_references.md)
file.

### Link to CFEngine keyword

The documentation pre-processor will create those automatically.

```
`classes` and `readfile()`
```

`classes` and `readfile()`

### Link to External URL

`[Markdown Documentation](http://daringfireball.net/projects/markdown/)`

[Markdown Documentation](http://daringfireball.net/projects/markdown/syntax)


## Lists

Unordered lists - Markdown supports other markers than the asterisk, but in 
CFEngine we use only `*`.

```
* Item 1
* Item 2
   * Item 2a
* Multi paragraph item

    Four spaces indented
```

* Item 1
* Item 2
   * Item 2a
* Multi paragraph item

    Four spaces indented



Ordered lists - the numbers you use don't matter.

```
1. first
1. second
9. Third
```

1. first
1. second
9. Third

## Tables

Wiki-syntax for tables is supported, and you can be a bit sloppy
about it, although it's better to align the `|` properly.

```
| Header | Left aligned | Centered | Right aligned |
|--------|:-------------|:--------:|--------------:|
|text    | text | X | 234 |
```

| Header | Left aligned | Centered | Right aligned |
|--------|:-------------|:--------:|--------------:|
|text    | text | X | 234 |


## Code

### Code Blocks

Just indent by four spaces:

```
    $ code block
    $ without syntax highlighting
```

    $ code block
    $ without syntax highlighting

If you want CFEngine syntax highlighting, use

    ```cf3
        # CFEngine block
    
        bundle agent example()
        {
        }
    ```

```cf3
    # CFEngine code block

    bundle agent example()
    {
    }
```

Other frequently used syntax highlighers are:

* bash

		```bash
		#!/bin/bash
        echo hi
        for i in `seq 1 10`;
        do
          echo $i
        done
		```

```bash
#!/bin/bash
echo hi
for i in `seq 1 10`;
do
  echo $i
done
```

* shell session

		```shell-session
		root@policy_server # /etc/init.d/cfengine3 stop
		```

```shell-session
	root@policy_server # /etc/init.d/cfengine3 stop
```




* sql

		```sql
	    SELECT
	         FileChanges.FileName,
	         Count(Distinct(FileChanges.HostKey)) AS DistinctHostCount,
	         COUNT(1) AS ChangeCount
	      FROM
	         FileChanges JOIN Contexts
	      WHERE 
	         Contexts.ContextName='ubuntu'
	      GROUP BY
	         FileChanges.FileName
	      ORDER BY
	         ChangeCount DESC
		```

```sql
SELECT
     FileChanges.FileName,
     Count(Distinct(FileChanges.HostKey)) AS DistinctHostCount,
     COUNT(1) AS ChangeCount
  FROM
     FileChanges JOIN Contexts
  WHERE 
     Contexts.ContextName='ubuntu'
  GROUP BY
     FileChanges.FileName
  ORDER BY
     ChangeCount DESC
```

* diff

		```diff
		diff --git a/README.md b/README.md
		index 92555a2..b49c0bb 100644
		--- a/README.md
		+++ b/README.md
		@@ -377,8 +377,12 @@ As a general note, avoiding abbreviations provides better readability.
 
		 * follow the [Policy Style Guide](manuals/policy-style.markdown)
		   in examples and code snippets
		-* always run it through Pygments plus the appropriate lexer (only cf3
		-  supported for now)
		+* always run it through Pygments plus the appropriate lexer
		+
		+Most important are the `cf3` lexer, as well as `bash`, `console`,
		+`diff`, `shell-session` and `postgresql`. But Jekyll supports
		+[many more lexers](http://pygments.org/docs/lexers/)
		+
		 * avoid custom color schemes and hand-coded HTML
		 * document the example after the example code
		```

```diff
diff --git a/README.md b/README.md
index 92555a2..b49c0bb 100644
--- a/README.md
+++ b/README.md
@@ -377,8 +377,12 @@ As a general note, avoiding abbreviations provides better readability.

 * follow the [Policy Style Guide](manuals/policy-style.markdown)
   in examples and code snippets
-* always run it through Pygments plus the appropriate lexer (only cf3
-  supported for now)
+* always run it through Pygments plus the appropriate lexer
+
+Most important are the `cf3` lexer, as well as `bash`, `console`,
+`diff`, `shell-session` and `postgresql`. But Jekyll supports
+[many more lexers](http://pygments.org/docs/lexers/)
+
 * avoid custom color schemes and hand-coded HTML
 * document the example after the example code
```


**Notes:** You need to keep an empty line in front of the code block. And
to put code into a list item, the code needs to be indented *twice*, ie:

```
* List item with code

        <code goes here>
```

* List item with code

        <code goes here>

### Inline code

    This renders as `inline code`.

This renders as `inline code`.

*****

## Headers

### Horizontal bar

`***`

***

`# Level 1`

# Level 1

`## Level 2`

## Level 2

`### Level 3`

### Level 3

`#### Level 4`

#### Level 4

`##### Level 5`

##### Level 5

`###### Level 6`

###### Level 6

*****
