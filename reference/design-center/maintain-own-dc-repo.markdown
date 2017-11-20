---
layout: default
title: Maintaining your own sketch repository
published: false
tags: [sketch, repository, reference, design center]
---

Some users and customers would like to maintain their own Design Center repo. It's pretty simple if you copy and paste these commands to run them as root. Add `-v` to see debug output if something goes wrong.

## Create Your Sketches

For example, say we start with `Utilities::Roles`. Copy the `roles` directory from the Design Center (`/var/cfengine/share/*Base/sketches/utilities/roles`) to `/my/repo/sketches` and edit `sketch.json` and `main.cf` as needed, let's say changing the list of roles.

```
cp -rp /var/cfengine/share/*Base/sketches/utilities/roles /my/repo/sketches/
```

## Copy The Sketch Template

<!--- TODO: This step is required for 3.6.0 but we hope to eliminate it in 3.6.1. -->

```
cp -rp /var/cfengine/share/*Base/sketches/sketch_template /my/repo/sketches/
```

## Make The cfsketches.json File

This will fail if the sketch.json files found are invalid, or if `/my/repo/sketches` doesn't exist.  It creates the sketch index file.

```
/var/cfengine/design-center/bin/cf-sketch --make_cfsketches --inputs /my/repo --is=/my/repo/sketches/cfsketches.json
```

## (Optional) Regenerate The README.md Files

This will regenerate the `README.md` files for each sketch, which will please your users.

```
/var/cfengine/design-center/bin/cf-sketch --make_readme --is=/my/repo/sketches/cfsketches.json
```

## Install Your Sketches!

```
/var/cfengine/design-center/bin/cf-sketch --install-all --is=/my/repo/sketches/cfsketches.json --inputs=/var/cfengine/design-center
```

See also: [Package The Sketch][Write a new Sketch#Package The Sketch]
