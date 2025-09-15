#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.150.0/hugo_0.150.0_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "62ff18d68f0bec73118d7dade9ffcfef8c174d6560469a838dcbdfe92ecd0a65  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
