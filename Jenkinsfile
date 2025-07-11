def repos = [
  'cfengine': [
    'core',
'enterprise',
'nova',
'masterfiles'
  ],
  'NorthernTechHQ': [
['nt-docs': 'main'],
  ]
]

rev_ref_description="Use NUMBER or 'pull/NUMBER/merge' for pull request (it's merged version, THIS DOESN'T MERGE THE PR) or 'pull/NUMBER/head' to run the tests on the non-merged code. Special syntax 'tag:SOME_TAG' can be used to use a tag as a revision."

/* comments OK?
TODO:
- [ ] provide a way of specifying refs in other repos, like a coordinated multi-pr build
*/
properties([
  buildDiscarder(logRotator(daysToKeepStr: '10'))
  parameters([
    string(name: 'CORE_REV', defaultValue: 'master'),
    string(name: 'NOVA_REV', defaultValue: 'master'),
    string(name: 'ENTERPRISE_REV', defaultValue: 'master'),
    string(name: 'MASTERFILES_REV', defaultValue: 'master'),
    string(name: 'DOCS_REV', defaultValue: 'master'),
    string(name: 'DOCS_BRANCH', defaultValue: 'master', description: 'Where to upload artifacts - to http://buildcache.cloud.cfengine.com/packages/build-documentation-$DOCS_BRANCH/ and https://docs.cfengine.com/docs/$DOCS_BRANCH/'),
    string(name: 'PACKAGE_JOB', defaultValue: 'testing-pr', description: 'where to take CFEngine HUB package from, a dir at http://buildcache.cloud.cfengine.com/packages/'),
    string(name: 'USE_NIGHTLIES_FOR', defaultValue: 'master', description: 'branch whose nightlies to use (master, 3.18.x, etc) - will be one of http://buildcache.cloud.cfengine.com/packages/testing-pr/jenkins-$USE_NIGHTLIES_FOR-nightly-pipeline-$NUMBER/'),
    string(name: 'NT_DOCS_REV', defaultValue: 'main', description: "${rev_ref_description}")
  ])
])

// clean workspace on Success (specify all the OTHER cases as false)

node('CONTAINERS') {
  dir('documentation') {
    checkout scm
  }

    stage('Checkout repositories') {
          // Note that stages created this way are NOT available for "Restart from Stage" in jenkins UI
repos.each { org ->
  println("organization is ${org.key}")
  org.value.each {  repo_data ->
    if (!(repo_data instanceof Map)) {
      repo_data=["${repo_data}": "master"]
    }
    repo_data.each{ repo, branch ->
      stage("Checkout ${repo}") {
        sh "mkdir -p ${repo}"
        dir ("${repo}")
        {
          git branch: "${branch}",
          credentialsId: 'autobuild',
          url: "git@github.com:${org.key}/${repo}"
        }
      }
    }
  }
}
} // for the stage
    stage('See what cloned') {
        sh 'pwd'
        sh 'whoami'
        sh 'ls -la'
        sh 'cd documentation; git log --oneline | head -n1'
    }
        withEnv([
'BRANCH=master',
'PACKAGE_JOB=testing-pr',
'PACKAGE_UPLOAD_DIRECTORY=jenkins-master-nightly-pipeline-152',
'PACKAGE_BUILD=1',
]) {
    stage('Build') {
        // hard code for now, won't actually publish yet so not too big of a deal
        sh 'bash -x documentation/generator/build/run.sh'
        archiveArtifacts artifacts: 'output/', fingerprint: true
    }
}
stage('Publish') {
  sshPublisher(publishers: [sshPublisherDesc(configName: 'buildcache.cloud.cfengine.com', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: '''set -x
export WRKDIR=`pwd`

mkdir -p upload
mkdir -p output

# find two tarballs
archive=`find upload -name \'cfengine-documentation-*.tar.gz\'`
tarball=`find upload -name packed-for-shipping.tar.gz`
echo "TARBALL: $tarball"
echo "ARCHIVE: $archive"

# unpack $tarball
cd `dirname $tarball`
tar zxvf packed-for-shipping.tar.gz
rm packed-for-shipping.tar.gz

# move $archive to the _site
mv $WRKDIR/$archive _site

ls -la
cd -

ls -la upload

# note: this triggers systemd job to AV-scan new files
# and move them to proper places
mv upload/* output
''', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: 'upload/$BUILD_TAG/build-documentation-$DOCS_BRANCH/$BUILD_TAG/', remoteDirectorySDF: false, removePrefix: '', sourceFiles: 'output/')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
}

stage('Clean workspace on Success') {
  cleanWs()
}
}
