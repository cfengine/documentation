---
layout: default
title: Verifying package signatures
published: true
sorting: 40
tags: [getting started, installation]
---

On the [Download CFEngine][enterprise software download page], you will find
sha256 checksums of all downloadable files which you can verify by using
`sha256sum` tool.

In addition to this, `*.deb` and `*.rpm` packages (with the exception of AIX rpms) are
cryptographically signed using gpg.


## Validating signature of RPM

NOTE: AIX rpms currently are NOT signed because it's not supported on older versions of AIX.

1. Import the public GPG key.

```console
# rpm --import https://cfengine-package-repos.s3.amazonaws.com/pub/gpg.key
```

2. Validate the signature.

```console
# rpm -K ./cfengine-nova-hub-3.12.2-2.x86_64.rpm 
./cfengine-nova-hub-3.12.2-2.x86_64.rpm: rsa sha1 (md5) pgp md5 OK
```

NOTE: If you don't import the public key first, you will get an error about the key missing:

```console
# rpm -K ./cfengine-nova-hub-3.12.2-2.x86_64.rpm 
./cfengine-nova-hub-3.12.2-2.x86_64.rpm: RSA sha1 ((MD5) PGP) md5 NOT OK (MISSING KEYS: (MD5) PGP#a86e7afa) 
```

## Validating signature of DEB

1. Import the public GPG key.

```console
# wget https://cfengine-package-repos.s3.amazonaws.com/pub/gpg.key
# mkdir /usr/share/debsig/keyrings/7061B663A86E7AFA
# gpg --no-default-keyring --keyring /usr/share/debsig/keyrings/7061B663A86E7AFA/debsig.gpg --import gpg.key
```

2. Create a policy.

```console
# mkdir /etc/debsig/policies/7061B663A86E7AFA
# cat >/etc/debsig/policies/7061B663A86E7AFA/cfengine3.pol
<?xml version="1.0"?>
<!DOCTYPE Policy SYSTEM "http://www.debian.org/debsig/1.0/policy.dtd">
<Policy xmlns="http://www.debian.org/debsig/1.0/">
  <Origin Name="cfengine3" id="7061B663A86E7AFA" Description="CFEngine 3"/>
  <Selection>
    <Required Type="origin" File="debsig.gpg" id="7061B663A86E7AFA"/>
  </Selection>
  <Verification MinOptional="0">
    <Required Type="origin" File="debsig.gpg" id="7061B663A86E7AFA"/>
  </Verification>
</Policy>
^D
```

3. Validate the signature.

```console
# debsig-verify cfengine-nova-hub_3.12.2-2_amd64.deb
debsig: Verified package from 'CFEngine 3' (cfengine3)
```
