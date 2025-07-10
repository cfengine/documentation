def cfengine_repos = ['core', 'enterprise', 'nova', 'masterfiles']

/* comments OK?
TODO:
- [ ] provide a way of specifying refs in other repos, like a coordinated multi-pr build
*/
pipeline {
  options { buildDiscarder(logRotator(numToKeepStr: '3')) }
  agent {
    label 'CONTAINERS'
  }

  stages {
    stage('Checkout repositories') {
      steps {
        script {
          cfengine_repos.each { repo ->
            stage("Checkout ${repo}") {
              git branch: "master",
              credentialsId: 'autobuild',
              url: "git@github.com:cfengine/${repo}"
            }
          }
        }
      }
    }
  }
}
