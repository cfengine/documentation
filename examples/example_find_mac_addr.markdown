---
layout: default
title: Find the MAC address
categories: [Examples, Find the MAC address]
published: true
alias: examples-find-the-mac-address.html
tags: [Examples, MAC address]
---

Finding the ethernet address can be hard, but on Linux it is straightforward. We will use CFEngine's built in function `execresult` to execute  commands adapted for different operating systems, assign the output to variables, and filter for the MAC adress. We then report on the result.

```cf3
    body common control
    
    {
    bundlesequence => { "example" };
    }


    bundle agent example
    {
    vars:

    linux::
     "interface" string => execresult("/sbin/ifconfig eth0","noshell");

    solaris::
     "interface" string => execresult("/usr/sbin/ifconfig bge0","noshell");

    freebsd::
     "interface" string => execresult("/sbin/ifconfig le0","noshell");

    darwin::
     "interface" string => execresult("/sbin/ifconfig en0","noshell");

    # Use the CFEngine function 'regextract' to match the MAC address,
    # assign it to an array called mac and set a class to indicate positive match
    classes:

     linux::

       "ok" expression => regextract(
                                    ".*HWaddr ([^\s]+).*(\n.*)*",
                                    "$(interface)",
                                    "mac"
                                    );

     solaris::

       "ok" expression => regextract(
                                    ".*ether ([^\s]+).*(\n.*)*",
                                    "$(interface)",
                                    "mac"
                                    );

     freebsd::

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

      "MAC address is $(mac[1])";

    }
```

This policy can be found in `/var/cfengine/masterfiles/example_find_mac_addr.cf`
