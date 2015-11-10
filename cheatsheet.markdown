---
layout: printable
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

`[top of the page][Markdown Cheatsheet], to the [Markdown Cheatsheet][], [inside page][Markdown Cheatsheet#Links] and [inside current page][#Links]`

<!--- Cheating here - this page is not published, so included from link map -->
[top of the page](markdown-cheatsheet.html), to the [Markdown Cheatsheet](markdown-cheatsheet.html), [inside page](markdown-cheatsheet.html#Links) and [inside current page](markdown-cheatsheet.html#Links)

**Note:** For known pages, see the 
[_references.md](https://github.com/cfengine/documentation-generator/blob/master/_references.md)
file.

### Link to CFEngine keyword

The documentation pre-processor will create those automatically.

```
`classes` and `readfile()`
```

<!--- cheat - otherwise we get ambiuous link target warnings -->
[`classes`][classes] and `readfile()`

However, the preprocess will not create links if the code word is in triple backticks:


    ```classes``` and ```readfile()```

```classes``` and ```readfile()```

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

### Inline code

    This renders as `inline code`.

This renders as `inline code`.

    This also renders as ```inline code```.

This also renders as ```inline code```.

See the note above on implicit linking - single backticks will link, triple backticks won't.

### Code Blocks

Code blocks are either indendented by four spaces:

Just indent by four spaces:

```
    $ code block
    $ without syntax highlighting
```

    $ code block
    $ without syntax highlighting

or use three backticks:

    ```
    some more code 
    in a block
    ```

```
some more code
in a block
```

To turn on syntax highlighting, specify the brush directly after the opening three
backticks. Syntax highlighting is provided by pygments. Find all available lexers [here](http://pygments.org/docs/lexers/).

#### CFEngine Code Blocks

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


Other frequently used syntax highlighers shown below.

#### Bash Script Code Blocks

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

#### Console Blocks

        ```console
		root@policy_server # /etc/init.d/cfengine3 stop
        ```

```console
root@policy_server # /etc/init.d/cfengine3 stop
```

#### SQL Code Blocks

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

#### Diff Code Blocks

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


### Code Blocks and Lists

If you want to include a code block within a list, put two tabs (8 spaces) in front of the entire block (4 to make the paragraph part of the list item, and 4 for it a code block):

```
* List item with code

        <code goes here>
```

* List item with code

        <code goes here>


You can also use backticks (and get syntax highlighting) - just make sure the backticks are indented once:

    1. First

    	```cf3
    	# CFEngine block
    
    	bundle agent example()
    	{
    	}
    	```

    2. Second
    3. Third

1. First

	```cf3
	# CFEngine block
    
	bundle agent example()
	{
	}
	```

2. Second
3. Third


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

## Including External Files

Sometimes it's nice to include an external file

<pre>
[%CFEngine_include_markdown(masterfiles/CHANGELOG.md)%]
</pre>


# Sandbox

## symlink example

[%CFEngine_include_snippet(masterfiles/lib/files.cf, ^body\slink_from\sln_s.*, ^##)%]


## Variables

Referencing a version of CFEngine? Consider if that appearance should be updated with each new version. For example on the title page.

Will it expand liquid (mustache) variables?

{% raw %}
site.CFE_manuals_version double mustache {{ site.CFE_manuals_version }}
site.CFE_manuals_version tripple mustache {{{ site.CFE_manuals_version }}}
{% endraw %}

[This jekyll documentation](http://jekyllrb.com/docs/posts/#including-images-and-resources)
indicates that liquid variables like {{ site.url }} can be used directly from
the markdown. Unfortunately it didn't work maybe it will without spaces as in
'{{site.url}}' or maybe its because my _config.yaml does not contain a url key.
it does have site.CFE_manuals_version '{{site.CFE_manuals_version}}'. Maybe I can use {{title}} or {{page.title}}.
