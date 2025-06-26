---
layout: default
title: Commands, scripts, and execution examples
sorting: 5
---

* [Command or script execution][Commands, scripts, and execution examples#Command or script execution]
* [Change directory for command][Commands, scripts, and execution examples#Change directory for command]
* [Commands example][Commands, scripts, and execution examples#Commands example]
* [Execresult example][Commands, scripts, and execution examples#Execresult example]
* [Methods][Commands, scripts, and execution examples#Methods]
* [Method validation][Commands, scripts, and execution examples#Method validation]
* [Trigger classes][Commands, scripts, and execution examples#Trigger classes]

## Command or script execution

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
