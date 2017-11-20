---
layout: default
title: Sketch Structure
published: false
tags: [sketch, structure, reference, design center]
---

All Design Center sketches consists of at least two files:

* `sketch.json`
* `main.cf`

There might be additional supporting files for testing and additional CFEngine
policy files (*.cf) for more advanced sketches.

## sketch.json

This file contains metadata about the sketch and declares the interface to the
sketch. A minimal sketch.json file looks like this:

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
        "depends": { "Other::Dependency::Sketch": { }, "cfengine": { "version": "3.6.0" }, "os": [ { "ubuntu" : "Ubuntu", "gentoo" : "Gentoo" } ] }
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

For a sketch to work well with the CFEngine Enterprise Design Center graphical
user interface (GUI), all of the above attributes must be specified. Some
additional requirements are noted below.

The `depends.os` attribute is checked when a user is activating a sketch, to
warn on cases where a user attempts to activate a sketch on an operating system
the sketch does not (yet) support. It is therefore useful to make sure that
all the operating systems listed in `depends.os` is working well with the sketch.
Each element has the format `{ "os_class" : "OS friendly name" }`. "OS friendly
name" is displayed in the GUI.

The `enterprise_compatible` tag must be set, otherwise it will not show up as
an available sketch in the GUI.

All items in api.bundlename:

* any element that takes input (excluding e.g. runenv and metadata) must have
`type` either `string` or `list` (support for more types will be added in the
future)
* `validation` must be a validation that has been defined in the API (living
either in `constdata.conf` or `vardata.conf`)
* the referenced validation can use `minimum_value`, `maximum_value`, or
`valid_regex`.  Other choices are available in Enterprise 3.6.

## Upgrading sketches

There are three ways to upgrade a Design Center sketch repository.

### Upgrade a Design Center sketch repository from the Github master branch of Design Center

`cf-sketch --install-all --inputs=/var/cfengine/design-center`

The `installsource` is omitted but defaults to the Github master branch, so the above is equivalent to:

`cf-sketch --install-all --inputs=/var/cfengine/design-center --installsource=https://raw.githubusercontent.com/cfengine/design-center/master/sketches/cfsketches.json`

### Upgrade a Design Center sketch repository from the Github 3.6.x branch of Design Center

`cf-sketch --install-all --inputs=/var/cfengine/design-center --installsource=https://raw.githubusercontent.com/cfengine/design-center/3.6.x/sketches/cfsketches.json`

### Upgrade a Design Center sketch repository from your own sketch repository

You would do this if you maintain sketches for your own organization.

`cf-sketch --install-all --inputs=/var/cfengine/design-center --installsource=/myrepo/sketches/cfsketches.json`
