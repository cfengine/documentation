---
layout: default
title: reports
published: true
tags: [reference, bundle common, reports, promises]
---

Reports promises simply print messages. Outputting a message without
qualification can be a dangerous operation. In a large installation it
could unleash an avalanche of messaging, so it is recommended that
reports are guarded appropriately.

[%CFEngine_include_example(reports.cf)%]

{% comment %} TODO: Should link to a page that describes all cfengine output
here where we explain that output from reports type promises are
prefixed with the letter R. {% endcomment %}

Messages output by report promises are prefixed with the letter R to
distinguish them from other output.

```cf3
bundle agent report
{
  reports:

    loadavg_high::

      "Processes:"
         printfile => cat("$(sys.statedir)/cf_procs");
}
```

Reports do not fundamentaly make changes to the system and report type promise
outcomes are *always* considered kept.

```cf3
bundle agent report
{
  vars:
    "classes" slist => classesmatching("report_.*");

  reports:
    "HI"
      classes => scoped_classes_generic("bundle", "report");

    "found class: $(classes)";
}

body classes scoped_classes_generic(scope, x)
# Define x prefixed/suffixed with promise outcome
{
  scope => "$(scope)";
  promise_repaired => { "promise_repaired_$(x)", "$(x)_repaired", "$(x)_ok", "$(x)_reached" };
  repair_failed => { "repair_failed_$(x)", "$(x)_failed", "$(x)_not_ok", "$(x)_not_kept", "$(x)_not_repaired", "$(x)_reached" };
  repair_denied => { "repair_denied_$(x)", "$(x)_denied", "$(x)_not_ok", "$(x)_not_kept", "$(x)_not_repaired", "$(x)_reached" };
  repair_timeout => { "repair_timeout_$(x)", "$(x)_timeout", "$(x)_not_ok", "$(x)_not_kept", "$(x)_not_repaired", "$(x)_reached" };
  promise_kept => { "promise_kept_$(x)", "$(x)_kept", "$(x)_ok", "$(x)_not_repaired", "$(x)_reached" };
}
```

```console
$ cf-agent -KIf ./example_report_outcomes.cf -b report
2015-05-13T12:48:12-0500     info: Using command line specified bundlesequence
R: HI
R: found class: report_ok
R: found class: report_kept
R: found class: report_reached
R: found class: report_not_repaired
```

****

## Attributes ##

[%CFEngine_include_markdown(common-attributes-include.markdown)%]

### friend_pattern

**Deprecated:** This attribute is kept for source compatibility,
and has no effect. Deprecated in CFEngine 3.4.

### intermittency

**Deprecated:** This attribute is kept for source compatibility,
and has no effect. Deprecated in CFEngine 3.4.

### printfile

**Description:** Outputs the content of a file to standard output

**Type:** `body printfile`

**See also:** [Common Body Attributes][Promise Types#Common Body Attributes]

#### file_to_print

**Description:** Path name to the file that is to be sent to standard
output

Include part of a file in a report.

**Type:** `string`

**Allowed input range:** `"?(/.*)`

#### number_of_lines

**Description:** Integer maximum number of lines to print from selected file

**Type:** `int`

**Default value:** `5`

**Allowed input range:** `-99999999999,99999999999`

**Note:** Prints lines from end of file when a negative number is passed to
argument `number_of_lines`

**Example:**

[%CFEngine_include_snippet(printfile.cf, #\+begin_src prep, .*end_src)%]

[%CFEngine_include_snippet(printfile.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(printfile.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:**

- Introduced negative number support in 3.18.0

### report_to_file

**Description:** The path and filename to which output should be appended

Append the output of the report to the named file instead of standard output.
If the file cannot be opened for writing then the report defaults to the
standard output.

**Type:** `string`

**Allowed input range:** `"?(/.*)`

**Example:**

```cf3
bundle agent main
{

  reports:

      "$(sys.date),This is a report from $(sys.host)"
        report_to_file => "/tmp/test_log";
}
```

### bundle_return_value_index

**Description:** The promiser is to be interpreted as a literal value that
the caller can accept as a result for this bundle; in other words, a
return value with array index defined by this attribute.

Return values are limited to scalars.

**Type:** `string`

**Allowed input range:** `[a-zA-Z0-9_$(){}\[\].:]+`

**Example:**

```cf3
bundle agent main
{
  methods:

     "any"
       usebundle => child,
       useresult => "my_return_var";

  reports:

     "My return was: '$(my_return_var[1])' and '$(my_return_var[2])' and '$(my_return_var[named])'";
}

bundle agent child
{
  reports:

   # Map these indices into the useresult namespace

     "this is a return value"
        bundle_return_value_index => "1";

     "this is another return value"
        bundle_return_value_index => "2";

     "bundle_return_value_index is not required to be numerical"
        bundle_return_value_index => "named";
}
```

**See also:** [methods useresult attribute][methods#useresult]

**History:** Introduced in 3.4.0.

### lastseen

**Deprecated:** This attribute is kept for source compatibility,
and has no effect. Deprecated in CFEngine 3.4.

### showstate

**Deprecated:** This attribute is kept for source compatibility,
and has no effect. Deprecated in CFEngine 3.5.
