#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.163.1/hugo_0.163.1_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "13d9ba5c3b2fca17a630f0251a8f41e97875a23a4b85b14ae8991d4282dae53f  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
