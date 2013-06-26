---
layout: default
title: Sketches Available in the Mission Portal
categories: [Manuals, Design Center, Sketches in the Mission Portal]
published: true
sorting: 30
alias: mission-portal-design-center-sketches-available.html
tags: [available, sketch, design center, mission portal, enterprise, repository, extend]
---

As seen in the [CFEngine Enterprise sketch flow][Sketch Flow in CFEngine Enterprise],
the contents of `/var/cfengine/design-center/sketches` controls what is 
available to users of the Design Center GUI. This document explains how to 
adjust the available sketches and add your own.

Please note that the Design Center GUI imposes requirements on the sketches to 
be able to sufficiently guide the user of the GUI. See
[Sketch Structure][Sketch Structure] for a complete list of sketch 
requirements for CFEngine Enterprise compatibility.

## Filtering of available sketches

Perhaps you do not want to offer all of the sketches that come out of the box 
with CFEngine Enterprise to all the users of the Design Center GUI. You have 
two options:

* Remove the sketch from `/var/cfengine/design-center/sketches`
* Remove the `enterprise_compatible` tag in `sketch.json` found in the 
  directory of the sketch.

After doing either of these, we will need to run `make` inside 
`/var/cfengine/design-center/sketches` in order to update the description of 
available sketches for the GUI (it regenerates 
`/var/cfengine/design-center/sketches/cfsketches.json`).


### Example: filtering out the Packages::removed sketch

In this example, we will remove the Packages::removed sketch from the GUI by 
removing its `enterprise_compatible` tag.

Prior to our change, the list of available sketches in the GUI looks like the 
following.

![Sketches available in the Mission Portal](mission-portal-sketches-available.png)

1. Log in as root on the server that hosts the CFEngine Enterprise Mission Portal.
2. Open sketch.json.

        # vim /var/cfengine/design-center/sketches/package_management/packages_removed/sketch.json

3. Change

         "tags": [ "cfdc", "packages", "enterprise_compatible" ],
        to
         "tags": [ "cfdc", "packages" ],

4. Change to sketch directory.

        # cd /var/cfengine/design-center/sketches/

5. Regenerate sketch descriptions.

        # make

The sketch is now filtered out from the GUI, as shown by the following GUI 
screen-shot.

![Sketches available in the Mission Portal after filtering](mission-portal-sketches-available-sketch-filtered.png)


## Adding a new sketch to the GUI

In order to add a new sketch, we must make sure it complies with the 
Enterprise [specification for sketches][Sketch Structure].

We will create a sketch that just echoes what the user inputs in the GUI.

1. Make the directory for our new sketch.

        # mkdir -p /var/cfengine/design-center/sketches/system/echo
        # cd /var/cfengine/design-center/sketches/system/echo

2. Fill `main.cf` with the following.

    ```cf3
        body file control
        {
              namespace => "myskeches_echo";
        }

        bundle agent echo(runenv, metadata, toprint)
        {
          classes:
              "$(vars)" expression => "default:runenv_$(runenv)_$(vars)";
              "not_$(vars)" expression => "!default:runenv_$(runenv)_$(vars)";

          vars:
              "vars" slist => { "@(default:$(runenv).env_vars)" };
              "$(vars)" string => "$(default:$(runenv).$(vars))";

              "activation_id" string => canonify("$(this.bundle)_$($(metadata)[activation][identifier])_$($(metadata)[activation][timestamp])");

          commands:
              "/bin/echo $(toprint)"
                  comment => "Print to console for testing",
                  handle => "$(activation_id)_echo";
        }
    ```

3. Fill `sketch.json` with the following.

        {
            manifest:
            {
                "main.cf": { desc: "main file", "version": "1.0.0" },
            },
            metadata:
            {
                "name": "System::echo",
                "description": "Print input to the console.",
                "version": "1.0.0",
                "license": "MIT",
                "tags": [ "cfdc", "enterprise_compatible" ],
                "authors": [ "Author Name <author.name@example.com>" ],
                "depends": { "CFEngine::stdlib": { "version": 105 }, "CFEngine::dclib": { }, "cfengine": { "version": "3.5.0" }, "os": [ { "linux" : "All linux distributions" } ] }
            },
            api:
            {
                echo:
                [
                    { type: "environment", name: "runenv", },
                    { type: "metadata", name: "metadata", },
                    { type: "string", name: "toprint", description: "String to print to the console", validation: "STRING_NONEMPTY", example: "Hello world!" }
                ],
            },
            namespace: "myskeches_echo",
            interface: [ "main.cf" ]
        }

3. Regenerate the description of the sketches.

        # cd /var/cfengine/design-center/sketches
        # make


The sketch is now available in the GUI, as shown below.

![New echo sketch available in the Mission Portal](mission-portal-sketch-add-echo.png)

When going to the configuration page of the new echo sketch (clicking on it), 
you can see the input and description we configured in its `sketch.json`.

![New echo sketch configuration in the Mission Portal](mission-portal-sketch-add-echo-activation.png)
