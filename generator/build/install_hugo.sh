#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.155.2/hugo_0.155.2_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "a680e2c6dd0e2244c237c85b549cb8697778cd068c84af1f7b0d9422827a554c  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
