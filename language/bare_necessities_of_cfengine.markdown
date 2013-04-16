### 1.11 The \`bare necessities' of a CFEngine 3

Here is the simplest \`Hello world' program in CFEngine 3:

    body common control
    {
    bundlesequence  => { "test" };
    }
    
    bundle agent test
    {
    reports:
    
     Yr2009::
        "Hello world";
    }

If you try to process this using the `cf-promises` command, you
will see something like this:

         atlas$ ~/LapTop/CFEngine3/trunk/src/cf-promises -r -f ./unit_null_config.cf
         Summarizing promises as text to ./unit_null_config.cf.txt
         Summarizing promises as html to ./unit_null_config.cf.html

The ‘-r’ option produces a report. Examine the files produced:

         cat ./unit_null_config.cf.txt
         firefox ./unit_null_config.cf.html

You will see a summary of how CFEngine interprets the files, either
in HTML or text. By default, the CFEngine components also dump a
debugging file, e.g. promise\_output\_agent.html,
promise\_output\_agent.txt with an expanded view.

