#!/bin/bash

set -ex

# All of these commands are executed by the jenkins user.

sudo apt-get install -y -qq wget ca-certificates

# some of packages below depend on tzdata. Installing it without DEBIAN_FRONTEND=noninteractive causes it to ask where in the world are you, interrupting the build process
DEBIAN_FRONTEND=noninteractive sudo --preserve-env=DEBIAN_FRONTEND apt-get install -y -qq tzdata

# Python is needed for our pre and post processing scripts.

sudo apt-get install -y -qq python3
