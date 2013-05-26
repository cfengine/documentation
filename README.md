# CFEngine Documentation

This repository hold the content for the technical CFEngine documentation in markdown files. If you have a texteditor,
know how to write markdown and English and would like to contribute to the CFEngine documentation, then we'd like to
invite you to collaborate here!

If you would like to notify us about incorrect documentation, but don't have the time or the knowledge to make a correction
directly here, then you can report the issue in the regular [CFEngine bug tracker](https://cfengine.com/dev/projects/core).
Use the "Documentation" category when you create bugs. And of course you can search the bug tracker for known issues with
the documentation, and maybe help the community of CFEngine users by correcting some of those here!

## Documentation Structure

Pages are organized hierarchically in category/subcategory relationships. Those are defined by the `categories` META
data in the markdown file:

    categories: [Path, Of, Categories, Page]

This creates the navigation structure on the left hand side of the published documentation. The HTML files are
all created into the same directory, so the alias META has to specify a unique filename.

    alias: path-of-categories-page.html

To make it easier to locate files in the repository, the markdown sources are organized in a directory structure that
corresponds with the categorization, ie

    documentation/path/of/categories/page.markdown

Filenames are lower-case. Markdown-files in each subdirectory can be created as well with content providing an overview
for that category.

### META tags

Additional META tags you should set are:

    layout: default

Leave this as default.

    title: The Title

The title of the page.

    published: true|false

Pages that set this tag to `false` will not be published.

    tags: [list, of, tags with space, all lowercase]

Keywords for this page, which will be displayed on top of the page, and used when generating the tag-pages.

    reviewed: yyyy-mm-dd
    reviewed-by: github-user

Keeping track of when a documentation page has last been reviewed.

META tag values will be interpreted literally, and cannot contain `:`, `[` and `]`.

### Image files

Image files are in the same directory as the markdown files that embed them. Give files unique names to avoid overwrites
in the generated website.

See [Style Guide - Charts and graphs](#Charts_and_graphs) for style requirements for images.

##Style Guide

Make sure you follow this style guide to make using CFEngine and the documentation a consistent and pleasant experience.

### Writing for the web

* use subheadings to structure content
* keep paragraphs short
* support scanning of pages

### Spelling

CFEngine documentation follows the American spelling.

### Punctuation

**Oxford comma**

In punctuation, a serial comma (also called Oxford comma) needs to be placed immediately before the conjunction
(often “and” or “or”) in a series of three or more terms.

*Example:*

I would like crackers, cheese, and garlic.

**The comma as a separator between compound sentences**

Use commata to separate independent clauses when they are joined by any of these seven coordinating conjunctions:
and, but, for, or, nor, so, yet.

However, the comma can be dropped in the following cases:

* if both independent clauses are quite short, especially if the two clauses are very closely related, and even more
so if the subject of both clauses is the same, or
* if only the first clause is quite short, especially if the two clauses are very closely related, and even more so if
the subject of both clauses is the same.

**Periods and spaces**

The period ending a sentence should be followed by 1 space.

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

### Code

* use proper, consistent indentation **TODO: coding style guide**
* always run it through Pygments plus the appropriate lexer
* avoid custom color schemes and hand-coded HTML
* document the example after the example code

### Structure of technical reference documentation

The structure of the technical documentation about CFEngine attributes or 
functions is as follows:

    ## Language Element

    **Synopsis:** One line summary.

    **Type:** `Datatype` - if applicable.

    **Allowed input range:** `value range` or
    ```cf3
        List
        of
        menu
        options
    ```

    **Default value:** `Language Element => default value`, if applicable

    **Example:** 
    ```f3
        Some code with 
        cf3 markers
        for syntax highlighting
    ```

    **Notes:**
    
    Additional information, spanning as many paragraphs as necessary, but mind
    the style guide.
    
    In case of menu option types t's important to cover all allowed values.
    
    If the example is long and complex, explain it here.

## Publishing

Jekyll is used to generate the HTML pages. The toolchain is available at https://github.com/cfengine/documentation-generator
After you compile pages, Jekyll will place all files into the _site folder, 
without subdirectories.

Commits in this repository trigger the documentation generator to run, which 
then updates the contents of http://cfengine.com/tmp_docs/
