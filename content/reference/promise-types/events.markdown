---
layout: default
title: events
keywords: [reactor, events]
---

`events` promises describe events for [`cf-reactor`][cf-reactor] to react to:
the event to watch for, with the [`when`](#when) body, and the bundles to run
when it happens, with the [`then`](#then) attribute. `events` promises can only
be made in `reactor` bundles, see [Reactor bundles][cf-reactor#Reactor bundles].

```cf3
bundle reactor motd_watch
{
  events:
    "motd_deleted"
      when => deleted("/etc/motd"),
      then => motd;
}

body when deleted(path)
{
  file_deleted => "$(path)";
}

bundle agent motd
{
  files:
    "/etc/motd" content => "This host is managed by CFEngine$(const.n)";
}
```

The promiser is the name of the event, which `cf-reactor` uses in its logs:

```output
    info: Registering a file_deleted watcher for events promise 'motd_deleted', on file '/etc/motd'
  notice: Reactor watcher 'motd_deleted' fired
```

Like other promises, `events` promises iterate over the lists used in their
promiser and attributes, and `cf-reactor` watches for the event of each
iteration separately:

```cf3
bundle reactor watch_config_files
{
  vars:
    "files" slist => { "/etc/hosts", "/etc/resolv.conf" };

  events:
    "$(files) deleted"
      when => deleted("$(files)"),
      then => log_deletion("$(files)");
}

body when deleted(path)
{
  file_deleted => "$(path)";
}

bundle agent log_deletion(path)
{
  reports:
    "$(path) was deleted";
}
```

`cf-reactor` watches for the event of identical `events` promises only once, so
their bundles are run once per event. `events` promises that differ, for example
by their promiser or their `then` bundles, are watched for separately, even when
they watch for the same event.

See [Running bundles on events][cf-reactor#Running bundles on events] for how
the bundles run on events differ from a `cf-agent` run.

**History:** Introduced in 3.29.0.

## Promise outcome

The outcome of an `events` promise is decided when `cf-reactor` evaluates its
policy:

- **kept** when `cf-reactor` watches for its event.
- **not kept** (`repair_failed`) when the promise is invalid, and its event is
  not watched for. For example, when the `when` body or the `then` attribute is
  missing or empty, or when one of the `then` bundles can't be found, or is
  neither an `agent` nor a `common` bundle. `cf-reactor` logs why the promise
  is invalid.

Use a [`classes`][Promise types#classes] body to define classes based on the
outcome:

```cf3
bundle reactor watch_hosts_file
{
  events:
    "hosts_deleted"
      when => deleted("/etc/hosts"),
      then => log_deletion("/etc/hosts"),
      classes => watching("hosts");
}

body classes watching(name)
{
  promise_kept => { "watching_$(name)" };
  repair_failed => { "not_watching_$(name)" };
}

body when deleted(path)
{
  file_deleted => "$(path)";
}

bundle agent log_deletion(path)
{
  reports:
    "$(path) was deleted";
}
```

## Attributes

{{< CFEngine_include_markdown(common-attributes.include.markdown) >}}

### then

**Description:** The bundle, or the list of bundles, to run in order when the
event happens.

Bundles are referred to like in a `bundlesequence`: by name, quoted or not, with
their arguments, if any, in parentheses. Arguments can use the variables of the
reactor bundle, and lists are passed with `@(list)`. Only `agent` and `common`
bundles can be run.

If one of the bundles can't be found, the `events` promise is not kept, and none
of its bundles are run.

**Type:** `bundle agent` or `bundle common`, or a list of them

**Example:**

```cf3
bundle reactor watch_motd
{
  vars:
    "admins" slist => { "alice", "bob" };

  events:
    "motd_deleted"
      when => deleted("/etc/motd"),
      then => { log_deletion("/etc/motd"), notify(@(admins)), motd };
}

body when deleted(path)
{
  file_deleted => "$(path)";
}

bundle agent log_deletion(path)
{
  reports:
    "$(path) was deleted";
}

bundle agent notify(users)
{
  reports:
    "Notifying $(users)";
}

bundle agent motd
{
  files:
    "/etc/motd" content => "This host is managed by CFEngine$(const.n)";
}
```

**History:** Introduced in 3.29.0.

### when

**Type:** `body when`

**See also:** [Common body attributes][Promise types#Common body attributes]

#### file_deleted

**Description:** The file whose deletion is the event.

The event happens when the file, which existed when `cf-reactor` last checked,
doesn't exist anymore. It happens on every deletion of the file: if the file is
created again and deleted again, it happens again.

**Type:** `string`

**Allowed input range:** (arbitrary string)

**Example:**

```cf3
body when deleted(path)
{
  file_deleted => "$(path)";
}
```

**Notes:**

- `cf-reactor` checks whether the file exists every second, so a file deleted
  and created again in the meantime may not be seen as deleted.
- If the file doesn't exist when `cf-reactor` starts watching for its deletion,
  the event only happens once the file has been created, and then deleted.
- Moving or renaming the file is a deletion, as nothing exists at its path
  anymore.
- Symbolic links are not followed: deleting a symbolic link is an event,
  deleting the file it points to is not.
- If `cf-reactor` can't tell whether the file exists, for example because of
  missing permissions, it logs an error, at most once a minute.
- `file_deleted` takes a single file. To watch for the deletion of several
  files, iterate over a list, as shown above.

**History:** Introduced in 3.29.0.
