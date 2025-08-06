pipeline {
  agent any

  stages {
    stage('Check environment'){
      steps {
script {
  if (env.CHANGE_ID) {
    echo pullRequest.getProperties()
  }
}
        sh "env"
        sh "echo env CHANGE_ID: ${env.CHANGE_ID}"
        sh "echo PR title: \"${pullRequest.title}\""
      }
    }
  }
}
