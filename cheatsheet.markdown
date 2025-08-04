---
layout: printable
title: Markdown cheatsheet
sorting: 1
alias: markdown-cheatsheet.html
---

Markdown formatting is simple, and the CFEngine generator adds a few things
to make it even simpler. Here's a list of the most commonly used formats.

**Remember:** _Always pull never push_

## Basic formatting

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

`_Italic_` _Italic_

### Heading levels

The number of `#` characters at the beginning of a line signifies the heading level (outside of a code block):

```markdown
# Level 1 (<h1>)

## Level 2 (<h2>)

### Level 3 (<h3>)

#### Level 4 (<h4>)

##### Level 5 (<h5>)

###### Level 6 (<h6>)
```

### Links

#### Link within documentation and to known pages

You can link to any documentation page using `[linktext][PageTitle]`.

##### Link to a specific section of a known page

You can link to any documentation page section using `[linktext][PageTitle#section]`.

When linking to a section, you should use the section name as it is rendered on the page.

For example, On the [functions][Functions] page we can link to the [collecting functions][Functions#collecting functions] section using `[collecting functions][Functions#collecting functions]`.

Sometimes (because `¯\_(ツ)_/¯`, maybe the page linked to hasn't been parsed yet) a page may not be automatically known. In this case an entry in [\_references.md](https://github.com/cfengine/documentation/blob/master/generator/_references.md).

###### Special characters in link targets

See generator/\_scripts/cfdoc_linkresolver.py for how various characters are changed to dashes (--, ,:,.,(,)) and erased (").
Dashes are removed from the beginning and end of links as well.

_Most_ (`¯\_(ツ)_/¯`) special characters are _okay_. For example:

- Link targets with `/` (forward slashes) work
  - `[Export/import][Settings#Export/import]` == [Export/import][Settings#Export/import]

Anchors with _underscores_ are problematic, _may_ need to be escaped.

For example `services_autorun` in the MPF documentation the underscore needs to be escaped with a `\`.

```
**See also:** [`services_autorun` in the Masterfiles Policy Framework][Masterfiles Policy Framework#services\_autorun]
```

**See also:** [`services_autorun` in the Masterfiles Policy Framework][Masterfiles Policy Framework#services\_autorun]

But not always! For example

```
**See also:** [cf_lock.lmdb][CFEngine directory structure#state/cf_lock.lmdb]
```

**See also:** [cf_lock.lmdb][CFEngine directory structure#state/cf_lock.lmdb]

Backticks are problematic. It seems impossible to link to anchors that contain backticks.

#### Link to CFEngine keyword

The documentation pre-processor will create those automatically.

```
`classes` and `readfile()`
```

<!--- cheat - otherwise we get ambiuous link target warnings -->

[`classes`][classes] and `readfile()`

However, the preprocess will not create links if the code word is in triple backticks:

    No links: ```classes``` and ```readfile()```

No links: `classes` and `readfile()`

#### Link to external URL

`[Markdown Documentation](http://daringfireball.net/projects/markdown/)`

[Markdown Documentation](http://daringfireball.net/projects/markdown/syntax)

### Lists

#### Unordered lists - Use dashes

We use dashes:

```markdown
- Item 1
- Item 2
  - Item 2a
- Multi paragraph item
  Indented with spaces to same level
```

- Item 1
- Item 2
  - Item 2a
- Multi paragraph item
  Indented with spaces to same level

#### Ordered lists - the numbers you use don't matter.

```
1. first
1. second
1. third
```

1. first
1. second
1. third

(Either use all 1's, or the correct numbers, 1., 2., 3.,).

#### Nested lists

```markdown
- Item 1
  1. First
  1. Second
  1. ABC
- Item 2
  - Item 2a (2 spaces)
    I am indented to the same level as 2a
- Multi paragraph item
  I am indented 2 spaces
```

- Item 1
  1. First
  2. Second
  3. ABC
- Item 2
  - Item 2a (2 spaces)
    I am indented to the same level as 2a
- Multi paragraph item
  I am indented 2 spaces

### Tables

Wiki-syntax for tables is supported, and you can be a bit sloppy
about it, although it's better to align the `|` properly.

```markdown
| Header | Left aligned | Centered | Right aligned |
| ------ | :----------- | :------: | ------------: |
| text   | text         |    X     |           234 |
```

| Header | Left aligned | Centered | Right aligned |
| ------ | :----------- | :------: | ------------: |
| text   | text         |    X     |           234 |

### Code

#### Inline code

    This renders as `inline code`.

This renders as `inline code`.

    This also renders as ```inline code```.

This also renders as `inline code`.

See the note above on implicit linking - single backticks will link, triple backticks won't.

#### Code blocks

Start a code block using triple backticks:

    ```
    some code
    in a block
    ```

```
some code
in a block
```

You can also create a code block by indenting your code by 4 spaces,
however this does not support syntax highlighting and triple backticks are preferred.

To turn on syntax highlighting, specify the language ("brush") directly after the opening three backticks.
Syntax highlighting is provided by pygments. Find all available lexers [here](http://pygments.org/docs/lexers/).

##### Command code blocks

```command
python3 -v
```

This code block will have `command` in the header and corresponding icon.

##### Command code block with output

To have a component that shows command, and it's output you need to place output code block following command one.

```command
uname
```

```output
Linux
```

You might also specify output syntax highlighting by adding language
after the starting backticks and placing `[output]` in the first line.
This line won't be shown in the resulted HTML.

```command
curl --user admin:admin https://test.cfengine.com/api/user
```

```json {output}
{
  "meta": { "page": 1, "count": 1, "total": 1, "timestamp": 1350994249 },
  "data": [
    { "id": "calvin", "external": true, "roles": ["Huguenots", "Marketing"] }
  ]
}
```

These two blocks will be joined into one element on the UI.

##### File code block

You can specify file name of the code block by adding `{file="<filename>"}` after the language specifier (i.e. on the end of the same line as the triple backticks and `cf3`).
This metadata won't be shown in the resulting HTML (it will be converted to the heading / frame).

```cf3 {file="policy.cf"}
bundle agent hello_world
{
  meta:
    "tags"
      slist => { "autorun" };
  vars:
    "github_path"
      string => "/tmp/github.com";
}
```

The resulting code block will show `policy.cf` as the filename.

##### CFEngine code blocks

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

Other frequently used syntax highlighters shown below.

##### Bash script code blocks

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

##### SQL code blocks

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

##### Diff code blocks

        ```diff
        diff --git a/README.md b/README.md
        index 92555a2..b49c0bb 100644
        --- a/README.md
        +++ b/README.md
        @@ -377,8 +377,12 @@ As a general note, avoiding abbreviations provides better readability.

         * follow the [Policy style guide](guide/writing-and-serving-policy/policy-style.markdown)
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

 * follow the [Policy style guide](guide/writing-and-serving-policy/policy-style.markdown)
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

##### JSON code blocks

{% raw %}

```json
{
  "classes": { "services_autorun": ["any"] }
}
```

{% endraw %}

```json
{
  "classes": { "services_autorun": ["any"] }
}
```

##### YAML code blocks

{% raw %}

```yaml
---
classes:
  services_autorun:
    - "any"
```

{% endraw %}

```yaml
---
classes:
  services_autorun:
    - "any"
```

#### Code blocks and lists

If you want to include a code block within a list, align it just as you would with a sentence, and use triple backticks:

    1. First

       ```cf3
       # CFEngine block

       bundle agent example() {}
       ```

    2. Second
    3. Third

1. First

   ```cf3
   # CFEngine block

   bundle agent example() {}
   ```

2. Second
3. Third

### Headers

#### Horizontal bar

`---`

---

## CFEngine extensions - custom macros

### Include example policy from core

Examples from cfengine/core can be rendered using the `CFEngine_include_example` macro.

- Lines inside `src` starting with `#@ ` are interpreted as markdown.

- Wrap macro in `raw` and `endraw` tags if the file contains mustache. This allows it to be rendered correctly.

  `[\%CFEngine_include_example(class-automatic-canonificiation.cf)\%]`

  {% raw %}
  [%CFEngine_include_example(class-automatic-canonificiation.cf)%]
  {% endraw %}

### Include snippet of text from a file

Sometimes it's nice to include a snippet from another file. For example, we dynamically generate the `--help` output for each component on each doc build and that output is included on each component page.

`[%CFEngine_include_snippet(cf-promises.help, [\s]*--[a-z], ^$)%]`

[%CFEngine_include_snippet(cf-promises.help, [\s]*--[a-z], ^$)%]

---

### Including external files

Sometimes it's nice to include an external file

<pre>
[%CFEngine_include_markdown(masterfiles/CHANGELOG.md)%]
</pre>

#### Including chunks of policy from the MPF

Here I am including a bundle named `cfe_autorun_inventory_listening_ports`. It may be a common or an agent bundle (in case the bundle ever changes types).

<pre>
[%CFEngine_include_snippet(inventory/any.cf, bundle\s+(agent|common)\s+cfe_autorun_inventory_listening_ports, \})%]
</pre>

[%CFEngine_include_snippet(inventory/any.cf, bundle\s+(agent|common)\s+cfe_autorun_inventory_listening_ports, \})%]

### Comments inside documentation

Sometimes it's nice to be able to put an internal comment into the
documentation that will not be rendered.

You can use the comment and endcomment tags in markdown files.

For example:

```
{% raw %}
{% comment %} TODO: We should try to improve this at some point.{% endcomment %}
{% endraw %}
```

Would render like this:

```
{% comment %} TODO: We should try to improve this at some point.{% endcomment %}
```

## FAQ

### When should I use `verbatim` vs **bold** or _italic_?

If it's code or something you would see on the command line (policy language, file names, command line options, binaries / CLI programs) use monospace (single backticks for inline, triple backticks for block, or when you have inline word that could also be an automatic link target that is undesirable, e.g. `files` ({% raw %}`files`{% endraw %}) vs `files` ({% raw %}`files`{% endraw %}) ).

If you are referring to something within UI / screenshots / buttons etc use bold and capitalize it as it is within the UI/Button/whatever.

**References:**

- https://www.patternfly.org/v4/ux-writing/punctuation/
- https://docs.microsoft.com/en-us/style-guide/procedures-instructions/formatting-text-in-instructions

## Sandbox

### symlink example

[%CFEngine_include_snippet(masterfiles/lib/files.cf, ^body\slink_from\sln_s.*, ^##)%]

### Self documenting policy

#### For the stdlib:

[%CFEngine_library_include(lib/commands)%]

#### For update.cf?

[%CFEngine_library_include(update)%]

#### for promises.cf?

[%CFEngine_library_include(promises)%]

## Variables

Referencing a version of CFEngine? Consider if that appearance should be
updated with each new version.

Variables that are defined in the front matter (thats the content between the
three dashes at the top) or in
[\_config.yaml](https://github.com/cfengine/documentation/blob/master/generator/_config.yml)
can be used directly within markdown.

For example this is the '{{site.CFE_manuals_version}}' version of the
documentation. That variable comes from \_config.yaml.

Since liquid variables look a lot like mustache variables any time you want to
show the actual variables will need to be inside of raw tags.

{% raw %}
site.CFE_manuals_version {{ site.CFE_manuals_version }}
{% endraw %}

## Testing

### Indention with included markdown

1. Verify that the selected hosts are upgrading successfully.

   - Mission Portal [Inventory reporting interface][Reporting UI#inventory management]

   - [Inventory API][Inventory API]

     ```console
     root@hub:~# curl -k \
     --user <admin>:<password> \
     -X POST \
     https://hub.localdomain/api/inventory  \
     -H 'content-type: application/json' \
     -d '{
           "sort":"Host name",
           "filter":{
              "CFEngine version":{
                 "not_match":"{{site.cfengine.branch}}.0"
              }
           },
           "select":[
              "Host name",
              "CFEngine version"
            ]
         }'
     ```

2. Some other thing
