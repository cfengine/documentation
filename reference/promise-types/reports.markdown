---
layout: default
title: reports
categories: [Reference, Promise Types, reports]
published: true
alias: reference-promise-types-reports.html
tags: [reference, bundles, common, reports, promises]
---

Reports promises simply print messages. Outputting a message without qualification can be a dangerous operation. In a large installation
it could unleash an avalanche of messaging.

```cf3
    reports:

    "literal string or file refererence",
       printfile = printfile_body,
       ...;
```

Messages outputted from report promises are prefixed with the letter R to distinguish them from other output, for example from `commands`.


```cf3
    bundle agent report
    {
    reports:

      linux::

       "/etc/passwd except $(const.n)"

        # printfile => pr("/etc/passwd","5");

         showstate => { "otherprocs", "rootprocs" };
    }
```

### friend_pattern

**Description**: Regular expression to keep selected hosts from the friends
report list

This regular expression should match hosts we want to exclude from
friend reports.

**Type**: `string`

**Allowed input range**: (arbitrary string)

**Example**:

```cf3
reports:

  linux::

   "Friend status report"

          lastseen => "0",
     friend_pattern => "host1|host2|.*\.domain\.tld";
```

### intermittency

**Description**: Real number threshold [0,1] of intermittency about current
peers, report above

**Type**: `real`

**Allowed input range**: `0,1`

**Default value:** `intermittency => "0"`


### printfile

**Description**: Outputs the content of a file to standard output

**Type**: `body printfile`

#### file_to_print

**Description**: Path name to the file that is to be sent to standard
output

Include part of a file in a report.

**Type**: `string`

**Allowed input range**: `"?(/.*)`

#### number_of_lines

**Description**: Integer maximum number of lines to print from selected
file

**Type**: `int`

**Allowed input range**: `0,99999999999`

**Example**:  

```cf3
     bundle agent example
     {
     reports:
       linux::
         "$(sys.date) - current message of the day:"
            printfile => "motd";
     }

     body printfile motd
     {
         file_to_print   => "/etc/motd";
         number_of_lines => "10";
     }
```


### report_to_file

**Description**: The path and filename to which output should be appended

Append the output of the report to the named file instead of standard output. 
If the file cannot be opened for writing then the report defaults to the 
standard output.

**Type**: `string`

**Allowed input range**: `"?(/.*)`

**Example**:  

```cf3
    bundle agent test
    {
    reports:

      linux::

       "$(sys.date),This is a report from $(sys.host)"

           report_to_file => "/tmp/test_log";
    }
```

### bundle_return_value_index

**Description**: The promiser is to be interpreted as a literal value that
the caller can accept as a result for this bundle; in other words, a
return value with array index defined by this attribute.

**Type**: `string`

**Allowed input range**: `[a-zA-Z0-9_$(){}\[\].:]+`

**Example**:  

```cf3
    body common control
    {
    bundlesequence => { "test" };
    }


    bundle agent test
    {
    methods:

       "any" usebundle => child,
        useresult => "my_return_var";


    reports:

      cfengine_3::

        "My return was: \"$(my_return_var[1])\" and \"$(my_return_var[2])\""; 
    
    }

    bundle agent child
    {
    reports:

     cfengine_3::

       # Map these indices into the useresult namespace

       "this is a return value"  
          bundle_return_value_index => "1";

       "this is another return value"  
          bundle_return_value_index => "2";

    }
```

**Notes**:

Return values are limited to scalars.

### showstate

**Deprecated**: This attribute is kept for source compatibility,
and has no effect.

### lastseen

**Deprecated**: This attribute is kept for source compatibility,
and has no effect.
