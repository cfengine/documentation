#!/bin/bash
# A script to output name of latest (successful) nightly build, given URL where to look and partial build name

BUILDCACHE_URL="${1:?undefined}" # usually http://buildcache.cfengine.com/packages/testing-pr/
GREP_EXPR="${2:?undefined}" # usually jenkins-master-nightly-pipeline

curl --silent "$BUILDCACHE_URL" | grep "$GREP_EXPR" | sed -r 's_.*<a href="([^"/]*)/">.*_\1_' | sort -rn | while read -r build; do
	# $build is something like jenkins-master-nightly-pipeline-962
	# verify that it has a deb file
	url="$BUILDCACHE_URL/$build/PACKAGES_HUB_x86_64_linux_ubuntu_16/"
	if curl --silent "$url" | grep -qF '.deb</a>'; then
		echo "$build"
		break
	fi
done
