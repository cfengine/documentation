#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.156.0/hugo_0.156.0_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "223c970129a33e59df948be9dd0d5287be9937df980487011970f1d536efe865  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
