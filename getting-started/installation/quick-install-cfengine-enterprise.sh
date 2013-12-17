#!/bin/bash
component="$1"
package_prefix="cfengine-nova"
package_version="3.5.2-1"
package_source="http://s3.amazonaws.com/cfengine.packages/Enterprise-$package_version"
TEST=false

function prepare_wget {
  if [ -e "/etc/debian_version" ]; then
    dpkg -l | grep -q wget || apt-get -y install wget
    return
  fi
  if [ -e "/etc/redhat-release" ]; then
    rpm -qa | grep -q wget || yum -y install wget
    return
  fi
  if [ -e "/etc/SuSE-release" ]; then
    rpm -qa | grep -q wget || zypper --non-interactive install vim
    return
  fi
}


function usage {
    echo "$0 [hub|client]"
    exit 1
}

if [[ $# != 1 ]]; then
    echo "Missing required argument"
    usage
fi

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
      if grep "Red Hat" /etc/redhat-release; then
          DISTRO="RedHatEnterpriseServer"
          RELEASE="$(awk '/release/ {print $7}' /etc/redhat-release)"
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


  echo "Sorry I don't know what distro this is"
}

function get_package_arch {
# Determine the architecture name used in the package name
if [ $uname_arch == "unknown" ]; then
    uname_arch=$(uname -m)
fi
case $1 in
    deb) 
        # Enterprise and community deb packages use different naming conventions
        # enterprise hub uses x86_64 and community and enterprise clients use amd64
        if [ $uname_arch == "x86_64" ]; then
            if [ $component == "client" ]; then
              package_arch="$uname_arch"
            else
              package_arch="amd64"
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

function construct_enterprise_package_name_deb {
  if [ "$component" == "hub" ]; then
    package_name="$package_prefix"-hub_"$package_version"_"$package_arch".deb
  elif [ "$component" == "client" ]; then
    package_name="$package_prefix"_"$package_version"_"$package_arch".deb
  else
      echo "Unknown component: $component"
      usage
  fi
}

function construct_enterprise_package_name_rpm {
  if [ "$component" == "hub" ]; then
    package_name="$package_prefix"-hub-"$package_version"."$package_arch".rpm
  elif [ "$component" == "client" ]; then
    package_name="$package_prefix"-"$package_version"."$package_arch".rpm
  else
      echo "Unknown component: $component"
      usage
  fi
}

function construct_package_name {
case $DISTRO in
    Ubuntu)
        get_package_arch deb 
        construct_enterprise_package_name_deb
        ;;
    Debian)
        get_package_arch deb 
        construct_enterprise_package_name_deb
        ;;
    RedHatEnterpriseServer)
        get_package_arch rpm
        construct_enterprise_package_name_rpm
        ;;
    SUSE)
        get_package_arch rpm
        construct_enterprise_package_name_rpm
        ;;
    CentOS)
        get_package_arch rpm
        construct_enterprise_package_name_rpm
        ;;
    *)
        echo "Sorry I don't know the package name format on this system"
        exit 1
        ;;
esac
}

function fetch_package {
    $run_prefix wget $package_source/Community-$package_version/$package_name
}

function fetch_enterprise_hub_package {
if [ "$uname_arch" != "x86_64" ]; then
  echo "Sorry, enterprise hubs require a 64 bit machine"
  exit 1
fi

case $DISTRO in
    Ubuntu)
        folder="ubuntu-$RELEASE-$uname_arch"
        ;;
    Debian)
          folder="debian-6.0-x86_64"
        ;;
    RedHatEnterpriseServer)
        if [ $(expr $RELEASE \< 6.0) ]; then
            folder="rhel-5.4-$uname_arch"
        elif [ $(expr $RELEASE \= 6.0) ]; then
            folder="rhel-6.0-$uname_arch"
        elif [ $(expr $RELEASE \> 6.0) ]; then
            folder="rhel-6.0-$uname_arch"
        else
            echo "Sorry I dont know how to fetch $DISTRO $RELEASE"
        fi
        ;;
    CentOS)
        if [ $(expr $RELEASE \< 6.0) ]; then
            folder="rhel-5.4-$uname_arch"
        elif [ $(expr $RELEASE \= 6.0) ]; then
            folder="rhel-6.0-$uname_arch"
        elif [ $(expr $RELEASE \> 6.0) ]; then
            folder="rhel-6.0-$uname_arch"
        else
            echo "Sorry I dont know how to fetch $DISTRO $RELEASE"
        fi
        ;;
    SUSE)
        folder="sles-11.1-$uname_arch"
        ;;
    *)
        echo "Sorry I dont know how to fetch the $component package for $DISTRO $RELEASE"
        exit 1
esac
  $run_prefix wget $package_source/$component/$folder/$package_name
}

function fetch_enterprise_client_package {
case $DISTRO in
    Ubuntu)
        folder="agent_deb_$uname_arch"
        ;;
    Debian)
        folder="agent_deb_$uname_arch"
        ;;
    RedHatEnterpriseServer)
        folder="agent_rpm_$uname_arch"
        ;;
    SUSE)
        folder="agent_rpm_$uname_arch"
        ;;
    CentOS)
        folder="agent_rpm_$uname_arch"
        ;;
     *)
        echo "Sorry I dont know how to fetch the $component package for $DISTRO $RELEASE"
        exit 1
       ;;
esac
  $run_prefix wget $package_source/$component/$folder/$package_name
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
    SUSE)
        $run_prefix rpm -i $package_name && thanks
        ;;
    CentOS)
        $run_prefix rpm -i $package_name && thanks
        ;;
    *)
        echo "Sorry I don't know how to install $package_name on $DISTRO $RELEASE"
        exit 1
esac
}

function cleanup {
    $run_prefix rm -f $package_name
}

prepare_wget
detect_distro
construct_package_name
if [ "$component" == "hub" ]; then
  fetch_enterprise_hub_package
else
  fetch_enterprise_client_package
fi
install_package
cleanup

