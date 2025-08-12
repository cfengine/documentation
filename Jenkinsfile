pipeline {
  agent { label 'CONTAINERS' }
  options {
    checkoutToSubdirectory('documentation')
  }
  environment {
    REPOS = "core enterprise nova masterfiles northerntechhq/nt-docs"
    BASE_BRANCH = "master"
  }
  stages {
    stage('Environment check') {
      steps {
        sh 'env'
        sh 'uname -a; pwd; whoami; ls'
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
      sh 'rm -rf $REPOS'
    }
  }
}
