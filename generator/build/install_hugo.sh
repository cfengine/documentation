#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.154.2/hugo_0.154.2_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "6473b8fe2ff0a5b13af217eb780f3a03aa34d43ba4506314c6156f11074a418d  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
