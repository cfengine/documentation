---
layout: default
title: Installing Policy Builder
sorting: 10
---

Policy Builder runs on macOS, Windows and Linux.
It includes everything it needs to build and check policy, so you don't need CFEngine installed on your computer.
Some features use other software, listed at the end of this page.

## Downloading and installing

Download Policy Builder from [cfengine.com/policy-builder](https://cfengine.com/policy-builder/#install).
The page offers the file for your computer, lists the files for the other systems, and gives the command that installs each Linux package.

The first time you open Policy Builder on macOS, macOS asks to confirm opening an app downloaded from the internet: click **Open**.

## Optional dependencies

- **Docker**, for [test environments][Test environments]: Docker Desktop, Colima, OrbStack or Docker Engine. Policy Builder finds a running Docker on its own.
- **git**, for keeping a project in version control and [deploying it to a hub][Deploying from Policy Builder] from a repository, and for creating a project on the **Master branch** masterfiles.
