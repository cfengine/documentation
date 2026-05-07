#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.161.1/hugo_0.161.1_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "fae28bf7909c1a42d1365b89d2e9e3d4194fbe5968ae0dd5504f562381018a1d  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
