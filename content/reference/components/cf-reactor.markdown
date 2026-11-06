---
layout: default
title: cf-reactor
keywords: [reactor, events]
aliases:
  - "/reference-components-cf-reactor.html"
---

`cf-reactor` is the event reaction daemon for CFEngine.
Instead of running policy on a fixed schedule like `cf-agent`, it watches for specific events on the host and runs policy as soon as one happens.

`cf-reactor` keeps the promises made in `reactor` bundles and is affected by the `common` control body.
On event, it runs the bundles of the [`then`][events#then] attribute of the [`events`][events] promise: `reactor` bundles without `events` promises, which behave like `agent` bundles, or `agent` and `common` bundles.
See [Reactor bundles][cf-reactor#Reactor bundles].

**Notes:**

- `cf-reactor` always considers the class `reactor` to be defined.
- This daemon reloads its policy when the SIGHUP signal is received.
- `SIGUSR1` sets the log level to debug.
- `SIGUSR2` sets the log level to notice.
- On CFEngine Enterprise hubs, `cf-reactor` has extra responsibilities, see [Enterprise hub tasks][cf-reactor#Enterprise hub tasks].

**History:**

- In 3.18.2 / 3.20.0 `cf-reactor` was introduced as an Enterprise-only hub component.
- In 3.29.0 `cf-reactor` was moved to CFEngine community, and `reactor` bundles and [`events`][events] promises were introduced for event driven CFEngine policy.

## Command reference

{{< CFEngine_include_snippet(cf-reactor.help, [\s]*--[a-z], ^$) >}}

See also: [Reactor normal ordering][Policy evaluation#Reactor normal ordering]

## Reactor bundles

There are two kinds of `reactor` bundles, depending on whether they have [`events`][events] promises:

- `reactor` bundles **with** `events` promises set up the events to react to.
  Besides `events` promises, they can only have [`meta`][meta], [`vars`][vars] and [`classes`][classes] promises.
  `cf-reactor` evaluates them every time it reads the policy, see [Reactor normal ordering][Policy evaluation#Reactor normal ordering].
- `reactor` bundles **without** `events` promises are run on event, from the [`then`][events#then] attribute of `events` promises.
  They can have all the promise types of `agent` bundles, including [custom promise types][custom], and `cf-reactor` runs them like `cf-agent` runs `agent` bundles.
  They are not evaluated when `cf-reactor` reads the policy.

Having other promise types than `meta`, `vars` and `classes` alongside `events` promises is an error, and so is referring to a `reactor` bundle with `events` promises in a `then` attribute.

With `reactor` bundles without `events` promises, a policy for `cf-reactor` does not need `agent` bundles:

```cf3
body when deleted(file)
{
  file_deleted => "$(file)";
}

bundle reactor watch
{
  vars:
    "file" string => "/tmp/a";

  events:
    "Keep $(file)"
      when => deleted("$(file)"),
      then => { create_file("$(file)"), report_restored("$(file)") };
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
```

**Note:** [`methods`][methods] promises can call `agent` and `common` bundles, but not `reactor` bundles.

## Under the hood

`cf-reactor` reads the policy and sets up event watchers based on the event promises declared in `reactor` bundles.
It then starts a thread that polls for each registered event.
When an event is detected, it is added to an event queue along with the corresponding event promise.
The daemon is then signaled to handle the event and run the bundles of the `then` attribute of the event promise, following the same execution model as `cf-agent`.

**Notes:**

- Event detection is based on polling, sped up by [wakeup sources](#wakeup-sources), but `cf-reactor` does not use busy-waiting.
  Instead, the polling thread sleeps between polling cycles and remains dormant when no events are registered.
- `cf-reactor` does not guarantee that an event will be handled immediately after it occurs.
  The delay depends on factors such as the polling interval, policy reloads, and slow code execution.
  However, `cf-reactor` guarantees that changes will be detected as fast as possible and the corresponding code executed, provided that execution does not fail.
- After a wakeup source wakes it up, `cf-reactor` waits 200 milliseconds before checking, so that a burst of changes is checked once.
- An event that fires more than 10 times in 60 seconds is delayed, starting at 10 seconds and doubling up to 5 minutes, until it calms down.
  The changes it holds back are handled in one run when the delay ends.
  Meanwhile, and while its bundles run, the event is not checked again: it is checked once when it can run.

### Wakeup sources

A wakeup source wakes an event's watcher up as soon as the operating system reports a change to the watched file or its directory, so that `cf-reactor` checks the event right away instead of at its next [`interval`][events#interval].
Each event uses the first available wakeup source of its [`wakeup_sources`][events#wakeup_sources] attribute.
Wakeup sources only decide _when_ an event is checked, never _whether_ it happened, and polling continues underneath all of them.
Changing the wakeup source never changes which events fire, only how soon.

- `ebpf` (Linux, Enterprise) loads a small program into the kernel that matches changes against the watched files' inodes before telling `cf-reactor`.
  It needs kernel 5.8 or later (or the RHEL 8 kernel) with BTF, and `CAP_SYS_ADMIN` (or `CAP_BPF` and `CAP_PERFMON`).
  It has no per-directory watch limits, and watches up to 65,536 files; further events use their next wakeup source, and `cf-reactor` logs a warning.
- `fanotify` and `inotify` (Linux, Enterprise) watch each file for writes and changes of its permissions or owner, and its parent directory for files being created, deleted and renamed.
  Files created and deleted in that directory are reported to `cf-reactor`, which ignores the ones for other files.
  `inotify` is limited by `fs.inotify.max_user_watches` and `fs.inotify.max_user_instances`, and `fanotify` by `fs.fanotify.max_user_marks`.
  When out of watches or marks, they watch files through their directories only, and `cf-reactor` logs a warning; a write through a file descriptor opened before the file was renamed into place is then only seen at the next interval.
  Raise the limit to watch more than about half as many files as it allows.
- `usn` (Windows, Enterprise) reads the change journal of NTFS and ReFS volumes, waiting for new records as they are written.
  It sees changes made while `cf-reactor` was stopped, and doesn't lose changes during bursts, so it comes before `rdcw`.
  It needs administrator rights and a change journal on the volume; `cf-reactor` never creates one.
  If the journal is deleted, recreated or overwritten past the last record read, every event on that volume is checked.
- `rdcw` (Windows, Enterprise) uses `ReadDirectoryChangesW` on the watched files' directories, and works on every local file system, including FAT32 and exFAT.
  When its buffer overflows during a burst, the events of that directory are checked.
  It isn't told when a watched directory, or one above it, is renamed or moved; `cf-reactor` notices within 5 seconds and watches the new location.
  Changes made while `cf-reactor` was stopped are found by the first check after it starts.
- `poll` only checks at the interval. It is the only wakeup source in CFEngine Community.

**Cost:** away from watched files, no wakeup source adds measurable CPU time to the rest of the system.
In a directory that holds a watched file, each file operation costs about 1 µs more with `ebpf`, `fanotify` or `inotify` (about 10%), counting the process making the change and `cf-reactor`.
At 1,000 file operations per second in one watched directory this is about 0.1% of a CPU core, so the choice of wakeup source makes no practical difference to CPU time.
Where the wakeup sources differ:

| Source     | Wakes the watcher after a change | Kernel resources                                                         |
| ---------- | -------------------------------- | ------------------------------------------------------------------------ |
| `ebpf`     | under 2 ms                       | up to 65,536 files, about 0.7 MB of locked memory for 1,000              |
| `fanotify` | about 20 ms                      | one mark per file and one per directory (`fs.fanotify.max_user_marks`)   |
| `inotify`  | about 20 ms                      | one watch per file and one per directory (`fs.inotify.max_user_watches`) |
| `usn`      | under 2 ms                       | one reader per volume, none per file                                     |
| `rdcw`     | under 3 ms                       | one directory handle per watched directory                               |
| `poll`     | at the next interval             | none                                                                     |

`cf-reactor` then waits 200 milliseconds before checking, so in practice the native wakeup sources react equally fast.
`fanotify` and `inotify` gather the changes of 20 milliseconds into one wakeup.
Measured on Ubuntu 24.04 (kernel 6.8) and Windows Server 2019, in virtual machines.

`file_content_modified` hashes the whole file when its size or modification time changed.
For a large file that is written to all the time, such as a log, this costs about as much with every wakeup source, since the event is limited to 10 runs a minute (see above) and checked once per run: hashing a 200 MB file appended to 20 times a second took about 20% of a CPU core.
Use `file_modified` for such files, which only compares the modification time.

**Changes only seen at the next interval:**

- writes through a memory mapping (`mmap`) that stays open, with every wakeup source
- with `ebpf`, writes on file systems that don't report them to the kernel's generic write path (for example some network file systems) until the file is closed
- with every wakeup source, changes on network file systems made by other hosts

**Notes:**

- On CFEngine Enterprise, the wakeup source each event uses is reported to the hub, in the `reactor_watchers` table of the reporting database.
- SELinux or other mandatory access control may deny `cf-reactor` a wakeup source; it then falls back to the next one in the list.

## Enterprise hub tasks

On CFEngine Enterprise hubs, `cf-reactor` also listens to `NOTIFY` events in the PostgreSQL database and performs actions when those events occur, and runs periodic hub tasks:

- Refreshing the `host_specific.json` files whenever there is an event in the `cmdb_refresh` channel.
- Refreshing the inventory of hosts.
- Handling the requests of the Build application (cfbs requests and responses).
- Running alerts, scheduled reports, the cleanup of hosts, and the update of health failures.
