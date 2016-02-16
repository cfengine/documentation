---
layout: default
title: Set up time management through NTP
published: true
tags: [Examples, Policy, ntp, file editing]
reviewed: 2013-06-09
reviewed-by: atsaloli
---


The following sets up a local NTP server that synchronizes with pool.ntp.org and
clients that synchronize with your local NTP server. See bottom of this example
if you don't want to build a server, but use a "brute force" method (repeated
ntpdate syncs).

This example demonstrates you can have a lot of low-level detailed control if you want it.

```cf3
	bundle agent system_time_ntp
	{
	 vars:

	  linux::

	   "cache_dir"   string => "$(sys.workdir)/cache";  # Cache directory for NTP config files

	   "ntp_conf"    string => "/etc/ntp.conf";  # Target file for NTP configuration

	   "ntp_server"  string => "172.16.12.161";  #
	   "ntp_network" string => "172.16.12.0";    # IP address and netmask of your local NTP server
	   "ntp_mask"    string => "255.255.255.0";  #

	   "ntp_pkgs"    slist => { "ntp" };         # NTP packages to be installed to ensure service


	# Define a class for the NTP server
	 classes:

	  any::

	   "ntp_hosts"         or => { classmatch(canonify("ipv4_$(ntp_server)")) };


	# Ensure that the NTP packages are installed
	 packages:

	  ubuntu::

	   "$(ntp_pkgs)"

		     comment => "setup NTP",
	      package_policy => "add",
	      package_method => generic;


	# Ensure existence of file and directory for NTP drift learning statistics
	 files:

	  linux::

	   "/var/lib/ntp/ntp.drift"

	      comment => "Enable ntp service",
	       create => "true";

	   "/var/log/ntpstats/."

	      comment => "Create a statistic directory",
		perms => mog("644","ntp","ntp"),
	       create => "true";

	  ntp_hosts::


	# Build the cache configuration file for the NTP server
	   "/var/cfengine/cache/ntp.conf"

		    comment => "Build $(this.promiser) cache file for NTP server",
		     create => "true",
	      edit_defaults => empty,
		  edit_line => restore_ntp_master("$(ntp_network)","$(ntp_mask)");

	  centos.ntp_hosts::


	# Copy the cached configuration file to its target destination
	   "$(ntp_conf)"

		comment => "Ensure $(this.promiser) in a perfect condition",
	      copy_from => local_cp("$(cache_dir)/ntp.conf"),
		classes => if_repaired("refresh_ntpd_centos");

	  ubuntu.ntp_hosts::

	   "$(ntp_conf)"

		comment => "Ensure $(this.promiser) in a perfect condition",
	      copy_from => local_cp("$(cache_dir)/ntp.conf"),
		classes => if_repaired("refresh_ntpd_ubuntu");

	  !ntp_hosts::


	# Build the cache configuration file for the NTP client
	   "$(cache_dir)/ntp.conf"

		    comment => "Build $(this.promiser) cache file for NTP client",
		     create => "true",
	      edit_defaults => empty,
		  edit_line => restore_ntp_client("$(ntp_server)");

	  centos.!ntp_hosts::


	# Copy the cached configuration file to its target destination
	   "$(ntp_conf)"

		comment => "Ensure $(this.promiser) in a perfect condition",
	      copy_from => local_cp("$(cache_dir)/ntp.conf"),
		    classes => if_repaired("refresh_ntpd_centos");

	  ubuntu.!ntp_hosts::

	   "$(ntp_conf)"

		comment => "Ensure $(this.promiser) in a perfect condition",
	      copy_from => local_cp("$(cache_dir)/ntp.conf"),
		classes => if_repaired("refresh_ntpd_ubuntu");


	# Set classes (conditions) for to restart the NTP daemon if there have been any changes to configuration
	 processes:

	  centos::

	   "ntpd.*"

	      restart_class => "refresh_ntpd_centos";

	  ubuntu::

	   "ntpd.*"

	      restart_class => "refresh_ntpd_ubuntu";


	# Restart the NTP daemon if the configuration has changed
	 commands:

	  refresh_ntpd_centos::

	   "/etc/init.d/ntpd restart";

	  refresh_ntpd_ubuntu::

	   "/etc/init.d/ntp restart";

	}

	#######################################################

	bundle edit_line restore_ntp_master(network,mask)
	{
	vars:
	 "list" string =>
	"######################################
	# ntp.conf-master

	driftfile /var/lib/ntp/ntp.drift
	statsdir /var/log/ntpstats/

	statistics loopstats peerstats clockstats
	filegen loopstats file loopstats type day enable
	filegen peerstats file peerstats type day enable
	filegen clockstats file clockstats type day enable

	# Use public servers from the pool.ntp.org project.
	# Please consider joining the pool (http://www.pool.ntp.org/join.html).
	# Consider changing the below servers to a location near you for better time
	# e.g. server 0.europe.pool.ntp.org, or server 0.no.pool.ntp.org etc.
	server 0.centos.pool.ntp.org
	server 1.centos.pool.ntp.org
	server 2.centos.pool.ntp.org

	# Permit time synchronization with our time source, but do not
	# permit the source to query or modify the service on this system.
	restrict -4 default kod nomodify notrap nopeer noquery
	restrict -6 default kod nomodify notrap nopeer noquery

	# Permit all access over the loopback interface.  This could
	# be tightened as well, but to do so would effect some of
	# the administrative functions.
	restrict 127.0.0.1
	restrict ::1

	# Hosts on local network are less restricted.
	restrict $(network) mask $(mask) nomodify notrap";

	insert_lines:
	 "$(list)";
	}

	#######################################################

	bundle edit_line restore_ntp_client(serverip)
	{
	vars:
	 "list" string =>
	"######################################
	# This file is protected by cfengine #
	######################################
	# ntp.conf-client

	driftfile /var/lib/ntp/ntp.drift
	statsdir /var/log/ntpstats/

	statistics loopstats peerstats clockstats
	filegen loopstats file loopstats type day enable
	filegen peerstats file peerstats type day enable
	filegen clockstats file clockstats type day enable

	# Permit time synchronization with our time source, but do not
	# permit the source to query or modify the service on this system.
	restrict -4 default kod nomodify notrap nopeer noquery
	restrict -6 default kod nomodify notrap nopeer noquery

	# Permit all access over the loopback interface.  This could
	# be tightened as well, but to do so would effect some of
	# the administrative functions.
	restrict 127.0.0.1
	restrict ::1
	server $(serverip)
	restrict $(serverip) nomodify";

	insert_lines:
	 "$(list)";
	}
```

This policy can be found in `/var/cfengine/share/doc/examples/example_ntp.cf`

If you don't want to build a server, you might do like this:

```cf3
	bundle agent time_management
	{
	 vars:

	  any::

	   "ntp_server" string => "no.pool.ntp.org";

	 commands:

	  any::

	      "/usr/sbin/ntpdate $(ntp_server)"

		 contain => silent;

	}
```

This is a hard reset of the time, it corrects it immediately. This may cause problems
if there are large deviations in time and you are using time sensitive software on your
system. An NTP daemon setup as shown above, on the other hand, slowly adapts the time
to avoid causing disruption. In addition, the NTP daemon can be configured to learn your
system's time drift and automatically adjust for it without having to be in touch with
the server at all times.


