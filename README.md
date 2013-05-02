Jekyll config for CFEngine documentation
===========


1. Installation
-
1. execute setup.sh script from _setup folder
2. do steps described in file step2.txt

2. Use
-

1. All *content* files should be inside *pages* folder
2. All files must have *meta* data on top. See (Page meta data section)
3. Templates are saved in the *_layouts* folder
4. Images and other materials saved in *media* folder
5. JS and css saved in _assets folder. To include new files open  *_includes/head.html* file
6. Make sure you set correct settings in _config.yml for CFE_OUTPUT and CFE_DIR 


3. Run
-

*cd* to the project root folder and type *jekyll*. Your can find your "compiled" files inside *pages* folder

4. Auto update and run as server
-

*cd*  to project root folder and type *jekyll --auth --server 4000*
where 4000 - port number.

NOTE: you must restart server after changes in _config.yml


5. Config
-

To configure jekyll open _config.yml. All options described at https://github.com/mojombo/jekyll/wiki/Configuration


6. Page meta data
-

```
---
layout: default
title: cf-agent
categories: [Components, cf-agent]
published: true
alias: cf-agent.html
tags: [cf-agent, promises]
---
```

Explanation:

You must use YAML format for metadata
You must place metadata on the top of the file and divide it with ---  (repeat "-" sign 3 times on new line)


*layout*: default - we have only 1 layout for pages now

*title*:  page title - string between <title></title>

*categories*:  where we should place this page, think about this as a breadcrumbs. Last point should be this page

*published*: true or false

*alias*: url (html file name) - use "url safe" names

*tags*: tags relevant to this doc


This instalation was tested on ubuntu 10.04 with vagrant and ruby 1.9.3.
Make sure your machine has everything according to jekyll requirements: https://github.com/mojombo/jekyll.
+ you need git installed to checkout documentation.

