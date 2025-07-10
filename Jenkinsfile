def cfengine_repos = ['core', 'enterprise', 'nova', 'masterfiles']

/* comments OK?
TODO:
- [ ] provide a way of specifying refs in other repos, like a coordinated multi-pr build
*/
properties([buildBlocker(blockLevel: <object of type hudson.plugins.buildblocker.BuildBlockerProperty.BlockLevel>, blockingJobs: '', scanQueueFor: <object of type hudson.plugins.buildblocker.BuildBlockerProperty.QueueScanScope>, useBuildBlocker: false), buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '3')), [$class: 'RebuildSettings', autoRebuild: false, rebuildDisabled: false]])
node('CONTAINERS') {
  dir('documentation') {
    checkout scm
  }

    stage('Checkout repositories') {
      steps {
        script {
          // Note that stages created this way are NOT available for "Restart from Stage" in jenkins UI
          cfengine_repos.each { repo ->
            stage("Checkout ${repo}") {
              steps {
                sh "mkdir -p ${repo}"
                dir ("${repo}")
                {
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
    stage('See what cloned') {
      steps {
        sh 'pwd'
        sh 'whoami'
        sh 'ls -la'
        sh 'cd documentation; git log --oneline | head -n1'
      }
    }
    stage('Build') {
      steps {
        sh 'bash -x documentation/generator/build/run.sh'
// need env BRANCH=$DOCS_BRANCH
      }
    }
}
