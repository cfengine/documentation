#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.160.0/hugo_0.160.0_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "2c49f8f153b159ac81ee76ddeb126e913fadf8d5376a9ddc479e8772766dbde3  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
