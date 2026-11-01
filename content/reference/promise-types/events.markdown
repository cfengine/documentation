---
layout: default
title: events
keywords: [reactor, events]
---

`events` promises describe events for [`cf-reactor`][cf-reactor] to react to: the event to watch for, with the [`when`](#when) body, and the bundles to run when it happens, with the [`then`](#then) attribute.
`events` promises can only be made in `reactor` bundles, alongside [`meta`][meta], [`vars`][vars] and [`classes`][classes] promises only.
See [Reactor bundles][cf-reactor#Reactor bundles].

```cf3
bundle reactor create_file(file)
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
bundle reactor report_deletion(file)
{
  reports:
    "$(file) was deleted, restoring it";
}

bundle reactor create_file(file)
{
  files:
    "$(file)" create => "true";
}

bundle reactor report_restored(file)
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

The bundles can be `reactor` bundles without `events` promises, `agent` bundles or `common` bundles.
A bundle name is looked up among the `agent` bundles first, then the `common` bundles, then the `reactor` bundles.
All promise types within `reactor` bundles without `events` promises and `agent` bundles behave like in `cf-agent` when executed in response to events.

**Notes:**

- variables and classes created in a bundle run on reaction to an event are destroyed right after the execution.
  The only exception are persistent classes.
- a `reactor` bundle with `events` promises cannot be run on event, it is an error to refer to one in `then`.

**Type:** `bundle reactor` without `events` promises, `bundle agent` or `bundle common`, or a list of them

### when

**Description:** The event to watch for.

**Type:** `body when`

**See also:** [Common body attributes][Promise types#Common body attributes]

All event types are mutually exclusive in a `when` body.

Event types:

- File events: [`file_deleted`](#file_deleted), [`file_created`](#file_created), [`file_modified`](#file_modified), [`file_content_modified`](#file_content_modified), [`file_permissions_changed`](#file_permissions_changed), [`file_owner_changed`](#file_owner_changed), [`file_size_exceeds`](#file_size_exceeds)

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
A [wakeup source](#wakeup_sources) can wake the check up earlier, so with one the interval mostly bounds how late a missed change is noticed.
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

#### wakeup_sources

**Description:** The wakeup sources that may wake this event's watcher up before its next interval, in order of preference.

A wakeup source is a way for the operating system to tell `cf-reactor` that the watched file, or its directory, changed; `poll` means none, only the interval.
It makes `cf-reactor` check the event right away instead of at the next interval.
It never decides whether the event happened: the check does, so the same events fire whatever the wakeup source.
Polling at the [`interval`](#interval) continues underneath every wakeup source, and catches what a wakeup source misses.

`cf-reactor` uses the first wakeup source in the list that is available on the host and can watch the event's target.
Without `wakeup_sources`, it tries `ebpf`, `fanotify`, `inotify`, `usn`, `rdcw` and `poll`, in that order.
CFEngine Community only has `poll`.
If none of the listed wakeup sources is available, the event is not watched and `cf-reactor` logs an error; list `poll` last to fall back to polling instead.

| Source     | Platform | Edition    |
| ---------- | -------- | ---------- |
| `ebpf`     | Linux    | Enterprise |
| `fanotify` | Linux    | Enterprise |
| `inotify`  | Linux    | Enterprise |
| `usn`      | Windows  | Enterprise |
| `rdcw`     | Windows  | Enterprise |
| `poll`     | All      | All        |

For how the wakeup sources differ, see [Wakeup sources][cf-reactor#Wakeup sources].

```cf3
body when passwd_modified
{
  file_content_modified => "/etc/passwd";
  interval => 300;
  wakeup_sources => { "inotify", "poll" };
}
```

**Type:** `slist`

**Allowed input range:** `poll`, `inotify`, `fanotify`, `ebpf`, `usn`, `rdcw`

**Notes:**

- changing `wakeup_sources` does not reset the event: on policy reload, a watcher keeps its state when only its wakeup sources change.
- with `wakeup_sources => { "poll" }` the event is only checked every `interval` seconds.

#### file_deleted

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

#### file_created

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

#### file_modified

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

**See also:** [`file_content_modified`](#file_content_modified)

#### file_content_modified

**Description:** Creates an event when the content of the regular file at the given path changes.

The event fires when the path is a regular file at two consecutive checks and the SHA-256 hash of its content differs.
Unlike [`file_modified`](#file_modified), touching the file or replacing it with a file of the same content is not a modification.
The file is read on every check, so it is more expensive than `file_modified` for large files.
Directories and symlinks have no content to hash, so they never fire this event.

```cf3
body when content_modified(file)
{
  file_content_modified => "$(file)";
}
```

**Type:** `string`

**Allowed input range:** (arbitrary string)

#### file_permissions_changed

**Description:** Creates an event when the permissions of the file at the given path change.

The event fires when the file exists at two consecutive checks with different permission bits, including the setuid, setgid and sticky bits.
Symlinks are not followed: changing the permissions of the target of a symlink does not fire the event for the symlink.

```cf3
body when permissions_changed(file)
{
  file_permissions_changed => "$(file)";
}
```

**Type:** `string`

**Allowed input range:** (arbitrary string)

#### file_owner_changed

**Description:** Creates an event when the owning user or group of the file at the given path changes.

The event fires when the file exists at two consecutive checks with a different owning user or group.
Symlinks are not followed: changing the owner of the target of a symlink does not fire the event for the symlink.

```cf3
body when owner_changed(file)
{
  file_owner_changed => "$(file)";
}
```

**Type:** `string`

**Allowed input range:** (arbitrary string)

#### file_size_exceeds

**Description:** Creates an event when the size of the file at the given path grows above [`size_threshold`](#size_threshold) bytes.

The event fires when the file is above the threshold at one check, and was below it or didn't exist at the previous one.
It fires once per crossing of the threshold: the file has to be below it at a check, for example after being truncated, before it can fire again.
A file created with a size above the threshold fires the event.

```cf3
body when size_exceeds(file)
{
  file_size_exceeds => "$(file)";
  size_threshold => "1048576";
}
```

**Type:** `string`

**Allowed input range:** (arbitrary string)

#### size_threshold

**Description:** The size, in bytes, above which [`file_size_exceeds`](#file_size_exceeds) fires.

Required with `file_size_exceeds`, and can't be used with other event types.

**Type:** `int`

**Allowed input range:** `0,99999999999`

#### User event type

##### User added

**Description:** Creates an event when the user with the given name is added.

The event fires when the user was missing at one check and exists at the next one.
It fires once per addition: the user has to be removed again before another addition is detected.
On Windows, only user accounts count, not groups or built-in accounts such as `SYSTEM`.

```cf3
body when added(user)
{
  user_added => "$(user)";
}
```

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Notes:**

- On Unix, users from network sources such as LDAP or sssd are not detected.

##### User removed

**Description:** Creates an event when the user with the given name is removed.

The event fires when the user existed at one check and is missing at the next one.
It fires once per removal: the user has to be added again before another removal is detected.
A failing lookup of the user is logged as an error, and is not taken as a removal.
On Windows, only user accounts count (`SidTypeUser`), not groups or built-in accounts such as `SYSTEM`.

```cf3
body when removed(user)
{
  user_removed => "$(user)";
}
```

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Notes:**

- On Unix, users from network sources such as LDAP or sssd may not be detected.
