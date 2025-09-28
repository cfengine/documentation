#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.150.1/hugo_0.150.1_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "c91fbd9d47c87d604a831b9ea86aa54009a686485df5f8b1d39758fddd5e5b09  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
