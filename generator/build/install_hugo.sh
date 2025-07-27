#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.148.1/hugo_0.148.1_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "69f787720e7bad18f13dce9d7c494f4a908bfdffbfdea483e6df529268aeec37  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
