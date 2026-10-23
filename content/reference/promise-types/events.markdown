---
layout: default
title: events
keywords: [reactor, events]
---

`events` promises describe events for [`cf-reactor`][cf-reactor] to react to: the event to watch for, with the [`when`](#when) body, and the bundles to run when it happens, with the [`then`](#then) attribute.
`events` promises can only be made in `reactor` bundles.

```cf3
bundle agent create_file(file)
{
  files:
    "$(file)" create => "true";
}

body when deleted(file)
{
  file_deleted => "$(file)";
}

bundle reactor main
{
  events:
    "Keep /tmp/a"
      when => deleted("/tmp/a"),
      then => create_file("/tmp/a");
}
```

**History:** Introduced in 3.29.0.

## Attributes

{{< CFEngine_include_markdown(common-attributes.include.markdown) >}}

### then

**Description:** The bundle, or the list of bundles, to run in order when the event happens.

```cf3
bundle agent report_deletion(file)
{
  reports:
    "$(file) was deleted, restoring it";
}

bundle agent create_file(file)
{
  files:
    "$(file)" create => "true";
}

bundle agent report_restored(file)
{
  reports:
    "$(file) was restored";
}

bundle reactor main
{
  events:
    "Keep /tmp/a"
      when => deleted("/tmp/a"),
      then => {
        report_deletion("/tmp/a"),
        create_file("/tmp/a"),
        report_restored("/tmp/a"),
      };
}
```

All promise types within `agent` bundles behave like in `cf-agent` when executed in response to events.

**Notes:**

- variables and classes created in a bundle run on reaction to an event are destroyed right after the execution.
  The only exception are persistent classes.

**Type:** `bundle agent` or `bundle common`, or a list of them

### when

**Description:** The event to watch for.

**Type:** `body when`

**See also:** [Common body attributes][Promise types#Common body attributes]

All event types are mutually exclusive in a `when` body.

```cf3
body when deleted(file)
{
  file_deleted => "$(file)";
  interval => 1;
}

bundle reactor main
{
  events:
    "Report deletion of /tmp/a"
      when => deleted("/tmp/a"),
      then => report_deletion("/tmp/a");
}
```

#### interval

**Description:** How often, in seconds, `cf-reactor` checks whether this event has happened.

Each event has its own interval.
A lower value means the event is noticed sooner but checked more often.
For how polling works, see [Under the hood][cf-reactor#Under the hood].

```cf3
body when deleted_slow(file)
{
  file_deleted => "$(file)";
  interval => 60;
}
```

**Type:** `int`

**Allowed input range:** `1,99999999999`

**Default value:** `1`

#### File event type

##### File deleted

**Description:** Creates an event when the file at the given path is deleted.

The event fires when the path existed at one check and is gone at the next one.
It fires once per deletion: the file has to be created again before another deletion is detected.

```cf3
body when deleted(file)
{
  file_deleted => "$(file)";
}
```

**Type:** `string`

**Allowed input range:** (arbitrary string)

##### File created

**Description:** Creates an event when a file is created at the given path.

The event fires when the path was missing at one check and exists at the next one.
It fires once per creation: the file has to be deleted again before another creation is detected.
Any type of file counts, for example a directory or a symlink, even one whose target does not exist.

```cf3
body when created(file)
{
  file_created => "$(file)";
}
```

**Type:** `string`

**Allowed input range:** (arbitrary string)

##### File modified

**Description:** Creates an event when the modification time of the file at the given path changes.

The event fires when the file exists at two consecutive checks with different modification times.
Writing to the file changes its modification time, but so does touching it without changing its content.
For a directory, creating, renaming or deleting a file in it changes its modification time.
Changing the permissions or the owner of the file doesn't change its modification time.
Symlinks are not followed: the modification time is the one of the symlink itself, not of its target.

```cf3
body when modified(file)
{
  file_modified => "$(file)";
}
```

**Type:** `string`

**Allowed input range:** (arbitrary string)

**See also:** [`file_content_modified`](#file-content-modified)
