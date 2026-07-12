#!/bin/bash

wget -nv https://github.com/gohugoio/hugo/releases/download/v0.164.0/hugo_0.164.0_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "d9c8b17285ea4ec004d9f814273ea910f2051ce02c284993fd1f91ba455ae50d  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
