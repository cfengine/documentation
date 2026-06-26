Building docs in a container
============================

This set of scripts lets you build docs in a container.
Currently, it's aimed towards using buildah on oslo-dc.

Prereq
------

You will need to have the following repos checked out:

* core (used for changelog, examples)
* nova (used for changelog)
* enterprise (used for changelog)
* masterfiles (used to document masterfies)
* documentation
* documentation-generator (this repo)

Usage
-----

If you have buildah installed:

1. clone the above repos

2. export the following env variables:

	* `$BRANCH` - Branch that we're actually building artifacts for,
	  for example, 3.18, master, or pr

	* `$PACKAGE_JOB` - where to take CFEngine HUB package from,
	  a dir at http://buildcache.cloud.cfengine.com/packages/,
	  usually testing-pr

	* `$PACKAGE_UPLOAD_DIRECTORY` - where to take CFEngine HUB package from,
	  a dir at http://buildcache.cloud.cfengine.com/packages/testing-pr/,
	  for example, jenkins-master-nightly-pipeline-943

	* `$PACKAGE_BUILD` - RELEASE of the build to be downloaded, usually 1

3. `cd` to directory with all repos and run `run.sh` from this dir

Details
-------

To make a container, cd to this directory and run:

	buildah build-using-dockerfile -t docs .

or

	docker build --tag docs .

To run docs job in a container, run:

	c=$(buildah from -v $PWD:/nt docs)
	buildah run $c bash -x documentation-generator/build/main.sh $BRANCH $PACKAGE_JOB $PACKAGE_UPLOAD_DIRECTORY $PACKAGE_BUILD
	buildah run $c bash -x documentation-generator/_scripts/_publish.sh $BRANCH
	buildah rm $c

or

	docker run --rm -it -v $PWD:/nt docs bash -x documentation-generator/build/main.sh $BRANCH $PACKAGE_JOB $PACKAGE_UPLOAD_DIRECTORY $PACKAGE_BUILD
	docker run --rm -it -v $PWD:/nt docs bash -x documentation-generator/_scripts/_publish.sh $BRANCH
