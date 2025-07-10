def cfengine_repos = ['core', 'enterprise', 'nova', 'masterfiles']
pipeline {
  options { buildDiscarder(logRotator(numToKeepStr: '3')) }
  agent {
    label 'CONTAINERS'
  }

  stages {
    script {
      cfengine_repos.each { repo ->
        stage("Checkout ${repo}") {
          git branch: "master",
          credentialsId: 'autobuild',
          url: 'git@github.com:cfengine/${repo}'
        }
      }
    }
  }
}
