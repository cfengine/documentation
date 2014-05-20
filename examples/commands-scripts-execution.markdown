---
layout: default
title: Commands, Scripts, and Execution Examples 
published: true
sorting: 5
tags: [Examples,Commands,Scripts]
---

* [Command or script execution][Commands, Scripts, and Execution Examples#Command or script execution]
* [Change directory for command][Commands, Scripts, and Execution Examples#Change directory for command]
* [Commands example][Commands, Scripts, and Execution Examples#Commands example]
* [Execresult example][Commands, Scripts, and Execution Examples#Execresult example]
* [Methods][Commands, Scripts, and Execution Examples#Methods]
* [Method validation][Commands, Scripts, and Execution Examples#Method validation]
* [Trigger classes][Commands, Scripts, and Execution Examples#Trigger classes]

## Command or script execution ##

Execute a command, for instance to start a MySQL service. Note that simple shell commands like rm or mkdir cannot be managed by CFEngine, so none of the protections that CFEngine offers can be applied to the process. Moreover, this starts a new process, adding to the burden on the system. See CFEngine 3 Best Practices http://cfengine.com/manuals/cf3-bestpractice.html for more information on how to best write policies.


[%CFEngine_include_example(command_or_script_execution.cf)%]

## Change directory for command


[%CFEngine_include_example(change_directory_for_command.cf)%]

## Commands example ##

## Commands example


[%CFEngine_include_example(commands_example.cf)%]

## Execresult example


[%CFEngine_include_example(execresult_example.cf)%]

## Methods


[%CFEngine_include_example(methods.cf)%]

## Method validation


[%CFEngine_include_example(method_validation.cf)%]

## Trigger classes


[%CFEngine_include_example(trigger_classes.cf)%]
