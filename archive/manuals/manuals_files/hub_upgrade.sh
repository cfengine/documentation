#!/bin/sh

# hub_upgrade.sh
# version 0.0.9
#
#
# Created by Nakarin Phooripoom on 11/29/12.
# Copyright 2012 CFEngine AS. All rights reserved.
#
# Description:
#  Script to Upgrade CFEngine 3 Enterprise HUB from version 2.1.x/2.2.x to 3.0.0
# 

# Simple howto
if [ $# -eq 0 ] ; then
 echo ""
 echo $"Usage: `basename $0` [target_version] [directory contains cfengine-nova and cfengine-nova-expansion RPM/DEB]"
 echo "-> [target_version] in 3-digit format: 3.0.0"
 echo "-> [directory] in full path without an ending slash: /path/to/the/packages/directory"
 echo "For Example:" 
 echo "-> $ sh $(basename $0) 3.0.0 /tmp  <---- without an ending \"/\" (slash)"
 exit 0
fi

# Simple check
if [ -f /etc/debian_version ]; then
 # case 1 
 ls $2/cfengine-nova*$1*deb > /dev/null 2>&1
 if [ $? = "2" ]; then
  echo "No valid CFEngine $1 packages in place. Upgrade process terminated."
  exit 0
 fi
 # case 2
 dpkg -l cfengine-nova | grep $1 > /dev/null 2>&1
 if [ $? = "0" ]; then
  echo "CFEngine 3 Enterprise version $1 is already installed. Do Nothing."
  exit 0
 fi
fi


if [ -f /etc/redhat-release -o -f /etc/SuSE-release ]; then
 # case 1
 ls $2/cfengine-nova*$1*rpm > /dev/null 2>&1
 if [ $? = "2" ]; then
  echo "No valid CFEngine $1 packages in place. Upgrade process terminated."
  exit 0
 fi
 # case 2
 rpm -q cfengine-nova | grep $1 > /dev/null 2>&1
 if [ $? = "0" ]; then
  echo "CFEngine 3 Enterprise version $1 is already installed. Do Nothing."
  exit 0
 fi
fi

# Script start from this point
# Define necessary variables
WORKDIR=/var/cfengine
if [ -f /etc/debian_version -a -f /usr/bin/lsb_release ]; then
 OS=$(lsb_release -i | cut -f2)
 VER=$(lsb_release -r | cut -f2)
 ARCH=$(uname -m)
 DOCROOT=/var/www
elif [ -f /etc/redhat-release ]; then
 OS=$(cat /etc/redhat-release | cut -d' ' -f1)
 VER=$(cat /etc/redhat-release | cut -d' ' -f3)
 ARCH=$(uname -m)
 DOCROOT=/var/www/html
elif [ -f /etc/SuSE-release ]; then
 OS=$(cat /etc/SuSE-release | grep SUSE)
 VER=$(cat /etc/SuSE-release | grep SUSE | cut -d' ' -f5)
 ARCH=$(uname -m)
 DOCROOT=/srv/www/htdocs
fi

# confirmation
echo "*****  YOU ARE RUNNING A SCRIPT TO UPGRADE CFENGINE FROM NOVA 2.1.x OR ENTERPRISE 2.2.x TO ENTERPRISE 3.0.0  *****"
echo "*****         THIS MIGHT CAUSE UNEXPECTED CHANGES TO POLICY, ALWAYS TEST IN A LAB ENVIRONMENT FIRST          *****"
echo "*****                               DO YOU WANT TO CONTINUE? PLEASE TYPE [yes/no]                            *****"
echo -n "ANSWER: "
read XXX
case $XXX in
yes)
 clear
 echo "**** ARE YOU REALLY SURE? PLEASE RE-CONFIRM. CFENGINE IS NOT RESPONSIBLE FOR CHANGES MADE BY THIS SCRIPT *****"
 echo "**** PLEASE TYPE [Yes, I am.] IF YOU STILL WISH TO PROCEED."
 echo -n "ANSWER: "
 read YYY
 case $YYY in
 "Yes, I am.")
  echo ""
#  echo "Nice to see you trusting in us. Let's continue. :-D"
#  echo ""
  ;;
 *)
  echo ""
  echo "-> Please type the exact content between the brackets. Upgrade process terminated."
  exit 0
 ;;
 esac
 ;;
no)
 echo ""
 echo "-> Please contact your sales representative if you would like an engineer"
 echo "   on site for the upgrade. Script terminiated."
 exit 0
 ;;
*)
 echo ""
 echo "-> UNABLE to COMPILE. Skip the whole process."
 exit 0
 ;;
esac

# Display a bit infomation about the HUB
echo "***** YOU ARE RUNNING *****"
echo ""
echo "Distrubution: $OS"
echo "Architecture: $ARCH"
echo "Version:      $VER"

# Alert for more info
sleep 1
echo ""
echo "***** START THE UPGRADE *****"

# Kill all CFEngine processes to ensure that the upgrade will be absolutely find
sleep 1
echo ""
echo "-> Ensure that no CFEngine and MongoDB processes are running."
echo "/etc/init.d/cfengine3 stop"
if [ -f /etc/init.d/cfengine3 ]; then
 /etc/init.d/cfengine3 stop
fi

# Backup is really important. Do it first.
sleep 1
echo ""
echo "-> Backup your current masterfiles directory. ($WORKDIR/masterfiles_$(date +%T_%F))"
 cp -r $WORKDIR/masterfiles $WORKDIR/masterfiles_$(date +%T_%F)

# Upgrade CFEngine binaries and Mission Portal
sleep 1
echo ""
echo "-> Upgrade cfengine-nova and cfengine-nova-expansion packages."
if [ -f /etc/redhat-release -o -f /etc/SuSE-release ]; then
 rpm -Fvh $2/cfengine-nova*$1*.rpm
 rpm -q cfengine-nova > /dev/null 2>&1
 if [ $? = "1" ]; then
  echo ""
  echo "***** TROUBLE - You don't have CFEngine 3 Enterprise installed. *****"
  echo "*****                 SCRIPT TERMINATED                         *****"
  exit 0
 fi
elif [ -f /etc/debian_version ]; then
 dpkg --install $2/cfengine-nova_*$1*.deb $2/cfengine-nova-*$1*.deb
fi

# Create folders to support a new structure
sleep 1
echo ""
for i in cfe_internal controls services libraries; do
 if [ ! -d $WORKDIR/masterfiles/$i ]; then
  echo "-> Create $WORKDIR/masterfiles/$i"
  mkdir -p $WORKDIR/masterfiles/$i
 fi
done

# Take care of CFE_* prefix files. Replace the current ones.
# (masterfiles/promises.cf need to be adjusted. See more in policy editing section.)
sleep 1
echo ""
echo "-> Copy CFE_ prefixed files to $WORKDIR/masterfiles/cfe_internal"
if [ -d $WORKDIR/masterfiles/cfe_internal ]; then
 cp -vf $WORKDIR/share/NovaBase/cfe_internal/CFE_* $WORKDIR/masterfiles/cfe_internal
 echo ""
 echo "-> Remove old CFE_ prefixed files"
 rm -f $WORKDIR/masterfiles/CFE_*
else
 cp -vf $WORKDIR/share/NovaBase/cfe_internal/CFE_* $WORKDIR/masterfiles
fi

# Copy example_use_goals.cf to cfe_internal directory
if [ -d $WORKDIR/masterfiles/cfe_internal ]; then
 sleep 1
 echo ""
 echo "-> Copy example_use_goals.cf to $WORKDIR/share/NovaBase/cfe_internal"
 cp -vf $WORKDIR/share/NovaBase/cfe_internal/example_use_goals.cf $WORKDIR/masterfiles/cfe_internal
fi

# Update CFEngine standard library
# (masterfiles/promises.cf need to be adjusted. See more in policy editing section.)
sleep 1
echo ""
echo "-> Copy the latest CFEngine standard library to masterfiles."
if [ -d $WORKDIR/masterfiles/libraries ]; then
 cp -vf $WORKDIR/share/NovaBase/libraries/cfengine_stdlib.cf $WORKDIR/masterfiles/libraries
 echo "-> Remove the old CFEngine standard library"
 rm -f $WORKDIR/masterfiles/cfengine_stdlib.cf
else
 cp -vf $WORKDIR/share/NovaBase/libraries/cfengine_stdlib.cf $WORKDIR/masterfiles
fi

# Move file_change.cf to masterfiles/services
# (masterfiles/promises.cf needs to be adjusted. See more in policy editing section.)
if [ -f $WORKDIR/masterfiles/file_change.cf -a -d $WORKDIR/masterfiles/services ]; then
 sleep 1
 echo ""
 echo "-> Move file_change.cf to $WORKDIR/masterfiles/services"
 mv $WORKDIR/masterfiles/file_change.cf $WORKDIR/masterfiles/services/file_change.cf
fi 


# Update Company knowledge. The contents in the file were changed a lot.
# It is pretty hard to use "sed" for all.
sleep 1
echo ""
echo "-> Copy the latest Company Knowledge file to masterfiles"
 cp -vf $WORKDIR/share/NovaBase/company_knowledge.cf $WORKDIR/masterfiles

# Introduce cf-sketch run file (cf-sketch-runfile.cf)
sleep 1
echo ""
echo "-> Copy cf-sketch run file to masterfiles"
 cp -vf $WORKDIR/share/NovaBase/cf-sketch-runfile.cf $WORKDIR/masterfiles

# Correct up cf-twin for cf-execd to be functioning correctly
sleep 1
echo ""
echo "-> Ensure $WORKDIR/bin/cf-twin is in good shape."
 cp -vf $WORKDIR/bin/cf-agent $WORKDIR/bin/cf-twin

# Remove MongoDB lock file. Just in case.
sleep 1
echo ""
echo "-> Remove MongoDB lock file."
 rm -f $WORKDIR/state/mongod.lock

# Wipe out a previous Mission Portal to avoid conflict
sleep 1
echo ""
echo "-> Reset default DOCROOT directory. ($DOCROOT)"
 rm -rf $DOCROOT/*

# This is a fun path. If the customers did change anything in failsafe/update,
# then it would be pretty hard to automatically correct up policy. We are trying
# the best to automate as much as possible.
sleep 1
echo ""
echo -n "-> Have you added custom promises to /var/cfengine/masterfiles/failsafe.cf or /var/cfengine/masterfiles/update.cf? Please type [yes/no]: "
read ANS
case $ANS in
yes)
 echo ""
 echo "-> Prepare a new mongod.conf only."
 mkdir -p $WORKDIR/masterfiles/failsafe
 cp -vf $WORKDIR/share/NovaBase/failsafe/mongod.conf $WORKDIR/masterfiles/failsafe
 UPDATE=1
 ;;
no)
 echo ""
 echo "-> Copy new FAILSAFE files to masterfiles."
 cp -rv $WORKDIR/share/NovaBase/failsafe $WORKDIR/masterfiles
 rm -f $WORKDIR/masterfiles/failsafe.cf
 mv $WORKDIR/masterfiles/failsafe/*.cf $WORKDIR/masterfiles
 UPDATE=0
 ;;
*)
 echo ""
 echo "-> UNABLE to COMPILE. Skip the whole process."
 exit 0
 ;;
esac

# File modification: many names were changed. We need to correct them up.
sleep 1
echo ""
echo "***** START POLICY EDITING *****"
echo ""

# Move CFE_knowledge.cf to cfe_internal/CFE_knowledge.cf
grep "cfe_internal/CFE_knowledge.cf" $WORKDIR/masterfiles/promises.cf > /dev/null 2>&1
if [ $? = "1" ]; then
 echo "-> Patch $WORKDIR/masterfiles/promises.cf for CFE_knowledge.cf"
 sed -i 's/"CFE_knowledge.cf",/"cfe_internal\/CFE_knowledge.cf",/g' $WORKDIR/masterfiles/promises.cf
fi
# Move CFE_hub_specific.cf to cfe_internal/CFE_hub_specific.cf
grep "cfe_internal/CFE_hub_specific.cf" $WORKDIR/masterfiles/promises.cf > /dev/null 2>&1
if [ $? = "1" ]; then
 echo "-> Patch $WORKDIR/masterfiles/promises.cf for CFE_hub_specific.cf"
 sed -i 's/"CFE_hub_specific.cf",/"cfe_internal\/CFE_hub_specific.cf",/g' $WORKDIR/masterfiles/promises.cf
fi
# Move CFE_cfengine.cf to cfe_internal/CFE_cfengine.cf
grep "cfe_internal/CFE_cfengine.cf" $WORKDIR/masterfiles/promises.cf > /dev/null 2>&1
if [ $? = "1" ]; then
 echo "-> Patch $WORKDIR/masterfiles/promises.cf for CFE_cfengine.cf"
 sed -i 's/"CFE_cfengine.cf",/"cfe_internal\/CFE_cfengine.cf",/g' $WORKDIR/masterfiles/promises.cf
fi

# Move cfengine_stdlib.cf to libraries/cfengine_stdlib.cf
grep "libraries/cfengine_stdlib.cf" $WORKDIR/masterfiles/promises.cf > /dev/null 2>&1
if [ $? = "1" ]; then
 sleep 1
 echo ""
 echo "-> Patch $WORKDIR/masterfiles/promises.cf for cfengine_stdlib.cf"
 sed -i 's/"cfengine_stdlib.cf",/"libraries\/cfengine_stdlib.cf",/g' $WORKDIR/masterfiles/promises.cf
fi

# Move file_change.cf to services/file_change.cf
grep "services/file_change.cf" $WORKDIR/masterfiles/promises.cf > /dev/null 2>&1
if [ $? = "1" ]; then
 sleep 1
 echo ""
 echo "-> Patch $WORKDIR/masterfiles/promises.cf for file_change.cf"
 sed -i 's/"file_change.cf",/"services\/file_change.cf",/g' $WORKDIR/masterfiles/promises.cf
fi

# Add example_use_goals.cf to cfe_internal/example_use_goals.cf
grep "cfe_internal/example_use_goals.cf" $WORKDIR/masterfiles/promises.cf > /dev/null 2>&1
if [ $? = "1" ]; then
 echo "-> Add example_use_goals.cf to $WORKDIR/masterfiles/promises.cf"
 sed -i 's/"cfe_internal\/CFE_knowledge.cf",/"cfe_internal\/CFE_knowledge.cf",\n                    "cfe_internal\/example_use_goals.cf",/g' $WORKDIR/masterfiles/promises.cf
fi

# Rename cfengine_management to cfe_internal_management
grep cfe_internal_management $WORKDIR/masterfiles/promises.cf > /dev/null 2>&1
if [ $? = "1" ]; then
 sleep 1
 echo ""
 echo "-> Found cfengine_management in $WORKDIR/masterfiles/promises.cf"
 echo "   Rename it to cfe_internal_management"
 sed -i 's/cfengine_management/cfe_internal_management/g' $WORKDIR/masterfiles/promises.cf
fi

# Add cfe_internal_hub_vars to promises.cf
grep cfe_internal_hub_vars $WORKDIR/masterfiles/promises.cf > /dev/null 2>&1
if [ $? = "1" ]; then
 sleep 1
 echo ""
 echo "-> Did not find cfe_internal_hub_vars in $WORKDIR/masterfiles/promises.cf"
 echo "   Add it to the bundlesequence."
 sed -i 's/"def",/"def",\n                    "cfe_internal_hub_vars",/g' $WORKDIR/masterfiles/promises.cf
fi

# Add cfsketch_run to promises.cf
grep cfsketch_run $WORKDIR/masterfiles/promises.cf > /dev/null 2>&1
if [ $? = "1" ]; then
 sleep 1
 echo ""
 echo "-> Did not find cfsketch_run in $WORKDIR/masterfiles/promises.cf"
 echo "   Add it to the bundlesequence."
 sed -i 's/"cfe_internal_hub_vars",/"cfe_internal_hub_vars",\n                    "cfsketch_run",/g' $WORKDIR/masterfiles/promises.cf
fi

# Add cf-sketch-runfile.cf to promises.cf
grep cf-sketch-runfile.cf $WORKDIR/masterfiles/promises.cf > /dev/null 2>&1
if [ $? = "1" ]; then
 sleep 1
 echo ""
 echo "-> Did not find cf-sketch-runfile.cf in $WORKDIR/masterfiles/promises.cf"
 echo "   Add it to the inputs section."
 sed -i 's/"libraries\/cfengine_stdlib.cf",/"libraries\/cfengine_stdlib.cf",\n                    "cf-sketch-runfile.cf",/g' $WORKDIR/masterfiles/promises.cf
fi

# Rename goal_1 to goal_infosec
grep goal_infosec $WORKDIR/masterfiles/promises.cf > /dev/null 2>&1
if [ $? = "1" ]; then
 sleep 1
 echo ""
 echo "-> Found goal_1 in $WORKDIR/masterfiles/promises.cf"
 echo "   Rename it to goal_infosec"
 sed -i 's/goal_1/goal_infosec/g' $WORKDIR/masterfiles/promises.cf
fi

# Rename goal_2 to goal_compliance
grep goal_compliance $WORKDIR/masterfiles/promises.cf > /dev/null 2>&1
if [ $? = "1" ]; then
 sleep 1
 echo ""
 echo "-> Found goal_2 in $WORKDIR/masterfiles/promises.cf"
 echo "   Rename it to goal_compliance"
 sed -i 's/goal_2/goal_compliance/g' $WORKDIR/masterfiles/promises.cf
fi

# If we copy share/NovaBase/failsafe then update.cf has to be removed and add
# update_bins.cf and update_policy.cf instead
if [ $UPDATE = "0" ]; then
 sleep 1
 echo ""
 echo "-> Found update.cf in $WORKDIR/masterfiles/promises.cf"
 echo "   change it to update_policy.cf and update_bins.cf"
 sed -i 's/"update.cf",/"update_bins.cf",\n                    "update_policy.cf",/g' $WORKDIR/masterfiles/promises.cf
fi

# Since depends_on is activated in Core 3.4.0, having it there in policy is slightly
# to make things getting worse. Remove it.
sleep 1
echo ""
echo "-> Remove depends_on from known CFEngine Policy files."
echo "   (file_change.cf and update.cf)" 
sed -i '/depends_on/d' $WORKDIR/masterfiles/services/file_change.cf
sed -i '/depends_on/d' $WORKDIR/masterfiles/update.cf

# Remove commercial_customer class from promises.cf because we don't need it now.
sleep 1
echo ""
echo "-> Remove commercial_customer class from $WORKDIR/masterfiles/promises.cf"
sed -i '/commercial_customer::/d' $WORKDIR/masterfiles/promises.cf

# Remove nova_edition and constellation_editon class from promises.cf 
# because we don't need it now.
sleep 1
echo ""
echo "-> Remove nova and constellation classes from $WORKDIR/masterfiles/promises.cf"
sed -i '/nova_edition.*::/d' $WORKDIR/masterfiles/promises.cf

# Remove garbage_collection from promises.cf. We have one in CFE_cfengine.cf
sleep 1
echo ""
echo "-> Remove the garbage_collection from $WORKDIR/masterfiles/promises.cf (now included in CFE_cfengine.cf)"
sed -i '/maintenance.*goal_3/d' $WORKDIR/masterfiles/promises.cf
sed -i '/comment.*rotation.*Nova/d' $WORKDIR/masterfiles/promises.cf
sed -i '/usebundle.*garbage_collection/d' $WORKDIR/masterfiles/promises.cf

# Alert for more info
sleep 1
echo ""
echo "***** FINISHED POLICY EDITING *****"

# Just info to finish up the process
if [ $UPDATE = "0" ]; then
 sleep 1
 echo ""
 $WORKDIR/bin/cf-promises -V
 echo ""
 echo "-> Please run "
 echo " $ $WORKDIR/bin/cf-promises -f $WORKDIR/masterfiles/failsafe.cf"
 echo "   and "
 echo " $ $WORKDIR/bin/cf-promises -f $WORKDIR/masterfiles/promises.cf"
 echo "   for syntax verification. (No complaints means verification passed.)"
 echo ""
 echo "-> If there are no errors,"
 echo "-> Please run "
 echo " $ $WORKDIR/bin/cf-agent -f $WORKDIR/masterfiles/failsafe.cf -IK"
 echo "   to finish the $1 upgrade."
fi

if [ $UPDATE = "1" ]; then
 sleep 1
 echo ""
 echo "-> Your HUB is partially upgraded."
 echo "-> Please synchronize contents from $WORKDIR/share/NovaBase/failsafe"
 echo "   to your failsafe/update files manually."
 echo "-> $WORKDIR/bin/mongod might not be started gracefully."
 echo "-> Feel free to register a ticket if you need any support."
 echo "   here: https://cfengine.com/otrs/customer.pl"
fi

sleep 1
echo ""
echo "***** DONE FOR NOW. ENJOY CFENGINE ENTERPRISE 3.0.0! *****"
