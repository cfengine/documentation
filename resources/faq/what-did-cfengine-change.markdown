---
layout: default
title: What did cfengine do?
published: true
tags: [getting started, faq, logging, reporting ]
---

This page presents a few ways of understanding what CFEngine has done to your machine.

## CFEngine Core/Community

### The verbose agent log

Running the agent in verbose mode ( `cf-agent --verbose` | `cf-agent -v` )
provides all of the details about each promise and its result

Example Policy (`/tmp/example.cf`):

```cf3
bundle agent main
{

  files:

      "/tmp/example"
        handle => "example_file_exists_and_contains_date",
        create => "true",
        edit_line => lines_present( $(sys.date) );
}

bundle edit_line lines_present(lines)
# @brief Ensure `lines` are present in the file. Lines that do not exist are appended to the file
# @param List or string that should be present in the file
#
# **Example:**
#
# ```cf3
# bundle agent example
# {
#  vars:
#    "nameservers" slist => { "8.8.8.8", "8.8.4.4" };
#
#  files:
#      "/etc/resolv.conf" edit_line => lines_present( @(nameservers) );
#      "/etc/ssh/sshd_config" edit_line => lines_present( "PermitRootLogin no" );
# }
# ```
{
  insert_lines:

      "$(lines)"
        comment => "Append lines if they don't exist";
}
```

In the verbose output as each promise is actuated a `BEGIN promsie` is emitted
with the promise handle or filename and line number position if it does not have
a handle. In the example output we can see that the promise for `/tmp/example`
was `REPAIRED`.

```
verbose: B: *****************************************************************
verbose: B: BEGIN bundle main
verbose: B: *****************************************************************
verbose: P: .........................................................
verbose: P: BEGIN promise 'example_file_exists_and_contains_date' of type "files" (pass 1)
verbose: P:    Promiser/affected object: '/tmp/example'
verbose: P:    Part of bundle: main
verbose: P:    Base context class: any
verbose: P:    Stack path: /default/main/files/'/tmp/example'[1]
verbose: Using literal pathtype for '/tmp/example'
verbose: No mode was set, choose plain file default 0600
   info: Created file '/tmp/example', mode 0600
verbose: Handling file edits in edit_line bundle 'lines_present'
verbose: V:     +  Private parameter: 'lines' in scope 'lines_present' (type: s) in pass 1
verbose: P: .........................................................
verbose: P: BEGIN promise 'promise_example_cf_32' of type "insert_lines" (pass 1)
verbose: P:    Promiser/affected object: 'Mon Dec  4 21:08:38 2017'
verbose: P:    Part of bundle: lines_present
verbose: P:    Base context class: any
verbose: P:    Stack path: /default/main/files/'/tmp/example'/default/lines_present/insert_lines/'Mon Dec  4 21:08:38 2017'[1]
verbose: P:
verbose: P:    Comment:  Append lines if they don't exist
verbose: Additional promise info: source path './example.cf' at line 32 comment 'Append lines if they don't exist'
verbose: Inserting the promised line 'Mon Dec  4 21:08:38 2017' into '/tmp/example' after locator
verbose: P: .........................................................
verbose: P: BEGIN promise 'promise_example_cf_32' of type "insert_lines" (pass 1)
verbose: P:    Promiser/affected object: 'Mon Dec  4 21:08:38 2017'
verbose: P:    Part of bundle: lines_present
verbose: P:    Base context class: any
verbose: P:    Stack path: /default/main/files/'/tmp/example'/default/lines_present/insert_lines/'Mon Dec  4 21:08:38 2017'[1]
verbose: P:
verbose: P:    Comment:  Append lines if they don't exist
verbose: P: .........................................................
verbose: P: BEGIN promise 'promise_example_cf_32' of type "insert_lines" (pass 1)
verbose: P:    Promiser/affected object: 'Mon Dec  4 21:08:38 2017'
verbose: P:    Part of bundle: lines_present
verbose: P:    Base context class: any
verbose: P:    Stack path: /default/main/files/'/tmp/example'/default/lines_present/insert_lines/'Mon Dec  4 21:08:38 2017'[1]
verbose: P:
verbose: P:    Comment:  Append lines if they don't exist
   info: Edit file '/tmp/example'
verbose: Handling file existence constraints on '/tmp/example'
verbose: A: Promise REPAIRED
verbose: P: END files promise (/tmp/example)
verbose: P: .........................................................
verbose: P: BEGIN promise 'example_file_exists_and_contains_date' of type "files" (pass 2)
verbose: P:    Promiser/affected object: '/tmp/example'
verbose: P:    Part of bundle: main
verbose: P:    Base context class: any
verbose: P:    Stack path: /default/main/files/'/tmp/example'[1]
verbose: Using literal pathtype for '/tmp/example'
verbose: P: .........................................................
verbose: P: BEGIN promise 'example_file_exists_and_contains_date' of type "files" (pass 3)
verbose: P:    Promiser/affected object: '/tmp/example'
verbose: P:    Part of bundle: main
verbose: P:    Base context class: any
verbose: P:    Stack path: /default/main/files/'/tmp/example'[1]
verbose: Using literal pathtype for '/tmp/example'
verbose: A: ...................................................
verbose: A: Bundle Accounting Summary for 'main' in namespace default
verbose: A: Promises kept in 'main' = 0
verbose: A: Promises not kept in 'main' = 0
verbose: A: Promises repaired in 'main' = 2
verbose: A: Aggregate compliance (promises kept/repaired) for bundle 'main' = 100.0%
verbose: A: ...................................................
verbose: B: *****************************************************************
verbose: B: END bundle main
verbose: B: *****************************************************************
verbose: Generate diff state reports for policy './example.cf' SKIPPED
verbose: No lock purging scheduled
verbose: Outcome of version (not specified) (agent-0): Promises observed - Total promise compliance: 0% kept, 100% repaired, 0% not kept (out of 2 events). User promise compliance: 0% kept, 100% repaired, 0% not kept (out of 2 events). CFEngine system compliance: 0% kept, 0% repaired, 0% not kept (out of 0 events).
```


### Promise logging

Promises can be configured to [log their outcomes][Promise Types#log_repaired]
to a file with `log_kept`, `log_repaired`, and `log_failed` attributes in an action body.

```cf3
body file control
{
  # reports.cf from stdlib needed for body printfile cat
  inputs => { "$(sys.libdir)/reports.cf" };
}

bundle agent main
{
  commands:
      "/bin/true"
        action => log_my_repairs( '/tmp/repaired.log' );

  reports:
      "/tmp/repaired.log"
        printfile => cat( $(this.promiser) );
}

body action log_my_repairs( file )
{
      log_repaired => "$(file)";
      log_string => "$(sys.date) REPAIRED $(this.promiser)";
}
```

Policy output:

```
R: /tmp/repaired.log
R: Mon Dec  4 21:21:38 2017 REPAIRED /bin/true
```

## CFEngine Enterprise

In addition to all of the core functionality CFEngine enterprise provides details logging without special configuration.

### Changes UI

The changes reporting interface is the easiest way to what repairs the agent is
making to your infrastructure.

![Enterprise Changes UI](enterprise-changes-ui.png)

### Changes API

Changes can also be queried from the [changes rest api][Changes REST API]. Here
we query for repairs made by `files` type promises.

Example query:

```console
[root@hub ~]# curl https://hub/api/v2/changes/policy?promisetype=files
```

Example response:

```json
  {
      "data": [
          {
              "bundlename": "cfe_internal_update_policy",
              "changetime": 1512427971,
              "hostkey": "SHA=01fe75e93ca88bbd381eb720e9b43d0840ea8727aae8fc84391c297c42798f5c",
              "hostname": "hub",
              "logmessages": [
                  "Copying from 'localhost:/var/cfengine/masterfiles/cf_promises_release_id'"
              ],
              "policyfile": "/var/cfengine/inputs/cfe_internal/update/update_policy.cf",
              "promisees": [],
              "promisehandle": "cfe_internal_update_policy_files_inputs_dir",
              "promiser": "/var/cfengine/inputs",
              "promisetype": "files",
              "stackpath": "/default/cfe_internal_update_policy/files/'/var/cfengine/inputs'[1]"
          },
          {
              "bundlename": "cfe_internal_setup_knowledge",
              "changetime": 1512428912,
              "hostkey": "SHA=01fe75e93ca88bbd381eb720e9b43d0840ea8727aae8fc84391c297c42798f5c",
              "hostname": "hub",
              "logmessages": [
                  "Owner of '/var/cfengine/httpd/htdocs/application/logs/./log-2017-12-04.log' was 0, setting to 497",
                  "Group of '/var/cfengine/httpd/htdocs/application/logs/./log-2017-12-04.log' was 0, setting to 497",
                  "Object '/var/cfengine/httpd/htdocs/application/logs/./log-2017-12-04.log' had permission 0644, changed it to 0640"
              ],
              "policyfile": "/var/cfengine/inputs/cfe_internal/enterprise/CFE_knowledge.cf",
              "promisees": [],
              "promisehandle": "cfe_internal_setup_knowledge_files_doc_root_application_logs",
              "promiser": "/var/cfengine/httpd/htdocs/application/logs/.",
              "promisetype": "files",
              "stackpath": "/default/cfe_internal_management/methods/'CFEngine_Internals'/default/cfe_internal_enterprise_main/methods/'hub'/default/cfe_internal_setup_knowledge/files/'/var/cfengine/httpd/htdocs/application/logs/.'[1]"
          }
      ],
      "total": 2,
      "next": null,
      "previous": null
  }
```

See Also: [query rest api][Tracking changes]

### Custom Reports and Query API

The custom reports interface and associated [query rest api][Query REST API] allow more flexible
reports to be run.

Queries can be made against the `promiselog` table. This query finds the
promises that are repaired the most excluding internal cfengine related promises
and promises from the standard library.

```sql
-- Find most frequently repaired promises excluding lib and cfe_internal directories
SELECT namespace,bundlename,promisetype,promisehandle, promiser, count(promiseoutcome)
AS count
FROM promiselog
WHERE promiseoutcome = 'REPAIRED'
AND policyfile
NOT ilike '%/lib/%'
AND policyfile
NOT ilike '%cfe_internal%'
GROUP BY namespace, bundlename, promisetype,promisehandle,promiser
ORDER BY count DESC
```
  
Reference: [query api examples][SQL Query Examples]

### promise_log.jsonl

**NOTE:*** These logs are purged upon collection by the hub.

Beginning with Enterprise 3.9.0 we began logging promise outcomes to a JSON
format in `$(sys.statedir)/promise_log.jsonl`
(`/var/cfengine/state/prmise_log.jsonl`).

Each promise outcome is logged along with the bundle name, promise handle, log
messages near the promise actuation, the promise namespace, policy filename,
promise hash, promise type, promisees, promiser, release id, stack path (call
path), and the timestamp of the agent ran.

Here is an example of the output in `promise_log.jsonl`:

```json
{
    "execution": {
        "bundle":"file_make_mustache",
        "handle":"",
        "log_messages":[
            "Created file '/var/cfengine/httpd/conf/httpd.conf.staged', mode 0600",
            "Updated rendering of '/var/cfengine/httpd/conf/httpd.conf.staged' from mustache template '/var/cfengine/inputs/cfe_internal/enterprise/templates/httpd.conf.mustache'"
        ],
        "namespace":"default",
        "policy_filename":"/var/cfengine/inputs/lib/files.cf",
        "promise_hash":"ebc3dce615bcdb724e53a9761a24f2e7ed4f2e01aed1ce85dc217a9d3429fed7",
        "promise_outcome":"REPAIRED",
        "promise_type":"files",
        "promisees":[
            "CFEngine Enterprise",
            "Mission Portal"],
        "promiser":"/var/cfengine/httpd/conf/httpd.conf.staged",
        "release_id":"<unknown-release-id>",
        "stack_path":"/default/cfe_internal_management/methods/'CFEngine_Internals'/default/cfe_internal_enterprise_mission_portal/methods/'Apache Configuration'/default/cfe_internal_enterprise_mission_portal_apache/methods/'Stage Apache Config'/default/file_make_mustache/files/'/var/cfengine/httpd/conf/httpd.conf.staged'[0]"
    },
    "timestamp":1470326639
},
{
    "execution":{
        "bundle":"mission_portal_apache_from_stage",
        "handle":"",
        "log_messages":[
            "Updated '/var/cfengine/httpd/conf/httpd.conf' from source '/var/cfengine/httpd/conf/httpd.conf.staged' on 'localhost'"
        ],
        "namespace":"default",
        "policy_filename":"/var/cfengine/inputs/cfe_internal/enterprise/mission_portal.cf",
        "promise_hash":"d730f2911834395411e4f3168847fc6cc522955f97652de41e02c8bc15f3f761",
        "promise_outcome":"REPAIRED",
        "promise_type":"files",
        "promisees":[
            "CFEngine Enterprise",
            "Mission Portal"
        ],
        "promiser":"/var/cfengine/httpd/conf/httpd.conf",
        "release_id":"<unknown-release-id>",
        "stack_path":"/default/cfe_internal_management/methods/'CFEngine_Internals'/default/cfe_internal_enterprise_mission_portal/methods/'Apache Configuration'/default/cfe_internal_enterprise_mission_portal_apache/methods/'Manage Final Apache Config'/default/mission_portal_apache_from_stage/files/'/var/cfengine/httpd/conf/httpd.conf'[0]"
    },
    "timestamp":1470326639
}
```
