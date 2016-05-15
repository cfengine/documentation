---
layout: default
title: STIGs
published: false
sorting: 80
tags: [overviews, special topics, guide]
---


CFEngine

Login | Register

    Products & Services
    Resources
    Company
    Events

Try Now
CFEngine.com just got a new look!

With the new cfengine.com we hope to serve you with a better browsing experience and faster access to relevant content.
Please write to us contact@cfengine.com if you see a broken link or if you can't find the page you're looking for.

if you are looking for the documentation please follow the links below:

    CFEngine 3.6
    CFEngine 3.5
    CFEngine 3.0
    CFEngine 2.X


if you are looking for the downloads please follow the links below:

    Community
    Enterprise


Thank you and we hope you like the new experience!
CFEngine STIGs Compliance Example

The Security Technical Implementation Guides (STIGs) are a method for standardized secure installation and maintenance of computer software and hardware created by the Defense Information Systems Agency (DISA) that provides configuration documents in support of the United States Department of Defense (DoD). For more information and additional STIGs tools, please refer to http://iase.disa.mil/stigs/

This page outlines how to achieve STIGs (Security Technical Implementation Guide) compliance with CFEngine 3.
What is the purpose of this CFEngine STIGs example?

This sample policy and documentation is provided as an example of how CFEngine can be used to achieve STIGs compliance on a Red Hat system. Although it is a fully functional CFEngine 3 policy, it is designed to be an example only. It is not intended to be implemented without prior full analysis. The intention is for the users to review the policy file and documentation, and then create and/or modify their own compliance policy.
What version of CFEngine is this example designed for?

The example policy is based on CFEngine 3 declarative language. It will work with both the community version of CFEngine 3 and the commercial CFEngine 3 Enterprise subscription. The policy is written with comments and handles per best practice in CFEngine 3.
Which version of STIGs is this example based on?

This example is based on UNIX Security Checklist Version 5, Release 1.30 -- updated August 26, 2011 which can be found here.  (see U_Unix-Sec3).
Can I adopt this policy and be STIGs compliant?

In theory yes, but in reality there is more to the process of becoming STIGs compliant. Understanding each requirement and executing a suitable action requires proper analysis and insight into the system(s). We strongly recommended that all users review the policy and its accompanying documentation before implementing a STIGs policy in CFEngine. STIGs feature specific guidelines on logins and access, so executing the policy may change your access control and user accounts, which may render you unable to log in and/or access the machine with your traditional procedure.
Does CFEngine (the company) assist on achieving STIGs compliance?

Yes. If you are a CFEngine Enterprise customer, CFEngine professional services are available to assist on multiple types of IT compliance, including STIGs, PCI, SOX etc. Contact us through your regular CFEngine representative or use the contact form to learn how CFEngine can help you implement and achieve desired compliance.
What are the different parts of this policy example?

    STIGs.cf — cfengine3 policy file (ASCII), to be run by cf-agent
    README.txt — Explanation of the various policy components (human readable), referencing STIGs requirements id (such as GEN000560)
    FAQ — Answers to frequently asked questions about this STIGs example

What are the terms of this STIGs example?

This example policy is intended as a practical example of how to achieve STIGs compliance within the CFEngine framework. It is provided on an as-is basis, with no promise of support or updates. CFEngine makes no warranty on its functionality and system compatibility; neither is CFEngine an authoritative source on STIGs compliance assessment, and hence this is not intended as a statement on applicability and relevance on STIGs.
Contact Us

    Products & Services
        What is CFEngine?
        Community Edition
        Enterprise Edition
        Design Center
        Smart Infrastructure
        CFEngine Code Editors
        CFEngine Training
        CFEngine Consulting
    Resources
        Help & Support
        Documentation
        CFEngine Downloads
        Community Forum
        White papers
        Videos & Webinars
        Security
        Solutions
        Archive Documentation
        CFEngine 2 to CFEngine 3
        Special Topics Guides
        Technical FAQ
        CFEngine Science
    Company
        What's new?
        Upcoming Events
        Leadership
        Customers
        Partners
        Careers
        Blog
        Contact Us
    Events

Contact us: USA +1 650 257 0233, International: +47 47 97 01 79 - contact@cfengine.com
CFEngine AS - Borggata 1, 0650 Oslo, Norway.
CFEngine, Inc. 700 E. El Camino Real, Suite 170, Mountain View, CA 94040 Contact Us

Copyright 2008-2014 CFEngine AS - All rights reserved
