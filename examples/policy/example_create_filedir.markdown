---
layout: default
title: Create files and directories
categories: [Examples, Policy, Create files and directories]
published: true
alias: examples-policy-create-files-and-directories.html
tags: [Examples, Policy, create, files and directories]
---

The following is a standalone policy that will create the file
`/home/mark/tmp/test_plain` and the directory `/home/mark/tmp/test_dir/`
and set permissions on both.

[%CFEngine_include_example(create_filedir.cf)%]

Example output:

```
# cf-agent -f unit_create_filedir.cf -I
2013-06-08T14:56:26-0700     info: /example/files/'/home/mark/tmp/test_plain': Created file '/home/mark/tmp/test_plain', mode 0640
2013-06-08T14:56:26-0700     info: /example/files/'/home/mark/tmp/test_dir/.': Created directory '/home/mark/tmp/test_dir/.'
2013-06-08T14:56:26-0700     info: /example/files/'/home/mark/tmp/test_dir/.': Object '/home/mark/tmp/test_dir' had permission 0755, changed it to 0750
# 
```
