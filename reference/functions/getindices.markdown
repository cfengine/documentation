---
layout: default
title: getindices
categories: [Reference, Functions, getindices]
published: true
alias: reference-functions-getindices.html
tags: [reference, data functions, functions, getindices]
---

[%CFEngine_function_prototype(array)%]

**Description:** Returns a list of keys in `array`.

Make sure you specify the correct scope when supplying the name of the
variable.

[%CFEngine_function_attributes(array)%]

**Example:**

```cf3
bundle agent example
{
  vars:

      "ps[relayhost]"                  string => "[$(mailrelay)]:587";
      "ps[mydomain]"                   string => "iu.hio.no";
      "ps[smtp_sasl_auth_enable]"      string => "yes";
      "ps[smtp_sasl_password_maps]"    string => "hash:/etc/postfix/sasl-passwd";
      "ps[smtp_sasl_security_options]" string => "";
      "ps[smtp_use_tls]"               string => "yes";
      "ps[default_privs]"              string => "mailman";
      "ps[inet_protocols]"             string => "all";
      "ps[inet_interfaces]"            string => "127.0.0.1";

      "parameter_name" slist => getindices("ps");

  reports:

      "Found key $(parameter_name)";
}
```
