#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.147.8/hugo_0.147.8_Linux-64bit.tar.gz -O hugo.tar.gz
echo "df3b6f9d62c49c15b0d4760fb4d2b8b30d49b32e0d20aa8a1e7382f51aa0ff13  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
