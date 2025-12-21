#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.153.1/hugo_0.153.1_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "2f53a9369478405b3f6ad5fe49da207b13248a18272940ae3061f75e57df3cc7  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
