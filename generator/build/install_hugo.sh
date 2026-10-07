#!/bin/bash

wget -nv https://github.com/gohugoio/hugo/releases/download/v0.167.0/hugo_0.167.0_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "4d84519b9f619e6d4c3fb45a50157abeabeb724f859c60605f44c23def6e1169  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
