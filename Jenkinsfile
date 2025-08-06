pipeline {
  agent { label 'CONTAINERS' }

  stages {
    stage('Check environment'){
      steps {
        sh "env"
        sh "echo env CHANGE_ID: ${env.CHANGE_ID}"
        sh "echo \"${pullRequest.title}\" > pull-request-title"
        sh "echo \"${pullRequest.body}\" > pull-request-body"
        sh "pwd; ls; whoami; uname -a"
withCredentials([sshUserPrivateKey(credentialsId:"autobuild", keyFileVariable: "key")]) {
        sh 'GIT_SSH_COMMAND = "ssh -i $key"'
        sh "git clone git@github.com:cfengine/nova --depth 1"
      }
}
    }
  }
}
