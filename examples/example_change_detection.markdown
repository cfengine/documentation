---
layout: default
title: Change detection
categories: [Examples, Change detection]
published: true
alias: examples-change-detection.html
tags: [Examples, change detection]
---

This is a standalone policy that will look for changes recursively in a directory and log them in the promise repaired log.

```cf3
    body common control

    {
    bundlesequence  => { "testbundle"  };
    }

    ########################################################

    bundle agent testbundle

    {
    files:

      "/home/mark/tmp/web" -> "me"  # Directory to monitor for changes.
                                    # The right arrow denotes a promisee,
                                    # or stakeholder, used for documentation purposes

       changes      => detect_all_change,
       depth_search => recurse("inf");
    }
```

This policy can be found in `/var/cfengine/share/doc/examples/unit_change_detect.cf`.
