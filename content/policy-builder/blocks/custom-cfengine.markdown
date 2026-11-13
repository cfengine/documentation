---
layout: default
title: Custom CFEngine and Call Method
sorting: 130
description: When no block does what you need, policy you write yourself or a bundle that already exists
---

This page is for when you already know some of the CFEngine policy language. Blocks cover the most common promises, but not everything CFEngine can do.
When no block does what you need, a **Custom CFEngine** block holds policy you write yourself, and a **Call Method** block runs a bundle that already exists elsewhere.
Both still sit on the canvas like any block: they have a label, a note, a condition, arrows and How often.

Keep them for the part no block covers: what stays in other blocks remains easy to read and edit for everyone working on the project.

## Custom CFEngine

A Custom CFEngine block has two fields:

- **Promises**: promise sections as you'd write them in a `bundle agent`, such as `files:` followed by its promises.
- **Bodies and bundles it uses**: any body or bundle the promises call that isn't in the _standard library_. The standard library is the collection of common bodies and bundles that comes with masterfiles (`lib/`), such as `mog()` for permissions or `recurse()` for directory depth; those need no definition here.

For example, to copy a directory and remove files the source doesn't have, which no block offers:

```cf3 {skip}
files:
  "/var/www/site"
    copy_from => mirror("/srv/site"),
    depth_search => default:recurse("inf");
```

with this in **Bodies and bundles it uses**:

```cf3
body copy_from mirror(from)
{
  source => "$(from)";
  purge => "true";
}
```

The promises become a bundle of their own, which the configuration's `main` bundle calls in its place on the canvas:

```cf3 {skip}
methods:
  "Mirror the site" usebundle => mirror_the_site;
```

A few rules follow from the block living in its configuration's namespace:

- The standard library's bodies and bundles need `default:` in front, such as `default:recurse("inf")` or `default:mog("644", "root", "root")`.
- Bodies and bundles from **Bodies and bundles it uses** are written without a namespace.
- `$(vars.name)` reads a variable of the same configuration; another configuration's needs its namespace, such as `$(common:vars.name)`.

Policy Builder checks the text as you type, with the CFEngine linter: problems are shown under the field, with their line.
If the text doesn't parse, the block is left out of the generated policy until it's fixed, and Properties says why.

**Tip:** say in the block's note what it does and why it's written by hand, so the next person reading the canvas knows.

## Call Method

**Call Method** runs a bundle that already exists: one from CFEngine's standard library, from a CFEngine Build module, or one written by hand outside the project.

- **Bundle name**: the bundle to call, such as `my_bundle`, looked up in the `default` namespace, or `ns:my_bundle` for another namespace.
- **Arguments**: one per line, in the bundle's parameter order. `$(…)` passes a variable's value, and `@(…)` a list.

Blocks on the canvas don't need Call Method to call each other: arrows already order them.

See [Bundles][] and [Bodies][] for how CFEngine defines and calls them.
