---
layout: default
title: Copy single files
categories: [Examples, Copy single files]
published: true
alias: examples-copy-single-files.html
tags: [Examples, copy files]
reviewed: 2013-06-01
reviewed-by: atsaloli
---

This is a standalone policy example that will copy single files, locally (`local_cp`) and from a remote site (`secure_cp`). The CFEngine Standard Library (cfengine_stdlib.cf) should be included in the `/var/cfengine/inputs/libraries/` directory and inputs list as below.

```cf3
    body common control
    {                       
    bundlesequence  => { "mycopy" };
    inputs => { "libraries/cfengine_stdlib.cf" };
    }

    bundle agent mycopy
    {
    files:
    
      "/tmp/test_plain"        # Path and name of the file we wish to copy to
    
          comment => "/tmp/test_plain promises to be an up-to-date copy of /bin/echo to demonstrate copying a local file",
        copy_from => local_cp("/bin/echo"); # Copy locally from path/filename

      "/tmp/test_remote_plain" # Path and name of the file we wish to copy to

          comment => "Demonstrate remote file copying.  /tmp/test_plain_remote promises to be a copy of cfengine://serverhost.example.org/repo/config-files/motd",
        copy_from => secure_cp("/repo/config-files/motd","serverhost.example.org"); # Copy remotely from path/filename and specified host
                                                                                    # Change to actual host name or IP address
}
```

This policy can be found in `/var/cfengine/share/doc/examples/unit_copy_stdlib.cf`.
