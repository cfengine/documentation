#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.160.1/hugo_0.160.1_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "2f72fefa6ce944907f74c36c35abcaa306cdd22e64647a9ee5b328fc0bfb67be  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
