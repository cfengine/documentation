---
layout: default
title: File and Directory Examples
published: true
sorting: 6
tags: [Examples,Files,Directories]
---

* [Create files and directories][File and Directory Examples#Create files and directories]
* [Copy single files][File and Directory Examples#Copy single files]
* [Copy directory trees][File and Directory Examples#Copy directory trees]
* [Disabling and rotating files][File and Directory Examples#Disabling and rotating files]
* [Add lines to a file][File and Directory Examples#Add lines to a file]
* [Check file or directory permissions][File and Directory Examples#Check file or directory permissions]
* [Commenting lines in a file][File and Directory Examples#Commenting lines in a file]
* [Copy files][File and Directory Examples#Copy files]
* [Copy and flatten directory][File and Directory Examples#Copy and flatten directory]
* [Copy then edit a file convergently][File and Directory Examples#Copy then edit a file convergently]
* [Deleting lines from a file][File and Directory Examples#Deleting lines from a file]
* [Deleting lines exception][File and Directory Examples#Deleting lines exception]
* [Delete files recursively][File and Directory Examples#Delete files recursively]
* [Editing files][File and Directory Examples#Editing files]
* [Editing tabular files][File and Directory Examples#Editing tabular files]
* [Inserting lines in a file][File and Directory Examples#Inserting lines in a file]
* [Back references in filenames][File and Directory Examples#Back references in filenames]
* [Add variable definitions to a file][File and Directory Examples#Add variable definitions to a file]
* [Linking files][File and Directory Examples#Linking files]
* [Listing files-pattern in a directory][File and Directory Examples#Listing files-pattern in a directory]
* [Locate and transform files][File and Directory Examples#Locate and transform files]
* [BSD flags][File and Directory Examples#BSD flags]
* [Search and replace text][File and Directory Examples#Search and replace text]
* [Selecting a region in a file][File and Directory Examples#Selecting a region in a file]
* [Warn if matching line in file][File and Directory Examples#Warn if matching line in file]

## Create files and directories ##

Create files and directories and set permissions.


[%CFEngine_include_snippet(create_files_and_directories.cf, .* )%]

## Copy single files ##

Copy single files, locally (local_cp) or from a remote site (secure_cp). The Community Open Promise-Body Library (COPBL; cfengine_stdlib.cf) should be included in the /var/cfengine/inputs/ directory and input as below.


[%CFEngine_include_snippet(copy_single_files.cf, .* )%]

## Copy directory trees ##

Copy directory trees, locally (local_cp) or from a remote site (secure_cp). (depth_search => recurse("")) defines the number of sublevels to include, ("inf") gets entire tree.


[%CFEngine_include_snippet(copy_directory_trees.cf, .* )%]

## Disabling and rotating files ##

Use the following simple steps to disable and rotate files. See the Community Open Promise-Body Library if you wish more details on what disable and rotate does.


[%CFEngine_include_snippet(disabling_and_rotating_files.cf, .* )%]

## Add lines to a file ##

There are numerous approaches to adding lines to a file. Often the order of a configuration file is unimportant, we just need to ensure settings within it. A simple way of adding lines is show below.


[%CFEngine_include_snippet(add_lines_to_a_file.cf, .* )%]

Also you could write this using a list variable:


[%CFEngine_include_snippet(add_lines_to_a_file_1.cf, .* )%]

## Check file or directory permissions


[%CFEngine_include_snippet(check_file_or_directory_permissions.cf, .* )%]

## Commenting lines in a file


[%CFEngine_include_snippet(commenting_lines_in_a_file.cf, .* )%]

## Copy files


[%CFEngine_include_snippet(copy_files.cf, .* )%]


## Copy and flatten directory


[%CFEngine_include_snippet(copy_and_flatten_directory.cf, .* )%]

## Copy then edit a file convergently

To convergently chain a copy followed by edit, you need a staging file. First you copy to the staging file. Then you edit the final file and insert the staging file into it as part of the editing. This is convergent with respect to both stages of the process.


[%CFEngine_include_snippet(copy_then_edit_a_file_convergently.cf, .* )%]

## Deleting lines from a file


[%CFEngine_include_snippet(deleting_lines_from_a_file.cf, .* )%]

## Deleting lines exception


[%CFEngine_include_snippet(deleting_lines_exception.cf, .* )%]

## Delete files recursively

The [rm_rf][lib/bundles.cf#rm_rf] and [rm_rf_depth][lib/bundles.cf#rm_rf_depth] bundles in the standard library make it easy to prune directory trees.

## Editing files

This is a huge topic. See also See Add lines to a file, See Editing tabular files, etc. Editing a file can be complex or simple, depending on needs.

Here is an example of how to comment out lines matching a number of patterns:


[%CFEngine_include_snippet(editing_files.cf, .* )%]


## Editing tabular files


[%CFEngine_include_snippet(editing_tabular_files.cf, .* )%]

## Inserting lines in a file


[%CFEngine_include_snippet(inserting_lines_in_a_file.cf, .* )%]

## Back references in filenames


[%CFEngine_include_snippet(back_references_in_filenames.cf, .* )%]

## Add variable definitions to a file


[%CFEngine_include_snippet(add_variable_definitions_to_a_file.cf, .* )%]

Results in:

* lhs1= Mary had a little pig
* lhs2=Whose Fleece was white as snow
* lhs3=And everywhere that Mary went

An example of this would be to add variables to /etc/sysctl.conf on Linux:


[%CFEngine_include_snippet(add_variable_definitions_to_a_file_1.cf, .* )%]

## Linking files


[%CFEngine_include_snippet(linking_files.cf, .* )%]

## Listing files-pattern in a directory


[%CFEngine_include_snippet(listing_files-pattern_in_a_directory.cf, .* )%]

## Locate and transform files


[%CFEngine_include_snippet(locate_and_transform_files.cf, .* )%]

## BSD flags ##


[%CFEngine_include_snippet(bsd_flags.cf, .* )%]

## Search and replace text


[%CFEngine_include_snippet(search_and_replace_text.cf, .* )%]

## Selecting a region in a file


[%CFEngine_include_snippet(selecting_a_region_in_a_file.cf, .* )%]

## Warn if matching line in file

[%CFEngine_include_snippet(warn_if_matching_line_in_file.cf, .* )%]
