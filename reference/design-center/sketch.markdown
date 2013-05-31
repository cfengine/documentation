---
layout: default
title: Sketch structure
sortkey: 1
categories: [ Reference, Design Center, Sketch ]
published: true
alias: reference-design-center-sketch.html
tags: [sketch, structure, reference, design center ]
---

## Sketch structure

All sketches consists of at least two files:

* sketch.json
* main.cf

There might be additional supporting files for testing and additional CFEngine policy files (*.cf) for more advanced sketches.

## sketch.json

This file contains metadata about the sketch and declares the interface to the sketch.
A minimal sketch.json file contains the following attributes:

````
{

    manifest:
    {
        "main.cf": { desc: "main file", "version": "1.05.2" },
    },

    metadata:
    {
        "name": "Category::sketch_name",
        "description": "What the sketch does",
        "version": "1.0",
        "license": "MIT",
        "tags": [ "cfdc", "enterprise_compatible" ],
        "authors": [ "user@example.com" ],
        "depends": { "CFEngine::stdlib": { "version": 105 }, "CFEngine::dclib": { }, "cfengine": { "version": "3.4.0" }, "os": [ { "ubuntu" : "Ubuntu", "gentoo" : "Gentoo" } ] }
    },

    api:
    {
        bundlename:
        [
            { type: "environment", name: "runenv", },
            { type: "metadata", name: "metadata", },
            { type: "string", name: "mystring", description: "Purpose of mystring", validation: "MYSTRING_VALIDATION", example: "example mystring contents" },
            { type: "list", name: "mylist", description: "Purpose of mylist", validation: "MYLIST_VALIDATION", example: "example mylist item contents" }
        ],
    },

    namespace: "cfdc_sketch_name_namespace",

    interface: [ "main.cf" ]
}
````

### CFEngine Enterprise Compatibility

For a sketch to work well with the CFEngine Enterprise Design Center graphical user interface (GUI), all of the above attributes must be specified. Some additional requirements are noted below.

The `enterprise_compatible` tag must be set, otherwise it will not show up as an available sketch in the GUI.

All items in api.bundlename:

* any element that takes input (exluding e.g. runenv and metadata) must have `type` either `string` or `list` (support for more types will be added in the future)
* `validation` must be a validation that has been defined in the API (living either in `constdata.conf` or `vardata.conf`)
* the referenced validation must only use `minimum_value`, `maximum_value`, or `valid_regex`


## main.cf

This is the CFEngine policy that "implements" the sketch.

````
body file control
{
      namespace => "cfdc_sketch_name_namespace";
}

bundle agent installed(runenv, metadata, mystring, mylist)
{
  vars:
      "vars" slist => { "@(default:$(runenv).env_vars)" };
      "$(vars)" string => "$(default:$(runenv).$(vars))";

      "activation_id" string => canonify("$(this.bundle)_$($(metadata)[activation][identifier])_$($(metadata)[activation][timestamp])");

  reports:
      "mystring contents: $(mystring)"
         handle => "$(activation_id)_report_mystring";

      "mylist contents: $(mylist)"
         handle => "$(activation_id)_report_mylist";
}
````

### CFEngine Enterprise Compatibility

In order to map a sketch activation to reports (so that sketch activation and compliance can be detected),
CFEngine Enterprise requires the `activation_id` above to be defined. This `activation_id` must be prefixed
the handle in at least one promise in the sketch order to detect that the sketch has been run.

It is also important that promises that are used to measure compliance (like package installations and file edits)
have this handle prefix. Otherwise, the reporting will not detect sketch failure when these promises are not kept.

It may also be beneficial to include extra promises for reporting purposes and prefix their handle with `activation_id`.
For example, a promise that will become not kept if a web service goes down will be helpful to detect noncompliance
in a sketch that upgrades that web service.