# CFEngine Documentation

This repository hold the content for the technical CFEngine documentation in markdown files. If you have a texteditor,
know how to write markdown and English and would like to contribute to the CFEngine documentation, then we'd like to
invite you to collaborate here!

If you would like to notify us about incorrect documentation, but don't have the time or the knowledge to make a correction
directly here, then you can report the issue in the regular [CFEngine bug tracker](https://cfengine.com/dev/projects/core).
Use the "Documentation" category when you create bugs. And of course you can search the bug tracker for known issues with
the documentation, and maybe help the community of CFEngine users by correcting some of those here!

## File Structure

Pages are organized hierarchically in category/subcategory relationships. Those are defined by the META data in the
markdown file:

    layout: default
    title: The Title
    categories: [Path, Of, Categories, This]
    published: true|false
    alias: path-of-categories-this.html
    tags: [List, of, Tags with space]

This creates the navigation structure to the left. The HTML files are all created into the same directory, so the alias
META has to specify a unique filename.

To make files easier to locate in the repository, the markdown sources are organized in a directory structure that
corresponds with the categorization, ie

* documentation/Path/Of/Categories/This.markdown

Markdown-files in each subdirectory can be created as well with content providing an overview for that category.

Note that the file name is not actually important, Jekyll will use the alias you specified in META alias. But keeping
this consistent gives us better navigation through the source files.

## Images files

...

## Style Guide

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

As a general note, avoiding abbreviations provides better readibility.

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

* use proper, consistent indentation
* always run it through Pygments plus the appropriate lexer
* avoid custom color schemes and hand-coded HTML

## Publishing

Jekyll is used to generate the HTML pages. The toolchain is avaiable at https://github.com/cfengine/documentation-generator
After you compile pages, Jekyll will place all files into the _site folder, without subdirectories.

Commits in this repository trigger the documentation generator to run, which then updates the contents of
http://cfengine.com/tmp_docs/
