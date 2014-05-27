---
layout: default
title: Sketches Available in the Mission Portal
published: true
sorting: 30
tags: [available, sketch, design center, mission portal, enterprise, repository, extend]
---

As seen in the [CFEngine Enterprise sketch flow][Sketch Flow in CFEngine Enterprise],
the contents of `/var/cfengine/design-center/sketches` controls what sketches are 
available to users of the Design Center app (UI) on the Mission Portal console. This page 
explains how to adjust the available sketches and add your own.

**Note:** The Design Center imposes special requirements on sketches for Enterprise compatibility. 
See the CFEngine [sketch structure][Sketch Structure] for a complete list of sketch 
requirements.

## Filter available sketches in the Design Center app

CFEngine Enterprise comes with many sketches that are available out of the box to all users 
of the Design Center app. You can remove some of them in one of two ways:

* Remove the sketch from `/var/cfengine/design-center/sketches`
* Remove the `enterprise_compatible` tag from the `sketch.json` file that is located in the 
  directory of the sketch.

After performing either of these options, you must run `make` inside 
`/var/cfengine/design-center/sketches` in order to update the description of 
available sketches for the app (it regenerates 
`/var/cfengine/design-center/sketches/cfsketches.json`).


### Example: Remove the Packages::removed sketch

This example describes how to remove the **Packages::removed** sketch from the Design Center app by 
removing its `enterprise_compatible` tag.

Prior to our change, the list of available sketches in the app looks like the 
following.

![Sketches available in the Mission Portal](mission-portal-sketches-available.png)

Perform the following steps:

1. Log in as root on the server that hosts the CFEngine Enterprise Mission Portal.

2. Open `sketch.json`:

        # vim /var/cfengine/design-center/sketches/package_management/packages_removed/sketch.json

3. Change the following line:

        From
        
         "tags": [ "cfdc", "packages", "enterprise_compatible" ],
         
        to
        
         "tags": [ "cfdc", "packages" ],

4. Go to the sketch directory:

        # cd /var/cfengine/design-center/sketches/

5. Regenerate sketch descriptions:

        # make

The sketch is now filtered out from the Design Center, as shown by the following screenshot:

![Sketches available in the Mission Portal after filtering](mission-portal-sketches-available-sketch-filtered.png)


## Add a new sketch to the Design Center app

In order to add a new sketch, make sure it complies with the 
Enterprise [specification for sketches][Sketch Structure].

Create a sketch that just echoes what the user inputs in the Design Center app.

1. Make the directory for your new sketch:

        # mkdir -p /var/cfengine/design-center/sketches/system/echo
        # cd /var/cfengine/design-center/sketches/system/echo

2. Fill `main.cf` with the following:

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

3. Fill `sketch.json` with the following:

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

3. Regenerate the description of the sketches:

        # cd /var/cfengine/design-center/sketches
        # make


The sketch is now available in the Design Center app, as shown below:

![New echo sketch available in the Mission Portal](mission-portal-sketch-add-echo.png)

Open the configuration page of the new echo sketch by clicking on it. 
The input and description we configured in its `sketch.json` file displays below:

![New echo sketch configuration in the Mission Portal](mission-portal-sketch-add-echo-activation.png)
