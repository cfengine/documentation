---
layout: default
title: Testing Policies
published: true
sorting: 50
tags: [manuals, systems, configuration management, automation, testing, work directory]
---

One of the practical advantages of CFEngine is that you can test it without
the need for root or administrator privileges. This is useful if you are
concerned about manipulating important system files, but naturally limits the
possibilities for what CFEngine is able to do.

CFEngine operates with the notion of a work-directory. The default work
directory for the `root` user is `/var/cfengine`. For any other user, the work
directory lies in the user's home directory, named `~/.cfagent`.

CFEngine prefers you to keep certain files here. You should not resist this
too strongly or you will make unnecessary trouble for yourself. The decision
to have this 'known directory' was made to simplify a lot of configuration.

To test CFEngine as an ordinary user, do the following:

Copy the binaries into the work directory:

```
    host$ mkdir -p ~/.cfagent/inputs
    host$ mkdir -p ~/.cfagent/bin
    host$ cp /var/cfengine/bin/cf-* ~/.cfagent/bin
    host$ cp /var/cfengine/inputs/*.cf ~/.cfagent/inputs
```

You can test the software and play with configuration files by editing the
basic directly in the `~/.cfagent/inputs` directory. For example, try the
following:

    host$ ~/.cfagent/bin/cf-promises
    host$ ~/.cfagent/bin/cf-promises --verbose

This is always the way to start checking a configuration in CFEngine 3. If a
configuration does not pass this check/test, you will not be allowed to use
it, and `cf-agent` will look for the file `failsafe.cf`.
