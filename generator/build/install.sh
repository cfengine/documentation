#!/bin/bash

set -ex

# All of these commands are executed by the jenkins user.
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install -y curl gnupg2 wget git

# some of packages below depend on tzdata. Installing it without DEBIAN_FRONTEND=noninteractive causes it to ask where 
# in the world are you, interrupting the build process
DEBIAN_FRONTEND=noninteractive sudo --preserve-env=DEBIAN_FRONTEND apt-get install -y tzdata

# Docslave specifics
# These packages are needed as a dependency of the nokogiri ruby gem (which in turn is a dependency of the sanitize ruby gem).


sudo apt-get install -y libxslt-dev libxml2-dev ruby ruby-dev rubygems build-essential python3

echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Python is needed for our pre and post processing scripts.
sudo apt-get install -y python3

sudo apt-get install -y gawk g++ gcc autoconf automake bison libc6-dev libffi-dev libgdbm-dev libncurses5-dev libsqlite3-dev  \ 
                        libtool libyaml-dev make pkg-config sqlite3 zlib1g-dev libgmp-dev libreadline-dev

sudo apt-get install -y python3-pygments

sudo apt-get install -y default-jdk


sudo gem install jekyll jekyll_asset_pipeline jekyll-paginatege read_yaml closure-compiler bundler closure-compiler  \
                 yui-compressor  albino execjs redcarpet uglifier sanitize


curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash - && sudo apt-get install -y nodejs

$(which node) --version
$(which npm) --version
$(which jekyll) --version
$(which ruby) --version

