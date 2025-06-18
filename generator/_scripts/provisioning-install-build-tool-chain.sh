#!/usr/bin/env bash

# This configuration is a copy from jenkins cloud init in https://ci.cfengine.com/configure

# Modifications
  #/usr/bin/env bash
  # usage

usage()
{
    echo "Usage: $0 [HOME]

    HOME :: Directory where gems are installed exists"

}

case $# in
    "0" )
        echo "No arguments supplied"
        HOME="$HOME"
        ;;
    "1" )
        HOME="$1"
        ;;
    * )
        echo "Error: Too many arguments"
        usage
        exit;;
esac

set -x

# All of these commands are executed by the jenkins user.

sudo apt-get update

# Docslave specifics
# These packages are needed as a dependency of the nokogiri ruby gem (which in turn is a dependency of the sanitize ruby gem).

sudo apt-get install -y libxslt-dev libxml2-dev

# Python is needed for our pre and post processing scripts.

sudo apt-get install -y python

# These packages are needed to satisfy rvm requirements.

sudo apt-get install -y libyaml-dev libsqlite3-dev sqlite3 autoconf libgmp-dev libgdbm-dev libncurses5-dev automake libtool bison pkg-config libffi-dev

# yui-compressor (ruby gem dependency) is written in java, so we need to install it.

sudo apt-get install -y default-jdk

sudo apt-get install -y libssl-dev zlib1g-dev

# For making cfenigne
sudo apt-get -qy install bison flex binutils build-essential fakeroot ntp dpkg-dev libpam0g-dev liblmdb-dev libpcre3-dev

