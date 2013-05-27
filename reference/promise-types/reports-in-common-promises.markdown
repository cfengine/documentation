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

**Synopsis**: Regular expression to keep selected hosts from the friends
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

**Synopsis**: Real number threshold [0,1] of intermittency about current
peers, report above

**Type**: `real`

**Allowed input range**: `0,1`

**Default value:** `intermittency => "0"`


#### lastseen

**Synopsis**: Integer time threshold in hours since current peers were
last seen, report absence

In reports: After this time has passed, CFEngine will begin to warn 
about the host being overdue. After the `lastseenexpireafter` expiry time, 
hosts will be purged from this host's database.

**Type**: `int`

**Allowed input range**: `0,99999999999`

**Default value**: `lastseen => 168 # one week`

<!--- **Documented in body agent control as deprecated**
In control: Determines whether CFEngine will record last seen
intermittency profiles (reliability diagnostics) in WORKDIR/lastseen.
This generates a separate file for each each host that connects to the
current host. For central hubs this can result is a huge number of
files.
-->

**Example**:  

<!--- **Documented in body agent control as deprecated**
In control:

```cf3
body agent control
{
lastseen => "false";
}
```
-->

```cf3
    reports:

      "Comment"

        lastseen => "10";
```

### printfile

**Synopsis**: Outputs the content of a file to standard output

**Type**: `body printfile`

#### file_to_print

**Synopsis**: Path name to the file that is to be sent to standard
output

Include part of a file in a report.

**Type**: `string`

**Allowed input range**: `"?(/.*)`

#### number_of_lines

**Synopsis**: Integer maximum number of lines to print from selected
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

**Synopsis**: The path and filename to which output should be appended

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

**Synopsis**: The promiser is to be interpreted as a literal value that
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

**Synopsis**: List of services about which status reports should be
reported to standard output

**Type**: `slist`

**Allowed input range**: (arbitrary string)

**Example**:  

```cf3
    reports:
      cfengine::

        "Current state:"
          showstate => {"www_in", "ssh_out", "otherprocs" };
```

**Notes**:  
   
The basic list of services is:

* users - Users logged in   
* rootprocs - Privileged system processes   
* otherprocs - Non-privileged process   
* diskfree - Free disk on / partition   
* loadavg - % kernel load utilization   
* netbiosns\_in - netbios name lookups (in)   
* netbiosns\_out - netbios name lookups (out)   
* netbiosdgm\_in - netbios name datagrams (in)   
* netbiosdgm\_out - netbios name datagrams (out)   
* netbiosssn\_in - netbios name sessions (in)   
* netbiosssn\_out - netbios name sessions (out)   
* irc\_in - IRC connections (in)   
* irc\_out - IRC connections (out)   
* cfengine\_in - CFEngine connections (in)   
* cfengine\_out - CFEngine connections (out)   
* nfsd\_in - nfs connections (in)   
* nfsd\_out - nfs connections (out)   
* smtp\_in - smtp connections (in)   
* smtp\_out - smtp connections (out)   
* www\_in - www connections (in)   
* www\_out - www connections (out)   
* ftp\_in - ftp connections (in)   
* ftp\_out - ftp connections (out)   
* ssh\_in - ssh connections (in)   
* ssh\_out - ssh connections (out)   
* wwws\_in - wwws connections (in)   
* wwws\_out - wwws connections (out)   
* icmp\_in - ICMP packets (in)   
* icmp\_out - ICMP packets (out)   
* udp\_in - UDP dgrams (in)   
* udp\_out - UDP dgrams (out)   
* dns\_in - DNS requests (in)   
* dns\_out - DNS requests (out)   
* tcpsyn\_in - TCP sessions (in)   
* tcpsyn\_out - TCP sessions (out)   
* tcpack\_in - TCP acks (in)   
* tcpack\_out - TCP acks (out)   
* tcpfin\_in - TCP finish (in)   
* tcpfin\_out - TCP finish (out)   
* tcpmisc\_in - TCP misc (in)   
* tcpmisc\_out - TCP misc (out)   
* webaccess - Webserver hits   
* weberrors - Webserver errors   
* syslog - New log entries (Syslog)   
* messages -  - New log entries (messages)   
* temp0 - CPU Temperature 0   
* temp1 - CPU Temperature 1   
* temp2 - CPU Temperature 2   
* temp3 - CPU Temperature 3   
* cpu - %CPU utilization (all)   
* cpu0 - %CPU utilization 0   
* cpu1 - %CPU utilization 1   
* cpu2 - %CPU utilization 2   
* cpu3 - %CPU utilization 3