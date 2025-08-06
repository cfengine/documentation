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
        sh "make"
      }
    }
  }
}
