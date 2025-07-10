def cfengine_repos = ['core', 'enterprise', 'nova', 'masterfiles']

/* comments OK?
TODO:
- [ ] provide a way of specifying refs in other repos, like a coordinated multi-pr build
*/
properties([buildDiscarder(logRotator(numToKeepStr: '3'))])

// clean workspace on Success (specify all the OTHER cases as false)
cleanWs cleanWhenAborted: false, cleanWhenFailure: false, cleanWhenNotBuilt: false, cleanWhenUnstable: false
node('CONTAINERS') {
  dir('documentation') {
    checkout scm
  }

    stage('Checkout repositories') {
          // Note that stages created this way are NOT available for "Restart from Stage" in jenkins UI
          cfengine_repos.each { repo ->
            stage("Checkout ${repo}") {
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
    stage('See what cloned') {
        sh 'pwd'
        sh 'whoami'
        sh 'ls -la'
        sh 'cd documentation; git log --oneline | head -n1'
    }
    stage('Build') {
        // hard code for now, won't actually publish yet so not too big of a deal
        withEnv([
'BRANCH=master',
'PACKAGE_JOB=testing-pr'
]) {
        sh 'bash -x documentation/generator/build/run.sh'
    }
}
}
