#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.152.2/hugo_0.152.2_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "52b6eda6c00f4449d96f0cbfd7300e834c26179c4fe68e0510ef566db52dba04  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
