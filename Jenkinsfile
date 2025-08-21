pipeline {
  agent { label 'CONTAINERS' }
  environment {
    REPOS = "core enterprise nova masterfiles northerntechhq/nt-docs"
    PR_BASE = getPR_BASE()
    PACKAGE_JOB = "cf-remote"
    PACKAGE_UPLOAD_DIRECTORY = "n/a"
    PACKAGE_BUILD = "n/a"
  }
  parameters {
    string(name: "CORE_REV", defaultValue: '', description: 'used for changelog, examples. Use NUMBER or "pull/NUMBER/merge" for pull request (it\'s merged version, THIS DOESN\'T MERGE THE PR) or "pull/NUMBER/head" to build the docs with the non-merged code. Special syntax \'tag:SOME_TAG\' can be used to use a tag as a revision.')
    string(name: "NOVA_REV", defaultValue: '', description: 'used for changelog. Use NUMBER or "pull/NUMBER/merge" for pull request (it\'s merged version, THIS DOESN\'T MERGE THE PR) or "pull/NUMBER/head" to build the docs with the non-merged code. Special syntax \'tag:SOME_TAG\' can be used to use a tag as a revision.')
    string(name: "ENTERPRISE_REV", defaultValue: '', description: 'used for changelog. Use NUMBER or "pull/NUMBER/merge" for pull request (it\'s merged version, THIS DOESN\'T MERGE THE PR) or "pull/NUMBER/head" to build the docs with the non-merged code. Special syntax \'tag:SOME_TAG\' can be used to use a tag as a revision.')
    string(name: "MASTERFILES_REV", defaultValue: '', description: 'used to document masterfiles. Use NUMBER or "pull/NUMBER/merge" for pull request (it\'s merged version, THIS DOESN\'T MERGE THE PR) or "pull/NUMBER/head" to build the docs with the non-merged code. Special syntax \'tag:SOME_TAG\' can be used to use a tag as a revision.')
    string(name: "DOCS_REV", defaultValue: '', description: 'Use NUMBER or "pull/NUMBER/merge" for pull request (it\'s merged version, THIS DOESN\'T MERGE THE PR) or "pull/NUMBER/head" to build the docs with the non-merged code. Special syntax \'tag:SOME_TAG\' can be used to use a tag as a revision.')
    string(name: "NT_DOCS_REV", defaultValue: '', description: 'Use NUMBER or "pull/NUMBER/merge" for pull request (it\'s merged version, THIS DOESN\'T MERGE THE PR) or "pull/NUMBER/head" to build the docs with the non-merged code. Special syntax \'tag:SOME_TAG\' can be used to use a tag as a revision.')
    string(name: "DOCS_BRANCH", defaultValue: getDOCS_BRANCH(), description: 'Where to upload artifacts - to http://buildcache.cloud.cfengine.com/packages/build-documentation-$DOCS_BRANCH/ and https://docs.cfengine.com/docs/$DOCS_BRANCH/')
    string(name: "PACKAGE_JOB", defaultValue: 'cf-remote', description: 'where to get CFEngine HUB package from, either a dir at http://buildcache.cloud.cfengine.com/packages like testing-pr or a keyword cf-remote to use cf-remote download')
    string(name: "USE_NIGHTLIES_FOR", defaultValue: '', description: 'branch whose nightlies to use (master, 3.18.x, etc) - will be one of http://buildcache.cloud.cfengine.com/packages/testing-pr/jenkins-$USE_NIGHTLIES_FOR-nightly-pipeline-$NUMBER/')
  }
  options {
    checkoutToSubdirectory('documentation')
  }
  stages {
    stage('Environment check') {
      steps {
        sh 'env'
        sh 'whoami; pwd; ls'
        sh 'uname -a; cat /etc/os-release'
      }
    }
    // we clean FIRST and NOT at the end of the job so that we can replay various stages and have the build result from previous runs
    stage('Clean workspace') {
      steps {
        sh 'for r in $REPOS; do rm -rf "$(basename "$r")"; done'
      }
    }
    stage('Checkout repositories'){
      steps {
        script {
          if (env.CHANGE_ID) {
            sh "echo \"${pullRequest.title}\" > pull-request-title"
            sh "echo \"${pullRequest.body}\" > pull-request-body"
          }
        }
        sh "curl -O https://raw.githubusercontent.com/cfengine/buildscripts/refs/heads/master/ci/create-revisions-file.sh"
        sh "chmod u+x ./create-revisions-file.sh"
        sh "./create-revisions-file.sh"
        sh "cat revisions"
        sh "curl -O https://gitlab.com/Northern.tech/OpenSource/GODS/-/raw/master/parallel_git_rev_fetch.sh"
        sh "chmod u+x ./parallel_git_rev_fetch.sh"

        withCredentials([sshUserPrivateKey(credentialsId:"autobuild", keyFileVariable: "key")]) {
          sh 'export GIT_SSH_COMMAND="ssh -i $key"; ./parallel_git_rev_fetch.sh revisions'
        }
      }
    }
    stage('Build documentation') {
      steps {
        sh 'bash -x documentation/generator/build/run.sh'
      }
    }
    stage('Publish to buildcache') {
      steps {
        sshPublisher(
          // we must use alwaysPublishFromMaster: true because our CONTAINERS build hosts are not in the private network which has access to buildcache.cloud.cfengine.com
          alwaysPublishFromMaster: true,
          publishers: [
            sshPublisherDesc(
              configName: 'buildcache.cloud.cfengine.com',
              transfers: [
                sshTransfer(
                  cleanRemote: false,
                  excludes: '',
                  execCommand: '''
#!/usr/bin/env bash
set -x
WRKDIR="$(pwd)"
export WRKDIR

mkdir -p upload
mkdir -p output

# find two tarballs
archive="$(find upload -name "cfengine-documentation-*.tar.gz")"
tarball=$(findfind upload -name packed-for-shipping.tar.gz)
echo "TARBALL: $tarball"
echo "ARCHIVE: $archive"

# unpack $tarball
( # shubshell to change directories
  cd "$(dirname "$tarball")" || exit
  tar zxvf packed-for-shipping.tar.gz
  rm packed-for-shipping.tar.gz

  # move $archive to the _site
  mv "$WRKDIR/$archive" _site

  ls -la
)

ls -la upload

# note: this triggers systemd job to AV-scan new files
# and move them to proper places
mv upload/* output
''',
                  execTimeout: 120000,
                  flatten: false,
                  makeEmptyDirs: false,
                  noDefaultExcludes: false,
                  patternSeparator: '[, ]+',
                  remoteDirectory: 'upload/$BUILD_TAG/build-documentation-$DOCS_BRANCH/$BUILD_TAG/',
                  remoteDirectorySDF: false,
                  removePrefix: '',
                  sourceFiles: 'output/'
                ) // sshTransfer
               ], // transfers
               usePromotionTimestamp: false,
               useWorkspaceInPromotion: false,
               verbose: false
             ) // sshPublisherDesc
           ] // publishers
         ) // sshPublisher
      } // steps
    } // stage('Publish to buildcache')
  } // stages
}
def getDOCS_BRANCH() {
  if (env.CHANGE_ID) {
    return "${env.CHANGE_TARGET}"
  } else {
    return "${env.BRANCH_NAME}"
  }
}
def getPR_BASE() {
  if (env.CHANGE_ID) {
    return "${pullRequest.base}"
  } else {
    return ""
  }
}
