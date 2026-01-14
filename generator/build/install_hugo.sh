#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.154.4/hugo_0.154.4_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "5e89a251fdd60b53ae11774650678fbc29547b1088a50289da2cd459d04aee00  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
