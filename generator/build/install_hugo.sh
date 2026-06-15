#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.163.2/hugo_0.163.2_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "eae3a1b94930de1f1dcb89fd5e885c33bba7fda1bae93412999956c945f9d5b0  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
