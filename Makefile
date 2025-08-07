.PHONY: check build
check:
	shellcheck generator/build/*.sh

build:
	
# wget https://gitlab.com/Northern.tech/OpenSource/GODS/-/raw/master/parallel_git_rev_fetch.sh
chmod u+x ./parallel_git_rev_fetch.sh
