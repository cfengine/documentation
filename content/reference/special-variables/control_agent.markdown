---
layout: default
title: control_agent
aliases:
  - "/reference-special-variables-default:control_agent.html"
---

Variables in the `default:control_agent` context are automatically created from attributes defined in `body agent control` following the pattern `default:default:control_agent.<attribute>`.

### default:control_agent.abortbundleclasses

Defines a list of regular expressions that match classes which if defined lead to termination of current bundle. If no list is defined, then a default of `abortbundle` is used.

**See also:** [`abortbundleclasses` in `body agent control`][cf-agent#abortbundleclasses]

### default:control_agent.abortclasses

Defines a list of regular expressions that result in cf-agent terminating itself upon definition of a matching class.

**See also:** [`abortclasses` in `body agent control`][cf-agent#abortclasses]

### default:control_agent.agentfacility

Controls the syslog facility used by `cf-agent`. Valid values are `LOG_USER`, `LOG_DAEMON`, `LOG_LOCAL0` through `LOG_LOCAL7`.

**See also:** [`agentfacility` in `body agent control`][cf-agent#agentfacility]

### default:control_agent.default_repository

Defines the default repository for file backups. When this variable is set, backup files will be placed in this location instead of the same directory as the edited file.

**See also:** [`default_repository` in `body agent control`][cf-agent#default_repository]

### default:control_agent.files_single_copy

Specifies a list of regular expressions that when matched will prevent the agent from performing subsequent copy operations on the same file.

**See also:** [`files_single_copy` in `body agent control`][cf-agent#files_single_copy]

### default:control_agent.maxconnections

Controls the maximum number of connections that cf-agent will open simultaneously.

**See also:** [`maxconnections` in `body agent control`][cf-agent#maxconnections]

### default:control_agent.timezone

Defines the timezone setting for the agent. Note that this variable provides the value for policy authors to implement their own timezone-related policy; it does not enforce timezone settings automatically.

**See also:** [`timezone` in `body agent control`][cf-agent#timezone]

### default:control_agent.agentaccess

Contains a list of user names that are allowed to execute cf-agent.

**See also:** [`agentaccess` in `body agent control`][cf-agent#agentaccess]

### default:control_agent.allclassesreport

Determines whether to generate the `allclasses.txt` report. If set to true, the `state/allclasses.txt` file will be written to disk during agent execution.

**See also:** [`allclassesreport` in `body agent control`][cf-agent#allclassesreport]

### default:control_agent.alwaysvalidate

A true/false flag that determines whether configurations will always be checked before executing, or only after updates. When set, `cf-agent` will force a revalidation of the input.

**See also:** [`alwaysvalidate` in `body agent control`][cf-agent#alwaysvalidate]

### default:control_agent.bindtointerface

Describes the interface to be used for outgoing connections. On multi-homed hosts, this defines the IP address of the interface for server traffic.

**See also:** [`bindtointerface` in `body agent control`][cf-agent#bindtointerface]

### default:control_agent.checksum_alert_time

Represents the persistence time for the checksum_alert class. When checksum changes trigger an alert, this value determines the longevity of that class.

**See also:** [`checksum_alert_time` in `body agent control`][cf-agent#checksum_alert_time]

### default:control_agent.childlibpath

Contains the LD_LIBRARY_PATH for child processes. This string sets the internal `LD_LIBRARY_PATH` environment of the agent.

**See also:** [`childlibpath` in `body agent control`][cf-agent#childlibpath]

### default:control_agent.copyfrom_restrict_keys

Restricts `cf-agent` to copying files from hosts that have a key explicitly defined in this list.

**See also:** [`copyfrom_restrict_keys` in `body agent control`][cf-agent#copyfrom_restrict_keys]

### default:control_agent.defaultcopytype

Sets the global default policy for comparing source and image in copy transactions. Possible values include: mtime, atime, ctime, digest, hash, binary.

**See also:** [`defaultcopytype` in `body agent control`][cf-agent#defaultcopytype]

### default:control_agent.dryrun

A boolean flag that if set, makes no changes to the system, and will only report what it needs to do.

**See also:** [`dryrun` in `body agent control`][cf-agent#dryrun]

### default:control_agent.editbinaryfilesize

Represents the limit on maximum binary file size to be edited. This is a global setting for the file-editing safety-net for binary files.

**See also:** [`editbinaryfilesize` in `body agent control`][cf-agent#editbinaryfilesize]

### default:control_agent.editfilesize

The limit on maximum text file size to be edited. This is a global setting for the file-editing safety-net.

**See also:** [`editfilesize` in `body agent control`][cf-agent#editfilesize]

### default:control_agent.environment

Contains environment variables to be inherited by children. This sets the runtime environment of the agent process.

**See also:** [`environment` in `body agent control`][cf-agent#environment]

### default:control_agent.files_auto_define

Contains a list of regular expressions matching filenames. When a file matching one of these regular expressions is copied, classes prefixed with `auto_` are defined.

**See also:** [`files_auto_define` in `body agent control`][cf-agent#files_auto_define]

### default:control_agent.hashupdates

Determines whether stored hashes are updated when change is detected in source. If 'true' the stored reference value is updated as soon as a warning message has been given.

**See also:** [`hashupdates` in `body agent control`][cf-agent#hashupdates]

### default:control_agent.inform

Sets the default output level 'permanently' within the class context indicated. It is equivalent to the command line option '-I'.

**See also:** [`inform` in `body agent control`][cf-agent#inform]

### default:control_agent.max_children

Represents the maximum number of background tasks that should be allowed concurrently. For the agent it represents the number of background jobs allowed concurrently.

**See also:** [`max_children` in `body agent control`][cf-agent#max_children]

### default:control_agent.mountfilesystems

Determines whether to mount any filesystems promised. It issues the generic command to mount file systems defined in the file system table.

**See also:** [`mountfilesystems` in `body agent control`][cf-agent#mountfilesystems]

### default:control_agent.nonalphanumfiles

Determines whether to warn about filenames with no alphanumeric content. This test is applied in all recursive/depth searches.

**See also:** [`nonalphanumfiles` in `body agent control`][cf-agent#nonalphanumfiles]

### default:control_agent.default_directory_create_mode

Determines the default directory permissions when `cf-agent` creates parent directories during `files` promise repairs.

**See also:** [`default_directory_create_mode` in `body agent control`][cf-agent#default_directory_create_mode], [`default:update_def.control_agent_default_directory_create_mode` in the standard library](/reference/masterfiles-policy-framework#configure-default-directory-creation-permissions-for-update-policy)

### default:control_agent.refresh_processes

Contains bundles to reload the process table before verifying the bundles named in this list (lazy evaluation).

**See also:** [`refresh_processes` in `body agent control`][cf-agent#refresh_processes]

### default:control_agent.repchar

Represents a character used to canonize pathnames in the file repository. Default value is `_`.

**See also:** [`repchar` in `body agent control`][cf-agent#repchar]

### default:control_agent.report_class_log

Enables logging of classes set by cf-agent. Each class set by cf-agent will be logged at the end of agent execution.

**See also:** [`report_class_log` in `body agent control`][cf-agent#report_class_log]

### default:control_agent.secureinput

Checks whether input files are writable by unauthorized users. If this is set, the agent will not accept an input file that is not owned by a privileged user.

**See also:** [`secureinput` in `body agent control`][cf-agent#secureinput]

### default:control_agent.sensiblecount

Represents the minimum number of files a mounted filesystem is expected to have. Default value is 2 files.

**See also:** [`sensiblecount` in `body agent control`][cf-agent#sensiblecount]

### default:control_agent.sensiblesize

Represents the minimum number of bytes a mounted filesystem is expected to have. Default value is 1000 bytes.

**See also:** [`sensiblesize` in `body agent control`][cf-agent#sensiblesize]

### default:control_agent.skipidentify

Determines whether to send an IP/name during server connection because address resolution is broken. Causes the agent to ignore its missing DNS credentials.

**See also:** [`skipidentify` in `body agent control`][cf-agent#skipidentify]

### default:control_agent.suspiciousnames

Contains names to skip and warn about if found during any file search. If CFEngine sees these names during recursive (depth) file searches, it will skip them and output a warning message.

**See also:** [`suspiciousnames` in `body agent control`][cf-agent#suspiciousnames]

### default:control_agent.verbose

Determines whether to switch on verbose standard output. It is equivalent to (and when present, overrides) the command line option '-v'.

**See also:** [`verbose` in `body agent control`][cf-agent#verbose]
