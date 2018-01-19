---
layout: default
title: Software Administration Examples
published: true
sorting: 4
tags: [Examples,Software Administration]
---

* [Software and patch installation][Software Administration Examples#Software and patch installation]
* [Postfix mail configuration][Software Administration Examples#Postfix mail configuration]
* [Set up a web server][Software Administration Examples#Set up a web server]
* [Add software packages to the system][Software Administration Examples#Add software packages to the system]
* [Application baseline][Software Administration Examples#Application baseline]
* [Service management (windows)][Software Administration Examples#Service management (windows)]
* [Software distribution][Software Administration Examples#Software distribution]
* [Web server modules][Software Administration Examples#Web server modules]
* Ensure a service is enabled and running
* Managing Software
* Install packages

## Software and patch installation ##

Example for Debian:


[%CFEngine_include_snippet(software_and_patch_installation.cf, .* )%]

Examples MSI for Windows, by name:


[%CFEngine_include_snippet(software_and_patch_installation_1.cf, .* )%]

Windows MSI by version:


[%CFEngine_include_snippet(software_and_patch_installation_1.cf, .* )%]

Examples for solaris:

[%CFEngine_include_snippet(packages_examples_solaris.cf, .* )%]

Examples for yum based systems:

[%CFEngine_include_snippet(software_and_patch_installation_1_2.cf, .* )%]

SuSE Linux's package manager zypper is the most powerful alternative:

[%CFEngine_include_snippet(software_and_patch_installation_1_2_3.cf, .* )%]

## Postfix mail configuration


[%CFEngine_include_snippet(postfix_mail_configuration.cf, .* )%]

## Set up a web server

Adapt this template to your operating system by adding multiple classes. Each web server runs something like the present module, which is entered into the bundlesequence like this:


[%CFEngine_include_snippet(set_up_a_web_server.cf, .* )%]

## Add software packages to the system ##


[%CFEngine_include_snippet(add_software_packages_to_the_system.cf, .* )%]

Note you can also arrange to hide all the differences between package managers on an OS basis, but since some OSs have multiple managers, this might not be 100 percent correct.

## Application baseline


[%CFEngine_include_snippet(application_baseline.cf, .* )%]

## Service management (windows)


[%CFEngine_include_snippet(service_management_(windows).cf, .* )%]

## Software distribution


[%CFEngine_include_snippet(software_distribution.cf, .* )%]

## Web server modules

The problem of editing the correct modules into the list of standard modules for the Apache web server. This example is based on the standard configuration deployment of SuSE Linux. Simply provide the list of modules you want and another list that you don't want.

[%CFEngine_include_snippet(web_server_modules.cf, .* )%]
