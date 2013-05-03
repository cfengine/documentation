---
layout: default
title: outputs-in-agent-promises
categories: [Bundles-for-agent,outputs-in-agent-promises]
published: true
alias: Bundles-for-agent-outputs-in-agent-promises.html
tags: [Bundles-for-agent,outputs-in-agent-promises]
---

### `outputs` promises in agent

\

Outputs promises allow promises to make meta-promises about their output
levels. More simply, you can switch on verbose or inform level output to
named promises, or whole bundles for debugging purposes.

If you use the -I or -v command line options, then CFEngine will
generate informative or verbose output for all the promises it is
processing. This can be a daunting collection of data when dealing with
even a medium-sized set of promises.

Output promises enable you to selectively debug individually named
promises (or bundles), thus eliminating the need for scanning unrelated
CFEngine output.

\

~~~~ {.verbatim}
outputs:

  "run_agent";      # Promise handle, verbose (default) output

  "web_server"      # Bundle handle, inform output
     output_level => "inform",
     promiser_type => "bundle";
~~~~

A very handy paradigm is to include outputs promises in every bundle,
and guard them with classes. For example:

~~~~ {.verbatim}
bundle agent some_function
{
vars:
    ...
classes:
    ...
outputs:
  debug_some_function::
      "some_function"
     output_level => "verbose",
     promiser_type => "bundle";
files:
    ...
}
~~~~

You can then execute your promises normally with no extra output, but
should you wish to temporarily enable debugging, you can simply do so
from the command line by specifying -D debug\_some\_function. You can
also supply multiple arguments to -D to debug multiple bundles. Of
course, you can also provide much finer-grained control by creating
outputs promises on specific promise handles.

\

The default behaviour is to print verbose output for listed promise
handles. See [handle in \*](#handle-in-_002a), for bundle names.

**History** This was introduced in Nova version 1.1.3 (2010), Community
version 3.4.0 (2012)

-   [output\_level in outputs](#output_005flevel-in-outputs)
-   [promiser\_type in outputs](#promiser_005ftype-in-outputs)

#### `output_level`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               verbose
               debug
               inform
~~~~

**Default value:** verbose

**Synopsis**: Output level to observe for the named promise or bundle
(meta-promise)

**Example**:\
 \

~~~~ {.verbatim}
commands:

  "/etc/init.d/agent start"

    handle => "run_agent",
    ifvarclass => "need_to_run_agent";

outputs:

  "run_agent"

    output_level => "inform"; 
~~~~

**Notes**:\
 \

With no attribute, `verbose` output is assumed.

#### `promiser_type`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               promise
               bundle
~~~~

**Default value:** promise

**Synopsis**: Output level to observe for the named promise or bundle
(meta-promise)

**Example**:\
 \

~~~~ {.verbatim}
outputs:

  "web_server"

     promiser_type => "bundle";
~~~~

**Notes**:\
 \

Without this attribute, CFEngine assumes a list of promises to report
on. There may be a promise for a thing that has the same name as a
bundle, and you must therefore explicitly specify when you want to
report on a bundle of promises.
