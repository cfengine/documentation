pipeline {
  agent any

  stages {
    stage('Checkout core') {
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
    stage('Checkout nova') {
      steps {
        sh 'mkdir -p nova'
        dir('nova')
        {
          git branch: "master",
          credentialsId: 'autobuild',
          url: 'git@github.com:cfengine/nova'
        }
      }
    }
  }
}
