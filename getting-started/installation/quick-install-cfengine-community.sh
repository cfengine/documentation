#!/bin/bash
package_prefix="cfengine-community"
package_version="3.5.2-1"
package_source="http://s3.amazonaws.com/cfengine.packages"
TEST=false


DISTRO=""
ARCH=""
uname_arch=$(uname -i)

lsb_release="/usr/bin/lsb_release"

if $TEST; then
    run_prefix="/bin/echo "
else
    run_prefix=""
fi


function detect_distro {
  if [ -e "$lsb_release" ]; then
      DISTRO=$($lsb_release --short --id)
      RELEASE=$($lsb_release --short --release)
      return 
  fi
  if [ -e "/etc/redhat-release" ]; then 
      if grep "CentOS" /etc/redhat-release; then
          DISTRO="$(awk '/release/ {print $1}' /etc/redhat-release)"
          RELEASE="$(awk '/release/ {print $3}' /etc/redhat-release)"
          return
      fi
  fi
  if [ -e "/etc/SuSE-release" ]; then
      if grep "Enterprise Server 11" /etc/SuSE-release; then
          DISTRO="SUSE"
          RELEASE=$(awk '/VERSION/ {print $3}' /etc/SuSE-release).$(awk '/PATCHLEVEL/ {print $3}' /etc/SuSE-release)
          return
      fi
  fi
  if [ -e "/etc/debian_version" ]; then
      DISTRO="Debian"
      RELEASE=$(cat /etc/debian_version)
      return
  fi


  echo "Sorry I was unable to determine the distro"
  exit 1
}

function get_package_arch {
# Determine the architecture name used in the package name
case $1 in
    deb) 
        if [ $uname_arch == "x86_64" ]; then
          package_arch="amd64"
	elif [ $uname_arch == "unknown" ]; then
	  uname_arch=$(uname -m)
	  if [ $uname_arch == "x86_64" ]; then
	    package_arch="amd64"
	  else
	    package_arch="i386" 
	  fi
        else
          package_arch="i386"
        fi
        ;;

    rpm)
        if [ $uname_arch == "x86_64" ]; then
          package_arch="$uname_arch"
        else
          package_arch="i386"
        fi
        ;;
    *)
        echo "Sorry I don't know about this platforms package architecture"
        ;;
esac
}

function construct_package_name {
case $DISTRO in
    Ubuntu)
        get_package_arch deb 
        package_name="$package_prefix"_"$package_version"_"$package_arch".deb
        ;;
    Debian)
        get_package_arch deb 
        package_name="$package_prefix"_"$package_version"_"$package_arch".deb
        ;;
    RedHatEnterpriseServer)
        get_package_arch rpm
        package_name="$package_prefix"-"$package_version"."$package_arch".rpm
        ;;
    CentOS)
        get_package_arch rpm
        package_name="$package_prefix"-"$package_version"."$package_arch".rpm
        ;;
    SUSE)
        get_package_arch rpm
        package_name="$package_prefix"-"$package_version"."$package_arch".rpm
        ;;
    *)
        echo "Sorry I don't know the package name format on this system"
        ;;
esac
}

function fetch_package {
    $run_prefix wget $package_source/Community-$package_version/$package_name
}

function thanks {
echo "Ready to bootstrap using /var/cfengine/bin/cf-agent --bootstrap <ip>"
}

function install_package {
case $DISTRO in
    Ubuntu)
        $run_prefix dpkg -i $package_name && thanks
        ;;
    Debian)
        $run_prefix dpkg -i $package_name && thanks
        ;;
    RedHatEnterpriseServer)
        $run_prefix rpm -i $package_name && thanks
        ;;
    CentOS)
        $run_prefix rpm -i $package_name && thanks
        ;;
    SUSE)
        $run_prefix rpm -i $package_name && thanks
        ;;
    *)
        echo "Sorry I dont know how to install $package_name on $DISTRO $RELEASE"
        exit 1
esac
}

function cleanup {
    $run_prefix rm -f $package_name
}

detect_distro
construct_package_name
fetch_package
install_package
cleanup
