#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.162.1/hugo_0.162.1_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "4bfcdb092d0306586f1b72e5687787ead053faab2d71f09951d3c5fecde66873  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
