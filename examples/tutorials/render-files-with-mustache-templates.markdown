---
layout: default
title: Render files with Mustache templates
sorting: 15
published: true
tags: [Examples, Tutorials, mustache]
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/BUajq2b081E" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In this tutorial we will show how to use CFEngine to manage file configurations using mustache templating.

How it works

When working with templates, you need a template and data (parameters). Based on this CFEngine will render a file that fills the data in the appropriate places based on the template. Let’s create a templating solution for our home grown myapp-application. Below you can see the desired end state of the config file to the left. The right column shows the template we will use.

<table>
<tr>
<td>
<strong>myapp.conf &#8211; desired end state</strong>:<br />
Port 3508<br />
Protocol 2<br />
Filepath /mypath/<br />
Encryption 256<br />
Loglevel 1<br />
Allowed users <br />
 &nbsp;&nbsp;&nbsp;thomas=admin<br />
 &nbsp;&nbsp;&nbsp;malin=guest
</td>
<td><strong>myapp.conf.template &#8211; the template:</strong>.<br />
Port {{port}}<br />
Protocol {{protocol}}<br />
Filepath {{filepath}}<br />
Encryption {{encryption-level}}<br />
Loglevel {{loglevel}}<br />
Allowed users {{#users}}<br />
 {{user}}={{level}}{{/users}}
</td>
</tr>
</table>

1. Create the template

Create a file called `/tmp/myapp.conf.template` with the following content:

```
    Port {{port}}
    Protocol {{protocol}}
    Filepath {{filepath}}
    Encryption {{encryption-level}}
    Loglevel {{loglevel}}
    Allowed users {{#users}}
      {{user}}={{level}}{{/users}}
```

2. Create CFEngine policy

Create a file called `/tmp/editconfig.cf` with the following content:

```cf3
bundle agent myapp_confs
{
  files:
      "/tmp/myapp.conf"
      create => "true",
      edit_template => "/tmp/myapp.conf.template",
      template_method => "mustache",
      template_data => parsejson('
         {
            "port": 3508,
            "protocol": 2,
            "filepath": "/mypath/",
            "encryption-level": 256,
            "loglevel": 1,
            "users":
               [
                {"user": "thomas", "level": "admin"},
                {"user": "malin", "level": "guest"}
               ]
          }
    ');
}
body agent __main__
{
  methods:
    "myapp_confs";
}
```

In this policy we tell CFEngine to ensure a file called `myapp.conf` exists. The content of the file shall be based on a template file called `/tmp/myapp.conf.template`. The template method we use is mustache. Next we define the key value pairs we want to apply using json format (port shall be 3508, protocol 2, etc.)

3. Test it out, and verify the result

Run CFEngine:

```console
# /var/cfengine/bin/cf-agent /tmp/editconfig.cf
```

Verify the result:

```console
# cat /tmp/myapp.conf
Port 3508
Protocol 2
Filepath /mypath/
Encryption 256
Loglevel 1
Allowed users 
  thomas=admin
  malin=guest
```

You should now see the existence of a file called `/tmp/myapp.conf` with content similar to the desired state described above.

4. Congratulation you are done!

With CFEngine you can simplify management of configurations using templating. CFEngine comes both with its own and the mustache templating engine.

PS. If you manually change anything in `myapp.conf`, CFEngine will now restore it back to its desired state upon next run.

If there is no change in the template (`myapp.conf.template`), the file (`myapp.config`), or the data used by the template, CFEngine will not make any changes.




