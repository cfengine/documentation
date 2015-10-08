Jekyll config for CFEngine documentation
===========


1. Installation
-
This installation was tested on ubuntu 10.04 with vagrant, ruby 1.9.3 and Java 7.
Make sure your machine has everything according to jekyll requirements: https://github.com/mojombo/jekyll.
+ you need git installed to checkout documentation.

You also need:
+ java - for closure compiler
+ python-pygments 1.5 or later for the code highlighting

Gems:
+ jekyll-asset-pipeline
+ closure-compiler
+ yui-compressor
+ redcarpet
+ albino
+ uglifier
+ execjs
+ sanitize

######if pandoc is used
+ pandoc-ruby
+ rdiscount

You can find additional information inside _setup/start.sh


Clean setup
--
1. Review and change file _setup/start.sh accordingly to your environment


Final steps
----
1. Do steps described in file _setup/step2.txt
2. Create pages folder and checkout CFEngine documentation inside. (https://github.com/cfengine/documentation)



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

