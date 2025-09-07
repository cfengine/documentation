#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.149.1/hugo_0.149.1_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "b68b6b9676947cd5147960b3fb9393262e4206f0b4c3ac3d29f6b730b4fa660b  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
