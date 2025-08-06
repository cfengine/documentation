pipeline {
  agent any

  stages {
    stage('Check environment'){
      steps {
script {
  if (env.CHANGE_ID) {
    echo pullRequest
  }
}
        sh "env"
        sh "echo env CHANGE_ID: ${env.CHANGE_ID}"
        sh "echo PR title: \"${pullRequest.title}\""
        sh "echo \"${pullRequest}\""
        sh "echo PR body: \"${pullRequest.body}\" | tee pull-request.data"
      }
    }
  }
}
