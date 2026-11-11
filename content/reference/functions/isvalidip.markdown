---
layout: default
title: isvalidip
aliases:
  - "/reference-functions-isvalidip.html"
---

{{< CFEngine_function_prototype(address, version) >}}

**Description:** Returns whether `address` is a valid IPv4 or IPv6 address.
An optional second argument `version`, either `"ipv4"` or `"ipv6"`, restricts
which IP version is accepted. By default, both are accepted.

The whole string must be an IP address:

- An IPv4 address consists of exactly four decimal numbers from 0 to 255,
  separated by dots, e.g. `192.168.1.10`.
- An IPv6 address consists of eight groups of 1 to 4 hexadecimal digits,
  separated by colons, e.g. `2001:0db8:0000:0000:0000:0000:0000:0001`. One
  sequence of zero groups may be shortened to `::`, e.g. `2001:db8::1`, and
  the last two groups may be written as an IPv4 address, e.g.
  `::ffff:192.0.2.128`.

Host names, surrounding whitespace, ports (`1.2.3.4:80`), brackets
(`[::1]`), subnet masks (`10.0.0.0/8`) and zone IDs (`fe80::1%eth0`) are not
accepted.

{{< CFEngine_function_attributes(address, version) >}}

**Example:**

```cfengine3
bundle agent main
{
  vars:
    "candidates"
      slist => {
        "1.2.3.4", "300.123.123.1", "FE80:CD00:0000:0CDE:1257:0000:211E:729C"
      };

  reports:
    "'$(candidates)' is a valid IP address" if => isvalidip("$(candidates)");

    "'$(candidates)' is a valid IPv4 address"
      if => isvalidip("$(candidates)", "ipv4");

    "'$(candidates)' is a valid IPv6 address"
      if => isvalidip("$(candidates)", "ipv6");

    "'$(candidates)' is not a valid IP address"
      unless => isvalidip("$(candidates)");
}
```

Output:

```
R: '1.2.3.4' is a valid IP address
R: 'FE80:CD00:0000:0CDE:1257:0000:211E:729C' is a valid IP address
R: '1.2.3.4' is a valid IPv4 address
R: 'FE80:CD00:0000:0CDE:1257:0000:211E:729C' is a valid IPv6 address
R: '300.123.123.1' is not a valid IP address
```

**See also:** `isipinsubnet()`, `iprange()`, `host2ip()`

**History:**

- Function added in 3.30.0.
