#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.155.1/hugo_0.155.1_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "6056ac054f7a159c8c95c8d5cf4f5ee255f27c3aada9b302bc3197d94305d8a7  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
