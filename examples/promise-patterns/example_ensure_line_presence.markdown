---
layout: default
title: Ensure line presence
categories: [Examples, Promise Patterns, Ensure line presence]
published: true
alias: examples-ensure-line-presence.html
tags: [Examples, Policy, line, insert, first, last, prepend, append]
---

If a line does not already exist, ensure that it is prepended or appended to the file.

[%CFEngine_include_example(ensure_line_present_prepend_append.cf)%]

Example usage:

```
# echo "existing line" > /tmp/test_line_prepend
# echo "existing line" > /tmp/test_line_append
# cf-agent -KI ensure_line_present_prepend_append.cf
info: /default/line_prepend/files/'/tmp/test_line_prepend'/default/prepend_if_no_line: Edit file '/tmp/test_line_prepend'
info: /default/line_append/files/'/tmp/test_line_append'/default/append_if_no_line: Edit file '/tmp/test_line_append'
# cat /tmp/test_line_prepend
I am the first line
existing line
# cat /tmp/test_line_append
existing line
I am the last line
# 
```
