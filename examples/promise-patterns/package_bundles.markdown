---
layout: default
title: Managing Software
categories: [Examples, Promise Patterns, Managing Software]
published: true
alias: examples-policy-package-bundles.html
tags: [Examples, Policy, Packages]
---

This example shows how to use the pre-defined bundles from the
standard library to manage software packages.

[%CFEngine_include_example(package_bundles.cf)%]

This code shows how to use the bundles `cfe_package_named_ensure_present()`,
`cfe_package_ensure_absent()` and `cfe_package_named_ensure_upgrade()` from
the [packages][Packages Bundles and Bodies] standard library.
