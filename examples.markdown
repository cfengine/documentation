---
layout: default
title: CFEngine Examples 
categories: [Examples]
published: true
sorting: 50
alias: examples.html
tags: [Examples]
---

You can find more examples for CFEngine Code in the Design Center
[GitHub repository](https://github.com/cfengine/design-center/tree/master/examples).

## Running the Example policies

The policy files can be found in `/var/cfengine/share/doc/examples`. You can 
test them locally by copying the respective _`example_file.cf`_ file into
`/var/cfengine/inputs` and running:

    $ /var/cfengine/bin/cf-agent -f example_file.cf

## Integrating the Example into your Main Policy

Make the example policy part of your main policy by
doing the following on your policy server:

1. Copy the file from `/var/cfengine/share/doc/examples` to
    `/var/cfengine/masterfiles`.

2. Delete the `body common control` section in
    `/var/cfengine/masterfiles/example_file.cf`:

  ```cf3
      body common control
      {
        bundlesequence  => { "testbundle" };
      }
  ```

3. Insert the example's bundle name in the `bundlesequence` section
    of the main policy file `/var/cfengine/masterfiles/promises.cf`:

  ```cf3
      bundlesequence => {
          ...
          "testbundle",
          ...
      };
  ```

4. Insert the policy file name in the `inputs` section of the main policy file
    `/var/cfengine/masterfiles/promises.cf`:

  ```cf3
      inputs => {
           ...
           "example_file.cf",
           ...
      };
  ```

5. *CONDITIONAL* If the example contains a control body section
   (e.g. `body agent control`):

  You cannot have duplicate control bodies (i.e. two
  agent control bodies, one in the main file and one
  in the example) as CFEngine won't know which it
  should use and they may conflict.

  To resolve this, copy the contents of the control body section from the
  example into the identically named control body section in the main policy
  file `/var/cfengine/masterfiles/promises.cf`and then remove the control body
  from the example.

6. You must remove the inputs section from the example, which 
   includes the external library:

  ```cf3
      inputs => {
        "libraries/cfengine_stdlib.cf"
      };
  ```
  This is necessary, since `cfengine_stdlib.cf` is already included
  in the inputs section of the master policy.

  The example policy will now be executed every five minutes along with the rest
  of your main policy.

**Notes:** You may have to fill the example with data before it will work.
For example, the LDAP query in `active_directory.cf` needs a domain name.
In the variable declaration, replace "cftesting" with your domain name:

```cf3
    vars:
        # NOTE: Edit this to your domain, e.g. "corp"
       "domain_name" string => "cftesting";
```
