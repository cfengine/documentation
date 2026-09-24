#!/bin/bash

wget -nv https://github.com/gohugoio/hugo/releases/download/v0.166.0/hugo_0.166.0_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "45228f5a52eb118b0ca168068f01d7df0447314a24056f1d29667ed9fc368308  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
