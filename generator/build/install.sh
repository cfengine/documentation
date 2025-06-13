#!/bin/bash

set -ex

# All of these commands are executed by the jenkins user.

sudo apt-get install -y curl gnupg2 wget git

# some of packages below depend on tzdata. Installing it without DEBIAN_FRONTEND=noninteractive causes it to ask where in the world are you, interrupting the build process
DEBIAN_FRONTEND=noninteractive sudo --preserve-env=DEBIAN_FRONTEND apt-get install -y tzdata

# Docslave specifics
# These packages are needed as a dependency of the nokogiri ruby gem (which in turn is a dependency of the sanitize ruby gem).

sudo apt-get install -y libxslt-dev libxml2-dev

# Python is needed for our pre and post processing scripts.

sudo apt-get install -y python3

# These packages are needed to satisfy rvm requirements.

# hint: to figure out rvm requirements, comment this line and watch output of `rvm install ... ruby`.
# To make script stop at that command, change --autolibs argument to read-fail.
# Also you likely will want to exclude 'libssl1.0-dev' since it's and openssl 1.0 library, which is not shipped on modern distros.
sudo apt-get install -y gawk g++ gcc autoconf automake bison libc6-dev libffi-dev libgdbm-dev libncurses5-dev libsqlite3-dev libtool libyaml-dev make pkg-config sqlite3 zlib1g-dev libgmp-dev libreadline-dev

sudo apt-get install -y default-jdk

curl -sL https://deb.nodesource.com/setup_16.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt-get install -y nodejs
node --version
npm --version
