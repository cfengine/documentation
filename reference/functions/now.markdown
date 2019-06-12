---
layout: default
title: now
published: true
tags: [reference, system functions, functions, now]
---

[%CFEngine_function_prototype()%]

**Description:** Return the time at which this agent run started
in system representation.

In order to provide an immutable environment against which to converge,
this value does not change during the execution of an agent.

**Examples:**

Reporting the system time of agent start and calculating what yesterday was.

```cf3
bundle agent example_now
{
  vars:
      "epoch" int => now();

      "24_hours_ago"
        string => format( "%d",
                          eval( "$(epoch)-86400", math, infix ));

  reports:
      "Today is $(with) or in unix format '$(epoch)'"
        with => strftime( gmtime, "%Y-%m-%d %T", $(epoch) );

      "24 hours ago was $(with) or in unix format '$(epoch)'"
        with => strftime( gmtime, "%Y-%m-%d %T", $(24_hours_ago) );
}

bundle agent __main__
{
  methods:
      "example_now";
}
```

**Output:**

```
R: Today is 2019-06-12 20:40:00 or in unix format '1560372000'
R: 24 hours ago was 2019-06-11 20:40:00 or in unix format '1560372000'
```

`files` type promises using ```file_select``` to limit recursive file selection
based on a time relative to the agent start can make use of this function.

```cf3
    bundle agent gzip_recent_pdfs
    {
       files:

         # Ensure that any file ending in .pdf that has been
         # modified in the last year is compressed

         "/tmp/"
           file_select => pdf_modified_within_last_year,
           transformer => '/bin/gzip $(this.promiser)';
    }

    body file_select pdf_modified_within_last_year
    # @brief Sllect files that have been modified in the last year AND end in .pdf
    {
      mtime       => irange(ago(1,0,0,0,0,0),now);
      leaf_name => { ".*\.pdf" };
      file_result => "mtime.leaf_name";
    }
```

`processes` type promises using ```process_select``` can use this function to
select processes based on relative execution time.

[%CFEngine_include_example(processes_define_class_based_on_process_runtime.cf)%]

