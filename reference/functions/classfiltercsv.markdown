---
layout: default
title: classfiltercsv
published: true
tags: [reference, csv, data functions, functions, classfiltercsv]
---

[%CFEngine_function_prototype(filename, has_header, class_column, optional_sort_column)%]

**Description:**
Parses CSV data from an [RFC 4180](http://www.ietf.org/rfc/rfc4180.txt) compliant file `filename` (`CRLF` line endings required), and returns a data variable that is
filtered by defined classes. If `has_header` is set to `true`, the columns in
the first line of the CSV file are used as keys for the data. `class_column`
specifies which column contains class names to filter by.

If `optional_sort_column` is defined, the data containers will be sorted by the
given column. Both `class_column` and `optional_sort_column` must be integer
indices starting from `0`, and must be at most the total amount of columns
minus `1`.

[%CFEngine_function_attributes(filename, has_header, class_column, optional_sort_column)%]

**Example:**

**Prepare CSV:**

[%CFEngine_include_snippet(classfiltercsv.cf, #\+begin_src prep, .*end_src)%]

**Policy:**

[%CFEngine_include_snippet(classfiltercsv.cf, #\+begin_src cfengine3, .*end_src)%]

**Output:**

[%CFEngine_include_snippet(classfiltercsv.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**

* If the CSV file is stored in a `git` repository the `.gitattributes` file can be used to ensure proper line endings.

   For example:

   ```
   # .gitattribtues
   *.csv     text eol=crlf
   RFC-4180-non-compliant-line-endings.csv eol=lf
   *.mustache text
   *.sh       text eol=lf
   ```

**See also:** [readcsv()][readcsv], [classmatch()][classmatch]

**History:**

- Introduced in CFEngine 3.14
