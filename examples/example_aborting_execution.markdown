---
layout: default
title: Aborting execution 
categories: [Examples, Aborting execution]
published: true
alias: examples-aborting-execution.html
tags: [Examples, aborting execution]
---

Sometimes it is useful to abort a bundle execution if certain conditions are not met,
for example when validating input to a bundle. The following policy uses a list of 
regular expressions for classes, or class expressions that `cf-agent` will watch out for.
If any of these classes becomes defined, it will cause the current bundle to be aborted.

```cf3
    body common control

    {
    bundlesequence  => { "testbundle"  };

    version => "1.2.3";
    }

    ###########################################

    body agent control

    {
    abortbundleclasses => { "invalid" };            # Abort bundle execution if this class is set
    }

    ###########################################

    bundle agent testbundle
    {
    vars:

     "userlist" slist => { "xyz", "mark", "jeang", "jonhenrik", "thomas", "eben" };

    methods:

     "any" usebundle => subtest("$(userlist)");

    }

    ###########################################

    bundle agent subtest(user)

    {
    classes:

      "invalid" not => regcmp("[a-z][a-z][a-z][a-z]","$(user)"); # The class 'invalid' is set if the user name does not
                                                                 # contain exactly four un-capitalized letters (bundle
                                                                 # execution will be aborted if set)

    reports:

     !invalid::

      "User name $(user) is valid at 4 letters";

     invalid::

      "User name $(user) is invalid";
    }
```

This policy can be found in `/var/cfengine/share/doc/examples/unit_abort.cf`.

To run this example file as part of your main policy you need to make an
additional change:

There cannot be two `body agent control` in the main policy. Copy and paste 
`abortbundleclasses => { "invalid" };` into /var/cfengine/masterfiles/controls/cf_agent.cf. 
If you add it to the end of the file it should look something like this:

```cf3
    ...
        #  dryrun => "true";
        
        abortbundleclasses => { "invalid" };
    }
```

Delete the `body agent control` section from /var/cfengine/masterfiles/unit_abort.cf.
