#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.163.3/hugo_0.163.3_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "ec422258f9a4ffc241de8707297e32311cd86fcc9b2813632617ff4d44935d91  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
