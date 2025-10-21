---
layout: default
title: General installation
sorting: 20
aliases:
  - "/getting-started-installation-general-installation.html"
---

{{< CFEngine_include_markdown(install-bootstrap-configure-summary.include.markdown) >}}

## Before installation

Check the [Pre-installation checklist][Pre-installation checklist] and [Supported platforms and versions][Supported platforms and versions] for requirements and other information that is useful for the installation procedure.

## Install packages

CFEngine Enterprise is provided in two packages; one is for the Policy
Server (hub) and the other is for each Host (client).

Note: See [Installing Community][Installing Community] for the community version of CFEngine)

**Log in as root** and then follow these steps to install CFEngine Enterprise:

1. On the designated Policy Server, install the `cfengine-nova-hub` package:

   ```
   [RedHat/CentOS/SUSE] # yum -y install /path/to/<server hub package>.rpm
   [Debian/Ubuntu]      # apt -y install /path/to/<server hub package>.deb
   ```

2. On each Host, install the `cfengine-nova` package:

   ```
   [RedHat/CentOS/SUSE] # yum -y install /path/to/<agent package>.rpm
   [Debian/Ubuntu]      # apt -y install /path/to/<agent package>.deb
   ```

Note: Install actions logged to `/var/logs/cfengine-install.log`.

## Bootstrap

Bootstrapping a client means to configure it initially. With CFEngine, the default bootstrap:

- records the server's address (accessible as `sys.policy_hub`) and public key, and gives the server the client's key to establish trust (see [Bootstrapping][Client server communication#Bootstrapping])
- copies **all** the contents of `/var/cfengine/masterfiles` on the policy server (AKA `sys.masterdir`) to `/var/cfengine/inputs` (AKA `sys.inputdir`). See `update.cf` for details.

Run the bootstrap command, **first** on the policy server:

1. Find the IP address of your Policy Server:

```command
ifconfig
```

2. Run the bootstrap command:

```command
sudo /var/cfengine/bin/cf-agent --bootstrap <IP address of policy server>
```

The bootstrap command must then be run on any client attaching itself to this server, using the ip address of the policy server (i.e. exactly the same as the command run on the policy server itself).

## Post-installation configuration

CFEngine itself is configured through policy as well (see [Components][] and
[Masterfiles Policy Framework][] for details). The following basic changes to the default policy will configure
`cf-serverd` and `cf-execd` for your environment.

### Configure agent email settings

By default an email a summary of any `cf-agent` run initiated by `cf-execd`. You
may want to adjust the mailto or mailfrom. If you have a centralized reporting
system like CFEngine Enterprise you may wish to disable agent emails all
together.

#### Configure mailto and mailfrom

The preferred way of setting `def.mailfrom` is from the
[augments file][Augments].

```json {file="def.json"}
{
  "vars": {
    "mailfrom": "sender@your.domain.here",
    "mailto": "recipient@your.domain.here"
  }
}
```

Alternatively you can alter the setting in `def.cf`.

**Note:** On some systems these modifications should hopefully work without
needing to make any additional changes elsewhere. However, any emails sent from
the system might also end up flagged as spam and sent directly to a user's junk
mailbox.

**Note:** It's best practice to restart daemons after adjusting it's settings to
ensure they have taken effect.

#### Disable agent emails

The preferred way to disable the agent from sending emails is to define
`cfengine_internal_disable_agent_email` from the [augments file][Augments].

```json {file="def.json"}
{
  "classes": { "cfengine_internal_disable_agent_email": ["any"] }
}
```

Alternatively you can define the class from `def.cf`.

**Note:** It's best practice to restart daemons after adjusting it's settings to
ensure they have taken effect.

### Server IP address and hostname

Edit `/etc/hosts` and add an entry for the IP address and hostname of the server.

### CFEngine Enterprise post-installation setup

See: [What steps should I take after installing CFEngine Enterprise?][FAQ#What steps should I take after installing CFEngine Enterprise]

## More detailed installation guides

Although most install procedures follow the same general workflow, there are several ways of installing CFEngine depending on your environment and which version of CFEngine you are using.

- [Installing Enterprise for production][Installing Enterprise for production]
- Install and test the latest version using our [native version][Installing Enterprise 25 Free], for free!
- Installing CFEngine on virtual machine instances using [Amazon Web Services' (AWS) EC2 service][Using Amazon Web Services]
  - This is especially useful for people running Windows on their workstation or laptop.
- Install and test the latest version using our pre-packaged [Vagrant environment][Using Vagrant]
- [Installing CFEngine Community Edition][Installing Community]

## Next steps

- Learn about [Writing and serving policy][Writing and serving policy]
