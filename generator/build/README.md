# Building docs in a container

This set of scripts lets you build docs in a container.
Currently, it's aimed towards using buildah on oslo-dc.

## Prereq

You will need to have the following repos checked out:

- core (used for changelog, examples)
- nova (used for changelog)
- enterprise (used for changelog)
- masterfiles (used to document masterfies)
- nt-docs (Hugo theme and build scripts)
- documentation

## Usage

If you have buildah installed:

1. clone the above repos (run `clone.sh`)

2. export the following env variables:
   - `$BRANCH` - Branch that we're actually building artifacts for,
     for example, 3.18, master, or pr

   - `$PACKAGE_JOB` - where to take CFEngine HUB package from,
     a dir at http://buildcache.cloud.cfengine.com/packages/,
     usually `testing-pr`

   - `$PACKAGE_UPLOAD_DIRECTORY` - where to take CFEngine HUB package from,
     a dir at http://buildcache.cloud.cfengine.com/packages/testing-pr/,
     for example, `jenkins-master-nightly-pipeline-943`

   - `$PACKAGE_BUILD` - RELEASE of the build to be downloaded, usually 1

   - `$LTS_VERSION` - LTS version, only used when `$BRANCH` is `lts`

3. `cd` to directory with all repos and run `run.sh` from this dir

## Details

The whole build runs in the stages of the [Dockerfile](Dockerfile), with the
directory holding all the repos as build context:

1. `tools` - Ubuntu build environment, runs `main.sh` (hub package, syntax
   JSON, pre-processing, `_scripts/_run.sh` to prepare the Hugo site)
2. `hugo` - official Hugo image, runs `npm ci && npm run build:all`
3. `postprocess` - runs `_scripts/_postprocess.sh` and `_scripts/_publish.sh`
4. `output` - just the tarballs from `/nt/output`

`run.sh` runs the build with buildah. To run it by hand, from the directory with
all repos:

    buildah build-using-dockerfile \
      --file documentation/generator/build/Dockerfile \
      --ignorefile documentation/generator/build/Dockerfile.dockerignore \
      --build-arg BRANCH=$BRANCH \
      --build-arg PACKAGE_JOB=$PACKAGE_JOB \
      --build-arg PACKAGE_UPLOAD_DIRECTORY=$PACKAGE_UPLOAD_DIRECTORY \
      --build-arg PACKAGE_BUILD=$PACKAGE_BUILD \
      --output type=local,dest=output .

or with docker, which picks up `Dockerfile.dockerignore` by itself:

    docker build \
      --file documentation/generator/build/Dockerfile \
      --build-arg BRANCH=$BRANCH \
      --build-arg PACKAGE_JOB=$PACKAGE_JOB \
      --build-arg PACKAGE_UPLOAD_DIRECTORY=$PACKAGE_UPLOAD_DIRECTORY \
      --build-arg PACKAGE_BUILD=$PACKAGE_BUILD \
      --output type=local,dest=output .

The tarballs (`packed-for-shipping.tar.gz` and
`cfengine-documentation-$BRANCH.tar.gz`) end up in `./output`.

To build and serve the docs locally with docker, including cloning the repos,
use `build-locally.sh` in the root of the documentation repo.
