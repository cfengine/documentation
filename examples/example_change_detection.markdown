---
layout: default
title: Change detection
categories: [Examples, Change detection]
published: true
alias: examples-change-detection.html
tags: [Examples, change detection]
reviewed: 2013-05-30
reviewed-by: atsaloli
---

This policy will look for changes recursively in a directory.

```cf3

    body common control
    
    {
    bundlesequence  => { "example"  };
    }
    
    ########################################################
    
    bundle agent example
    
    {
    files:
    
      "/home/mark/tmp/web"    # Directory to monitor for changes.
    
       changes      => detect_all_change,
       depth_search => recurse("inf");
    }
        
    #########################################################
        
    body changes detect_all_change
    
    {
    report_changes => "all";  
    update_hashes  => "true";
    }
    
    #########################################################
    
    body depth_search recurse(d)
    
    {
    depth        => "$(d)";
    }
```

This policy can be found in `/var/cfengine/share/doc/examples/unit_change_detect.cf`.
