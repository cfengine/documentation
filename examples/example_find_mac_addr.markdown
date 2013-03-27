## Find the MAC address

Finding the ethernet address can be hard, but on Linux it is straightforward. We will use CFEngine's built in function `execresult` to execute  commands adapted for different operating systems, assign the output to variables, and filter for the MAC adress. We then report on the result.

    bundle agent test
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

This policy does not exist as an example file in the current packages, but will be included from Community 3.5.0 and Enterprise 3.1.0 on. You can still integrate it into your main policy:

1. Copy the above content into a file called `/var/cfengine/masterfiles/example_find_mac_addr.cf`.

2. Insert the bundle name in the `bundlesequence` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

	    bundlesequence => {
		                    ...
		                    "test",
		                    ...
		                  };

3. Insert the policy file name in the `inputs` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

            inputs => {
                        ...
                        "example_find_mac_addr.cf",
                        ...
                      };

This policy snippet will now be executed every five minutes along with the rest of your main policy.
