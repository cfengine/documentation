pipeline {
  agent { label 'CONTAINERS' }
  parameters {
    string(name: "CORE_REV", defaultValue: 'master', description: 'used for changelog, examples. Use NUMBER or "pull/NUMBER/merge" for pull request (it\'s merged version, THIS DOESN\'T MERGE THE PR) or "pull/NUMBER/head" to run the tests on the non-merged code. Special syntax \'tag:SOME_TAG\' can be used to use a tag as a revision.')
  }
  options {
    checkoutToSubdirectory('documentation')
  }
  environment {
    REPOS = "core enterprise nova masterfiles northerntechhq/nt-docs"
    BASE_BRANCH = "master"
    PACKAGE_JOB = "cf-remote"
    PACKAGE_UPLOAD_DIRECTORY = "n/a"
    PACKAGE_BUILD = "n/a"
  }
  stages {
    stage('Environment check') {
      steps {
        sh 'env'
        sh 'uname -a; pwd; whoami; ls'
      }
    }
    stage('Clean workspace') {
      steps {
        sh 'for r in $REPOS; do rm -rf "$(basename "$r")"; done'
      }
    }
    stage('Checkout repositories'){
      steps {
        sh "echo \"${pullRequest.title}\" > pull-request-title"
        sh "echo \"${pullRequest.body}\" > pull-request-body"
        sh "pwd; ls; whoami; uname -a"
        sh "curl -O https://raw.githubusercontent.com/craigcomstock/buildscripts/refs/heads/ENT-12581/ci/create-revisions-file.sh"
        sh "chmod u+x ./create-revisions-file.sh"
        sh "./create-revisions-file.sh"
        sh "cat revisions"
        sh "curl -O https://gitlab.com/Northern.tech/OpenSource/GODS/-/raw/master/parallel_git_rev_fetch.sh"
        sh "chmod u+x ./parallel_git_rev_fetch.sh"

        withCredentials([sshUserPrivateKey(credentialsId:"autobuild", keyFileVariable: "key")]) {
          sh 'export GIT_SSH_COMMAND="ssh -i $key"; ./parallel_git_rev_fetch.sh revisions'
        }
        sh 'BRANCH=${DOCS_BRANCH} bash -x documentation/generator/build/run.sh'
      }
    }
  }
  post {
    cleanup {
      sh 'for r in $REPOS; do rm -rf "$(basename "$r")"; done'
    }
  }
}
