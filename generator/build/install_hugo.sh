#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.153.3/hugo_0.153.3_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "051a486ef6c7e5e9a05da9d83161d65ba1423f25b10e06af2f47f009bb8d5c1c  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
