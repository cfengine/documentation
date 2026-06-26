#!/bin/sh

for repo in core nova enterprise masterfiles documentation; do
    git clone "git@github.com:cfengine/$repo.git"
done
