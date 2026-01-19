#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.154.5/hugo_0.154.5_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "99b2f2f3db3e65bbbdb5840bc5158e271975b17d152904bb750ebae3c2a2aecc  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
