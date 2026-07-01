# CFEngine Documentation

This repository holds the sources for the technical
[CFEngine documentation](https://cfengine.com/docs) in
markdown files. If you have a texteditor, know how to write
[markdown](http://daringfireball.net/projects/markdown/syntax) and
English and would like to contribute to the CFEngine documentation, then we'd
like to invite you to collaborate here!

If you would like to notify us about incorrect documentation, but don't have
the time or the knowledge to make a correction directly here, then you can
report the issue in the regular [CFEngine bug
tracker](https://cfengine.com/dev/projects/core).  Use the "Documentation"
category when you create bugs. And of course you can search the bug tracker
for known issues with the documentation, and help the community of
CFEngine users by correcting some of them.

## Writing Documentation

The CFEngine documentation is written in regular
[markdown](http://daringfireball.net/projects/markdown/syntax), with some
extensions as documented below. Check out the
[cheatsheet](https://cfengine.com/docs/master/markdown-cheatsheet.html)!

To keep the source readable in git and workable with a broad range of tools,
keep the line length in paragraphs below 78 characters.

If you don't know git, then you can still contribute to the documentation
using the GitHub interface as long as you have a GitHub account. Fork this
repository (called the *upstream*) using the GitHub web interface, make
changes in your fork and create pull requests so that your changes can be
merged into the *upstream* repository.

It is in general advisable to make small commits that are submitted through
pull requests frequently. Otherwise any structural changes to documentation
content can cause merge conflicts that are hard to resolve.

## Documentation Structure

### Structure

Pages are organized hierarchically in category/subcategory relationships,
corresponding to the organization of the .markdown files in the repository.

The content of the file

    documentation/path/of/categories.markdown

will generate a HTML page

    docs.cfengine.com/version/path-of-categories.html

with equivalent location in the left-hand navigation tree.

The documentation generation inserts a link to the source markdown in the
footer of each page.

### META tags

Additional META tags you should set are:

    layout: default

Leave this as `default`.

    title: "The Title"

The title of the page. Quoting is only necessary if the title contains YAML
keywords (like "on").

    published: true|false

Pages that set this tag to `false` will not be part of the navigation structure.
The HTML content will however be generated.

    tags: [list, of, tags with space, all lowercase]

Keywords for this page, which will be displayed on top of the page, and used
when generating the tag-pages.

    reviewed: yyyy-mm-dd
    reviewed-by: github-user

Keeping track of when a documentation page has last been reviewed.

    sorting: number

Sort order within the parent category. Tip: make jumps in 10's so that pages
can be inserted later.

META tag values will be interpreted literally, and cannot contain `:`, `[` and
`]`.

### Image files

Image files are in the same directory as the markdown files that embed them.
Give files unique names to avoid overwrites in the generated website.

See [Style Guide - Charts and graphs](#Charts_and_graphs) for style
requirements for images.

*Warning:* It is important for images and other binary files to be marked as a
binary file in `.gitattributes`. Binary file patterns not specifically marked
may be mangled and corrupted within git.

### Links

To link to pages within the documentation, use the syntax:

    [Link text][Page Title]

If `Link text` is the title of the target page, you can also use this shorthand:

    [Page Title][]

To link to a section within the target page, use:

    [Link text][Page Title#Section in Page]

To links to sections within the current page, you can also skip the page title:

    [Go to section][#Section in Current Page]

For standard URLs and locations to link to, see the
[mapping](https://github.com/cfengine/documentation-generator/blob/master/_references.md).

#### Automatic linking

The documentation generator automatically creates links for words in code
markers if that word exists as a page or section title.

    **See also:** `attribute_name`, `function()`

This will automatically link to the section or page with title
*attribute_name*. To make explicit links from code words, use
`code` markers in the link text.

    **See also:** [`attribute_name`][page#attributename]

When the word is a function, mark it as such using `()`:

    **See also:** [`classify()`][classify]

Section titles of the form

    ### section title

are included in that automatic linking. To exclude a section header
from that automatic linking, use the form

    ### section title, no linking ###

which is otherwise equivalent for the markdown renderer.

To use keywords in inline code *without* creating an automatic link, use
triple backticks:

    The ```meta``` parameter to this function...

With single backticks, this would link to the documentation of the `meta` attribute or promise type.

### Macros

The documentation generator will pre-process the markdown content
before passing it to Jekyll for the rendering. The pre-processor
understands and replaces the macros. Macros all have the form

`[%CFEngine_MACRO(parameters)%]`

and need to be used as a separate line, as the entire line will be
replaced by the pre-processor.

#### Quoting policy files

The following macros read code from a file and inject the text in
that file into the documentation. Contol comments in the file
and regular expressions passed to the macros can be used to specify
which sections of the file should be injected.

The injected lines will be in a CFEngine code block. Comment lines
(ie lines starting with `#`) are omitted, unless they start with
`#@ `, in which case they interrupt the code block and are rendered
as markdown. All lines between a lines starting with `#[%-%]` and `#[%+%]`
are skipped.

The generator searches for `filename` in the `core/examples`
subdirectory of WKRDIR.

* `[%CFEngine_include_example(filename)%]`

Injects the code from `filename`.

* `[%CFEngine_include_snippet(filename, begin_rx, end_rx [optional])%]`

Searches `filename` for the first line that matches the regular
expression `begin_rx`, and injects all lines as a code block from
there until the first line that matches `end_rx`. If `end_rx` is
omitted, all lines until the end of the file will be injected.

If the line that matches the regular expression is a comment, then
it is excluded from the quote, otherwise it is included.

* `[%CFEngine_include_markdown(filename, begin_rx, end_rx [optional])%]`

Searches `filename` for the first line that matches the regular
expression `begin_rx`, and injects all lines **verbatim** from there
until the first line that matches `end_rx`. If `end_rx` is omitted,
all lines until the end of the file will be injected.

#### Documenting Policy Libraries

* `[%CFEngine_library_include(filename)%]`

Parses the JSON version of the CFEngine policy in `filename` and generates
documentation from it.

The generator searches for the library in JSON format in the `_generated` subdirectory of
the documentation generator. `filename` needs to be provided without file
extension.

The generator parses comments between bundle/body
prototype declaration and the opening `{` as doxygen syntax, supporting
the following tags:

    @brief text

Generates the **Description** section.

    @param attr text

Includes `text` in the documentation for attribute `attr` within the
**Arguments** section.

    @return text

Generates the **Return value** statement.

The content in `text` is then rendered as standard markdown, and can span
multiple lines and paragraphs.

    @ignore

The generator will completely ignore this body or bundle; no documentation
will be emitted.

All comments before the first doxygen-style tag will be ignored.

#### Documenting CFEngine Syntax Elements

The following macros require the syntax map to be generated
via `cf-promises -s` into a file `syntax_map.json` within the
`_generated` subdirectory of the documentation generator.

* `[%CFEngine_function_prototype(arg1, arg2, ...)%]`

Renders the prototype of the function that has the same name as the
title of the current page. Parameters `arg1` etc are used for the names
of the parameters:

```
    **Prototype:** `title(arg1, arg2, ...)`

    **Return type:** `type`
```

Use this before a `**Description:**` section in which the behavior of the
function as well as the individual parameters are then explained.

* `[%CFEngine_function_attributes(arg1, arg2, ...)%]`

Renders a list of attributes for the function that has the same name as the
title of the current page. `arg1` etc are used for the parameter names:

```
    **Arguments:**

    * `arg1`: `type1`, in the range: `regex`
    * `arg2`: `type2`, one of
        * `option1`
        * `option2`
```

Links to known keywords are generated automatically.

Document the individual parameters either directly in the `**Description:**`
section, or as a block after using this macro. You cannot use the macro if
individual options of option-type parameters need detailed explanation.

* `[%CFEngine_promise_attribute(default)%]`

Renders the syntax description of the current promise attribute. The current
markdown needs to comply with the following:

The current page title is assumed to be the promise type. The current level-3
header is assumed to be the attribute name, or - if the current promise
attribute is a body type - the name of the body. In a body type, the current
level 4 header is interpreted to be the body attribute.

**Example:**

```
    ---
    title: promise_type
    ---

    ## Attributes

    ### attribute1

    [%CFEngine_promise_attribute(default)%]

    This will document "attribute1" of "promise_type"

    ### body

    #### attribute1

    [%CFEngine_promise_attribute(default)%]

    This will document "attribute1" of "body"
```

The generated markdown is:

```
    **Type:** `type`

    **Allowed input range:** `range`

    * `option1`
    * `option2`
```

If a `default` parameter is provided, then a `**Default value:**` statement
is created.

* `[%CFEngine_function_table()%]`

Renders a table of built-in functions, grouped by function category.

* `[%CFEngine_syntax_map(subtree)%]`

Renders a nested tree of CFEngine words, starting at `subtree`.

#### Other Macros

* `[%CFEngine_redirect(target)]`

Injects javascript that redirects the current page to the HTML page for `target`,
which needs to be a title or title#section combination as in regular `[text][title#section]`
links.

## Content Style Guide

Make sure you follow this style guide to make using CFEngine and the
documentation a consistent and pleasant experience.

### Writing for the web

* use subheadings to structure content
* keep paragraphs short
* support scanning of pages

### Spelling

CFEngine documentation follows the American spelling.

### Punctuation

**Oxford comma**

In punctuation, a serial comma (also called Oxford comma) needs to be placed
immediately before the conjunction (often “and” or “or”) in a series of three
or more terms.

*Example:*

I would like crackers, cheese, and garlic.

**The comma as a separator between compound sentences**

Use commata to separate independent clauses when they are joined by any of
these seven coordinating conjunctions: and, but, for, or, nor, so, yet.

However, the comma can be dropped in the following cases:

* if both independent clauses are quite short, especially if the two clauses
  are very closely related, and even more so if the subject of both clauses is
  the same, or
* if only the first clause is quite short, especially if the two clauses are
  very closely related, and even more so if the subject of both clauses is the
  same.

**Periods and spaces**

The period ending a sentence should be followed by 1 space.

### Emphasizing

When referring to technical words, such as CFEngine keywords, filenames or commands,
use backticks to format that word as code (ie monospaced font). If the word is a
known word, a link will automatically generated (see above).

When referring to UI elements or interactive functionality, use `*italic*`.

To highlight sections of texts without starting a new header, use `**bold**`.

### Abbreviations

As a general note, avoiding abbreviations provides better readability.

**Latin expressions commonly used in English**

* i.e. (that is)
* e.g. (for example)
* cf. (compare)
* etc. (and so forth)
* vs.(versus)
* et al. (and others)

### Charts and graphs

* use clear shapes
* avoid shadows
* stick to black, white, and grey
* avoid background fill colors on large items

## Technical reference documentation

* follow the [Policy Style Guide](manuals/policy-style.markdown)
  in examples and code snippets
* use the appropriate lexer for syntax highlighting via Pygments

  Most important are the `cf3` lexer, as well as `bash`, `console`,
  `diff`, `shell-session` and `sql`. But Jekyll supports
  [many more lexers](http://pygments.org/docs/lexers/)

* avoid custom color schemes and hand-coded HTML
* document the example after the example code

The structure of the technical documentation about CFEngine attributes,
functions etc is as follows:

### Promise Attributes

Promise attributes are documented within the respective promise types's reference
page. Level-3 headers are used to start a new attribute (if the promise attribute
requires a body template, then see next section).

    ----
    title: promise-type
    ----

    ...

    ### Promise Attribute

    **Description:** One line summary.

    Longer explanation on what it does and why it is useful,
    over multiple paragraphs if necessary.

    [%CFEngine_promise_attribute(default value)%]

    More information about special input values.

    **Example:**

    ```f3
        Some code with
        cf3 markers
        for syntax highlighting
    ```

    If the example requires explanation, do it here. Consider using
    CFEngine comments within the code directly to explain. Preferably,
    use the `include_snippet` macro (see above) to inject code from an external
    .cf file that is known to run and produce the expected output.

    **Notes:**

    Additional information, spanning as many paragraphs as necessary, but mind
    the style guide.

    **See also:** `related_attribute`, [`attribute`][other_page#attribute]

### Bodies

For promise attributes with a body type, you can start with an example of that
body type, with the most relevant attributes set to self-explanatory values.

    ### attribute

    **Description:** One line summary.

    Longer explanation on what this body template is used for,
    over multiple paragraphs if necessary.

    [%CFEngine_promise_attribute()%]

    **Example:**

    ```cf3
    body promise_attribute example
    {
       attribute1 => "value1";
       attribute2 => "value2";
    }
    ```

Start explaining each attribute in the body then using level4-headings,
following the style for promise attributes as explained above. Examples
should be a code snippet at this point, no need for a complete piece of
runnable code.

### Functions

No header necessary - there is one function per page, and the page's
title is the name of the function.

    [%CFEngine_function_prototype(parameter1, parameters2, ...)%]

    **Description:** Returns something based on `parameter1` and `parameter2`.

    Longer explanation on what it does and why it is useful then afterwards.

    Summarize what the function does and reference the most important parameters by
    name, typical use cases etc.

    Over multiple paragraphs if necessary.

    [%CFEngine_function_attributes(parameter1, parameter2)%]

    Explain important attribute values, correlations and limitations.

    **Example:**

    ```cf3
        Some code with
        cf3 markers
        for syntax highlighting
    ```

    If the example requires explanation, do it here. Consider using
    CFEngine comments within the code directly to explain, and the `include_snippet`
    macro to inject code from an external .cf file that is known to work.

    **Notes:**

    Additional information, spanning as many paragraphs as necessary, but mind
    the style guide.

    **See also:** `related_function()`, `related_attribute`


**Note:** The `function_attributes` macro will generate a simple enumeration of all attributes,
with the types and allowed in put range coming from the syntax map, and the names as
provided. If you want to explain each attribute directly after it being listed, don't
use the macro, and list the attributes explicitly:

    **Arguments:**

    * `named`: valid input

    First argument does this.

    * `parameters`: valid input

    This argument does that.


### Special Variables

Special Variables are documented within the page of their context.

    ### context.variable

    Explanation.

    **See also:** `other_variable`

## Publishing

Jekyll is used to generate the HTML pages. The toolchain is available at
https://github.com/cfengine/documentation-generator. After you compile pages,
Jekyll will place all files into the _site folder, without subdirectories.

Commits in this repository trigger the documentation generator to run, which
then updates the contents of http://cfengine.com/docs/

The documentation generation creates a log file that lists undocumented
syntax elements, ambiguous link targets and other stuff that can be improved at
https://cfengine.com/docs/master/cfdoc_log.html

## License

See the LICENSE file.
