#!/bin/bash

## RVM install for better ruby support https://rvm.io/rvm/install/
# install curl
sudo apt-get install curl

#download rvm
curl -#L https://get.rvm.io | bash -s stable --autolibs=3 --ruby

#add rvm to known  scripts
source /home/vagrant/.rvm/scripts/rvm

#install ruby
rvm install ruby-1.9.3

#switch to it and make default
rvm --default use 1.9.3


#install build essentials for make
sudo apt-get install build-essential


## Install Java  used for google closure
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java7-installer
## it will ask about license

#Jekyll
gem install jekyll


sudo apt-get install python-pygments

gem install jekyll-asset-pipeline
gem install closure-compiler
gem install yui-compressor
gem install redcarpet
gem install albino
gem install uglifier
gem install execjs
gem install sanitize


#if pandoc is used
gem install pandoc-ruby
gem install rdiscount