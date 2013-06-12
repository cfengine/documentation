---
layout: default
title: Version Control
categories: [Manuals, Version Control]
published: true
sorting: 30
alias: version-control.html
tags: [manuals, version control, git, subversion]
---

CFEngine is policy is stored in `/var/cfengine/masterfiles` on the policy server. It is common that this directory is backed by a version control system (VCS), such as git or subversion. In this document we will focus on git, but CFEngine is VCS agnostic.

## Repository synchronization

When `/var/cfengine/masterfiles` is backed by VCS, it may be useful to have an agent policy that periodically checks the VCS server for the latest version fetches any updates.

After installing CFEngine on the policy server, before bootstrapping the agent to itself, we create a git clone of our masterfiles.

`git clone git@github.com:upstream/masterfiles.git /var/cfengine/masterfiles/`

The following policy uses git pull with the --ff-only flag to avoid potentially bad merges. This assumes that no development takes place in `/var/cfengine/masterfiles` itself.


```
bundle agent vcs_update
{
commands:
  "/usr/bin/git"
    args => "pull --ff-only origin master",
    contain => masterfiles_contain;
}

body contain masterfiles_contain
{
  chdir => "/var/cfengine/masterfiles";
}
```

## Commit hooks

Commit hooks are scripts that are run when a respository is updated. We can use a hook to notify a policy developer if an update causes a syntax error. While the agent on the policy server should not copy from `/var/cfengine/masterfiles` to `/var/cfengine/inputs` if the new policy does not pass validation, it can nevertheless be helpful to employ VCS commit hooks. A hook needs to be installed on the VCS server. Git and subversion stores its hooks under directories `.git/hooks` and `hooks` respectively in their respository directories on the server.

### Example git update hook

We can use a git update hook to prevent a change from being made unless it passes syntax checking. The idea is to check out the revision in a temporary directory and run `cf-promises` on it. Here is an example hook.

```
#!/bin/sh                                                                                                                                                                

# --- Command line                                                                                                                                                       
REF_NAME="$1"
OLD_REV="$2"
NEW_REV="$3"

GIT=/usr/bin/git
TAR=/bin/tar
CF_PROMISES=/home/a10021/Source/core/cf-promises/cf-promises
TMP_CHECKOUT_DIR=/tmp/cfengine-post-commit-syntax-check/
MAIN_POLICY_FILE=promises.cf

echo "Creating temporary checkout directory at ${TMP_CHECKOUT_DIR}"
mkdir -p ${TMP_CHECKOUT_DIR}

echo "Clearing potential data in temporary checkout directory"
rm -rf ${TMP_CHECKOUT_DIR}/*
rm -rf ${TMP_CHECKOUT_DIR}/.svn

echo "Checking out revision ${REV} from ${REPOS} to file://${TMP_CHECKOUT_DIR}"
${GIT} archive ${NEW_REV} | tar -x -C ${TMP_CHECKOUT_DIR}
if [ $? -ne 0 ]; then
    echo "Error checking out repository to temporary folder during post-commit syntax checking!" >&2
    return 1
fi


echo "Running cf-promises -cf on ${TMP_CHECKOUT_DIR}/${MAIN_POLICY_FILE}"
${CF_PROMISES} -cf ${TMP_CHECKOUT_DIR}/${MAIN_POLICY_FILE}

if [ $? -ne 0 ]; then
    echo "There were policy errors in pushed revision ${REV}" >&2
    return 1
else
    echo "Policy check completed successfully!"
    return 0
fi

```

### Example subversion post-commit hook

For subversion, the principle is essentially the same. Note that for a post-commit hook the check is run after update, so the repository may be left with a syntax error, but the committer is notifed.

```
#!/bin/sh

REPOS="$1"
REV="$2"

SVN=/usr/bin/svn
CF_PROMISES=/home/a10021/Source/core/cf-promises/cf-promises
TMP_CHECKOUT_DIR=/tmp/cfengine-post-commit-syntax-check/
MAIN_POLICY_FILE=trunk/promises.cf

echo "Creating temporary checkout directory at ${TMP_CHECKOUT_DIR}"
mkdir -p ${TMP_CHECKOUT_DIR}

echo "Clearing potential data in temporary checkout directory"
rm -rf ${TMP_CHECKOUT_DIR}/*
rm -rf ${TMP_CHECKOUT_DIR}/.svn

echo "Checking out revision ${REV} from ${REPOS} to file://${TMP_CHECKOUT_DIR}"
${SVN} co -r ${REV} file://${REPOS} ${TMP_CHECKOUT_DIR}
if [ $? -ne 0 ]; then
    echo "Error checking out repository to temporary folder during post-commit syntax checking!" >&2
    return 1
fi


echo "Running cf-promises -cf on ${TMP_CHECKOUT_DIR}/${MAIN_POLICY_FILE}"
${CF_PROMISES} -cf ${TMP_CHECKOUT_DIR}/${MAIN_POLICY_FILE}

if [ $? -ne 0 ]; then
    echo "There were policy errors in committed revision ${REV}" >&2
    return 1
else
    echo "Policy check completed successfully!"
    return 0
fi
```