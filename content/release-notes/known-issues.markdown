---
layout: default
title: Known issues
sorting: 50
aliases:
  - "/release-notes-known-issues.html"
---

CFEngine defects are managed in our [bug tracker][bug tracker].
Please report bugs or unexpected behavior there, following the documented guideline for new bug reports.

- Issues [affecting {{site.CFE_manuals_version}}](https://northerntech.atlassian.net/issues/?jql=project+in+%28ENT%2C+CFE%29+AND+affectedVersion+%7E+%22{{site.CFE_manuals_version}}.*%22+AND+status+not+in+%28+%22Rejected%22%29)
- Issues [fixed in {{site.CFE_manuals_version}}](https://northerntech.atlassian.net/issues/?jql=project+in+%28ENT%2C+CFE%29+AND+fixVersion+%7E+%22{{site.CFE_manuals_version}}.*%22)

On this page (below) we will only mention a subset of known issues, which are very severe or noticeable, which we'd like to communicate with users.

## 3.26.0 Hub package installation hangs with cf-remote on Ubuntu

**Ticket:** [CFE-4528](https://northerntech.atlassian.net/browse/CFE-4528)

The `dpkg -i` command seems to cause cf-remote to hang forever in this particular case.
Issue is specific to 3.26.0, hub, and Ubuntu.
Client packages work, other OSes work, and previous versions also work.
We will fix this issue before 3.27.0 LTS.

**Workarounds:**

- If you've already ran the command and see it hanging:
  - Open another terminal and connect with SSH.
  - Look at the installation log (`sudo less /var/log/CFEngineInstall.log`).
  - You should see that installation completed successfully and there is a setup code.
  - Interrupt (Ctrl-c) the hanging `cf-remote` command.
  - Run bootstrap manually.
  - Use the setup code from the install log to set up Mission Portal for the first time.
- Otherwise, just download and install CFEngine manually, without cf-remote, or use a different platform, like RHEL, for your hub.
