#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.159.1/hugo_0.159.1_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "297e18fa21e4796d80a3270c1234873f5a979cb9a329a0c93d9888a1b39f106c  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
