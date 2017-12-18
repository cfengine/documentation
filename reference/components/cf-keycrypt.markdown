---
layout: default
title: cf-keycrypt
published: true
sorting: 10
tags: [Components, cf-keycrypt]
keywords: [agent]
---

`cf-keycrypt` allows you to encrypt data using cfengine keys.

The most straight forward usage of `cf-keycrypt` is to encrypt data for a
specific node from the hub since the hub already has each nodes public keys.
However data can be encrypted for multiple hosts by generating and distributing
keys for that group.

[%CFEngine_include_snippet(cf-keycrypt.help, [\s]*--[a-z], ^$)%]

# Encrypting Data

From the command line:

```
cf-keycrypt -e /var/cfengine/ppkeys/root-SHA=35d5d693dd86b3b01af00905ab14114568c14b0f580e3f07cd5c8eeaeb8db550.pub \
  -i /file_to_encrypt -o /encrypted_output_file
```

# Decrypting Data

From the command line:

```
cf-keycrypt -d /var/cfengine/ppkeys/localhost.priv \
  -i /encrypted_input_file -o /decrypted_output_file
```

From policy:

```cf3
      "secret"
        comment => "We decrypt the encrypted file directly into a variable.",
        string => execresult("$(sys.cf_keycrypt) -d $(private_key) -i $(encrypted_file) -o -", noshell);
```

[%CFEngine_include_snippet(cf-keycrypt.cf, #\+begin_src cfengine3, .*end_src)%]

Example Output:

[%CFEngine_include_snippet(cf-keycrypt.cf, #\+begin_src\s+static_example_output\s*, .*end_src)%]

**History:**

* Added in 3.12.0
