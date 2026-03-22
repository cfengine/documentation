#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.158.0/hugo_0.158.0_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "d0d8f0735dccef76e900719a70102f269c418e010a02e3e0f9e206a208346e2f  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
