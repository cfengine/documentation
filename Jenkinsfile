pipeline {
  agent any

  stages {
    stage('Check environment'){
      steps {
        sh 'env'
        sh 'echo env CHANGE_ID: ${env.CHANGE_ID}'
        sh 'echo missing var: ${nope.NOPE}'
        sh 'echo PR title: ${pullRequest.title}'
        sh 'echo PR body: ${pullRequest.body}'
      }
    }
  }
}
