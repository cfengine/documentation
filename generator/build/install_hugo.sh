#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.148.2/hugo_0.148.2_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "b2fbef73c965ff439ccca0bdf15d7ca64f59363d62916326e24d5552e6968aa3  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
