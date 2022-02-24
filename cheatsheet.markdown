---
layout: printable
title: Markdown Cheatsheet
published: true
sorting: 1
alias: markdown-cheatsheet.html
---

Markdown formatting is simple, and the CFEngine generator adds a few things
to make it even simpler. Here's a list of the most commonly used formats.

# Basic formatting
## Remember

* **"Always pull never push"**

## Basic Formatting

```
One
Paragraph

Two
Paragraphs
```

One
Paragraph

Two
Paragraphs


`**Bold**` **Bold**

`*Italic*` *Italic*


## Links

### Link within documentation and to known pages

You can link to any documentation page using `[linktext][PageTitle]`.

#### Link to a specific section of a known page

You can link to any documentation page section using `[linktext][PageTitle#section]`.

When linking to a section, you should use the section name as it is rendered on the page.

For example, On the [functions][Functions] page we can link to the [collecting functions][Functions#collecting functions] section using `[collecting functions][Functions#collecting functions]`.

Sometimes (because `¯\_(ツ)_/¯`, maybe the page linked to hasn't been parsed yet) a page may not be automatically known. In this case an entry in [_references.md](https://github.com/cfengine/documentation-generator/blob/master/_references.md) of the [documentation-generator](https://github.com/cfengine/documentation-generator) may be required.

##### Special Characters in link targets

_Most_ (`¯\_(ツ)_/¯`) special characters are _okay_. For example:

* Link targets with `/` (forward slashes) work
   * ```[Export/Import][Settings#Export/Import]``` == [Export/Import][Settings#Export/Import]

Anchors with _underscores_ are problematic, they need to be escaped.

For example ```services_autorun``` in the MPF documentation the underscore needs to be escaped with a ```\```.

```**See also:** [`services_autorun` in the Masterfiles Policy Framework][Masterfiles Policy Framework#services\_autorun]```

**See also:** [`services_autorun` in the Masterfiles Policy Framework][Masterfiles Policy Framework#services\_autorun]

Actually, it seems that escaping underscores is not /required/.  This git grep finds links wehre target includes an underscore (`_`), some are not escaped and work.

`git grep '\[.*]\[.*_.*\]'`

```
README.md:    **See also:** `related_attribute`, [`attribute`][other_page#attribute]
cheatsheet.markdown:```**See also:** [`services_autorun` in the Masterfiles Policy Framework][Masterfiles Policy Framework#services\_autorun]```
cheatsheet.markdown:**See also:** [`services_autorun` in the Masterfiles Policy Framework][Masterfiles Policy Framework#services\_autorun]
enterprise-cfengine-guide/federated-reporting.markdown:See `cfengine_enterprise_federation:semanage_installed` in [cfe_internal/enterprise/federation/federation.cf][cfe_internal/enterprise/federation/federation.cf] for details on which packages are used for various distributions.
enterprise-cfengine-guide/hub_administration/adjusting-schedules.markdown:[hub_schedule][cf-hub#hub_schedule] defined in `body hub control` which also
enterprise-cfengine-guide/reporting.markdown:is configured by [`report_data_select` bodies][access#report_data_select].
enterprise-cfengine-guide/reporting.markdown:for either [inclusion][access#metatags_include] or
enterprise-cfengine-guide/reporting.markdown:[exclusion][access#metatags_exclude]. `cf-hub` collects `variables` that are not
enterprise-cfengine-guide/reporting.markdown:[`metatags_include`][access#metatags_include] and do not have any meta tags
enterprise-cfengine-guide/reporting.markdown:matching [`metatags_exclude`][access#metatags_exclude] and does not have a
enterprise-cfengine-guide/reporting.markdown:handle matching [`promise_handle_exclude`][access#promise_handle_exclude].
enterprise-cfengine-guide/reporting.markdown:matching [`metatags_include`][access#metatags_include] that do not have any meta
enterprise-cfengine-guide/reporting.markdown:tags matching [`metatags_exclude`][access#metatags_exclude].
enterprise-cfengine-guide/reporting.markdown:[`metatags_include`][access#metatags_include], ```noreport``` in
enterprise-cfengine-guide/reporting.markdown:[`metatags_exclude`][access#metatags_exclude] and ```noreport_.*``` in
enterprise-cfengine-guide/reporting.markdown:[`promise_handle_exclude`][access#promise_handle_exclude].
enterprise-cfengine-guide/reporting.markdown:[promise_handle_include][access#promise_handle_include] or
enterprise-cfengine-guide/reporting.markdown:[promise_handle_exclude][access#promise_handle_exclude].
enterprise-cfengine-guide/reporting/client-initiated-reporting.markdown:**See also:** [`call_collect_interval`][cf-serverd#call_collect_interval], [`collect_window`][cf-serverd#collect_window]
examples/example-snippets/basic-file-directory.markdown:The [rm_rf][lib/bundles.cf#rm_rf] and [rm_rf_depth][lib/bundles.cf#rm_rf_depth] bundles in the standard library make it easy to prune directory trees.
examples/example-snippets/promise-patterns/example_ssh_keys.markdown:Note: special variable [`$(sys.policy_hub)`][sys.policy_hub] contains the hostname of
examples/example-snippets/windows-registry.markdown:* [unit_registry_cache.cf][Windows Registry Examples#unit_registry_cache.cf]
examples/example-snippets/windows-registry.markdown:* [unit_registry.cf][Windows Registry Examples#unit_registry.cf]
examples/tutorials/file_comparison.markdown:2. [global_vars][#global_vars] - sets up some global variables for later use.
examples/tutorials/file_comparison.markdown:4. [create_aout_source_file][#create_aout_source_file] - creates a source file.
examples/tutorials/file_comparison.markdown:5. [create_aout][#create_aout] - compiles the source file.
examples/tutorials/file_comparison.markdown:6. [test_delete][#test_delete] - deletes a file.
examples/tutorials/file_comparison.markdown:7. [do_files_exist_1][#do_files_exist_1] - checks the existence of files.
examples/tutorials/file_comparison.markdown:8. [create_file_1][#create_file_1] - creates a file.
examples/tutorials/file_comparison.markdown:9. [outer_bundle_1][#outer_bundle_1] - adds text to a file.
examples/tutorials/file_comparison.markdown:10. [copy_a_file][#copy_a_file] - copies the file.
examples/tutorials/file_comparison.markdown:11. [do_files_exist_2][#do_files_exist_2] - checks the existence of both files.
examples/tutorials/file_comparison.markdown:12. [list_file_1][#list_file_1] - shows the contents of each file.
examples/tutorials/file_comparison.markdown:14. [outer_bundle_2][#outer_bundle_2] - modifies the contents of the second file.
examples/tutorials/file_comparison.markdown:15. [list_file_2][#list_file_2] - shows the contents of both files and uses CFEngine functionality to compare the modified time for each file.
examples/tutorials/tags.markdown:[MPF inventory policy][inventory/any.cf#cfe_autorun_inventory_listening_ports],
examples/tutorials/tags.markdown:[variablesmatching_as_data][variablesmatching_as_data]
guide/faq/integrate-custom-policy.markdown:**See also:** [`services_autorun` in the Masterfiles Policy Framework][Masterfiles Policy Framework#services\_autorun]
guide/faq/mustache-templating.markdown:**See also:** [`template_method` `mustache` extensions][files#template_method mustache extensions]
guide/faq/what-did-cfengine-change.markdown:Promises can be configured to [log their outcomes][Promise Types#log_repaired]
guide/installation-and-configuration/secure-bootstrap.markdown:**Note:** If you are using [protocol_version `1` or `classic`][Components#protocol_version]
guide/introduction/networking.markdown:    [`encrypt`][files#encrypt]) - not applicable if you are using new [`protocol_version`][Components#protocol_version].
guide/introduction/networking.markdown:documentation for body [`copy_from`][files#copy_from].
guide/introduction/networking.markdown:cf-serverd. [Protocol 2][Components#protocol_version]
guide/introduction/networking.markdown:[body common control `tls_ciphers`][Components#tls_ciphers].
guide/introduction/networking.markdown:[body common control `tls_min_version`][Components#tls_min_version].
reference/common-attributes-include.markdown:#### [depends_on][Promise Types#depends_on]
reference/common-body-attributes-include.markdown:##### [inherit_from][Promise Types#inherit_from]
reference/components.markdown:using the [`body copy_from protocol_version`][files#protocol_version]
reference/components.markdown:**See also:**  [`body copy_from protocol_version`][files#protocol_version], `allowlegacyconnects`, [`allowtlsversion`][cf-serverd#allowtlsversion], [`allowciphers`][cf-serverd#allowciphers], [`tls_min_version`][Components#tls_min_version], [`tls_ciphers`][Components#tls_ciphers], [`encrypt`][files#encrypt], [`logencryptedtransfers`][cf-serverd#logencryptedtransfers], [`ifencrypted`][access#ifencrypted]
reference/components.markdown:**See also:** [`protocol_version`][Components#protocol_version], [`allowciphers`][cf-serverd#allowciphers], [`tls_min_version`][Components#tls_min_version], [`allowtlsversion`][cf-serverd#allowtlsversion], [`encrypt`][files#encrypt], [`logencryptedtransfers`][cf-serverd#logencryptedtransfers], [`ifencrypted`][access#ifencrypted]
reference/components.markdown:**See also:** [`protocol_version`][Components#protocol_version], [`allowciphers`][cf-serverd#allowciphers], [`tls_ciphers`][Components#tls_ciphers], [`allowtlsversion`][cf-serverd#allowtlsversion], [`encrypt`][files#encrypt], [`ifencrypted`][access#ifencrypted], [`logencryptedtransfers`][cf-serverd#logencryptedtransfers]
reference/components/cf-agent.markdown:**See also:** [`edit_backup` in ```body edit_defaults```][files#edit_backup], [`copy_backup` in ```body copy_from```][files#copy_backup]
reference/components/cf-agent.markdown:**See also:** [`body action expireafter`][Promise Types#expireafter], [`body contain exec_timeout`][commands#exec_timeout], [`body executor control agent_expireafter`][cf-execd#agent_expireafter]
reference/components/cf-agent.markdown:**See also:** [select_end_match_eof in delete_lines][delete_lines], [select_end_match_eof in field_edits][field_edits], [select_end_match_eof in insert_lines][insert_lines], [select_end_match_eof in replace_patterns][replace_patterns]
reference/components/cf-execd.markdown:**See also:** [`body action expireafter`][Promise Types#expireafter], [`body contain exec_timeout`][commands#exec_timeout], [`body agent control expireafter`][cf-agent#expireafter]
reference/components/cf-monitord.markdown:[`$(mon.av_cpu)`][mon#mon.av_cpu]) to `cf-agent`, which may use them to inform
reference/components/cf-runagent.markdown:**See also:** [bundle resource_type in server access promises][access#resource_type], [cfruncommand in body server control][cf-serverd#cfruncommand]
reference/components/cf-runagent.markdown:**See also:** [body `copy_from` timeout][files#timeout], [agent `default_timeout`][cf-agent#default_timeout]
reference/components/cf-serverd.markdown:**See also:** [`protocol_version`][Components#protocol_version]
reference/components/cf-serverd.markdown:[`protocol_version`][Components#protocol_version] 1 (classic protocol),
reference/components/cf-serverd.markdown:[`protocol_version`][Components#protocol_version],
reference/components/cf-serverd.markdown:[`tls_ciphers`][Components#tls_ciphers],
reference/components/cf-serverd.markdown:[`tls_min_version`][Components#tls_min_version],
reference/components/cf-serverd.markdown:[`protocol_version`][Components#protocol_version] 1 (classic protocol),
reference/components/cf-serverd.markdown:[`protocol_version`][Components#protocol_version],
reference/components/cf-serverd.markdown:[`tls_ciphers`][Components#tls_ciphers],
reference/components/cf-serverd.markdown:[`tls_min_version`][Components#tls_min_version],
reference/components/cf-serverd.markdown:**See also:** [cf-runagent][cf-runagent], [bundle resource_type in server access promises][access#resource_type]
reference/components/cf-serverd.markdown:**See also:** [`ifencrypted`][access#ifencrypted], [`encrypt`][files#encrypt], [`tls_ciphers`][Components#tls_ciphers], [`tls_min_version`][Components#tls_min_version], [`allowciphers`][cf-serverd#allowciphers], [`allowtlsversion`][cf-serverd#allowtlsversion], [`protocol_version`][Components#protocol_version]
reference/enterprise-api-ref/host.markdown:After 5-10 minutes (one reporting iteration based on the [hub schedule][cf-hub#hub_schedule]), the main thread of cf-hub will pick up the deletion job.
reference/functions/execresult.markdown:**See also:** [`returnszero()`][returnszero], [`execresult_as_data()`][execresult_as_data].
reference/functions/findfiles.markdown:**See also:** [`bundlesmatching()`][bundlesmatching], [`findfiles_up()`][findfiles_up].
reference/functions/packagesmatching.markdown:**IMPORTANT:** Please note that you need to provide `package_inventory` attribute in `body common control` in order to be able to use this function. Also depending on the value(s) of `package_inventory` only packages from selected package modules will be returned. For more information about `package_inventory` please read [`package_inventory`][Components#package_inventory] section.
reference/functions/packageupdatesmatching.markdown:**IMPORTANT:** Please note that you need to provide `package_inventory` attribute in `body common control` in order to be able to use this function. Also depending on the value(s) of `package_inventory` only packages from selected package modules will be returned. For more information about `package_inventory` please read [`package_inventory`][Components#package_inventory] section.
reference/functions/usemodule.markdown:**See also:** [read_module_protocol()][read_module_protocol], [Module Protocol][commands#module]
reference/functions/variablesmatching.markdown:**See also:** [classesmatching()][classesmatching], [bundlesmatching()][bundlesmatching], [variablesmatching_as_data()][variablesmatching_as_data]
reference/language-concepts/classes.markdown:**See also:** [`persistance` classes attribute][classes#persistence], [`persist_time` in classes body][Promise Types#persist_time], [`lib/event.cf`][lib/event.cf] in the MPF, [`lib/feature.cf`][lib/feature.cf] in the MPF
reference/language-concepts/modules.markdown:Variables and Classes Modules are the original way to extend CFEngine. The Variable and Class Module Protocol allows for *variables* and *classes* to be defined. The protocol can be interpreted by functions like [`usemodule()`][usemodule] and [`read_module_protocol()`](read_module_protocol) as well as output from [*commands* type promises][commands] with the [`module => "true"`][commands#module] attribute.
reference/language-concepts/normal-ordering.markdown:Within [`edit_line` bundles in files promises][edit_line],
reference/masterfiles-policy-framework/lib-files.markdown:See the [`files` promises][files] and [`edit_line` bundles][edit_line]
reference/masterfiles-policy-framework/lib.markdown:* [`$(sys.local_libdir)`][sys#sys.local_libdir] (relative to the root of your policy inputs)
reference/promise-types.markdown:| [guest_environments][guest_environments] |        | x     |        |         |
reference/promise-types.markdown:with [`body contain exec_timeout`][commands#exec_timeout] in commands type
reference/promise-types.markdown:**See also:** [`body contain exec_timeout`][commands#exec_timeout], [`body agent control expireafter`][cf-agent#expireafter], [`body executor control agent_expireafter`][cf-execd#agent_expireafter]
reference/promise-types.markdown:Log messages to [syslog_host][Components#syslog_host] as
reference/promise-types.markdown:If possible, perform the verification of the current promise in the background (up to [`max_children` in body agent control][cf-agent#max_children]).
reference/promise-types.markdown:**See also:** [`max_children` in body agent control][cf-agent#max_children]
reference/promise-types.markdown:**See also:** [`persistance` classes attribute][classes#persistence], [`persist_time` in classes body][Promise Types#persist_time]
reference/promise-types/access.markdown:[`protocol_version`][Components#protocol_version] 2 or
reference/promise-types/access.markdown:**See also:** [`protocol_version`][Components#protocol_version], [`allowtlsversion`][cf-serverd#allowtlsversion], [`allowciphers`][cf-serverd#allowciphers], [`tls_min_version`][Components#tls_min_version], [`tls_ciphers`][Components#tls_ciphers], [`encrypt`][files#encrypt], [`logencryptedtransfers`][cf-serverd#logencryptedtransfers], [`ifencrypted`][access#ifencrypted]
reference/promise-types/access.markdown:for [query][access#resource_type] resources, and allows filtering of data reported to the
reference/promise-types/access.markdown:[`resource_type => "query"`][access#resource_type], as this is the resource type that is being affected.
reference/promise-types/classes.markdown:**See also:** [`persistance` classes attribute][classes#persistence], [`persist_time` in classes body][Promise Types#persist_time]
reference/promise-types/commands.markdown:**See also:** [`body action expireafter`][Promise Types#expireafter],  [`body agent control expireafter`][cf-agent#expireafter], [`body executor control agent_expireafter`][cf-execd#agent_expireafter]
reference/promise-types/commands.markdown:**See also:** [usemodule()][usemodule], [read_module_protocol()][read_module_protocol]
reference/promise-types/files.markdown:**See also:** [Common Body Attributes][Promise Types#Common Body Attributes], [`default_repository` in ```body agent control```][cf-agent#default_repository], [`edit_backup` in ```body edit_defaults```][files#edit_backup]
reference/promise-types/files.markdown:**See also:** [`protocol_version`][Components#protocol_version], [`ifencrypted`][access#ifencrypted], [`protocol_version`][Components#protocol_version], [`tls_ciphers`][Components#tls_ciphers], [`tls_min_version`][Components#tls_min_version], [`allowciphers`][cf-serverd#allowciphers], [`allowtlsversion`][cf-serverd#allowtlsversion]
reference/promise-types/files.markdown:**See also:** [link_type][files#link_type].
reference/promise-types/files.markdown:**See also:** [`seed_cp`][seed_cp] in the MPF, [`compare`][files#compare] in body `copy_from`
reference/promise-types/files.markdown:**See also:** [`protocol_version`][Components#protocol_version] in
reference/promise-types/files.markdown:**Default Value:** [`default_timeout`][cf-agent#default_timeout]
reference/promise-types/files.markdown:**See also:** [agent `default_timeout`][cf-agent#default_timeout], [`cf-runagent` timeout][cf-runagent#timeout]
reference/promise-types/files.markdown:see [`bundle agent rm_rf_depth` in the standard library][lib/bundles.cf#rm_rf_depth].
reference/promise-types/files.markdown:**See also:** [`default_repository` in ```body agent control```][cf-agent#default_repository], [`copy_backup` in ```body copy_from```][files#copy_backup], [`rotate` in `body edit_defaults`][files#rotate]
reference/promise-types/files.markdown:**See also:** [`edit_backup` in ```body edit_defaults```][files#edit_backup]
reference/promise-types/files.markdown:**Type:** [`edit_line`][edit_line]
reference/promise-types/files.markdown:**Type:** [`edit_xml`][edit_xml]
reference/promise-types/files/edit_line.markdown:modified with [`select_end_match_eof`][cf-agent#select_end_match_eof].
reference/promise-types/files/edit_line.markdown:**See also:** [`select_end_match_eof` in body agent control][cf-agent#select_end_match_eof]
reference/promise-types/files/edit_line/delete_lines.markdown:**See also:** [```select_region``` with `edit_line` operations][edit_line#select_region], [```select_region``` in `field_edits`][field_edits#select_region], [```select_region``` in `insert_lines`][field_edits#select_region], [```select_region``` in `replace_patterns`][replace_patterns#select_region]
reference/promise-types/files/edit_line/field_edits.markdown:**See also:** [```select_region``` with `edit_line` operations][edit_line#select_region], [```select_region``` in `delete_lines`][delete_lines#select_region], [```select_region``` in `insert_lines`][insert_lines#select_region], [```select_region``` in `replace_patterns`][replace_patterns#select_region]
reference/promise-types/files/edit_line/insert_lines.markdown:**See also:** [```select_region``` with `edit_line` operations][edit_line#select_region], [```select_region``` in `delete_lines`][delete_lines#select_region], [```select_region``` in `field_edits`][field_edits#select_region], [```select_region``` in `replace_patterns`][replace_patterns#select_region]
reference/promise-types/files/edit_line/replace_patterns.markdown:**See also:** [```select_region``` with `edit_line` operations][edit_line#select_region], [```select_region``` in `delete_lines`][delete_lines#select_region], [```select_region``` in `field_edits`][field_edits#select_region], [```select_region``` in `insert_lines`][insert_lines#select_region]
reference/promise-types/files/edit_xml/delete_attribute.markdown:**See also:** [Common `edit_xml` attributes][edit_xml#common attributes]
reference/promise-types/measurements.markdown:By default in the [Masterfiles Policy Framework][Masterfiles Policy Framework], `cf-serverd` uses two variables, `def.default_data_select_host_monitoring_include` and `def.default_data_select_policy_hub_monitoring_include` to [configure which measurements will be included in enterprise reporting][mpf-configure-measurement-collection].
reference/promise-types/measurements.markdown:This is mutually exclusive of [`select_line_matching`][measurements#select_line_matching].
reference/promise-types/packages-deprecated.markdown:available. *See Also* [package_latest][lib/packages.cf#package_latest]
reference/promise-types/packages-deprecated.markdown:[package_specific_latest][lib/packages.cf#package_specific_latest] in the
reference/promise-types/packages.markdown:[`package_module`][Components#package_module] attribute
reference/promise-types/packages.markdown:  flexible [naming convention][packages (deprecated)#package_name_convention].
reference/promise-types/packages.markdown:[`package_module`][Components#package_module] in Components
reference/promise-types/services.markdown:[`$(this.service_policy)`][this#this.service_policy] may be used to fill in
reference/promise-types/services.markdown:[`$(this.service_policy)`][this#this.service_policy] variable is only defined
reference/promise-types/services.markdown:**See also:** [generic standard_services][Services Bodies and Bundles#standard_services]
reference/special-variables/connection.markdown:[`protocol_version`][Components#protocol_version] >=2 ( or "latest" ).
reference/special-variables/sys.markdown:**Note:** The *keys* in this array are [canonified][canonify]. For example, the entry for `wlan0.1` would be found under the `wlan0_1` key. Ref: [CFE-3224](https://tracker.mender.io/browse/CFE-3224).
reference/special-variables/sys.markdown:- The *values* in this array are [canonified][canonify]. For example, the entry for `wlan0.1` would be `wlan0_1`. Ref: [CFE-3224](https://tracker.mender.io/browse/CFE-3224).
reference/special-variables/sys.markdown:**Note:** The *keys* in this array are [canonified][canonify]. For example, the entry for `wlan0.1` would be found under the `wlan0_1` key. Ref: [CFE-3224](https://tracker.mender.io/browse/CFE-3224).
reference/special-variables/sys.markdown:**Note:** The *keys* in this array are [canonified][canonify]. For example, the entry for `wlan0.1` would be found under the `wlan0_1` key. Ref: [CFE-3224](https://tracker.mender.io/browse/CFE-3224).
reference/special-variables/sys.markdown:**Note:** The *keys* in this array are [canonified][canonify]. For example, the entry for `wlan0.1` would be found under the `wlan0_1` key. Ref: [CFE-3224](https://tracker.mender.io/browse/CFE-3224).
reference/special-variables/sys.markdown:**See also:** [`sys.policy_entry_dirname`][sys.policy_entry_dirname] [`sys.policy_entry_filename`][sys.policy_entry_dirname]
reference/special-variables/sys.markdown:**See also:** [`sys.policy_entry_basename`][sys#sys.policy_entry_basename] [`sys.policy_entry_filename`][sys.policy_entry_filename]
reference/special-variables/sys.markdown:**See also:** [`sys.policy_entry_basename`][sys#sys.policy_entry_basename] [`sys.policy_entry_dirname`][sys#sys.policy_entry_dirname]
```




### Link to CFEngine keyword

The documentation pre-processor will create those automatically.

```
`classes` and `readfile()`
```

<!--- cheat - otherwise we get ambiuous link target warnings -->
[`classes`][classes] and `readfile()`

However, the preprocess will not create links if the code word is in triple backticks:


    ```classes``` and ```readfile()```

```classes``` and ```readfile()```

### Link to External URL

`[Markdown Documentation](http://daringfireball.net/projects/markdown/)`

[Markdown Documentation](http://daringfireball.net/projects/markdown/syntax)


## Lists

### Unordered lists - Markdown supports other markers than the asterisk, but in
CFEngine we use only `*`.

```
* Item 1
* Item 2
   * Item 2a
* Multi paragraph item

    Four spaces indented
```

* Item 1
* Item 2
   * Item 2a
* Multi paragraph item

    Four spaces indented

### Ordered lists - the numbers you use don't matter.

```
1. first
1. second
9. Third
```

1. first
1. second
9. Third

### Nested lists

```

* Item 1
  1. First
  2. First
    1. 1.2.1
* Item 2
  * Item 2a (2 spaces)
      
      I am indented 4 spaces

* Multi paragraph item

    I am indented four spaces
```

* Item 1
  1. First
  2. First
    1. 1.2.1
* Item 2
  * Item 2a (2 spaces)
      
      I am indented 4 spaces

* Multi paragraph item

    I am indented four spaces


## Tables

Wiki-syntax for tables is supported, and you can be a bit sloppy
about it, although it's better to align the `|` properly.

```
| Header | Left aligned | Centered | Right aligned |
|--------|:-------------|:--------:|--------------:|
|text    | text | X | 234 |
```

| Header | Left aligned | Centered | Right aligned |
|--------|:-------------|:--------:|--------------:|
|text    | text | X | 234 |


## Code

### Inline code

    This renders as `inline code`.

This renders as `inline code`.

    This also renders as ```inline code```.

This also renders as ```inline code```.

See the note above on implicit linking - single backticks will link, triple backticks won't.

### Code Blocks

Code blocks are either indendented by four spaces:

Just indent by four spaces:

```
    $ code block
    $ without syntax highlighting
```

    $ code block
    $ without syntax highlighting

or use three backticks:

    ```
    some more code
    in a block
    ```

```
some more code
in a block
```

To turn on syntax highlighting, specify the brush directly after the opening three
backticks. Syntax highlighting is provided by pygments. Find all available lexers [here](http://pygments.org/docs/lexers/).

#### CFEngine Code Blocks

If you want CFEngine syntax highlighting, use

    ```cf3
    # CFEngine block

    bundle agent example()
    {
    }
    ```

```cf3
# CFEngine code block

bundle agent example()
{
}
```


Other frequently used syntax highlighers shown below.

#### Bash Script Code Blocks

		```bash
		#!/bin/bash
        echo hi
        for i in `seq 1 10`;
        do
          echo $i
        done
		```

```bash
#!/bin/bash
echo hi
for i in `seq 1 10`;
do
  echo $i
done
```

#### Console Blocks

        ```console
		root@policy_server # /etc/init.d/cfengine3 stop
        ```

```console
root@policy_server # /etc/init.d/cfengine3 stop
```

#### SQL Code Blocks

		```sql
	    SELECT
	         FileChanges.FileName,
	         Count(Distinct(FileChanges.HostKey)) AS DistinctHostCount,
	         COUNT(1) AS ChangeCount
	      FROM
	         FileChanges JOIN Contexts
	      WHERE
	         Contexts.ContextName='ubuntu'
	      GROUP BY
	         FileChanges.FileName
	      ORDER BY
	         ChangeCount DESC
		```

```sql
SELECT
     FileChanges.FileName,
     Count(Distinct(FileChanges.HostKey)) AS DistinctHostCount,
     COUNT(1) AS ChangeCount
  FROM
     FileChanges JOIN Contexts
  WHERE
     Contexts.ContextName='ubuntu'
  GROUP BY
     FileChanges.FileName
  ORDER BY
     ChangeCount DESC
```

#### Diff Code Blocks

		```diff
		diff --git a/README.md b/README.md
		index 92555a2..b49c0bb 100644
		--- a/README.md
		+++ b/README.md
		@@ -377,8 +377,12 @@ As a general note, avoiding abbreviations provides better readability.

		 * follow the [Policy Style Guide](guide/writing-and-serving-policy/policy-style.markdown)
		   in examples and code snippets
		-* always run it through Pygments plus the appropriate lexer (only cf3
		-  supported for now)
		+* always run it through Pygments plus the appropriate lexer
		+
		+Most important are the `cf3` lexer, as well as `bash`, `console`,
		+`diff`, `shell-session` and `postgresql`. But Jekyll supports
		+[many more lexers](http://pygments.org/docs/lexers/)
		+
		 * avoid custom color schemes and hand-coded HTML
		 * document the example after the example code
		```

```diff
diff --git a/README.md b/README.md
index 92555a2..b49c0bb 100644
--- a/README.md
+++ b/README.md
@@ -377,8 +377,12 @@ As a general note, avoiding abbreviations provides better readability.

 * follow the [Policy Style Guide](guide/writing-and-serving-policy/policy-style.markdown)
   in examples and code snippets
-* always run it through Pygments plus the appropriate lexer (only cf3
-  supported for now)
+* always run it through Pygments plus the appropriate lexer
+
+Most important are the `cf3` lexer, as well as `bash`, `console`,
+`diff`, `shell-session` and `postgresql`. But Jekyll supports
+[many more lexers](http://pygments.org/docs/lexers/)
+
 * avoid custom color schemes and hand-coded HTML
 * document the example after the example code
```


#### JSON Code Blocks

{% raw %}
```json
{
  "classes":{
    "services_autorun": [ "any" ]
  }
}
```
{% endraw %}


```json
{
  "classes":{
    "services_autorun": [ "any" ]
  }
}
```

#### YAML Code Blocks

{% raw %}
```yaml
---
  classes:
    services_autorun:
      - "any"
```
{% endraw %}


```yaml
---
  classes:
    services_autorun:
      - "any"
```

### Code Blocks and Lists

If you want to include a code block within a list, put two tabs (8 spaces) in front of the entire block (4 to make the paragraph part of the list item, and 4 for it a code block):

```
* List item with code

        <code goes here>
```

* List item with code

        <code goes here>


You can also use backticks (and get syntax highlighting) - just make sure the backticks are indented once:

    1. First

    	```cf3
    	# CFEngine block

    	bundle agent example()
    	{
    	}
    	```

    2. Second
    3. Third

1. First

	```cf3
	# CFEngine block

	bundle agent example()
	{
	}
	```

2. Second
3. Third


*****

## Headers

### Horizontal bar

`***`

***

`# Level 1`

# CFEngine Extensions
## Example policy from core

Examples from cfengine/core can be rendered using the `CFEngine_include_example` macro.

- Lines inside `src` starting with `#@ ` are interpreted as markdown.

- Wrap macro in `raw` and `endraw` tags if the file contains mustache. This allows it to be rendered correctly. 

  `[\%CFEngine_include_example(class-automatic-canonificiation.cf)\%]`

  {% raw %}
  [%CFEngine_include_example(class-automatic-canonificiation.cf)%]
  {% endraw %}

## Include snippet of text from a file

Sometimes it's nice to include a snippet from another file. For example, we dynamically generate the `--help` output for each component on each doc build and that output is included on each component page.

  `[%CFEngine_include_snippet(cf-promises.help, [\s]*--[a-z], ^$)%]`

  [%CFEngine_include_snippet(cf-promises.help, [\s]*--[a-z], ^$)%]


# Level 1

`## Level 2`

## Level 2

`### Level 3`

### Level 3

`#### Level 4`

#### Level 4

`##### Level 5`

##### Level 5

`###### Level 6`

###### Level 6

*****

## Including External Files

Sometimes it's nice to include an external file

<pre>
[%CFEngine_include_markdown(masterfiles/CHANGELOG.md)%]
</pre>

### Including chunks of policy from the MPF

Here I am including a bundle named `cfe_autorun_inventory_listening_ports`. It may be a common or an agent bundle (in case the bundle ever changes types).

<pre>
[%CFEngine_include_snippet(inventory/any.cf, bundle\s+(agent|common)\s+cfe_autorun_inventory_listening_ports, \})%] 
</pre>

[%CFEngine_include_snippet(inventory/any.cf, bundle\s+(agent|common)\s+cfe_autorun_inventory_listening_ports, \})%] 

#### body delete tidy from lib/files.cf in the MPF

[%CFEngine_include_MPF_snippet(lib/files.cf, body\s+delete\s+tidy, \})%]

## Comments inside documentation

Sometimes it's nice to be able to put an internal comment into the
documentation that will not be rendered.

You can use the comment and endcomment tags in markdown files.

For example:

```
{% raw %}
{% comment %} TODO: We should try to improve this at some point.{% endcomment %}
{% endraw %}
```

Would render like this:

```
{% comment %} TODO: We should try to improve this at some point.{% endcomment %}
```

# FAQ
## When should I use `verbatim` vs **bold** or *italic*?

If it's code or something you would see on the command line (policy language, file names, command line options, binaries / CLI programs) use monospace (single backticks for inline, triple backticks for block, or when you have inline word that could also be an automatic link target that is undesirable, e.g. `files` ({% raw %}`files`{% endraw %}) vs ```files``` ({% raw %}```files```{% endraw %}) ).

If you are referring to something within UI / screenshots / buttons etc use bold and capitalize it as it is within the UI/Button/whatever.

  
**References:**

* https://www.patternfly.org/v4/ux-writing/punctuation/
* https://docs.microsoft.com/en-us/style-guide/procedures-instructions/formatting-text-in-instructions

# Sandbox

## symlink example

[%CFEngine_include_snippet(masterfiles/lib/files.cf, ^body\slink_from\sln_s.*, ^##)%]



## Self Documenting Policy
### For the stdlib:

[%CFEngine_library_include(lib/commands)%]

### For update.cf?

[%CFEngine_library_include(update)%]

### for Promises.cf?

[%CFEngine_library_include(promises)%]

# Variables
Referencing a version of CFEngine? Consider if that appearance should be
updated with each new version.

Variables that are defined in the front matter (thats the content between the
three dashes at the top) or in
[_config.yaml](https://github.com/cfengine/documentation-generator/blob/master/_config.yml)
in the documentation-generator repository can be used directly within markdown.

For example this is the '{{site.CFE_manuals_version}}' version of the
documentation. That variable comes from _config.yaml.

Since liquid variables look a lot like mustache variables any time you want to
show the actual variables will need to be inside of raw tags.

{% raw %}
site.CFE_manuals_version {{ site.CFE_manuals_version }}
{% endraw %}

# Testing
## Indention with included markdown

1. Verify that the selected hosts are upgrading successfully.

   - Mission Portal [Inventory reporting interface][Reporting UI#inventory management]

   - [Inventory API][Inventory API]

     ```console
     root@hub:~# curl -k \
     --user <admin>:<password> \
     -X POST \
     https://hub.localdomain/api/inventory  \
     -H 'content-type: application/json' \
     -d '{
           "sort":"Host name",
           "filter":{
              "CFEngine version":{
                 "not_match":"{{site.cfengine.branch}}.0"
              }
           },
           "select":[
              "Host name",
              "CFEngine version"
            ]
         }'
     ```
  
2. Some other thing


