pipeline {
  agent { label 'CONTAINERS' }
  environment {
    REPOS = "core enterprise nova masterfiles"
    BASE_BRANCH = "master"
  }
  stages {
    stage('Check environment'){
      steps {
        sh "env"
        sh "echo env CHANGE_ID: ${env.CHANGE_ID}"
        sh "echo \"${pullRequest.title}\" > pull-request-title"
        sh "echo \"${pullRequest.body}\" > pull-request-body"
        sh "pwd; ls; whoami; uname -a"
sh "wget https://raw.githubusercontent.com/cfengine/buildscripts/refs/heads/master/ci/create-revisions-file.sh"
sh "./create-revisions-file.sh"
sh "wget https://gitlab.com/Northern.tech/OpenSource/GODS/-/raw/master/parallel_git_rev_fetch.sh"
sh "chmod u+x ./parallel_git_rev_fetch.sh"
withCredentials([sshUserPrivateKey(credentialsId:"autobuild", keyFileVariable: "key")]) {
  sh 'GIT_SSH_COMMAND="ssh -i $key" ./parallel_git_rev_fetch.sh revisions'
# problem: does rev_fetch expect to be at the "top-level dir?"
      }
  sh 'cd ..; BRANCH=${DOCS_BRANCH} bash -x documentation/generator/build/run.sh'
}
    }
  }
}

todo: publish-over-ssh
