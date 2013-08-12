---
layout: default
title: Change detection
categories: [Examples, Policy, Change detection]
published: true
alias: examples-policy-change-detection.html
tags: [Examples, Policy, change detection]
reviewed: 2013-06-08
reviewed-by: atsaloli
---

This policy will look for changes recursively in a directory.

[%CFEngine_include_example(change_detect.cf)%]

Here is an example run.

First, let's create some files for CFEngine to monitor:


```
# mkdir /etc/example 
# date > /etc/example/example.conf  
```

CFEngine detects new files and adds them to the file integrity database:

```
# cf-agent -f unit_change_detect.cf
2013-06-06T20:53:26-0700    error: /example/files/'/etc/example':
File '/etc/example/example.conf' was not in 'md5' database - new file found
# cf-agent -f unit_change_detect.cf -K
```

If there are no changes, CFEngine runs silently:

```
# cf-agent -f unit_change_detect.cf
#   
```

Now let's update the mtime, and then the mtime and content. 
CFEngine will notice the changes and record the new profile:

```
# touch /etc/example/example.conf # update mtime
# cf-agent -f unit_change_detect.cf -K
2013-06-06T20:53:52-0700    error: Last modified time for
'/etc/example/example.conf' changed 'Thu Jun  6 20:53:18 2013'
-> 'Thu Jun  6 20:53:49 2013'
# date >> /etc/example/example.conf # update mtime and content
# cf-agent -f unit_change_detect.cf -K
2013-06-06T20:54:01-0700    error: Hash 'md5' for '/etc/example/example.conf' changed!
2013-06-06T20:54:01-0700    error: /example/files/'/etc/example': Updating hash for
'/etc/example/example.conf' to 'MD5=8576cb25c9f78bc9ab6afd2c32203ca1'
2013-06-06T20:54:01-0700    error: Last modified time for '/etc/example/example.conf'
changed 'Thu Jun  6 20:53:49 2013' -> 'Thu Jun  6 20:53:59 2013'
#
```
