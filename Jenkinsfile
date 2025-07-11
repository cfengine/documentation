pipeline {
  agent any

  stages {
    stage('Check environment'){
      steps {
        sh 'env'
script {
                if (env.CHANGE_ID) {
echo pullRequest.title
echo pullRequest.body
                }
}
      }
    }
  }
}
