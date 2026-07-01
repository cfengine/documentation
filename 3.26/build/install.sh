#!/bin/bash

set -ex

# All of these commands are executed by the jenkins user.

sudo apt-get install -y curl gnupg2 wget git

# some of packages below depend on tzdata. Installing it without DEBIAN_FRONTEND=noninteractive causes it to ask where in the world are you, interrupting the build process
DEBIAN_FRONTEND=noninteractive sudo --preserve-env=DEBIAN_FRONTEND apt-get install -y tzdata

# Docslave specifics
# These packages are needed as a dependency of the nokogiri ruby gem (which in turn is a dependency of the sanitize ruby gem).

sudo apt-get install -y libxslt-dev libxml2-dev

# Python is needed for our pre and post processing scripts.

sudo apt-get install -y python3

# These packages are needed to satisfy rvm requirements.

# hint: to figure out rvm requirements, comment this line and watch output of `rvm install ... ruby`.
# To make script stop at that command, change --autolibs argument to read-fail.
# Also you likely will want to exclude 'libssl1.0-dev' since it's and openssl 1.0 library, which is not shipped on modern distros.
sudo apt-get install -y gawk g++ gcc autoconf automake bison libc6-dev libffi-dev libgdbm-dev libncurses5-dev libsqlite3-dev libtool libyaml-dev make pkg-config sqlite3 zlib1g-dev libgmp-dev libreadline-dev

# We currently use pygments for syntax highlighting. Jekyll 0.12.1 errors during install without this.

sudo apt-get install -y python3-pygments

# yui-compressor (ruby gem dependency) is written in java, so we need to install it.

sudo apt-get install -y default-jdk



## Install RVM and Ruby
## RVM helps us manage the ruby dependencies and ruby versions in a contained way.

# Install mpapis public key (might need `gpg2` and or `sudo`)
#keyserver=keys.gnupg.net
keyserver=keyserver.ubuntu.com
gpg2 --keyserver hkps://$keyserver --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB

echo "Downloading and installing Ruby Version Manager"
# Download the installer
curl -O https://raw.githubusercontent.com/rvm/rvm/master/binscripts/rvm-installer
curl -O https://raw.githubusercontent.com/rvm/rvm/master/binscripts/rvm-installer.asc

if gpg2 --verify rvm-installer.asc; then
    bash rvm-installer --autolibs=read-fail --ignore-dotfiles stable
else
    echo "Ruby Version Manager signature check fail."
    echo "Github is hacked, or trying to hack us, or our script is wrong. Aborting everything"
    exit 1
fi

# rvm commands are insane scripts which pollut output
# so instead of set -x we just echo each command ourselves
set +x
echo "+ source ~/.rvm/scripts/rvm"
# shellcheck disable=SC1090
source ~/.rvm/scripts/rvm

echo "+ rvm_rubygems_version=none rvm install --autolibs=read-only ruby-1.9.3-p551 -C --without-openssl"
rvm_rubygems_version=none rvm install --autolibs=read-only ruby-1.9.3-p551 -C --without-openssl

gem install jekyll --version 0.12.1
gem install jekyll-asset-pipeline --version 0.1.6
gem install closure-compiler --version 1.1.8
gem install yui-compressor --version 0.9.6
gem install albino --version 1.3.3
gem install execjs --version 1.4.0
gem install redcarpet --version 2.2.2
gem install uglifier --version 1.3.0
gem install sanitize --version 2.0.3

cat > /tmp/jekyll-0.12.1-cfengine.patch <<EOF
--- page.rb	2016-09-09 14:52:17.329751803 +0000
+++ page.rb.cfengine	2016-09-09 15:00:06.813929546 +0000
@@ -129,6 +129,26 @@
     # Returns nothing.
     def write(dest)
       path = destination(dest)
+
+    #+Caption: CFEngine Customization to Jekyll 0.12.1
+    #+BEGIN_SRC ruby
+    # Added by: Dmitry
+      if site.config['CFE_OUTPUT'] == true && site.config['CFE_DIR'] !=''
+        dest = File.join(@base, site.config['CFE_DIR'])
+           if (self.data['alias'] !=nil)
+              path = File.join(dest, CGI.unescape(self.data['alias']))
+           else
+              path = File.join(dest, CGI.unescape(self.url))
+           end
+        path = File.join(path, "index.html") if self.data['alias'] =~ /\/$/
+
+      else
+        # use standard  jekyll
+        path = destination(dest)
+      end
+    #+END_SRC
+
+
       FileUtils.mkdir_p(File.dirname(path))
       File.open(path, 'w') do |f|
         f.write(self.output)
EOF

cd /home/jenkins/.rvm/gems/ruby-1.9.3-p551/gems/jekyll-0.12.1/lib/jekyll/ 
patch -b page.rb < /tmp/jekyll-0.12.1-cfengine.patch

curl -sL https://deb.nodesource.com/setup_16.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt-get install -y nodejs
node --version
npm --version
