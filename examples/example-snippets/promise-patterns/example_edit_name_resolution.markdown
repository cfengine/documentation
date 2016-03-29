---
layout: default
title: Set up name resolution with DNS
published: true
tags: [Examples, Policy, dns, file editing, files]
reviewed: 2013-06-08
reviewed-by: atsaloli
---

There are many ways to configure name resolution. A simple and straightforward approach is to implement this as a simple editing promise for the `/etc/resolv.conf` file.

```cf3

body common control
{
bundlesequence => { "edit_name_resolution" };
}

bundle agent edit_name_resolution
{

files:

  "/tmp/resolv.conf"   # This is for testing, change to "$(sys.resolv)" to put in production

     comment       => "Add lines to the resolver configuration",
     create        => "true",     # Make sure the file exists, create it if not
     edit_line     => resolver,   # Call the resolver bundle defined below to do the editing
     edit_defaults => empty;      # Baseline memory model of file to empty before processing
                                  # bundle edit_line resolver
}

bundle edit_line resolver
{

insert_lines:

 any::   # Class/context where you use the below nameservers. Change to appropriate class
	 # for your system (if not any::, for example server_group::, ubuntu::, etc.)

  # insert the search domain or name servers we want
  "search mydomain.tld" location => start;  # Replace mydomain.tld with your domain name
                              # The search line will always be at the start of the file
  "nameserver 128.39.89.8";
  "nameserver 128.39.74.66";
}

body edit_defaults empty
{
empty_file_before_editing => "true";
}

body location start
{
before_after => "before";
}
```


Example run:

```
# cf-agent -f unit_edit_name_resolution.cf  # set up resolv.conf
# cat /tmp/resolv.conf # show resolv.conf
search mydomain.tld
nameserver 128.39.89.8
nameserver 128.39.74.66
# echo 'nameserver 0.0.0.0' >> /tmp/resolv.conf  # mess up resolv.conf
# cf-agent -f ./unit_edit_name_resolution.cf -KI  # heal resolv.conf
2013-06-08T18:38:12-0700     info: This agent is bootstrapped to '192.168.183.208'
2013-06-08T18:38:12-0700     info: Running full policy integrity checks
2013-06-08T18:38:12-0700     info: /edit_name_resolution/files/'/tmp/resolv.conf': Edit file '/tmp/resolv.conf'
# cat /tmp/resolv.conf # show healed resolv.conf
search mydomain.tld
nameserver 128.39.89.8
nameserver 128.39.74.66
#
```
