---
layout: default
title: Public key distribution
published: true
tags: [cfengine enterprise, hub administration, key distribution, trust establishment]
---

> How can I arrange for the hosts in my infrastructure to trust a new key?

If you are deploying a new hub, or authorizing a non-hub to copy files from
peers you will need to establish trust before communication can be established.

In order for trust to be established each host must have the public key of the
other host stored in `$(sys.ppkeys)` named for the public key sha.

For example, we have 2 hosts. host001 with public key sha
`SHA=917962161107efaed9610de3e034085373142f577fb7e7b9bddec2955b748836` and hub
with public key sha
`SHA=af00250085306c68bb6d5f489f0239e2d7ff8a1f53f2d00e77c9ad2044309dfe`. For
trust to be established `host001` must have
`$(sys.workdir)/ppkeys/root-SHA=af00250085306c68bb6d5f489f0239e2d7ff8a1f53f2d00e77c9ad2044309dfe.pub`
and hub must have
`$(sys.workdir)/ppkeys/root-SHA=917962161107efaed9610de3e034085373142f577fb7e7b9bddec2955b748836.pub`.
The files must be root owned with write access restricted to the owner (644 or
less).

This policy shows how public keys can be stored in a central location on the
policy server and automatically installed on all hosts.


```cf3
bundle agent trust_distkeys
#@ brief Example public key distribution
{
  meta:

      "tags" slist => { "autorun" };

  vars:

      "keystore"
        comment => "We want all hosts to trust these hosts because they perform
                    critical functions like policy serving.",
        string => ifelse( isvariable( "def.trustkeys[keystore])" ), "$(def.trustkeys[keystore])",
                                      "distkeys");

  files:

      "$(sys.workdir)/ppkeys/."
        handle => "trust_distkeys",
        comment => "We need trust all the keys stored in `$(keystore)` on
                   `$(sys.policy_hub)` so that we can communicate with them
                   using the CFEngine protocol.",
        copy_from => remote_dcp( $(keystore), $(sys.policy_hub) ),
        depth_search => basedir,
        file_select => public_keys,
        perms => mog( 644, root, root );
}

bundle server share_distkeys
#@ brief Share the directory containing public keys we need to distribute
{
  access:

    (policy_server|am_policy_hub)::

      "/var/cfengine/distkeys/"
        admit_ips => { "0.0.0.0/0" },
        shortcut => "distkeys",
        handle => "access_share_distkeys",
        comment => "This directory contains public keys of hosts that should be
                    trusted by everyone.";

}

body depth_search basedir
#@ brief Search the files in the top level of the source directory
{
      include_basedir => "true";
      depth => "1";
}

body file_select public_keys
#@ brief Select plain files matching public key file naming patterns
{
        # root-SHA=abc123.pub
        leaf_name => { "\w+-(SHA|MD5)=[[:alnum:]]+\.pub" };
        file_types => { "plain" };

        file_result => "leaf_name.file_types";
}
```
