# CFEngine Documentation

## File Structure

Pages are organized hierarchically in category/subcategory relationships. Create a file with the same name as
the category, and create folder with the same name and place files inside:

* category.markdown
* category
    * category_subcategory.markdown

You must specify relation in the META categories too, ie 

cf-agent.markdown
categories: [Components, cf-agent]

cf-agent_inner.markdown
categories: [Components, cf-agent, cf-agent_inner]

Note that the file name is not actually important, Jekyll will use the alias you specified in META alias.
But keeping this consistent gives us better navigation through the source files.

## Style Guide

* US English

## Publishing

Jekyll is used to generate the HTML pages. The toolchain is avaiable at https://github.com/cfengine/documentation-generator
After you compile pages, Jekyll will place all files into the _site folder, without subdirectories.

Commits in this repository trigger the documentation generator to run, which then updates the contents of
http://cfengine.com/tmp_docs/
