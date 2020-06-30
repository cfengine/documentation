---
layout: default
title: cfe_internal/
published: true
tags: [reference, cfe_internal, MPF]
---

This directory contains policy related to the internal control and functioning
of CFEngine and its various components. This directory provides policeis that
function at a higher level than those found in controls. For example, policy
related to log rotation can be found here, while settings related to access
control rules are organized under controls.

Note: Many of the tuneables specified in these files have been exposed in the
`def` bundle for use via the `augments` file. It is reccomended that direct
modifications to these files be limited in order to ease policy framework
upgrades. If you are altering one of these files, please consider making a pull
request to expose the tunable.

