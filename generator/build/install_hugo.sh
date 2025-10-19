#!/bin/bash

wget https://github.com/gohugoio/hugo/releases/download/v0.151.2/hugo_0.151.2_Linux-64bit.tar.gz -O hugo.tar.gz
 echo "834c65d0cc27b5f1da54031e6827642b874ad7d33b72e20fd4c64749e213d593  hugo.tar.gz" | sha256sum -c
if [ $? -eq 1 ]; then
  exit 2
fi

tar -zxvf hugo.tar.gz
sudo mv hugo /usr/local/bin/hugo
sudo chmod +x /usr/local/bin/hugo
rm hugo.tar.gz
