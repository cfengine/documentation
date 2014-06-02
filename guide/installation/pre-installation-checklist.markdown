---
layout: default
title: Pre-Installation Checklist
published: true
sorting: 1
tags: [guide, installation]
---

## Required / Good to Know Knowledge ##

* Linux
* SSH
* bash
* command line text editing (e.g. vi/vim, Emacs)

See Also: [Quick-Start Guide to Using vi][Quick-Start Guide to Using vi], [Quick-Start Guide to Using PuTTY][Quick-Start Guide to Using PuTTY]

## Things Systems Adminstrators Should Find Out ##

* Specifications and Operating System for the Policy Server
	* Needs to run on a 64-bit version of Linux
	* You need a minimum of 2 GB of available memory and a modern 64 bit processor.
	* Plan for approximately 100MB of disk space per host.
	* Needs to run on a dedicated OS with a vanilla installation
	* Verify that the machine’s network connection is working and that port 5308

* Specifications and operating systems of host machines
	* 256 MB available memory in order to run the CFEngine agent software (cf-agent)
	See [General Requirements][Pre-Installation Checklist#General Requirements] and [Supported Platforms][Supported Platforms]

CFEngine bundles all critical dependencies into the package; therefore,
additional software is not required.
	
See Also: [Supported Platforms][Supported Platforms]	


