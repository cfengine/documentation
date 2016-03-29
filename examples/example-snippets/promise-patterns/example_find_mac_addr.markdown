---
layout: default
title: Find the MAC address
published: true
tags: [Examples, Policy, MAC address]
reviewed: 2013-06-08
reviewed-by: atsaloli
---

Finding the ethernet address can vary between operating systems.

We will use CFEngine's built in function `execresult` to execute commands
adapted for different operating systems, assign the output to variables,
and filter for the MAC address. We then report on the result.

```cf3
body common control
{
bundlesequence => { "example" };
}


bundle agent example
{
vars:

  linux::
    "interface" string => execresult("/sbin/ifconfig eth0", "noshell");

  solaris::
    "interface" string => execresult("/usr/sbin/ifconfig bge0", "noshell");

  freebsd::
    "interface" string => execresult("/sbin/ifconfig le0", "noshell");

  darwin::
    "interface" string => execresult("/sbin/ifconfig en0", "noshell");

# Use the CFEngine function 'regextract' to match the MAC address,
# assign it to an array called mac and set a class to indicate positive match
classes:

  linux::

  "ok" expression => regextract(
                                ".*HWaddr ([^\s]+).*(\n.*)*",  # pattern to match
                                "$(interface)",  # string to scan for pattern
                                "mac"  # put the text that matches the pattern into this array
                                );

  solaris|freebsd::

   "ok" expression => regextract(
                                ".*ether ([^\s]+).*(\n.*)*",
                                "$(interface)",
                                "mac"
                                );


  darwin::

   "ok" expression => regextract(
                                "(?s).*ether ([^\s]+).*(\n.*)*",
                                "$(interface)",
                                "mac"
                                );

# Report on the result
reports:

  ok::

    "MAC address is $(mac[1])";  # return first element in array "mac"

}
```

This policy can be found in `/var/cfengine/masterfiles/example_find_mac_addr.cf`

Example run:

```
# cf-agent -f example_find_mac_addr.cf
2013-06-08T16:59:19-0700   notice: R: MAC address is a4:ba:db:d7:59:32
#
```

While the above illustrates the flexiblity of CFEngine in
running external commands and parsing their output,
as of CFEngine 3.3.0, Nova 2.2.0 (2011), you can get the MAC
address natively:

```cf3
body common control
{
bundlesequence => { "example" };
}


bundle agent example
{
vars:

  linux::   "interface" string => "eth0";

  solaris:: "interface" string => "bge0";

  freebsd:: "interface" string => "le0";

  darwin::  "interface" string => "en0";


reports:

    "MAC address of $(interface) is: $(sys.hardware_mac[$(interface)])";
}
```
