---
layout: default
title: Aborting execution 
categories: [Examples, Policy, Aborting execution]
published: true
alias: examples-policy-aborting-execution.html
tags: [Examples, Policy, aborting execution]
reviewed: 2013-05-30
reviewed-by: atsaloli
---

Sometimes it is useful to abort a bundle execution if certain conditions are not met,
for example when validating input to a bundle. The following policy uses a list of 
regular expressions for classes, or class expressions that `cf-agent` will watch out for.
If any of these classes becomes defined, it will cause the current bundle to be aborted.

```cf3

body common control
{
bundlesequence  => { "example"  };
}

body agent control
{
abortbundleclasses => { "invalid" };      # Abort bundle execution if this class is set
}

###########################################

bundle agent example
{
vars:

  #"userlist" slist => { "mark", "john" };           # contains all valid entries
  "userlist" slist => { "mark", "john", "thomas" };  # contains one invalid entry

classes:

  "invalid" not => regcmp("[a-z][a-z][a-z][a-z]","$(userlist)"); # The class 'invalid' is set if the user name does not
                                                                 # contain exactly four un-capitalized letters (bundle
                                                                 # execution will be aborted if set)

reports:

  !invalid::

    "User name $(userlist) is valid at 4 letters";
}
```

This policy can be found in `/var/cfengine/share/doc/examples/unit_abort.cf`.

This is how the policy runs when the userlist is valid:

    # cf-agent -f unit_abort.cf
    R: User name mark is valid at 4 letters
    R: User name john is valid at 4 letters
    # 

This is how the policy runs when the userlist contains an invalid entry:

    # cf-agent -f unit_abort.cf
    Bundle example aborted on defined class "invalid"
    # 

To run this example file as part of your main policy you need to make an
additional change:

There cannot be two `body agent control` in the main policy. Delete the
`body agent control` section from /var/cfengine/masterfiles/unit_abort.cf.
Copy and paste `abortbundleclasses => { "invalid" };` into
/var/cfengine/masterfiles/controls/cf_agent.cf.  If you add it to
the end of the file it should look something like this:

```cf3
...
    #  dryrun => "true";
    
    abortbundleclasses => { "invalid" };
}
```

