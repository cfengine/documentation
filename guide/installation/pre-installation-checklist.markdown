---
layout: default
title: Pre-Installation Checklist
published: true
sorting: 1
tags: [guide, installation]
---

## Download Packages

[Download CFEngine](http://cfengine.com/product/free-download)

## Required / Good to Know Knowledge ##

* Linux
* SSH
* bash
* command line text editing (e.g. vi/vim, Emacs)

See Also: [Quick-Start Guide to Using vi][Quick-Start Guide to Using vi], [Quick-Start Guide to Using PuTTY][Quick-Start Guide to Using PuTTY]

## Requirements for CFEngine ##

* Requirements for the Policy Server:
	* Needs to run on a 64-bit version of Linux
	* You need a minimum of 2 GB of available memory and a modern 64 bit processor.
	* Plan for approximately 100MB of disk space per host.
	* Needs to run on a dedicated OS with a vanilla installation
	* Verify that the machine’s network connection is working
	* Communication between host and server requires that port 5308 be open.
	* Mission Portal requires that port 80 is open.

* Requirements for CFEngine hosts:
	* 256 MB available memory in order to run the CFEngine agent software (cf-agent)
	
CFEngine bundles all critical dependencies into the package; therefore,
additional software is not required.
	
See Also: [Supported Platforms][Supported Platforms]	


