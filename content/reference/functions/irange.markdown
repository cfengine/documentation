---
layout: default
title: irange
---

[%CFEngine_function_prototype(arg1, arg2)%]

**Description:** Define a range of integer values for CFEngine internal use.

Used for any scalar attribute which requires an integer range. You can
generally interchangeably say `"1,10"` or `irange("1","10")`. However, if
you want to create a range of dates or times, you must use `irange()` if you
also use the functions `ago()`, `now()`, `accumulated()`, etc.

[%CFEngine_function_attributes(arg1, arg2)%]

**Example:**

```cf3
irange("1","100");

irange(ago(0,0,0,1,30,0), "0");
```

**See also:**

* Functions commonly used with [`irange()`][irange]
  * [`ago()`][ago]
  * [`now()`][now]
  * [`accumulated()`][accumulated]
* Attributes of type ```irange```
  * [`atime` in body `file_select`][files#atime]
  * [`copy_size` in body `copy_from`][files#copy_size]
  * [`ctime` in body `file_select`][files#ctime]
  * [`mtime` in body `file_select`][files#mtime]
  * [`match_range` in body `process_count`][processes#match_range]
  * [`pgid` in body `process_select`][processes#pgid]
  * [`pid` in body `process_select`][processes#pid]
  * [`ppid` in body `process_select`][processes#ppid]
  * [`priority` in body `process_select`][processes#priority]
  * [`rsize` in body `process_select`][processes#rsize]
  * [`search_size` in body `file_select`][files#search_size]
  * [`stime_range` in body `process_select`][processes#stime_range]
  * [`threads` in body `process_select`][processes#threads]
  * [`ttime_range` in body `process_select`][processes#ttime_range]
  * [`vsize` in body `process_select`][processes#vsize]
