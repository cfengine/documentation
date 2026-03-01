#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.157.0/hugo_0.157.0_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "78e0a49ec4fb32bfac70a06028297f79b3273fb7e2475eb7ffa1bc208f4c2552  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
