pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        sh 'mkdir -p core'
        dir('core')
        {
          git branch: "master",
          credentialsId: 'autobuild',
          url: 'git@github.com:cfengine/core'
        }
      }
    }
  }
}
