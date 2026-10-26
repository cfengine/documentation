#!/bin/bash

# go and git are needed by Hugo to download modules (llms-txt)
sudo apt-get update -qq
sudo apt-get install -y -qq golang-1.26-go git
sudo ln -sf /usr/lib/go-1.26/bin/go /usr/local/bin/go

wget -nv https://github.com/gohugoio/hugo/releases/download/v0.168.0/hugo_0.168.0_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "fada83ad56bb27ed4cb7dd81590303bdac16140f944ac4e66fc248117e2d5594  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
