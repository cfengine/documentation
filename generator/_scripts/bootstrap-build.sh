#/usr/bin/env bash

usage()
{
  echo "Usage: $0 [WORKDIR] [BRANCH]

    WORKDIR :: Defaults to current working directory
    BRANCH :: Branch to build (defaults to currently checked out branch in current working directory)"

}

case $# in
  "0" )
    echo "No arguments supplied"
    export WRKDIR="$(pwd)"
    BRANCH="$(git symbolic-ref --quiet --short HEAD)"
    ;;
  "1" )
    export WRKDIR=$1
    BRANCH="$(git symbolic-ref --short HEAD 2>/dev/null)"
    ;;
  "2" )
    export WRKDIR=$1
    BRANCH="$2"
    ;;
  * )
    echo "Error: Too many arguments"
    usage
    exit;;
esac

echo "Set WRKDIR=$WRKDIR"
echo "Set BRANCH=$BRANCH"

# Make Prepare masterfiles for policy docs
cd $WRKDIR/masterfiles
NO_CONFIGURE=1 ./autogen.sh

cd $WRKDIR

$WRKDIR/documentation-generator/_scripts/cfdoc_bootstrap.py $BRANCH 

# Prepare core for syntax docs
cd $WRKDIR/core
NO_CONFIGURE=1 ./autogen.sh
