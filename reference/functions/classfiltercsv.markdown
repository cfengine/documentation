---
layout: default
title: classfiltercsv
published: true
tags: [reference, csv, data functions, functions, classfiltercsv]
---

[%CFEngine_function_prototype(filename, has_header, class_column, optional_sort_column)%]

**Description:**
Parses CSV data from the file `filename`, and returns a data variable that is
filtered by defined classes. If `has_header` is set to `true`, the columns in
the first line of the CSV file are used as keys for the data. `class_column`
specifies which column contains class names to filter by.

If `optional_sort_column` is defined, the data containers will be sorted by the
given column. Both `class_column` and `optional_sort_column` must be integer
indices starting from `0`, and must be at most the total amount of columns
minus `1`.

[%CFEngine_function_attributes(filename, has_header, class_column, optional_sort_column)%]

**Example:**

{%raw%}
[%CFEngine_include_example(classfiltercsv.cf)%]
{%endraw%}

**See also:** [readcsv()][readcsv], [classmatch()][classmatch]

**History:** Introduced in CFEngine 3.14
