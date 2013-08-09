---
layout: default
title: regcmp
categories: [Reference, Functions, regcmp]
published: true
alias: reference-functions-regcmp.html
tags: [reference, data functions, functions, regcmp]
---

[%CFEngine_function_prototype(regex, string)%]

**Description:** Returns whether the [anchored][anchored] regular expression 
`regex` matches the `string.`

[%CFEngine_function_attributes(regex, string)%]

**Example:**

```cf3
    bundle agent subtest(user)
    {
    classes:

      "invalid" not => regcmp("[a-z]{4}","$(user)");

    reports:

     !invalid::

      "User name $(user) is valid at exactly 4 letters";

     invalid::

      "User name $(user) is invalid";
    }
```

If the string contains multiple lines, then it is necessary to code these
explicitly, as regular expressions do not normally match the end of line
as a regular character (they only match end of string). You can do this
using either standard regular expression syntax or using the additional
features of PCRE (where `(?ms)` changes the way that ., `^` and `$` behave), e.g.

```cf3
     bundle agent example
     {
     vars:
     
       "x" string = "
           NAME: apache2 - Apache 2.2 web server
           CATEGORY: application
           ARCH: all
           VERSION: 2.2.3,REV=2006.09.01
           BASEDIR: /
           VENDOR: http://httpd.apache.org/ packaged for CSW by Cory Omand
           PSTAMP: comand@thor-20060901022929
           INSTDATE: Dec 14 2006 16:05
           HOTLINE: http://www.blastwave.org/bugtrack/
           EMAIL: comand@blastwave.org
           STATUS: completely installed
         ";
     
     classes:
     
       "pkg_installed" expression = regcmp("(.*\n)*STATUS:\s+completely installed\n(.*\n)*",$(x));
     
       "base_is_root" expression = regcmp("(?ms).*^BASEDIR:\s+/$.*", $(x));
     
     reports:
     
       pkg_installed::
     
         "installed";
     
       base_is_root::
     
         "in root";
     }
```
