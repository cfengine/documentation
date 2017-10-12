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

Execute a command, for instance to start a MySQL service. Note that simple shell commands like rm or mkdir cannot be managed by CFEngine, so none of the protections that CFEngine offers can be applied to the process. Moreover, this starts a new process, adding to the burden on the system.


[%CFEngine_include_snippet(command_or_script_execution.cf, .* )%]

## Change directory for command


[%CFEngine_include_snippet(change_directory_for_command.cf, .* )%]

## Commands example

[%CFEngine_include_snippet(commands_example.cf, .* )%]

## Execresult example


[%CFEngine_include_snippet(execresult_example.cf, .* )%]

## Methods


[%CFEngine_include_snippet(methods.cf, .* )%]

## Method validation


[%CFEngine_include_snippet(method_validation.cf, .* )%]

## Trigger classes

[%CFEngine_include_snippet(trigger_classes.cf, .* )%]
