---
layout: default
title: Version Control
published: true
sorting: 60
tags: [manuals, writing policy, version control, git, subversion]
---

By default, CFEngine policy is published `/var/cfengine/masterfiles` on the policy
server. It is recommended that this directory be backed by a version control system
(VCS), such as Git or Subversion.

## Repository synchronization

CFEngine Enterprise ships with
[masterfiles-stage](https://github.com/cfengine/core/tree/master/contrib/masterfiles-stage),
tooling to assist with deploying policy from a version control system.

Enterprise users can configure automatic publication of policy from Mission Portal as described in [Policy Deployment] or by using the [VCS settings API][VCS settings API]. Community users can also install and use this tooling by following the
[installation instructions](https://github.com/cfengine/core/tree/master/contrib/masterfiles-stage#installation).

## Commit hooks

Commit hooks are scripts that are run when a repository is updated. We can use
a hook to notify a policy developer if an update causes a syntax error. While
the agent on the policy server should not copy from
`/var/cfengine/masterfiles` to `/var/cfengine/inputs` if the new policy does
not pass validation, it can nevertheless be helpful to employ VCS commit
hooks. A hook needs to be installed on the VCS server. Git and subversion
store their hooks on the server, under directories `.git/hooks` and `hooks`,
respectively.

### Example Git update hook

We can use a Git update hook to prevent a change from being made unless it
passes syntax checking. The idea is to check out the revision in a temporary
directory and run `cf-promises` on it. Here is an example hook.

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

For subversion, the principle is essentially the same. Note that for a
post-commit hook the check is run after update, so the repository may be left
with a syntax error, but the committer is notified.

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
