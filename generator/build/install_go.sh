#!/bin/bash
# Go (and git) are needed by Hugo to download modules (llms-txt).
# Install the upstream Go tarball rather than a distro package, since
# golang-1.26-go is not available on the Ubuntu 22.04 build image.
set -e

GO_VERSION=1.26.10
GO_SHA256=ccfe7ae822d2c2f41f4fe7c956199967a4dac22d0ee0d2b2bfdb440aab3b20c5

sudo apt-get install -y -qq git

wget -nv "https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz" -O go.tar.gz
echo "${GO_SHA256}  go.tar.gz" | sha256sum -c
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go.tar.gz
sudo ln -sf /usr/local/go/bin/go /usr/local/bin/go
rm go.tar.gz
go version
