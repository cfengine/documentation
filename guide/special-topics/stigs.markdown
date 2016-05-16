---
layout: default
title: STIGs
published: true
sorting: 80
tags: [overviews, special topics, guide]
---

# CFEngine STIGs Compliance Example

The Security Technical Implementation Guides (STIGs) are a method for
standardized secure installation and maintenance of computer software and
hardware created by the Defense Information Systems Agency (DISA) that provides
configuration documents in support of the United States Department of Defense
(DoD). For more information and additional STIGs tools, please refer to
http://iase.disa.mil/stigs/

This page outlines how to achieve STIGs (Security Technical Implementation
Guide) compliance with CFEngine 3. What is the purpose of this CFEngine STIGs
example?

This sample policy and documentation is provided as an example of how CFEngine
can be used to achieve STIGs compliance on a Red Hat system. Although it is a
fully functional CFEngine 3 policy, it is designed to be an example only. It is
not intended to be implemented without prior full analysis. The intention is for
the users to review the policy file and documentation, and then create and/or
modify their own compliance policy. What version of CFEngine is this example
designed for?

The example policy is based on CFEngine 3 declarative language. It will work
with both the community version of CFEngine 3 and the commercial CFEngine 3
Enterprise subscription. The policy is written with comments and handles per
best practice in CFEngine 3. Which version of STIGs is this example based on?

This example is based on UNIX Security Checklist Version 5, Release 1.30 --
updated August 26, 2011 which can be found here. (see U_Unix-Sec3). Can I adopt
this policy and be STIGs compliant?

In theory yes, but in reality there is more to the process of becoming STIGs
compliant. Understanding each requirement and executing a suitable action
requires proper analysis and insight into the system(s). We strongly recommended
that all users review the policy and its accompanying documentation before
implementing a STIGs policy in CFEngine. STIGs feature specific guidelines on
logins and access, so executing the policy may change your access control and
user accounts, which may render you unable to log in and/or access the machine
with your traditional procedure. Does CFEngine (the company) assist on achieving
STIGs compliance?

Yes. If you are a CFEngine Enterprise customer, CFEngine professional services
are available to assist on multiple types of IT compliance, including STIGs,
PCI, SOX etc. Contact us through your regular CFEngine representative or use the
contact form to learn how CFEngine can help you implement and achieve desired
compliance. What are the different parts of this policy example?

* [STIGs.cf](./STIGs.cf)

  CFEngine policy file (ASCII), to be run by cf-agent

* [README](./STIGs_readme.txt)

  Explanation of the various policy components (human readable), referencing
  STIGs requirements id (such as ```GEN000560```)

# What are the terms of this STIGs example?

This example policy is intended as a practical example of how to achieve STIGs
compliance within the CFEngine framework. It is provided on an as-is basis, with
no promise of support or updates. CFEngine makes no warranty on its
functionality and system compatibility; neither is CFEngine an authoritative
source on STIGs compliance assessment, and hence this is not intended as a
statement on applicability and relevance on STIGs. Contact Us
