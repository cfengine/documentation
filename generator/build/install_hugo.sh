#!/bin/bash

wget -nv https://github.com/gohugoio/hugo/releases/download/v0.165.0/hugo_0.165.0_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "5c3a37a5450b3e386e5b75a87a790fea2d04a796d75e171216c80ef48a32b432  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
