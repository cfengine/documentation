#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.151.0/hugo_0.151.0_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "1fea04cb0d467a90981f9837ad6ab171fe27e0d6d1bdd5fa4ba54a3464c90114  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
