---
layout: default
title: Policy Server Setup
sorting: 4
published: true
tags: [guide, policy server, setup, configuration]
---

## Basic Policy Server Setup ##

There are two essential things that need to be taken care of when setting up a simple policy server:

1. Bootstrapping
2. Configuration

### 1. Bootstrap the Policy Server ###

The Policy Server must be bootstrapped to itself. 

1. Find the IP address of your Policy Server:

		
		$ ifconfig
		

2. Run the bootstrap command:

		
		$ sudo /var/cfengine/bin/cf-agent --bootstrap <IP address of policy server>
		

Note: The bootstrap command must also be run on any client attaching itself to this server, using the ip address of the policy server (i.e. exactly the same as the command run on the policy server itself).

### 2. Basic Policy Server Configuration ###

#### def.cf ####

1. Find the following line:
		
		"domain"  string    => "your.domain.here",
		
2. Change **your.domain.here** to your domain name, e.g. **example.com**.

#### controls/cf_execd.cf ####

1. Find the following line:
		
		mailto => "some-admin-list@me.local";
		
2. Change **some-admin-list@me.local** to your email address.

Note: On some systems this modification should hopefully work without needing to make any additional changes elsewhere. However, any emails sent from the system might also end up flagged as spam and sent directly to a user's junk mailbox.

#### Server IP Address and Hostname ####

Edit /etc/hosts and add an entry for the IP address and hostname of the server.


