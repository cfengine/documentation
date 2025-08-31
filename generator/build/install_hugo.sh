#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.149.0/hugo_0.149.0_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "102f5130c86d5f11043b6064025240f7587e4fcbda3e2232d50714c29eed808e  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
