#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.155.3/hugo_0.155.3_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "6c280fb8aae09b0dea9a83dbb6c3429bf7fd683839b454bd00c4e21f60440c45  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
