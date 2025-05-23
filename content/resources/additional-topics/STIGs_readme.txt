##########################################################################
#                          CFE RHEL5 STIGs v5r1                            #
##########################################################################

The Security Technical Implementation Guides (STIGs) is a methodology for standardized secure installation and maintenance of computer software and hardware created by the Defense Information Systems Agency (DISA) who provides configuration documents in support of the United States Department of Defense (DoD). 

This document contains technical guidance to "lock down" information systems/software that might otherwise be vulnerable to a malicious computer attack implemented based on a configuraton management tool called CFEngine 3. We strongly recommended to all users going through this document before executing the CFE policy in order to avoid any unpredicted bahaviours to your systems. The CFE policy is applied for "RHEL5" at a current stage.

Reference:
  UNIX Security Checklist Version 5, Release 1.30 - Updated August 26, 2011
  http://iase.disa.mil/stigs/os/unix/u_unix_checklist_v5r1-30_20110729.zip (See U_Unix-Sec3)

GEN000020
GEN000040
GEN000060
GEN000440
GEN000460
GEN000480
GEN000500
GEN000540
GEN000560
GEN000580
GEN000600
GEN000620
GEN000640
GEN000700
GEN000800
GEN000920
GEN000980
GEN001020
GEN001080
GEN001120
GEN001180
GEN001220
GEN001240
GEN001260
GEN001280
GEN001300
GEN001320
GEN001340
GEN001360
GEN001380
GEN001400
GEN001420
GEN001440
GEN001460
GEN001480
GEN001500
GEN001520
GEN001540
GEN001560
GEN001580
GEN001620
GEN001660
GEN001680
GEN001720
GEN001740
GEN001760
GEN001780
GEN001800
GEN001820
GEN001880
GEN001960
GEN002040
GEN002100
GEN002120
GEN002160
GEN002180
GEN002200
GEN002220
GEN002320
GEN002340
GEN002360
GEN002420
GEN002480
GEN002560
GEN002640
GEN002660
GEN002680
GEN002700
GEN002720
GEN002740
GEN002760
GEN002780
GEN002800
GEN002820
GEN002840
GEN002860
GEN002960
GEN002980
GEN003040
GEN003060
GEN003080
GEN003100
GEN003120
GEN003140
GEN003180
GEN003200
GEN003240
GEN003260
GEN003280
GEN003300
GEN003320
GEN003340
GEN003400
GEN003420
GEN003460
GEN003480
GEN003500
GEN003520
GEN003600
GEN003660
GEN003700
GEN003720
GEN003740
GEN003760
GEN003780
GEN003860
GEN003865
GEN003960
GEN003980
GEN004000
GEN004360
GEN004380
GEN004440
GEN004480
GEN004500
GEN004540
GEN004560
GEN004580
GEN004640
GEN004880
GEN004900
GEN004920
GEN004940
GEN005000
GEN005320
GEN005360
GEN005400
GEN005420
GEN005500
GEN005540
GEN005600
GEN005740
GEN005760
GEN006100
GEN006120
GEN006140
GEN006160
GEN006180
GEN006200
GEN006260
GEN006280
GEN006300
GEN006320
GEN006340
GEN006360
GEN006520
GEN006620
LNX00140
LNX00160
LNX00220
LNX00320
LNX00340
LNX00360
LNX00400
LNX00420
LNX00440
LNX00480
LNX00500
LNX00520
LNX00580
LNX00620
LNX00640
LNX00660

##############################################################################
#                                                                            #
# CAT I:                                                                     #
#   Vulnerabilities that allow an attacker immediate access into a machine,  #
#   allow superuser access, or bypass a firewall.                            #
#                                                                            #
##############################################################################

######################################
(GEN000560: CAT I) (Previously – G018)
######################################

The SA will ensure each account in the /etc/passwd file has a password assigned or is disabled in the password, shadow, or equivalent, file by disabling the password and/or by assigning a false shell in the password file.

vars:
   "shadow" -> { "GEN000560" }
      comment => "Read all contents in /etc/shadow for string manipulation later on",
       handle => "stig_vars_redhat_strings_from_etc_shadow",
       string => readfile("/etc/shadow", 99999);

   "shadow_list" -> { "GEN000560" } 
      comment => "Break strings into a list",
       handle => "stig_vars_redhat_list_from_etc_shadow",
        slist => splitstring("$(shadow)","[\n]",500);

methods:
   "UNIX STIG 3.2.1" -> { "GEN000560" }
        comment => "CAT I (Previously - G018) UNIX STIG: 3.2.1 Password Guidelines",
         handle => "stig_methods_redhat_unix_stig_3_2_1",
      usebundle => disable_accounts_without_passwd("$(shadow_list)");


bundle agent disable_accounts_without_passwd(string)
{
 classes:

   "name_ok" -> { "GEN000560" }
         comment => "Extract only a name field from an inputs string",
          handle => "disable_accounts_without_passwd_classes_name_field",
      expression => regextract(
                              "^[\w-]+",
                              "$(string)",
                              "name"
                              );

   "passwd_ok" -> { "GEN000560" }
         comment => "Extract only a passwd field from an inputs string",
          handle => "disable_accounts_without_passwd_classes_passwd_field",
      expression => regextract(
                              ":(.*?):",
                              "$(string)",
                              "passwd"
                              );

   "no_passwd" -> { "GEN000560" }
      comment => "Check if there is a password or not",
       handle => "disable_accounts_without_passwd_classes_no_passwd",
          not => regcmp(".*\$.*","$(passwd[1])");

#

 files:

  "/etc/passwd" -> { "GEN000560" }
        comment => "Set user shell /sbin/nologin",
         handle => "disable_accounts_without_passwd_files_etc_passwd",
      edit_line => set_user_field("$(name[0])","7","/sbin/nologin"),
             if => "no_passwd";
}

######################################
(GEN001400: CAT I) (Previously – G047)
######################################

The SA will ensure the owner of the /etc/passwd  and /etc/shadow files (or equivalent) is root.

 files:
   "/etc/passwd" -> { "GEN001080", "GEN001380", "GEN001400" }
        comment => "CAT I && III (Previously - G047, G048, G229) UNIX STIG: 3.3 Root Account, 3.4 File and Directory Controls",
         handle => "stig_files_redhat_set_root_shell",
          perms => mog("644", "root","root"),
      edit_line => set_user_field("root","7","/bin/bash");

   "/etc/shadow" -> { "GEN001400", "GEN001420" }
      comment => "CAT I (Previously - G047) UNIX STIG: 3.4 File and Directory Controls",
       handle => "stig_files_redhat_etc_shadow",
        perms => mog("400","root","root");

######################################
(GEN002160: CAT I) (Previously – G072) 
######################################

The SA will ensure no shell has the suid bit set.

 vars:
   "shell_files" -> { "GEN002160", "GEN002180", "GEN002200", "GEN002220" }
      comment => "List of login shells from /etc/shells",
       handle => "stig_vars_redhat_shell_files",
        slist => readstringlist("/etc/shells", "#.*", "[\n]", 10, 1000);

 files:
   "$(shell_files)" -> { "GEN002160", "GEN002180", "GEN002200", "GEN002220" }
      comment => "CAT I & II (Previously - G072, G073, G074, G075) UNIX STIG: 3.10 Shells",
       handle => "stig_files_redhat_shell_files",
        perms => mog("0755","root","root");

######################################
(GEN002040: CAT I) 
######################################

The SA will ensure .rhosts, .shosts, hosts.equiv, nor shosts.equiv are used, unless justified and documented with the IAO.

 vars:
   "hosts_related_files" -> { "GEN002040" }
      comment => "List of hosts related files",
       handle => "stig_vars_redhat_hosts_related_files",
        slist => {
                  "/root/.rhosts",
                  "/root/.shosts",
                  "/etc/hosts.equiv",
                 };

 classes:
   "do_$(hosts_related_files)" -> { "GEN002040" } 
      comment => "Check if the files are symlinks",
       handle => "stig_classes_redhat_hosts_related_files",
          not => islink("$(hosts_related_files)");

 files:
   "$(hosts_related_files)" -> { "GEN002040" }
         comment => "CAT I UNIX STIG: 3.9 Trusted System/System Access Control Files",
          handle => "stig_files_redhat_remove_and_symlink_hosts_related_files",
          delete => tidy,
       link_from => ln_s("/dev/null"),
              if => canonify("do_$(hosts_related_files)");

######################################
(GEN002700: CAT I) (Previously – G095)
######################################

The SA will ensure audit data files have permissions of 640, or more restrictive.

 files:
   "/etc/audit/audit.rules" -> { "GEN002660", "GEN002700", "GEN002720", "GEN002740", "GEN002760", "GEN002780", "GEN002800", "GEN002820", "GEN002840" }
             comment => "CAT I (Previously - G093, G095, G100-G106) UNIX STIG: 3.16 Audit Requirements",
              handle => "stig_files_redhat_etc_audit_audit_rules",
               perms => m("640"),
       edit_defaults => empty,
           edit_line => maintain_audit_rules;

   "$(system_log_files)" -> { "GEN001260", "GEN002700" }
           comment => "CAT I & II (Previously - G095) UNIX STIG: 3.4 File and Directory Controls, 3.16 Audit Requirements",
            handle => "stig_files_redhat_system_log_files",
      depth_search => recurse("inf"),
       file_select => exclude2("cron.*","audit"),
             perms => m("600");

bundle edit_line maintain_audit_rules
{
 insert_lines:
"# This file contains the auditctl rules that are loaded
# whenever the audit daemon is started via the initscripts.
# The rules are simply the parameters that would be passed
# to auditctl.

# GEN002660 GEN002720 GEN002740 GEN002760 GEN002780 GEN002800 GEN002820 GEN002840

# First rule - delete all
-D

# Enable auditing
-e 1

# Increase the buffers to survive stress events.
# Make this bigger for busy systems
-b 8192

# Failure of auditd causes a kernel panic
-f 2

# GEN002720 Logon/Logout
-w /bin/login -p x
-w /bin/logout -p x

# GEN002740 DAC permission changes
-a exit,always -S chmod -S chown -S chown32 -S fchmod -S fchown -S fchown32 -S lchown -S lchown32

# GEN002760 Unauthorized file access attempts
-a exit,always -F success=0 -S open -S mknod -S pipe -S mkdir -S creat -S truncate -S truncate64 -S ftruncate -S ftruncate64

# GEN002780 Privileged commands
-a exit,always -S chroot -S mount -S umount -S umount2 -S adjtimex -S kill
-w /usr/sbin/pwck
-w /bin/chgrp
-w /usr/bin/newgrp
-w /usr/sbin/groupadd
-w /usr/sbin/groupmod
-w /usr/sbin/groupdel
-w /usr/sbin/useradd
-w /usr/sbin/userdel
-w /usr/sbin/usermod
-w /usr/bin/chage
-w /usr/bin/setfacl
-w /usr/bin/chacl

# GEN002800 Deleting files
-a exit,always -S unlink -S rmdir

# GEN002820 System administration actions
# These two lines could be the cause of problems with filling audit logs and preventing system usage after installation
-w /var/log/audit/audit.log
-w /var/log/audit/audit[1-4].log
-w /var/log/messages
-w /var/log/lastlog
-w /var/log/faillog
-w /etc/audit/auditd.conf -p wa
-w /etc/audit/audit.rules -p wa
-w /etc/selinux/config -p wa
-w /etc/passwd -p wa
-w /etc/shadow -p wa
-w /etc/group  -p wa
-w /etc/ssh/sshd_config
-w /etc/pam.d
-w /etc/login.defs
-w /etc/rc.d/init.d
-w /etc/inittab -p wa
-w /var/run/utmp
-w /var/run/wtmp
-a exit,always -S acct -S reboot -S sched_setparam -S sched_setscheduler -S setdomainname -S setrlimit -S settimeofday -S stime -S swapon

# GEN002840 Security personnel actions
-a exit,always -S init_module -S delete_module -S setxattr -S lsetxattr -S fsetxattr -S removexattr -S lremovexattr -S fremovexattr
-w /bin/su" -> { "GEN002660", "GEN002720", "GEN002740", "GEN002760", "GEN002780", "GEN002800", "GEN002820", "GEN002840" }
       comment => "Ensure /etc/audit/audit.rules has good contents",
        handle => "maintain_audit_rules_insert_lines_gen002660_gen002720_gen002840",
   insert_type => "preserve_block";
}

######################################
(GEN004580: CAT I) (Previously – G647) 
######################################

The SA will ensure .forward files are not used.

 vars:
   "homes" -> { "GEN004580" }
      comment => "String source of all home directories on the system",
       handle => "stig_vars_redhat_homes_source",
       string => execresult("/bin/cut -d: -f6 /etc/passwd","noshell");

   "home_list" -> { "GEN004580" }
      comment => "List of all home directories on the system (ready to use)",
       handle => "sting_vars_redhat_home_list",
        slist => splitstring("$(homes)", "[\n]", 100);

 files:
   "$(home_list)/.forward" -> { "GEN004580" }
      comment => "CAT I (Previously - G647) UNIX STIG: 4.7 Sendmail or Equivalent",
       handle => "stig_files_redhat_home_dot_forward",
       delete => tidy;

######################################
(GEN004640: CAT I) (Previously – V126) 
######################################

The SA will ensure the decode entry is disabled (deleted or commented out) from the alias file.

 files:
   "/etc/aliases" -> { "GEN004360", "GEN004380", "GEN004640" }
        comment => "CAT I & II (Previously - G127, G128, V126) UNIX STIG: 4.7 Sendmail or Equivalent",
         handle => "stig_files_redhat_etc_aliases",
          perms => mog("644","root","root"),
      edit_line => comment_lines_matching("decode:\h+root","#"),
        classes => if_repaired("restart_aliases");

 commands:
  restart_aliases::
   "/usr/bin/newaliases" -> { "GEN004640" }
      comment => "CAT I (Previously - V126) 4.7 Sendmail or Equivalent",
       handle => "sting_commands_redhat_restart_aliases";

######################################
(GEN005500: CAT I) (Previously – G701)
######################################

The IAO and SA will ensure SSH Protocol version 1 is not used, nor will Protocol version 1 compatibility mode be used.

 files:
   "/etc/ssh/sshd_config" -> { "GEN001120", "GEN005500", "GEN005540" }
        comment => "CAT I & II (Previously - G500, G701) UNIX STIG: 3.3.1 Encrypted Root Access, 4.15 Secure Shell (SSH) and Equivalents",
         handle => "stig_files_redhat_etc_ssh_sshd_config",
      edit_line => maintain_sshd_config,
        classes => if_repaired("restart_sshd");

   "/etc/ssh/ssh_config" -> { "GEN005500" }
        comment => "CAT I UNIX STIG: 4.15 Secure Shell (SSH) and Equivalents",
         handle => "stig_files_redhat_etc_ssh_ssh_config",
      edit_line => maintain_ssh_config;

 commands:
  restart_sshd::  
   "/sbin/service sshd restart" -> { "GEN005500", "GEN005540" }
      comment => "CAT I & II (Previously - G701) UNIX STIG: 4.15 Secure Shell (SSH) and Equivalents",
       handle => "stig_commands_redhat_restart_sshd";

bundle edit_line maintain_sshd_config
{
 delete_lines:
  "^Banner.*" -> { "GEN005540" }
     comment => "Clear up an existing Banner.",
      handle => "maintain_sshd_config_delete_lines_gen005540";

  "^PermitRootLogin.*" -> { "GEN001120" }
     comment => "Clear up an existing PermitRootLogin",
      handle => "maintain_sshd_config_delete_lines_gen001120";

  "^Protocol.*" -> { "GEN005500" }
     comment => "Clear up an existing Protocol",
      handle => "maintain_sshd_config_delete_lines_gen005500";

 insert_lines:
  "Banner /etc/ssh/ssh_banner   # GEN005540" -> { "GEN005540" }
     comment => "Configure a warning banner.",
      handle => "maintain_sshd_config_insert_lines_gen005540";

  "PermitRootLogin no   # GEN001120" -> { "GEN001120" }
     comment => "Don't allow root to use SSH directly.",
      handle => "maintain_sshd_config_insert_lines_gen001120";

  "Protocol 2   # GEN005500" -> { "GEN005500" }
     comment => "Allow only SSH Protocol version 2",
      handle => "maintain_sshd_config_insert_lines_gen005500";
}

bundle edit_line maintain_ssh_config
{
 delete_lines:
  "^Ciphers.*" -> { "GEN005500" }
     comment => "Clear up an existing Ciphers",
      handle => "maintain_ssh_config_delete_lines_gen005500";

 insert_lines:
  "Ciphers aes256-cbc,aes192-cbc,blowfish-cbc,cast128-cbc,aes128-cbc,3des-cbc" -> { "GEN005500" }
     comment => "Allow only specific ciphers to be used",
      handle => "maintain_ssh_config_insert_lines_gen005500";
}

######################################
(GEN005000: CAT I) (Previously – G649)
######################################

The SA will implement the anonymous FTP account with a non-functional shell such as /bin/false.

-> See (GEN002640: CAT II) (Previously – G092)

#####################################
(LNX00140: CAT I) (Previously – L072)
#####################################

The SA will configure the GRUB Console Boot Loader with a MD5 encrypted password.

 files:
   "/boot/grub/menu.lst" -> { "LNX00140" }
        comment => "CAT I (Previously - L072) UNIX STIG: 12.4.1.1 Password Protecting the GRUB Console Boot Loader",
         handle => "stig_files_redhat_boot_grub_menu_lst",
      edit_line => maintain_grub;

bundle edit_line maintain_grub
{
 delete_lines:
  "^password.*" -> { "LNX00140" }
     comment => "Clear up an existing MD5 encrypted password.",
      handle => "maintain_grub_delete_lines_lnx00140";

 insert_lines:
  # default password is cfengine
  "password --md5 $(const.dollar)1$(const.dollar)8fI020$(const.dollar)YPs7MCo3A1ZkS7xagjYnb0   # LNX00140" -> { "LNX00140" }
     comment => "Use an MD5 encrypted password to GRUB",
      handle => "maintain_grub_insert_lines_lnx00140",
     location => before("^title.*");
}

#####################################
(LNX00320: CAT I) (Previously – L140)
#####################################

The SA will delete accounts that provide a special privilege such as shutdown and halt.

 vars:
   "accounts_to_delete" -> { "LNX00320", "LNX00340" }
      comment => "List of unnecessary accounts",
       handle => "stig_vars_redhat_accounts_to_delete",
        slist => {
                  "ftp", 
                  "shutdown",
                  "halt",
                  "game",
                  "news",
                  "operator",
                  "gopher",
                  "nfsnobody",
                 };

 methods:
   "UNIX STIG 4.8/UNIX STIG 12.9" -> { "LNX00320", "LNX00340" }
        comment => "CAT I & II (Previously - G107, V052, L140, L142) UNIX STIG: 4.8 File Transfer Protocol (FTP) and Telnet, 12.9 Default Accounts",
         handle => "stig_methods_redhat_unix_stig_4_8_12_9",
      usebundle => deleting_accounts("$(accounts_to_delete)");

bundle agent deleting_accounts(name)
{
 files:

  "/etc/passwd" -> { "LNX00320", "LNX00340" }
       comment => "Remove unnecessary accounts from /etc/passwd",
        handle => "deleting_accounts_files_etc_passwd",
     edit_line => delete_lines_matching("^$(name):.*");

  "/etc/shadow" -> { "LNX00320", "LNX00340" }
       comment => "Remove unnecessary accounts from /etc/shadow",
        handle => "deleting_accounts_files_etc_shadow",
     edit_line => delete_lines_matching("^$(name):.*");
}

#####################################
(LNX00580: CAT I) (Previously – L222)
#####################################

The SA will disable the Ctrl-Alt-Delete sequence unless the system is located in a controlled access area accessible only by SAs.

-> See (GEN000020: CAT II) (Previously – G001)

#############################################################################
#                                                                           #
# CAT II:                                                                   # 
#   Vulnerabilities that provide information that have a high potential of  #
#   giving access to an intruder.                                           #
#                                                                           #
#############################################################################

#######################################
(GEN000020: CAT II) (Previously – G001)
#######################################

The IAO and SA will ensure, if configurable, the UNIX host is configured to require a password for access to single-user and maintenance modes.

 files:
   "/etc/inittab" -> { "GEN000020", "GEN000040", "GEN000060", "LNX00580" }
        comment => "CAT I & II (Previously - G001, G002, G003, L222) UNIX STIG: 2.5.1.1 System Equipment, 12.14 The /etc/inittab File",
         handle => "stig_files_redhat_etc_inittab",
      edit_line => maintain_inittab,
        classes => if_repaired("restart_inittab");

 commands:
   "/sbin/init q" -> { "GEN000020", "GEN000040", "GEN000060", "LNX00580" }
       comment => "CAT I & II (Previously - G001, G002, G003, L222) UNIX STIG: 2.5.1.1 System Equipment, 12.14 The /etc/inittab File",
        handle => "stig_commands_redhat_restart_inittab",
       contain => silent;

bundle edit_line maintain_inittab
{
 delete_lines:
  "~:S:wait.*" -> { "GEN000020", "GEN000040", "GEN000060" }
     comment => "Configured to require a password when boot to single-user mode.",
      handle => "maintain_inittab_delete_lines_gen000020_gen000040_gen000060";

  "^ca::ctrlaltdel.*" -> { "LNX00580" }
     comment => "Disable CTRL+ALT+DEL.",
      handle => "maintain_inittab_delete_lines_lnx00580";

 insert_lines:
  "~:S:wait:/sbin/sulogin   # GEN000020, GEN000040, GEN000060" -> { "GEN000020", "GEN000040", "GEN000060" }
     comment => "Configured to require a password when boot to single-user mode.",
      handle => "maintain_inittab_insert_lines_gen000020_gen000040_gen000060";

  "ca:12345:ctrlaltdel:/bin/echo \"CTRL-ALT-DEL is disabled\"   # LNX00580" -> { "LNX00580" }
     comment => "Disable CTRL+ALT+DEL.",
      handle => "maintain_inittab_insert_lines_lnx00580";
}

#######################################
(GEN000040: CAT II) (Previously – G002)
#######################################

The SA will ensure a UNIX host that cannot be configured to require a password when booted to single-user mode is justified and documented with the IAO.

-> See (GEN000020: CAT II) (Previously – G001)

#######################################
(GEN000060: CAT II) (Previously – G003)
#######################################

The SA will ensure a UNIX host that cannot be configured to require a password when booted to single-user mode is located in a controlled access area accessible only by SAs.

-> See (GEN000020: CAT II) (Previously – G001)

#######################################
(GEN000440: CAT II) (Previously – G012)
#######################################

The SA will ensure all logon attempts (both successful and unsuccessful) are logged to a system log file.

 files:
   "/etc/syslog.conf" -> { "GEN000440", "GEN003160", "GEN003660", "GEN005400", "GEN005420" }
        comment => "CAT II & III (Previously - G012, G209, G656, G657) UNIX STIG: 3.1.3 Account Access, 4.14 System Logging Daemon",
         handle => "stig_files_redhat_etc_syslog_conf",
          perms => mog("640","root","root"),
      edit_line => maintain_syslog_conf,
        classes => if_repaired("restart_syslog");

 commands:
  restart_syslog::
   "/etc/init.d/syslog restart" -> { "GEN000440", "GEN003160", "GEN003660", "GEN005400", "GEN005420" }
      comment => "CAT II & III (Previously - G012, G209, G656, G657) UNIX STIG: 3.1.3 Account Access, 4.14 System Logging Daemon",
       handle => "stig_commands_redhat_restart_syslog";

bundle edit_line maintain_syslog_conf
{
 delete_lines:
  "^auth.notice.*" -> { "GEN003660" }
     comment => "Delete existing auth.notice log",
      handle => "maintain_syslog_conf_delete_lines_gen003660";

 replace_patterns:
  "^authpriv\.\*\h+(?!/var/log/secure).*" -> { "GEN000440" }
          comment => "Check authentication log will be shown in /var/log/secure",
           handle => "maintain_syslog_conf_replace_patterns_gen000440_1",
     replace_with => value("authprivdummy");
  "^authprivdummy$" -> { "GEN000440" }
          comment => "Check authentication log will be shown in /var/log/secure",
           handle => "maintain_syslog_conf_replace_patterns_gen000440_2",
     replace_with => value("authpriv.*$(const.t)$(const.t)$(const.t)$(const.t)$(const.t)$(const.t)/var/log/secure");

  "^cron\.\*h+(?!/var/log/cron).*" -> { "GEN003160" }
          comment => "Check cron log will be shown in /var/log/cron",
           handle => "maintain_syslog_conf_replace_patterns_gen003160_1",
     replace_with => value("crondummy");
  "^crondummy$" -> { "GEN003160" }
          comment => "Check cron log will be shown in /var/log/cron",
           handle => "maintain_syslog_conf_replace_patterns_gen003160_2",
     replace_with => value("cron.*$(const.t)$(const.t)$(const.t)$(const.t)$(const.t)$(const.t)$(const.t)/var/log/cron");

 insert_lines:
  "auth.notice$(const.t)$(const.t)$(const.t)$(const.t)$(const.t)$(const.t)/var/log/messages" -> { "GEN003660" }
     comment => "Log authentication notice and informational data",
      handle => "maintain_syslog_conf_insert_lines_gen003660";
}

#######################################
(GEN000460: CAT II) (Previously – G013)
#######################################

The SA will ensure, after three consecutive failed logon attempts for an account, the account is locked for 15 minutes or until the SA unlocks the account.

 files:
   "/etc/pam.d/system-auth-ac" -> { "GEN000460", "GEN000600", "GEN000620", "GEN000640", "GEN000800" }
            comment => "CAT II (Previously - G013, G019, G606) UNIX STIG: 3.1.3 Account Access, 3.2.1 Password Guidelines",
             handle => "stig_files_redhat_etc_pam_d_system_auth",
      edit_defaults => empty,
          edit_line => maintain_system_auth;

bundle edit_line maintain_system_auth
{
 insert_lines:
"#%PAM-1.0
# GEN000460, GEN000600, GEN000620, GEN000640, GEN000800
auth       required       pam_tally.so deny=3 onerr=fail unlock_time=900

auth        required      pam_env.so
auth        required      pam_unix.so nullok try_first_pass audit

account     required      pam_unix.so
account     required      pam_tally.so
password    required      pam_cracklib.so try_first_pass retry=3 minlen=10 dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 difok=-2
password    required      pam_unix.so md5 shadow nullok try_first_pass use_authtok remember=10

session     optional      pam_keyinit.so revoke
session     required      pam_limits.so
session     required      pam_unix.so" -> { "GEN000460", "GEN000600", "GEN000620", "GEN000640", "GEN000800" }
       comment => "Ensure /etc/pam.d/system-auth-ac has good contents",
        handle => "maintain_system_auth_insert_lines_gen000460",
   insert_type => "preserve_block";
}

#######################################
(GEN000480: CAT II) (Previously – G015)
#######################################

The SA will ensure the logon delay between logon prompts after a failed logon is set to at least four seconds.

 files:
   "/etc/login.defs" -> { "GEN000480", "GEN000540", "GEN000580", "GEN000700" }
        comment => "CAT II (Previously - G004, G019, G020) UNIX STIG: 3.1.3 Account Access, 3.2.1 Password Guidelines",
         handle => "stig_files_redhat_etc_login_defs",
      edit_line => maintain_login_defs;

bundle edit_line maintain_login_defs
{
 replace_patterns:
 "^PASS_MAX_DAYS\h+(?!90).*" -> { "GEN000700" }
    comment => "Passwords will be expired in 90 days.",
     handle => "maintain_login_defs_replace_patterns_gen000700_1",
    replace_with => value("PASS_MAX_DAYSdummy90");
 "^PASS_MAX_DAYSdummy90" -> { "GEN000700" }
    comment => "Passwords will be expired in 90 days.",
     handle => "maintain_login_defs_replace_patterns_gen000700_2",
    replace_with => value("PASS_MAX_DAYS   90   # GEN000700");

 "^PASS_MIN_DAYS\h+(?!1).*" -> { "GEN000540" }
    comment => "Passwords can be changed once every 24 hours.",
     handle => "maintain_login_defs_replace_patterns_gen000540_1",
    replace_with => value("PASS_MIN_DAYSdummy1");
 "^PASS_MIN_DAYSdummy1" -> { "GEN000540" }
    comment => "Passwords can be changed once every 24 hours.",
     handle => "maintain_login_defs_replace_patterns_gen000540_2",
    replace_with => value("PASS_MIN_DAYS    1   # GEN000540");

  "^PASS_MIN_LEN\h+(?!8).*" -> { "GEN000580" }
     comment => "A password does not contain a minimum of 8 characters",
      handle => "maintain_login_defs_replace_patterns_gen000580_1",
     replace_with => value("PASS_MIN_LENdummy8");
  "^PASS_MIN_LENdummy8" -> { "GEN000580" }
     comment => "A password does not contain a minimum of 8 characters",
      handle => "maintain_login_defs_replace_patterns_gen000580_2",
     replace_with => value("PASS_MIN_LEN    8   # GEN000580");

 delete_lines:
  "^FAIL_DELAY.*" -> { "GEN000480" }
     comment => "Clear up an existing login delay.",
      handle => "maintain_login_defs_delete_lines_gen000480";

 insert_lines:
  "FAIL_DELAY     4   # GEN000480" -> { "GEN000480" }
     comment => "The login delay between login prompts after a failed login is set to less than four seconds.",
      handle => "maintain_login_defs_insert_lines_gen000480";  
}

#######################################
(GEN000500: CAT II) (Previously – G605)
#######################################

The SA will configure systems to log out interactive processes (i.e., terminal sessions, ssh sessions, etc.,) after 15 minutes of inactivity or ensure a password protected screen lock mechanism is used and is set to lock the screen after 15 minutes of inactivity.

 files:
   "/etc/profile" -> { "GEN000500" }
        comment => "CAT II (Previously - G605) UNIX STIG: 3.1.4 Inactivity Timeout/Locking",
         handle => "stig_vars_redhat_etc_profile",
      edit_line => maintain_etc_profile;

bundle edit_line maintain_etc_profile
{
 delete_lines:
  "^TMOUT.*" -> { "GEN000500" }
     comment => "Clear up all TMOUT lines",
      handle => "maintain_etc_profile_delete_lines_gen000500";

 insert_lines:
  "TMOUT=900" -> { "GEN000500" }
     comment => "Set TMOUT to lock the screen after 15 minutes of inactivity",
      handle => "maintain_etc_profile_insert_lines_gen000500";
}

#######################################
(GEN000540: CAT II) (Previously – G004)
#######################################

The SA will ensure passwords are not changed more than once a day.

-> See (GEN000480: CAT II) (Previously – G015)

#######################################
(GEN000580: CAT II) (Previously – G019)
#######################################

The IAO will ensure all passwords contain a minimum of eight characters.

-> See (GEN000480: CAT II) (Previously – G015)

#######################################
(GEN000600: CAT II) (Previously – G019)
#######################################

The IAO will ensure passwords include at least two alphabetic characters, one of which must be capitalized.

-> See (GEN000600: CAT II) (Previously – G015)

#######################################
(GEN000620: CAT II) (Previously – G019)
#######################################

The IAO will ensure passwords include at least one numeric character.

-> See (GEN000480: CAT II) (Previously – G015)

#######################################
(GEN000640: CAT II) (Previously – G019)
#######################################

The IAO will ensure passwords contain at least one special character, avoid ‘#’ and ‘@’.

-> See (GEN000480: CAT II) (Previously – G015)

#######################################
(GEN000700: CAT II) (Previously – G020)
#######################################

The SA will ensure passwords are changed at least every 90 days.

-> See (GEN000460: CAT II) (Previously – G013)

#######################################
(GEN000800: CAT II) (Previously – G606)
#######################################

The SA will ensure passwords will not be reused within the last ten changes.

-> See (GEN000460: CAT II) (Previously – G013)

######################################
GEN000920: CAT II) (Previously – G023)
######################################

The SA will ensure the root account home directory (other than ‘/’) has permissions of 700. Do not change the permissions of the ‘/’ directory to anything other than 0755.

 files:
   "/" -> { "GEN000920" }
           comment => "CAT II (Previously - G023) UNIX STIG: 3.3 Root Account",
            handle => "stig_files_redhat_not_root_and_tmp_dir",
      depth_search => recurse("1"),
       file_select => only_dir_exclude2("root","tmp"),
             perms => mog("755","root","root");

   "/root" -> { "GEN000920" }
      comment => "CAT II (Previously - G023) UNIX STIG: 3.3 Root Account",
       handle => "stig_files_redhat_root_dir",
        perms => mog("700","root","root");

body file_select only_dir_exclude2(name1,name2)
{
file_types  => { "dir" };
leaf_name  => { "$(name1)", "$(name2)"};
file_result => "!leaf_name.file_types";
}

#######################################
(GEN000980: CAT II) (Previously – G026)
#######################################

The SA will ensure root can only log on as root from the system console, and then only when necessary to perform system maintenance.

 files:
   "/etc/securetty" -> { "GEN000980", "LNX00620", "LNX00640", "LNX00660" }
        comment => "CAT II UNIX STIG: 3.3 Root Account, 12.17 The /etc/securetty File",
         handle => "stig_files_redhat_etc_securetty",
          perms => mog("640","root","root"),
      edit_line => maintain_securetty;

bundle edit_line maintain_securetty
{
 delete_lines: 
  "vc/(\d+)" -> { "GEN000980" }
    comment => "Allow root to login only from the system console.",
     handle => "maintain_securetty_delete_lines_gen000980_1";

  "tty(\d+)" -> { "GEN000980" }
    comment => "Allow root to login only from the system console.",
     handle => "maintain_securetty_delete_lines_gen000980_2";

 insert_lines:
  "console" -> { "GEN000980" }
    comment => "Allow root to login only from the system console.",
     handle => "maintain_securetty_insert_lines_gen000980";
}

###################
(GEN001020: CAT II)
###################

The IAO will enforce users requiring root privileges to log on to their personal account and invoke the /bin/su - command to switch user to root

 files:
   "/etc/pam.d/sshd" -> { "GEN001020" }
        comment => "CAT II UNIX STIG: 3.3 Root Account",
         handle => "stig_files_redhat_etc_pamd_sshd",
      edit_line => maintain_pamd_sshd;

   "/etc/pam.d/login" -> { "GEN001020" }
        comment => "CAT II UNIX STIG: 3.3 Root Account",
         handle => "stig_files_redhat_etc_pamd_login",
      edit_line => maintain_pamd_login;

   "/etc/security/access.conf" -> { "GEN001020", "LNX00400", "LNX00420", "LNX00440" }
        comment => "CAT II (Previously - L044, L045, L046) UNIX STIG: 3.3 Root Account, 12.11 Console Access ",
         handle => "stig_files_redhat_etc_security_access_conf",
          perms => mog("640","root","root"),
      edit_line => maintain_security_access_conf;

bundle edit_line maintain_pamd_sshd
{
 insert_lines:
  "account    required     pam_access.so" -> { "GEN001020" }
      comment => "Root privilege must be gained via switch from user account",
       handle => "maintain_pamd_sshd_insert_lines_gen001020",
     location => after("^(account.*auth)$");
}

bundle edit_line maintain_pamd_login
{
 insert_lines:
  "account    required     pam_access.so" -> { "GEN001020" }
      comment => "Root privilege must be gained via switch from user account",
       handle => "maintain_pamd_login_insert_lines_gen001020",
     location => after("^(account.*auth)$");
}

bundle edit_line maintain_security_access_conf
{
 insert_lines:
"# Only access for root is cron
+ : root : cron crond tty1
- : ALL EXCEPT users : ALL" -> { "GEN001020" }
       comment => "Allow only root uses cron",
        handle => "maintain_security_access_conf_insert_lines_gen001020",
   insert_type => "preserve_block";
}

#######################################
(GEN001120: CAT II) (Previously – G500)
#######################################

The SA will configure the encryption program for direct root access only from the system console.

-> See (GEN005500: CAT I) (Previously – G701)

#######################################
(GEN001180: CAT II) (Previously – G036)
#######################################

The SA will ensure all daemons have permissions of 755, or more restrictive.

 vars:
   "network_services_daemon_files" -> { "GEN001180" } 
      comment => "List of Network services daemon files",
       handle => "stig_vars_redhat_network_services_daemon_files",
        slist => { 
                  "/var/cfengine/state/cf_incoming.nfsd",
                  "/var/cfengine/state/cf_outgoing.nfsd",
                  "/usr/sbin/.*",
                 };

 files:
   "$(network_services_daemon_files)" -> { "GEN001180" }
      comment => "CAT II (Previously - G036) UNIX STIG: 3.4 File and Directory Controls",
       handle => "stig_files_redhat_network_services_daemon_files",
        perms => m("755");

#######################################
(GEN001220: CAT II) (Previously - G045)
#######################################

The SA will ensure the owner of all system files, programs, and directories is a system account

 vars:
   "system_dirs" -> { "GEN001220", "GEN001240" }
      comment => "List of important system directories",
       handle => "stigs_vars_redhat_5_system_dirs",
        slist => { 
                  "/etc",
                  "/bin",
                  "/sbin",
                  "/usr/bin",
                  "/usr/sbin",
                 };

 files:
   "$(system_dirs)" -> { "GEN001220", "GEN001240" }
      comment => "CAT II (Previously - G045, G046) UNIX STIG: 3.4 File and Directory Controls",
       handle => "stigs_files_redhat_5_system_dirs",
        perms => mog("755","root","root");

#######################################
(GEN001240: CAT II) (Previously - G046)
#######################################

The SA will ensure the group owner of all system files, programs, and directories is a system group.

--> See (GEN001240: CAT II) (Previously - G046)

#######################################
(GEN001260: CAT II) (Previously – G037)
#######################################

The SA will ensure all system log files have permissions of 640, or more restrictive.

 vars:
   "system_log_files" -> { "GEN001260" } 
      comment => "List of system log files",
       handle => "stig_vars_redhat_system_log_files",
        slist => { 
                  "/var/log"
                 };

 files:
   "$(system_log_files)" -> { "GEN001260", "GEN002700" }
           comment => "CAT I & II (Previously - G095) UNIX STIG: 3.4 File and Directory Controls, 3.16 Audit Requirements",
            handle => "stig_files_redhat_system_log_files",
      depth_search => recurse("inf"),
       file_select => exclude2("cron.*","audit"),
             perms => m("600");

body file_select exclude2(name1,name2)
{
leaf_name  => { "$(name1)", "$(name2)"};
file_result => "!leaf_name";
}

#######################################
(GEN001300: CAT II) (Previously - G043)
#######################################

The SA will ensure all system library files have permissions of 755, or more restrictive.

 vars:
   "library_dirs" -> { "GEN001300" } 
      comment => "List of library files",
       handle => "stigs_vars_redhat_5_library_dirs",
        slist => { 
                  "/usr/lib",
                 };

 files:
   "$(library_dirs)" -> { "GEN001300" }
           comment => "CAT II (Previously - G043) UNIX STIG: 3.4 File and Directory Controls",
            handle => "stigs_files_redhat_5_library_dirs",
      depth_search => recurse("inf"),
             perms => m("755");

#######################################
(GEN001320: CAT II) (Previously - G039)
#######################################

The SA will ensure the owner of all NIS/NIS+/yp files is root, sys, or bin.

 vars:
   "nis_nisplus_yp_files" -> { "GEN001320", "GEN001340", "GEN001360" }
      comment => "List of NIS/NIS+/yp files",
       handle => "stigs_vars_redhat_5_nis_nisplus_yp_files",
        slist => { 
                  "/var/yp",
                 };

 files:
   "$(nis_nisplus_yp_files)" -> { "GEN001320", "GEN001340", "GEN001360" }
           comment => "CAT II (Previously - G039, G040, G041) UNIX STIG: 3.4 File and Directory Controls",
            handle => "stigs_files_redhat_5_nis_nisplus_yp_files",
      depth_search => recurse("inf"),
#       file_select => plain,
             perms => mog("755","root","root");

#######################################
(GEN001340: CAT II) (Previously - G040)
#######################################

The SA will ensure the group owner of all NIS/NIS+/yp files is root, sys, bin, or other.

-> See (GEN001320: CAT II) (Previously – G039)

#######################################
(GEN001360: CAT II) (Previously - G041)
#######################################

The SA will ensure all NIS/NIS+/yp files have permissions of 755, or more restrictive.

-> See (GEN001320: CAT II) (Previously – G039)

#######################################
(GEN001380: CAT II) (Previously – G048)
#######################################

The SA will ensure the /etc/passwd file has permissions of 644, or more restrictive.

-> See (GEN001400: CAT I) (Previously – G047)

#######################################
(GEN001420: CAT II) (Previously – G050)
#######################################

The SA will ensure the /etc/shadow file (or equivalent) has permissions of 400.

-> See (GEN001400: CAT I) (Previously – G047)

#######################################
(GEN001480: CAT II) (Previously – G053)
#######################################

The SA will ensure user home directories have initial permissions of 700, and never more permissive than 750.

 vars:
   "home_users" -> { "GEN001440", "GEN001460", "GEN001480", "GEN001500", "GEN001520" }
      comment => "Create a tmp file listing HOME users",
       handle => "stig_vars_redhat_home_users_tmp",
       string => execresult("/bin/grep home /etc/passwd | /bin/awk -F':' '{print $1}'","useshell");

   "users_list" -> { "GEN001440", "GEN001460", "GEN001480", "GEN001500", "GEN001520" }
      comment => "Read the tmp file to create an actual list of HOME users",
       handle => "stig_vars_redhat_home_users_list",
        slist => splitstring("$(home_users)", "[\n]", 500);

 files:
   "/home/$(users_list)/." -> { "GEN001440", "GEN001460", "GEN001480", "GEN001500", "GEN001520", "GEN001540", "GEN001560" }
           comment => "CAT II & III & IV, (Previously - G051, G052, G053, G054, G055, G067, G068) UNIX STIG: 3.5, 3.6 Home Directories and User Files",
            handle => "stig_files_redhat_home_users",
            create => "true",
      depth_search => recurse("inf"),
             perms => mog("700","$(users_list)","$(users_list)");

#######################################
(GEN001500: CAT II) (Previously – G054)
#######################################

The SA will ensure the user’s home directory is owned by the user.

-> See (GEN001480: CAT II) (Previously – G053)

#######################################
(GEN001520: CAT II) (Previously – G055)
#######################################

The SA will ensure the user’s home directory is owned the user’s primary group, exceptions may exist for application directories, which will be documented with the IAO.

-> See (GEN001480: CAT II) (Previously – G053)

#######################################
(GEN001560: CAT II) (Previously – G068)
#######################################

The user, application developers, and the SA will ensure user files and directories will have an initial permission no more permissive than 700, and never more permissive than 750.

 vars:
   "umask_files" -> { "GEN001560", "GEN002560" }
      comment => "List of files which contain system and user default umask",
       handle => "stig_vars_redhat_umask_files",
        slist => { 
                  "/etc/bashrc",
                  "/etc/csh.cshrc",
                  "/etc/csh.login",
                 };

 files:
   "$(umask_files)" -> { "GEN001560", "GEN002560" }
        comment => "CAT II (Previously - G068, G089), UNIX STIG: 3.6 User Files, 3.13 Umask",
         handle => "stig_files_redhat_etc_bashrc",
      edit_line => maintain_umask("077");

bundle edit_line maintain_umask(mask)
{
 replace_patterns:
  "\h+umask\s(?!$(mask)$).*" -> { "GEN002560" }
     comment => "Ensure umask is 077",
      handle => "maintain_umask_replace_patterns_gen002560",
     replace_with => value("    umask 077");	
}

-> Also see (GEN001480: CAT II) (Previously – G053)

#######################################
(GEN001580: CAT II) (Previously – G058)
#######################################

The SA will ensure run control scripts have permissions of 755, or more restrictive.

 vars:
   "rc_files" -> { "GEN001580", "GEN001620", "GEN001660", "GEN001680" }
      comment => "List of Run Control Scripts",
       handle => "stig_vars_redhat_rc_files",
        slist => {
                  "/etc/rc.d/rc",
                  "/etc/rc.d/rc.local",
                  "/etc/rc.d/rc.sysinit",
                 };
 files:
   "$(rc_files)" -> { "GEN001580", "GEN001620", "GEN001660", "GEN001680" }
      comment => "CAT I & II (Previously - G058, G061, G611, G612) UNIX STIG: 3.7 Run Control Scripts",
       handle => "stig_files_redhat_rc_files",
        perms => mog("755","root","root");

   "/etc/rc.d/init.d" -> { "GEN001580", "GEN001620", "GEN001660", "GEN001680" }
           comment => "CAT I & II (Previously - G058, G061, G611, G612) UNIX STIG: 3.7 Run Control Scripts",
            handle => "stig_files_redhat_run_control_scripts_etc_rcd_initd",
      depth_search => recurse("1"),
       file_select => exclude("iptables"),
             perms => mog("755","root","root");

#######################################
(GEN001620: CAT II) (Previously – G061)
#######################################

The SA will ensure run control scripts files do not have the suid or sgid bit set.

-> See (GEN001580: CAT II) (Previously – G058)

#######################################
(GEN001660: CAT II) (Previously – G611)
#######################################

The SA will ensure the owner of run control scripts is root.

-> See (GEN001580: CAT II) (Previously – G058)

#######################################
(GEN001680: CAT II) (Previously – G612)
#######################################

The SA will ensure the group owner of run control scripts is root, sys, bin, other, or the system default.

-> See (GEN001580: CAT II) (Previously – G058)

###################
(GEN001720: CAT II)
###################

The SA will ensure global initialization files have permissions of 644, or more restrictive.

 vars:
   "global_init_files" -> { "GEN001720", "GEN001740", "GEN001760", "GEN001780" }
      comment => "List of Global Initialization files",
       handle => "stig_vars_redhat_global_init_files",
        slist => {
                  "/etc/profile",
                  "/etc/bashrc",
                  "/etc/environment",
                 };

 files:
   "$(global_init_files)" -> { "GEN001720", "GEN001740", "GEN001760", "GEN001780" }
        comment => "CAT II (Previously - G112) UNIX STIG: 3.8.1 Global Initialization Files",
         handle => "stig_files_redhat_global_init_files",
      edit_line => append_if_no_line("mesg n"),
          perms => mog("644","root","root");

###################
(GEN001740: CAT II)
###################

The SA will ensure the owner of global initialization files is root.

-> See (GEN001720: CAT II)

###################
(GEN001760: CAT II)
###################

The SA will ensure the group owner of global initialization files is root, sys, bin, other, or the system default.

-> See (GEN001720: CAT II)

#######################################
(GEN001800: CAT II) (Previously – G038)
#######################################

The SA will ensure all default/skeleton dot files have permissions of 644, or more restrictive.

 vars:
   "skeleton_dot_files" -> { "GEN001800", "GEN001820" }
      comment => "List of default/skeleton dot files",
       handle => "stig_vars_redhat_skeleton_dot_files",
        slist => {
                  "/etc/skel/.bash_logout",
                  "/etc/skel/.bash_profile",
                  "/etc/skel/.emacs",
                  "/etc/skel/.bashrc",
                 };

 files:
   "$(skeleton_dot_files)" -> { "GEN001800", "GEN1820" }
      comment => "CAT II (Previously - G038) UNIX STIG: 3.8.1 Global Initialization Files",
       handle => "stig_files_redhat_skeleton_dot_files",
        perms => mog("644","root","root");

###################
(GEN001820: CAT II)
###################

The SA will ensure the owner of all default/skeleton dot files is root or bin.

-> See (GEN001800: CAT II) (Previously – G038)

#######################################
(GEN001880: CAT II) (Previously - G057)
#######################################

The SA will ensure local initialization files have permissions of 740, or more restrictive. The following files/directories are to be excluded from GEN001880:
   .dt        (a directory, this should have permissions of 755)
   .dtprofile (a file, this should have permissions of 755)

 vars:
   "excluded_local_init_files" -> { "GEN001880" }
      comment => "List of excluded local initialization files",
       handle => "stigs_vars_redhat_5_excluded_local_init_files",
        slist => {
                  ".dt",
                  ".dtprofile",
                 };

 files:
   "/home/$(users_list)/$(excluded_local_init_files)" -> { "GEN001880" }
      comment => "CAT II (Previously - G057) 3.8.2 Local Initialization Files",
       handle => "stigs_files_redhat_5_local_init_files",
        perms => mog("755","$(users_list)","$(users_list)");

###################
(GEN002100: CAT II)
###################

The SA will ensure .rhosts is not supported in the pluggable authentication module (PAM).

 vars:
   "pam_files" -> { "GEN002100" }
      comment => "List of PAM files to disable .rhosts",
       handle => "stig_vars_redhat_pam_files",
        slist => { 
                  "/etc/pam.d/ekshell",
                  "/etc/pam.d/kshell",
                 };

 files:
   "$(pam_files)" -> { "GEN002100" }
        comment => "CAT II UNIX STIG: 3.9 Trusted System/System Access Control Files",
         handle => "stig_files_redhat_pam_files",
      edit_line => comment_lines_matching("^auth.*pam_rhosts_auth.so","#");

#######################################
(GEN002120: CAT II) (Previously – G069)
#######################################

The SA will ensure the /etc/shells (or equivalent) file exits.

 files:
   "/etc/shells" -> { "GEN002120" }
            comment => "CAT II (Previously - G069) UNIX STIG: 3.10 Shells",
             handle => "stig_files_redhat_etc_shells",
             create => "true",
      edit_defaults => empty,
              perms => mog("644","root","root"),
          edit_line => maintain_etc_shells;

bundle edit_line maintain_etc_shells
{
 insert_lines:
"/bin/sh
/bin/bash
/sbin/nologin
/bin/tcsh
/bin/csh
/bin/ksh
/bin/ksh93" -> { "GEN002120" }
       comment => "Ensure /etc/shells has good contents",
        handle => "maintain_etc_shells_insert_lines_gen002120",
   insert_type => "preserve_block";
}

######################################
(GEN002160: CAT I) (Previously – G072)
######################################

The SA will ensure no shell has the suid bit set.

 vars:
   "shell_files" -> { "GEN002160", "GEN002180", "GEN002200", "GEN002220" }
      comment => "List of login shells from /etc/shells",
       handle => "stig_vars_redhat_shell_files",
        slist => readstringlist("/etc/shells", "#.*", "[\n]", 10, 1000);

 files:
   "$(shell_files)" -> { "GEN002160", "GEN002180", "GEN002200", "GEN002220" }
      comment => "CAT I & II (Previously - G072, G073, G074, G075) UNIX STIG: 3.10 Shells",
       handle => "stig_files_redhat_shell_files",
        perms => mog("0755","root","root");

#######################################
(GEN002180: CAT II) (Previously – G073)
#######################################

The SA will ensure no shell has the sgid bit set.

-> See (GEN002160: CAT I) (Previously – G072)

#######################################
(GEN002200: CAT II) (Previously – G074)
#######################################

The SA will ensure the owner of all shells is root or bin.

-> See (GEN002160: CAT I) (Previously – G072)

#######################################
(GEN002220: CAT II) (Previously – G075)
#######################################

The SA will ensure all shells (excluding /dev/null and sdshell) have permissions of 755, or more restrictive.

-> See (GEN002160: CAT I) (Previously – G072)

#######################################
(GEN002320: CAT II) (Previously – G501)
#######################################

The SA will ensure the audio devices have permissions of 644, or more restrictive.

 files:
   "/etc/security/console.perms.d/50-default.perms" -> { "GEN002320" }
        comment => "CAT II (Previously - G501) UNIX STIG: 3.11 Device Files",
         handle => "stig_files_redhat_security_default_perms",
      edit_line => remove_audio_devices;

   "/etc/udev/rules.d/55-audio-perms.rules" -> { "GEN002320", "GEN002340", "GEN002360" }
        comment => "CAT II (Previously - G501, G502, G504) UNIX STIG: 3.11 Device Files",
         handle => "stig_files_redhat_audio_perms_rules",
         create => "true",
      edit_line => maintain_audio_devices;

bundle edit_line remove_audio_devices
{
 delete_lines:
  ".*sound.*" -> { "GEN002320" }
     comment => "Delete all lines contains a word, sound",
      handle => "remove_audio_devices_delete_lines_sound_gen002320";

  ".*snd.*" -> { "GEN002320" }
     comment => "Delete all lines contains a word, snd",
      handle => "remove_audio_devices_delete_lines_snd_gen002320";

  ".*mixer.*" -> { "GEN002320" }
     comment => "Delete all lines contains a word, mixer",
      handle => "remove_audio_devices_delete_lines_mixer_gen002320";
}

bundle edit_line maintain_audio_devices
{
 insert_lines:
  "SUBSYSTEM==\"sound|snd\", OWNER=\"root\", GROUP=\"root\", MODE=\"0644\"",
     comment => "Append a line to ensure audio devices' permission and ownership",
      handle => "maintain_audio_devices_insert_lines_gen002320";
}

#######################################
(GEN002340: CAT II) (Previously – G502)
#######################################

The SA will ensure the owner of audio devices is root.

-> See (GEN002320: CAT II) (Previously – G501)

#######################################
(GEN002360: CAT II) (Previously – G504)
#######################################

The SA will ensure the group owner of audio devices is root, sys, or bin.

-> See (GEN002320: CAT II) (Previously – G501)

#######################################
(GEN002420: CAT II) (Previously – G086)
#######################################

The SA will ensure user filesystems, removable media, and remote filesystems will be mounted with the nosuid option.

 vars:
   "fstab_contents" -> { "GEN001080", "GEN002420" }
      comment => "All Contents of /etc/fstab",
       handle => "stig_vars_redhat_fstab_contents",
       string => readfile("/etc/fstab","4000");

   "fstab_list" -> { "GEN002420" }
      comment => "Break string into a list",
       handle => "stig_vars_redhat_list_from_etc_fstab",
        slist => splitstring("$(fstab_contents)", "[\n]", 100);

 methods:
   "UNIX STIG 3.12.1" -> { "GEN002420" }
        comment => "CAT II (Previously - G086) UNIX STIG: 3.12.1 Set User ID (suid)",
         handle => "stig_methods_redhat_unix_stig_3_12_1",
      usebundle => filesystem_mounted_with_nosuid("/etc/fstab","$(fstab_list)");

bundle agent filesystem_mounted_with_nosuid(path,string)
{
 classes:
    "option_ok" expression => regextract(
                                 "\S+\s+\S+\s+\S+\s+(\S+)",
                                 "$(string)",
                                 "option"
                                 );

 classes:
  "have_home"      expression => regcmp(".*\/home.*", "$(string)");
  "have_boot"      expression => regcmp(".*\/boot.*", "$(string)");
  "have_sys"       expression => regcmp(".*\/sys.*", "$(string)");
  "have_usr"       expression => regcmp(".*\/usr.*", "$(string)");
  "have_usr_local" expression => regcmp(".*\/usr\/local.*", "$(string)");
  "no_acl"         not => regcmp(".*acl.*", "$(string)");

 files:
  "$(path)"
     edit_line => set_fstab_field("/home","4","$(option[1]),nosuid,nodev,acl"),
            if => "have_home.no_acl";
  "$(path)"
     edit_line => set_fstab_field("/boot","4","$(option[1]),nosuid,acl"),
            if => "have_boot.no_acl";
  "$(path)"
     edit_line => set_fstab_field("/sys","4","$(option[1]),nosuid,acl"),
            if => "have_sys.no_acl";
  "$(path)"
     edit_line => set_fstab_field("/usr","4","$(option[1]),nodev,acl"),
            if => "have_usr.no_acl";
  "$(path)"
     edit_line => set_fstab_field("/usr/local","4","$(option[1]),nodev,acl"),
            if => "have_usr_local.no_acl";
}

bundle edit_line set_fstab_field(path,field,val)
{
field_edits:
 ".*\$(path)\s.*"
        comment => "Edit a user attribute in the password file",
     edit_field => col("\s+","$(field)","$(val)","set");
}

#######################################
(GEN002480: CAT II) (Previously – G079)
#######################################

The SA will ensure no world writable files exist and world writable directories are public directories.

 files:
   "/var/cfengine/state/cf_incoming.*" -> { "GEN002480" }
      comment => "CAT II (Previously - G079) UNIX STIG: 3.12.3 Stick Bit",
       handle => "stig_files_redhat_cf_incoming_files",
        perms => m("644");

#######################################
(GEN002560: CAT II) (Previously – G089)
#######################################

The SA will ensure the system and user umask is 077.

-> See (GEN001560: CAT II) (Previously – G068)

#######################################
(GEN002640: CAT II) (Previously – G092)
#######################################

The SA will ensure logon capability to default system accounts (e.g., bin, lib, uucp, news, sys, guest, daemon, and any default account not normally logged onto) will be disabled by making the default shell /bin/false, /usr/bin/false, /sbin/false, /sbin/nologin, or /dev/null, and by locking the password.

 vars:
   "allusers_not_root" -> { "GEN002640", "GEN003300", "GEN003320" }
      comment => "List of all system accounts but root and hypen users",
       handle => "stig_vars_redhat_list_allusers_not_root",
        slist => getusers("root,avahi-autoipd","0");

   "$(allusers_not_root)_uid" -> { "GEN002640" }
      comment => "List of system UIDs",
       handle => "stig_vars_redhat_allusers_not_root_uid",
          int => getuid("$(allusers_not_root)");

 classes:
   "$(allusers_not_root)_less_than_500" -> { "GEN002640" }
         comment => "Check if the UID less than 500 (System accounts)",
          handle => "stig_classes_redhat_uid_less_than_500",
      expression => islessthan("$($(allusers_not_root)_uid)","500");

 files:
   "/etc/passwd" -> { "GEN002640", "GEN005000" }
         comment => "CAT I & II (Previously - G649, G092) UNIX STIG: 3.15 Default Accounts, 4.8.1 FTP Configuration",
          handle => "stig_files_redhat_default_accounts_shell",
       edit_line => set_user_field("$(allusers_not_root)","7","/sbin/nologin"),
              if => "$(allusers_not_root)_less_than_500";

   "/etc/passwd" -> { "GEN002640" }
         comment => "CAT II (Previously - G092) UNIX STIG: 3.15 Default Accounts",
          handle => "stig_files_redhat_default_accounts_shell_for_badnaming_users",
       edit_line => set_user_field("avahi-autoipd","7","/sbin/nologin");

#######################################
(GEN002660: CAT II) (Previously – G093)
#######################################

The SA will configure and implement auditing.

 files:
   "/etc/audit/audit.rules" -> { "GEN002660", "GEN002700", "GEN002720", "GEN002740", "GEN002760", "GEN002780", "GEN002800", "GEN002820", "GEN002840" }
             comment => "CAT I (Previously - G093, G095, G100-G106) UNIX STIG: 3.16 Audit Requirements",
              handle => "stig_files_redhat_etc_audit_audit_rules",
               perms => m("640"),
       edit_defaults => empty,
           edit_line => maintain_audit_rules;

bundle edit_line maintain_audit_rules
{
 insert_lines:
"# This file contains the auditctl rules that are loaded
# whenever the audit daemon is started via the initscripts.
# The rules are simply the parameters that would be passed
# to auditctl.

# GEN002660 GEN002720 GEN002740 GEN002760 GEN002780 GEN002800 GEN002820 GEN002840

# First rule - delete all
-D

# Enable auditing
-e 1

# Increase the buffers to survive stress events.
# Make this bigger for busy systems
-b 8192

# Failure of auditd causes a kernel panic
-f 2

# GEN002720 Logon/Logout
-w /bin/login -p x
-w /bin/logout -p x

# GEN002740 DAC permission changes
-a exit,always -S chmod -S chown -S chown32 -S fchmod -S fchown -S fchown32 -S lchown -S lchown32

# GEN002760 Unauthorized file access attempts
-a exit,always -F success=0 -S open -S mknod -S pipe -S mkdir -S creat -S truncate -S truncate64 -S ftruncate -S ftruncate64

# GEN002780 Privileged commands
-a exit,always -S chroot -S mount -S umount -S umount2 -S adjtimex -S kill
-w /usr/sbin/pwck
-w /bin/chgrp
-w /usr/bin/newgrp
-w /usr/sbin/groupadd
-w /usr/sbin/groupmod
-w /usr/sbin/groupdel
-w /usr/sbin/useradd
-w /usr/sbin/userdel
-w /usr/sbin/usermod
-w /usr/bin/chage
-w /usr/bin/setfacl
-w /usr/bin/chacl

# GEN002800 Deleting files
-a exit,always -S unlink -S rmdir

# GEN002820 System administration actions
# These two lines could be the cause of problems with filling audit logs and preventing system usage after installation
-w /var/log/audit/audit.log
-w /var/log/audit/audit[1-4].log
-w /var/log/messages
-w /var/log/lastlog
-w /var/log/faillog
-w /etc/audit/auditd.conf -p wa
-w /etc/audit/audit.rules -p wa
-w /etc/selinux/config -p wa
-w /etc/passwd -p wa
-w /etc/shadow -p wa
-w /etc/group  -p wa
-w /etc/ssh/sshd_config
-w /etc/pam.d
-w /etc/login.defs
-w /etc/rc.d/init.d
-w /etc/inittab -p wa
-w /var/run/utmp
-w /var/run/wtmp
-a exit,always -S acct -S reboot -S sched_setparam -S sched_setscheduler -S setdomainname -S setrlimit -S settimeofday -S stime -S swapon

# GEN002840 Security personnel actions
-a exit,always -S init_module -S delete_module -S setxattr -S lsetxattr -S fsetxattr -S removexattr -S lremovexattr -S fremovexattr
-w /bin/su" -> { "GEN002660", "GEN002720", "GEN002740", "GEN002760", "GEN002780", "GEN002800", "GEN002820", "GEN002840" }
       comment => "Ensure /etc/audit/audit.rules has good contents",
        handle => "maintain_audit_rules_insert_lines_gen002660_gen002720_gen002840",
   insert_type => "preserve_block";
}

#######################################
(GEN002680: CAT II) (Previously – G094)
#######################################

The SA will ensure audit data files and directories will be readable only by personnel authorized by the IAO.

 files:
   "/var/log/audit" -> { "GEN002680" }
      comment => "CAT II (Previously - G094) UNIX STIG: 3.16 Audit Requirements",
       handle => "stig_files_redhat_var_log_audit",
        perms => m("700");

######################################################
(GEN002720-GEN002840: CAT II) (Previously – G100-G106)
######################################################

The SA will configure the auditing system to audit the following events for all users and root:
- Logon (unsuccessful and successful) and logout (successful)
- Process and session initiation (unsuccessful and successful)
- Discretionary access control permission modification (unsuccessful and successful use of chown/chmod)
- Unauthorized access attempts to files (unsuccessful)
- Use of privileged commands (unsuccessful and successful)
- Use of print command (unsuccessful and successful)
- Export to media (successful)
- System startup and shutdown (unsuccessful and successful)
- Files and programs deleted by the user (successful and unsuccessful)
- All system administration actions
- All security personnel actions

-> See (GEN002660: CAT II) (Previously – G093)

#######################################
(GEN002860: CAT II) (Previously – G674)
#######################################

The SA and/or IAO will ensure old audit logs are closed and new audit logs are started daily.

 files:
   "/etc/logrotate.d/audit" -> { "GEN002860" }
             comment => "CAT II (Previously - G674) UNIX STIG: 3.16 Audit Requirements",
              handle => "stig_files_redhat_logrotated_audit",
              create => "true",
               perms => mog("644","root","root"),
       edit_defaults => empty,
           edit_line => maintain_logrotated_audit;

bundle edit_line maintain_logrotated_audit
{
 insert_lines:
"/var/log/audit/audit.log {
$(const.t)daily
$(const.t)notifempty
$(const.t)missingok
$(const.t)postrotate
$(const.t)/sbin/service auditd restart 2> /dev/null > /dev/null || true
$(const.t)endscript
}" -> { "GEN002860" }
       comment => "Ensure old audit logs are closed and new audit logs are started daily",
        handle => "maintain_logrotated_audit_insert_lines_gen002860",
   insert_type => "preserve_block";
}

#######################################
(GEN002960: CAT II) (Previously – G200)
#######################################

The SA will control access to the cron utilities via the cron.allow and/or cron.deny file(s).

 vars:
   "cron_users" -> { "GEN002960" }
      comment => "List of users who would be able to use cron utility",
       handle => "stig_vars_redhat_cron_users",
        slist => { 
                  "root",
#                  "user1",
#                  "user2",
#                  "user3",
                 };

 files:
   "/etc/cron.deny" -> { "GEN002960", "GEN003060", "GEN003200", "GEN003260" }
            comment => "CAT II (Previously - G620, G623) UNIX STIG: 3.17.3 Restrictions",
             handle => "stig_files_redhat_etc_cron_deny",
             create => "true",
              perms => mog("600","root","root"),
      edit_defaults => empty,
          edit_line => append_if_no_line("ALL");
   
   "/etc/cron.allow" -> { "GEN002960", "GEN002980","GEN003060", "GEN003240" }
            comment => "CAT II (Previously - G622) UNIX STIG: 3.17.3 Restrictions",
             handle => "stig_files_redhat_etc_cron_allow",
             create => "true",
              perms => mog("600","root","root"),
      edit_defaults => empty,
          edit_line => maintain_cron_allow("@(STIG.cron_users)");

bundle edit_line maintain_cron_allow(name)
{
 insert_lines:
  "$(name)" -> { "GEN002960" }
     comment => "Allow users from the list to use cron utility",
      handle => "maintain_cron_allow_insert_lines_gen02960";
}

#######################################
(GEN002980: CAT II) (Previously – G201)
#######################################

The SA will ensure the cron.allow file has permissions of 600, or more restrictive.

-> See (GEN002960: CAT II) (Previously – G200)

###################
(GEN003040: CAT II)
###################

The SA will ensure the owner of crontabs is root or the crontab creator.

 vars:
   "cron_dirs" -> { "GEN003040", "GEN003080" } 
      comment => "List of cron directories",
       handle => "stig_vars_redhat_cron_dirs",
        slist => { 
                  "/etc/cron.hourly",
                  "/etc/cron.daily",
                  "/etc/cron.weekly",
                  "/etc/cron.monthly",
                  "/etc/cron.d",
                 };

   "other_cron_dirs" -> { "GEN003040", "GEN003080" } 
      comment => "List of other cron directories",
       handle => "stig_vars_redhat_other_cron_dirs",
        slist => { 
                  "/var/spool/cron",
                 };

   "cron_files" -> { "GEN003040", "GEN003080" }
      comment => "List of cron files",
       handle => "stig_vars_redhat_cron_files",
        slist => {
                  "/etc/crontab",
                  "/usr/share/logwatch/scripts/logwatch.pl",
                 };

 files:
   "$(cron_dirs)" -> { "GEN003040", "GEN003080" }
            comment => "CAT II (Previously - G205) UNIX STIG: 3.17.3 Restrictions",
             handle => "stig_files_redhat_cron_dirs_600",
       depth_search => recurse("inf"),
              perms => mog("600","root","root");

   "$(other_cron_dirs)" -> { "GEN003040", "GEN003080" }
            comment => "CAT II (Previously - G205) UNIX STIG: 3.17.3 Restrictions",
             handle => "stig_files_redhat_other_cron_dirs_700",
       depth_search => recurse("inf"),
              perms => mog("700","root","root");

   "$(cron_files)" -> { "GEN003040", "GEN003080" }
      comment => "CAT II (Previously - G205) UNIX STIG: 3.17.3 Restrictions",
       handle => "stig_files_redhat_other_cron_files",
        perms => mog("600","root","root");

###################
(GEN003060: CAT II)
###################

The SA will ensure default system accounts (with the possible exception of root) will not be listed in the cron.allow file. If there is only a cron.deny file, the default accounts (with the possible exception of root) will be listed there.

-> See (GEN003040: CAT II)

#######################################
(GEN003080: CAT II) (Previously – G205)
#######################################

The SA will ensure crontabs have permissions of 600, or more restrictive, (700 for some Linux crontabs, which is detailed in the UNIX Checklist).

-> See (GEN003040: CAT II)

#######################################
(GEN003100: CAT II) (Previously – G206)
#######################################

The SA will ensure cron and crontab directories have permissions of 755, or more restrictive.

 files:
   "/etc" -> { "GEN003100", "GEN003120", "GEN003140" }
           comment => "CAT II (Previously - G206, G207) UNIX STIG: 3.17.3 Restrictions",
            handle => "stig_files_redhat_cron_dirs_755",
      depth_search => recurse("1"),
       file_select => cron_dirs,
             perms => mog("755","root","root");

   "/var/spool" -> { "GEN003100", "GEN003120", "GEN003140" }
           comment => "CAT II (Previously - G206, G207) UNIX STIG: 3.17.3 Restrictions",
            handle => "stig_files_redhat_other_cron_dirs_755",
      depth_search => recurse("1"),
       file_select => cron_dirs,
             perms => mog("755","root","root");

body file_select cron_dirs
{
leaf_name => { "cron.*" };
file_types  => { "dir" };
file_result => "leaf_name.file_types";
}

#######################################
(GEN003120: CAT II) (Previously – G207)
#######################################

The SA will ensure the owner of the cron and crontab directories is root or bin.

-> See (GEN003100: CAT II) (Previously – G206)

#######################################
(GEN003140: CAT II) (Previously – G208)
#######################################

The SA will ensure the group owner of the cron and crontab directories is root, sys, or bin.

-> See (GEN003100: CAT II) (Previously – G206)

#######################################
(GEN003160: CAT II) (Previously – G209)
#######################################

The SA is responsible for ensuring cron logging is implemented.

-> See (GEN000440: CAT II) (Previously – G012)

#######################################
(GEN003180: CAT II) (Previously – G210)
#######################################

The SA will ensure cron logs have permissions of 600, or more restrictive.

 files:
   "/var/log/cron.*" -> { "GEN003180" }
      comment => "CAT II (Previously - G210) UNIX STIG: 3.17.3 Restrictions",
       handle => "stig_files_redhat_var_log_cron",
        perms => mog("600","root","root");

#######################################
(GEN003200: CAT II) (Previously – G620)
#######################################

The SA will ensure the cron.deny file has permissions of 600, or more restrictive.

-> See (GEN002960: CAT II) (Previously – G200)

#######################################
(GEN003240: CAT II) (Previously – G622)
#######################################

The SA will ensure the owner and group owner of the cron.allow file is root.

-> See (GEN002960: CAT II) (Previously – G200)

#######################################
(GEN003260: CAT II) (Previously – G623)
#######################################

The SA will ensure the owner and group owner of the cron.deny file is root.

-> See (GEN002960: CAT II) (Previously – G200)

#######################################
(GEN003280: CAT II) (Previously – G211)
#######################################

The SA will ensure access to at will be controlled via the at.allow and/or the at.deny file(s).

 files:
   "/etc/at.deny" -> { "GEN003280", "GEN003300", "GEN003320", "GEN003340", "GEN003480" }
        comment => "CAT II (Previously - G211, G212, G213, G214, G630) UNIX STIG: 3.18.3 Restrictions",
         handle => "stig_files_redhat_etc_at_deny_all_not_root",
         create => "true",
          perms => mog("600","root","root"),
      edit_line => append_if_no_lines("@(STIG.at_deny_users)");

#######################################
(GEN003300: CAT II) (Previously – G212)
#######################################

The SA will ensure the at.deny file is not empty.

-> See (GEN002640: CAT II) (Previously – G092)

#######################################
(GEN003320: CAT II) (Previously – G213)
#######################################

The SA will ensure default system accounts (with the possible exception of root) are not listed in the at.allow file. If there is only an at.deny file, the default accounts (with the possible exception of root) will be listed there.

-> See (GEN003280: CAT II) (Previously – G211)

 files:
   "/etc/at.allow" -> { "GEN003320", "GEN003340", "GEN003460" }
            comment => "CAT II (Previously - G213, G214, G629) UNIX STIG: 3.18.3 Restrictions",
             handle => "stig_files_redhat_etc_at_allow",
             create => "true",
              perms => mog("600","root","root"),
      edit_defaults => empty,
          edit_line => maintain_at_allow;

bundle edit_line maintain_at_allow
{
 insert_lines:
  "root" -> { "GEN003320" }
     comment => "Remove all restricted users",
      handle => "maintain_at_allow_insert_lines_gen03320";
}

#######################################
(GEN003340: CAT II) (Previously – G214)
#######################################

The SA will ensure the at.allow and at.deny files have permissions of 600, or more restrictive.

-> See (GEN003280: CAT II) (Previously – G211) and (GEN003320: CAT II) (Previously – G213)

#######################################
(GEN003400: CAT II) (Previously – G625)
#######################################

The SA will ensure the at (or equivalent) directory has permissions of 755, or more restrictive.

 files:
   "/var/spool/at/spool/" -> { "GEN003400", "GEN003420" }
      comment => "CAT II (Previously - G625, G626) UNIX STIG: 3.18.3 Restrictions",
       handle => "stig_files_redhat_var_spool_at_spool",
        perms => mog("755","root","root");

#######################################
(GEN003420: CAT II) (Previously – G626)
#######################################

The SA will ensure the owner and group owner of the at (or equivalent) directory is root, sys, bin, or daemon.

-> See (GEN003400: CAT II) (Previously – G625)

#######################################
(GEN003460: CAT II) (Previously – G629)
#######################################

The SA will ensure the owner and group owner of the at.allow file is root.

-> See (GEN003320: CAT II) (Previously – G213)

#######################################
(GEN003480: CAT II) (Previously – G630)
#######################################

The SA will ensure the owner and group owner of the at.deny file is root.

-> See (GEN003280: CAT II) (Previously – G211)

###################
(GEN003600: CAT II)
###################

The SA will ensure network parameters are securely set.

 files:
   "/etc/sysctl.conf" -> { "GEN003600", "GEN005600", "LNX00480", "LNX00500","LNX00520" }
        comment => "CAT II (Previously - L204, L206, L208) UNIX STIG: 3.20.5 Network Security Settings, 12.12 Kernel Configuration File",
         handle => "stig_files_redhat_etc_sysctl_conf",
          perms => mog("600","root","root"),
      edit_line => maintain_sysctl_conf,
        classes => if_repaired("restart_sysctl");

 commands:
  restart_sysctl::  
   "/sbin/sysctl -p" -> { "GEN003600" }
      comment => "CAT II UNIX STIG: 3.20.5 Network Security",
       handle => "stig_commands_redhat_restart_sysctl",
      contain => silent;

bundle edit_line maintain_sysctl_conf
{
 delete_lines:
  "^net.ipv4.tcp_max_syn_backlog.*" -> { "GEN003600" }
     comment => "Clear up an existing Network parameters.",
      handle => "maintain_sysctl_conf_delete_lines_gen003600";

  "^net.ipv4.ip_forward.*" -> { "GEN005600" }
     comment => "Clear up an existing ip_forward parameters.",
      handle => "maintain_sysctl_conf_delete_lines_gen005600";

 insert_lines:
  "net.ipv4.tcp_max_syn_backlog = 1280" -> { "GEN003600" }
     comment => "Secure Network parameters.",
      handle => "maintain_sysctl_conf_insert_lines_gen003600";

  "net.ipv4.ip_forward = 0" -> { "GEN005600" }
     comment => "Disable IP forwarding.",
      handle => "maintain_sysctl_conf_insert_lines_gen005600";
}

###################
(GEN003660: CAT II)
###################

The SA will ensure the authentication notice and informational data is logged.

-> See (GEN000440: CAT II) (Previously – G012)

###################
(GEN003700: CAT II)
###################

The SA will ensure inetd (xinetd for Linux) is disabled if all inetd/xinetd based services are disabled.

 files:
   "unneeded_services" -> { "GEN003700", "GEN003860" }
      comment => "List of unneeded inetd/xinetd services to be disabled",
       handle => "stig_vars_redhat_unneeded_services",
        slist => {
                  "bluetooth",
                  "irda",
                  "im_sensors",
                  "portmap",
                  "rawdevices",
                  "rpcgssd",
                  "rpcidmapd",
                  "rpcsvcgssd",
                  "sendmail",
                  "xinetd",
                  "finger"
                 };
   "$(unneeded_services)_status" -> { "GEN003700", "GEN003860" } 
      comment => "List of service status of those unneeded services",
       handle => "stig_vars_redhat_unneeded_services_status",
       string => execresult("/sbin/chkconfig --list $(unneeded_services)","noshell");

 classes:
   "$(unneeded_services)_on" -> { "GEN003700", "GEN003860" } 
         comment => "Check if those unneeded services are on or not",
          handle => "stig_classes_redhat_unneeded_services_on",
      expression => regcmp(".*:on.*","$($(unneeded_services)_status)");

 commands:
   "/sbin/chkconfig $(unneeded_services) off" -> { "GEN003700", "GEN003860" }
         comment => "CAT II (Previously - V046) UNIX STIG: 4 Network Services",
          handle => "stig_commands_redhat_disable_unneeded_services",
              if => "$(unneeded_services)_on";

#######################################
(GEN003720: CAT II) (Previously – G107)
#######################################

The SA will ensure the owner of the inetd.conf (xinetd.conf file and the xinetd.d directory for Linux) file is root or bin. This is to include any directories defined in the includedir parameter.

 files:
   "/etc/xinetd.d" -> { "GEN003720", "GEN003740" }
      comment => "CAT II (Previously - G107, G108) UNIX STIG: 4 Network Services",
       handle => "stig_files_redhat_etc_xinetdd_dir",
        perms => mog("755","root","root");

   "/etc/xinetd.d" -> { "GEN003720" }
           comment => "CAT II (Previously - G107) UNIX STIG: 4 Network Services",
            handle => "stig_files_redhat_etc_xinetdd_files",
      depth_search => recurse("inf"),
             perms => mog("644","root","root");

   "/etc/xinetd.conf" -> { "GEN003720", "GEN003740" }
      comment => "CAT II (Previously - G107, G108) UNIX STIG: 4 Network Services",
       handle => "stig_files_redhat_etc_xinetd_conf",
        perms => mog("440","root","root");

#######################################
(GEN003740: CAT II) (Previously – G108)
#######################################

The SA will ensure the inetd.conf (xinetd.conf for Linux) file has permissions of 440, or more restrictive. The Linux xinetd.d directory will have permissions of 755, or more restrictive. This is to include any directories defined in the includedir parameter.

-> See (GEN003720: CAT II) (Previously – G107)

#######################################
(GEN003760: CAT II) (Previously – G109)
#######################################

The SA will ensure the owner of the services file is root or bin.

 files:
   "/etc/services" -> { "GEN003760", "GEN003780" }
      comment => "CAT II (Previously - G109, G110) UNIX STIG: 4 Network Services",
       handle => "stig_files_redhat_etc_services",
        perms => mog("644","root","root");

#######################################
(GEN003780: CAT II) (Previously – G110)
#######################################

The SA will ensure the services file has permissions of 644, or more restrictive.

-> See (GEN003760: CAT II) (Previously – G109)

#######################################
(GEN003960: CAT II) (Previously – G631)
#######################################

The SA will ensure the owner of the traceroute command is root.

 files:
   "/bin/traceroute" -> { "GEN003960", "GEN003980", "GEN004000" }
      comment => "CAT II (Previously - G631, G632, G633) UNIX STIG: 4.5 Traceroute",
       handle => "stig_files_redhat_bin_traceroute",
        perms => mog("700","root","root");

#######################################
(GEN003980: CAT II) (Previously – G632)
#######################################

The SA will ensure the group owner of the traceroute command is root, sys, or bin.

-> See (GEN003960: CAT II) (Previously – G631)

#######################################
(GEN004000: CAT II) (Previously – G633)
#######################################

The SA will ensure the traceroute command has permissions of 700, or more restrictive.

-> See (GEN003960: CAT II) (Previously – G631)

#######################################
(GEN004360: CAT II) (Previously – G127)
#######################################

The SA will ensure the aliases file is owned by root.

 files:
   "/etc/aliases" -> { "GEN004360", "GEN004380", "GEN004640" }
        comment => "CAT I & II (Previously - G127, G128, V126) UNIX STIG: 4.7 Sendmail or Equivalent",
         handle => "stig_files_redhat_etc_aliases",
          perms => mog("644","root","root"),
      edit_line => comment_lines_matching("decode:\h+root","#"),
        classes => if_repaired("restart_aliases");

#######################################
(GEN004380: CAT II) (Previously – G128)
#######################################

The SA will ensure the aliases file has permissions of 644, or more restrictive.

-> See (GEN004360: CAT II) (Previously – G127)

#######################################
(GEN004480: CAT II) (Previously – G135)
#######################################

The SA will ensure the owner of the critical sendmail log file is root.

 files:
   "/var/log/maillog" -> { "GEN004480", "GEN004500" }
      comment => "CAT II (Previously - G135, G136) UNIX STIG: 4.7 Sendmail or Equivalent",
       handle => "stig_files_redhat_var_log_maillog",
        perms => mog("600","root","root");

#######################################
(GEN004500: CAT II) (Previously – G136)
#######################################

The SA will ensure the critical sendmail log file has permissions of 644, or more restrictive.

-> See (GEN004480: CAT II) (Previously – G135)

###################
(GEN004540: CAT II)
###################

The SA will ensure the help sendmail command is disabled.

 files:
   "/etc/mail/sendmail.cf" -> { "GEN004440", "GEN004540", "GEN004560" }
        comment => "CAT II & IV (Previously - G133, G646) UNIX STIG: 4.7 Sendmail or Equivalent",
         handle => "stig_files_redhat_etc_mail_sendmail_cf",
      edit_line => maintain_sendmail,
        classes => if_repaired("restart_sendmail");

 commands:
  restart_sendmail::  
   "/sbin/service sendmail restart" -> { "GEN004540", "GEN004560" }
      comment => "CAT II (Previously - G646) UNIX STIG: 4.7 Sendmail or Equivalent",
       handle => "stig_commands_redhat_restart_sendmail";

bundle edit_line maintain_sendmail
{
 replace_patterns:
  "^O LogLevel=(?!9).*" -> { "GEN004440" }
          comment => "Disable the sendmail help command.",
           handle => "maintain_sendmail_replace_patterns_gen004440",
     replace_with => value("O LogLevel=9");

  "^(O.*helpfile)$" -> { "GEN004540" }
          comment => "Disable the sendmail help command.",
           handle => "maintain_sendmail_replace_patterns_gen004540",
     replace_with => comment("#");

  "^O SmtpGreetingMessage=\$j Sendmail \$v/\$Z; \$b" -> { "GEN004560" }
          comment => "Hide sendmail version.",
           handle => "maintain_sendmail_replace_patterns_gen004560",
     replace_with => value("O SmtpGreetingMessage=$j Sendmail STIG-GEN004560; $b"); 	
}

#######################################
(GEN004560: CAT II) (Previously – G646)
#######################################

To help mask the e-mail version, the SA will use the following in place of the original sendmail greeting message: O SmtpGreetingMessage= Mail Server Ready ; $b

-> See (GEN004540: CAT II)

#######################################
(GEN004880: CAT II) (Previously – G140)
#######################################

The SA will ensure the ftpusers file exists.

 files:
   "/etc/ftpusers" -> { "GEN004880", "GEN004920", "GEN004940" }
      comment => "CAT II (Previously - G140, G142, G143) UNIX STIG: 4.8.1 FTP Configuration",
       handle => "stig_files_redhat_etc_ftpusers",
       create => "true",
        perms => mo("640","root");

#######################################
(GEN004900: CAT II) (Previously – G141)
#######################################

The SA will ensure the ftpusers file contains the usernames of users not allowed to use FTP, and contains, at a minimum, the system pseudo-users usernames and root.

 files:
   "/etc/ftpusers" -> { "GEN004900" }
         comment => "CAT II (Previously - G141) UNIX STIG: 4.8.1 FTP Configuration",
          handle => "stig_files_redhat_editing_etc_ftpusers",
       edit_line => maintain_ftpusers("$(allusers_not_root)"),
              if => "$(allusers_not_root)_less_than_500";

bundle edit_line maintain_ftpusers(name)
{
 insert_lines:
  "root" -> { "GEN004900" }
     comment => "Add system accounts to /etc/ftpusers",
      handle => "maintain_ftpusers_insert_lines_root_gen004900";

  "avahi-autoipd" -> { "GEN004900" }
     comment => "Add system accounts to /etc/ftpusers",
      handle => "maintain_ftpusers_insert_lines_avahi_autoipd_gen004900";

  "$(name)" -> { "GEN004900" }
     comment => "Add system accounts to /etc/ftpusers",
      handle => "maintain_ftpusers_insert_lines_system_accounts_gen004900";
}

#######################################
(GEN004920: CAT II) (Previously – G142)
#######################################

The SA will ensure the owner of the ftpusers file is root.

-> See (GEN004900: CAT II) (Previously – G141)

#######################################
(GEN004940: CAT II) (Previously – G143)
#######################################

The SA will ensure the ftpusers file has permissions of 640, or more restrictive.

-> See (GEN004900: CAT II) (Previously – G141)

#######################################
(GEN005320: CAT II) (Previously – G225)
#######################################

The SA will ensure the snmpd.conf file has permissions of 700, or more restrictive.

 files:
   "/etc/snmp/snmpd.conf" -> { "GEN005320", "GEN005360" }
      comment => "CAT II (Previously - G225) UNIX STIG: 4.13 Simple Network Management Protocol (SNMP)",
       handle => "stig_files_redhat_etc_snmp_snmpd_conf",
        perms => mog("700","root","sys");

###################
(GEN005360: CAT II)
###################

The SA will ensure the owner of the snmpd.conf file is root with a group owner of sys and the owner of MIB files is root with a group owner of sys or the application.

-> See (GEN005320: CAT II) (Previously – G225)

#######################################
(GEN005400: CAT II) (Previously – G656)
#######################################

The SA will ensure the owner of the /etc/syslog.conf file is root with permissions of 640, or more restrictive.

-> See (GEN000440: CAT II) (Previously – G012)

#######################################
(GEN005420: CAT II) (Previously – G657)
#######################################

The SA will ensure the group owner of the /etc/syslog.conf file is root, sys, or bin.

-> See (GEN000440: CAT II) (Previously – G012)

###################
(GEN005540: CAT II)
###################

The SA will ensure SSH is configured to work with TCP_WRAPPERS except in cases where the encryption utility can be configured for IP filtering and still display banners before granting access.

-> See (GEN005500: CAT I) (Previously – G701)

###################
(GEN005600: CAT II)
###################

The SA will ensure IP forwarding is disabled if the system is not dedicated as a router.

-> See (GEN003600: CAT II)

#######################################
(GEN005740: CAT II) (Previously – G178)
#######################################

The SA will ensure the owner of the export configuration file is root.

 files:
   "/etc/exports" -> { "GEN005740", "GEN005760" }
      comment => "CAT II & III (Previously - G178, G179) UNIX STIG: 4.20 Network Filesystem (NFS)",
       handle => "stig_files_redhat_etc_export",
        perms => mog("644","root","root");

#######################################
(GEN006100: CAT II) (Previously – L050)
#######################################

The SA will ensure the owner of the/etc/samba/smb.conf file is root.

 files:
   "/etc/samba/smb.conf" -> { "GEN006100", "GEN006120", "GEN006140" }
      comment => "CAT II (Previously - L050, L051, L052) UNIX STIG: 4.24 Samba",
       handle => "stig_files_redhat_etc_samba_smb_conf",
        perms => mog("644","root","root");

#######################################
(GEN006120: CAT II) (Previously – L051)
#######################################

The SA will ensure the group owner of the /etc/samba/smb.conf file is root.

-> See (GEN006100: CAT II) (Previously – L050)

#######################################
(GEN006140: CAT II) (Previously – L052)
#######################################

The SA will ensure the /etc/samba/smb.conf file has permissions of 644, or more restrictive.

-> See (GEN006100: CAT II) (Previously – L050)

#######################################
(GEN006160: CAT II) (Previously – L054)
#######################################

The SA will ensure the owner of smbpasswd is root.

 files:
   "/usr/bin/smbpasswd" -> { "GEN006160", "GEN006180", "GEN006200" }
      comment => "CAT II (Previously - L054, L055, L056) UNIX STIG: 4.24 Samba",
       handle => "stig_files_redhat_usr_bin_smbpasswd",
        perms => mog("600","root","root");

#######################################
(GEN006180: CAT II) (Previously – L055)
#######################################

The SA will ensure group owner of smbpasswd is root.

-> See (GEN006160: CAT II) (Previously – L054)

#######################################
(GEN006200: CAT II) (Previously – L057)
#######################################

The SA will configure permissions for smbpasswd to 600, or more restrictive.

-> See (GEN006160: CAT II) (Previously – L054)

#######################################
(GEN006260: CAT II) (Previously – L154)
#######################################

The SA will ensure the /etc/news/hosts.nntp file has permissions of 600, or more restrictive.

 files:
   "/etc/news/hosts.nntp" -> { "GEN006260" }
      comment => "CAT II (Previously - L154) UNIX STIG: 4.25 Internet Network News (INN)",
       handle => "stig_files_redhat_etc_news_hosts_nttp",
        perms => m("600");

#######################################
(GEN006280: CAT II) (Previously – L156)
#######################################

The SA will ensure the /etc/news/hosts.nntp.nolimit file has permissions of 600, or more restrictive.

 files:
   "/etc/news/hosts.nntp.nolimit" -> { "GEN006280" }
      comment => "CAT II (Previously - L156) UNIX STIG: 4.25 Internet Network News (INN)",
       handle => "stig_files_redhat_etc_news_hosts_nttp_nolimit",
        perms => m("600");

#######################################
(GEN006300: CAT II) (Previously – L158)
#######################################

The SA will ensure the /etc/news/nnrp.access file has permissions of 600, or more restrictive.

 files:
   "/etc/news/nnrp.access" -> { "GEN006300" }
      comment => "CAT II (Previously - L158) UNIX STIG: 4.25 Internet Network News (INN)",
       handle => "stig_files_redhat_etc_news_nnrp_access",
        perms => m("600");

#######################################
(GEN006320: CAT II) (Previously – L160)
#######################################

The SA will ensure the /etc/news/passwd.nntp file has permissions of 600, or more restrictive.

 files:
   "/etc/news/passwd.nntp" -> { "GEN006320" }
      comment => "CAT II (Previously - L160) UNIX STIG: 4.25 Internet Network News (INN)",
       handle => "stig_files_redhat_etc_news_passwd_nntp",
        perms => m("600");

#######################################
(GEN006340: CAT II) (Previously – L162)
#######################################

The SA will ensure the owner of all files under the /etc/news subdirectory is root or news.

 files:
   "/etc/news" -> { "GEN006340", "GEN006360" }
           comment => "CAT II (Previously - L162, L164) UNIX STIG: 4.25 Internet Network New (INN)",
            handle => "stig_files_redhat_etc_news",
      depth_search => recurse("inf"),
             perms => og("root","root");

#######################################
(GEN006360: CAT II) (Previously – L164)
#######################################

The SA will ensure the group owner of all files in /etc/news is root or news.

-> See (GEN006340: CAT II) (Previously – L162)

#######################################
(GEN006520: CAT II) (Previously – G189)
#######################################

The SA will ensure security tools and databases have permissions of 740, or more restrictive.

 vars:
   "security_tools" -> { "GEN006520" }
      comment => "List of security tools and databases",
       handle => "stig_vars_redhat_security_tools",
        slist => {
                  "/etc/rc.d/init.d/iptables",
                  "/sbin/iptables",
                  "/usr/share/logwatch/scripts/services/iptables",
                 };

 files:
   "$(security_tools)" -> { "GEN006520" }
      comment => "CAT II (Previously - G189) UNIX STIG: 6 UNIX Security Tools",
       handle => "stig_files_redhat_security_tools",
        perms => mog("740","root","root");

###################
(GEN006620: CAT II)
###################

The SA will ensure an access control program (e.g., TCP_WRAPPERS) hosts.deny and hosts.allow files (or equivalent) are used to grant or deny system access to specific hosts.

 vars:
   "hosts_allow" -> { "GEN006620" }
      comment => "List of hosts to be assigned to /etc/hosts.allow",
       handle => "stig_vars_redhat_hosts_allow",
        slist => { 
                  "ALL:10.",
                  "ALL:172.16.",
                  "ALL:192.168.",
                 };

 files:
   "/etc/hosts.allow" -> { "GEN006620" }
        comment => "CAT II UNIX STIG: 6.6 Access Control Programs and TCP_WRAPPERS",
         handle => "stig_files_redhat_etc_hosts_allow",
      edit_line => append_if_no_lines("@(STIG.hosts_allow)");
   
   "/etc/hosts.deny" -> { "GEN006620" }
        comment => "CAT II UNIX STIG: 6.6 Access Control Programs and TCP_WRAPPERS",
         handle => "stig_files_redhat_etc_hosts_deny",
      edit_line => append_if_no_line("ALL: ALL");

######################################
(LNX00160: CAT II) (Previously – L074)
######################################

The SA will ensure the grub.conf file has permissions of 600, or more restrictive.

 files:
   "/boot/grub/grub.conf" -> { "LNX00160" }
      comment => "CAT II (Previously - L074) UNIX STIG: 12.4.1.1 Password Protecting the GRUB Console Boot Loader",
       handle => "stig_files_redhat_boot_grub_grub_conf",
        perms => m("600");

######################################
(LNX00220: CAT II) (Previously – L080)
######################################

The SA will ensure the lilo.conf file has permissions of 600 or more restrictive.

 files:
   "/etc/lilo.conf" -> { "LNX00220" }
      comment => "CAT II (Previously - L080) UNIX STIG: 12.4.1.2 Password Protecting the LILO Boot Loader",
       handle => "stig_files_redhat_etc_lilo_conf",
        perms => m("600");

######################################
(LNX00340: CAT II) (Previously – L142)
######################################

The SA will delete accounts that provide no operational purpose, such as games or operator, and will delete the associated software.

-> See (LNX00320: CAT I) (Previously – L140)

######################################
(LNX00360: CAT II) (Previously – L032)
######################################

The SA will enable the X server -audit (at level 4) and -s option (with 15 minutes as the timeout time) options.

 classes:
   "have_xwindows" -> { "LNX00360" }
         comment => "Check if the machine has X windows installed",
          handle => "stig_classes_redhat_have_xwindows",
      expression => fileexists("/etc/gdm/custom.conf");

 files:
   "/etc/gdm/custom.conf" -> { "LNX00360" }
         comment => "CAT II (Previously - L032) UNIX STIG: 12.10 X Windows",
          handle => "stig_files_redhat_etc_gdm_custom_conf",
       edit_line => maintain_gdm_custom_conf,
              if => "have_xwindows";

bundle edit_line maintain_gdm_custom_conf
{
 insert_lines:
"[server-Standard]
name=Standard server
command=/usr/bin/Xorg -br -audit 4 -s 15
flexible=true" -> { "LNX00360" }
       comment => "Enable X server audit level 4 and 15 minutes timeout time",
        handle => "maintain_gdm_custom_conf_insert_lines_lnx00360",
   insert_type => "preserve_block"; 
}

######################################
(LNX00400: CAT II) (Previously – L044)
######################################

The SA will ensure the owner of the /etc/login.access or /etc/security/access.conf file is root.

-> See (GEN001020: CAT II)

######################################
(LNX00420: CAT II) (Previously – L045)
######################################

The SA will ensure the group owner of the /etc/login.access or /etc/security/access.conf file is root.

-> See (GEN001020: CAT II)

######################################
(LNX00440: CAT II) (Previously – L046)
######################################

The SA will ensure/etc/login.access or /etc/security/access.conf file will be 640, or more restrictive.

-> See (GEN001020: CAT II)

######################################
(LNX00480: CAT II) (Previously – L204)
######################################

The SA will ensure the owner of the /etc/sysctl.conf file is root.

-> See (GEN003600: CAT II)

######################################
(LNX00500: CAT II) (Previously – L206)
######################################

The SA will ensure the group owner of the /etc/sysctl.conf file is root.

-> See (GEN003600: CAT II)

######################################
(LNX00520: CAT II) (Previously – L208)
######################################

The SA will ensure the /etc/sysctl.conf file has permissions of 600, or more restrictive.

-> (GEN003600: CAT II)

##################
(LNX00620: CAT II)
##################

The SA will ensure the group owner of the /etc/securetty file is root,sys, or bin.

-> See (GEN000980: CAT II) (Previously – G026)

##################
(LNX00640: CAT II)
##################

The SA will ensure the owner of the /etc/securetty file is root.

-> See (GEN000980: CAT II) (Previously – G026)

##################
(LNX00660: CAT II)
##################

The SA will ensure the /etc/securetty file has permissions of 640, or more restrictive.

-> See (GEN000980: CAT II) (Previously – G026)

##########################################################################################
#                                                                                        #
# CAT III:                                                                               #
#   Vulnerabilities that provide information that potentially could lead to compromise.  #
#                                                                                        #
##########################################################################################

########################################
(GEN001080: CAT III) (Previously – G229)
########################################

The SA will ensure the root shell is not located in /usr if /usr is partitioned.

 vars:
   "usr_dir" -> { "GEN001080" }
      comment => "/usr directory",
       handle => "stig_vars_redhat_usr_directory",
       string => "/usr/bin";

   "shells" -> { "GEN001080" }
      comment => "List of Root shells",
       handle => "stig_vars_redhat_root_shells",
        slist => { "bash", "sh" };

   "fstab_contents" -> { "GEN001080", "GEN002420" }
      comment => "All Contents of /etc/fstab",
       handle => "stig_vars_redhat_fstab_contents",
       string => readfile("/etc/fstab","4000");

 files:
   "$(usr_dir)/$(shells)" -> { "GEN001080" }
         comment => "CAT III, (Previously - G229) UNIX STIG: 3.3 Root Account",
          handle => "stig_files_redhat_usr_bin_root_shells",
          rename => disable,
              if => "have_usr_partitioned.have_usr_$(shells)";

   "$(usr_dir)/$(shells).cfdisabled" -> { "GEN001080" }
      comment => "CAT III, (Previously - G229) UNIX STIG: 3.3 Root Account",
       handle => "stig_files_redhat_usr_bin_root_shells_cfdisabled",
        perms => mog("400","root","root");

-> Also see (GEN001400: CAT I) (Previously – G047)

########################################
(GEN001280: CAT III) (Previously – G042)
########################################

The SA will ensure all manual page files (i.e., files in the man and cat directories) have permissions of 644, or more restrictive.

 vars:
   "manual_page_files" -> { "GEN001280" } 
      comment => "List of manual page files",
       handle => "stig_vars_redhat_manual_page_files",
        slist => { 
                  "/usr/share/man",
                 };

 files:
   "$(manual_page_files)" -> { "GEN001280" }
           comment => "CAT III, UNIX STIG: 3.4 File and Directory Controls",
            handle => "stig_files_redhat_manual_page_files",
      depth_search => recurse("inf"),
             perms => m("644");

########################################
(GEN001540: CAT III) (Previously – G067)
########################################

The user, application developers, and the SA will ensure files and directories (excluding a limited set of local initialization files) in user home directory trees will be owned by the user who owns the home directory.

-> See (GEN001480: CAT II) (Previously – G053)

########################################
(GEN001780: CAT III) (Previously – G112)
########################################

The SA will ensure global initialization files contain the command mesg n.

 vars:
   "global_init_files" -> { "GEN001720", "GEN001740", "GEN001760", "GEN001780" }
      comment => "List of Global Initialization files",
       handle => "stig_vars_redhat_global_init_files",
        slist => {
                  "/etc/profile",
                  "/etc/bashrc",
                  "/etc/environment",
                 };

 files:
   "$(global_init_files)" -> { "GEN001720", "GEN001740", "GEN001760", "GEN001780" }
        comment => "CAT II (Previously - G112) UNIX STIG: 3.8.1 Global Initialization Files",
         handle => "stig_files_redhat_global_init_files",
      edit_line => append_if_no_line("mesg n"),
          perms => mog("644","root","root");

########################################
(GEN001960: CAT III) (Previously - G610)
########################################

The SA will ensure local initialization files do not contain the command mesg –y or mesg y.

 files:
   "/home/$(users_list)/..*" -> { "GEN001960" }
        comment => "CAT III (Perviously - G610) 3.8.2 Local Initialization Files",
         handle => "stigs_files_redhat_5_remove_mesg_file",
      edit_line => remove_mesg_y;

bundle edit_line remove_mesg_y
{
 delete_lines:
  ".*mesg\h+\-y.*"
     comment => "Remove mesg -y",
      handle => "remove_mesg_y_delete_lines_gen001960_1";
  ".*mesg\h+y.*"
     comment => "Remove mesg y",
      handle => "remove_mesg_y_delete_lines_gen001960_2";
}

####################
(GEN003500: CAT III)
####################

The SA will ensure core dumps are disabled or restricted.

 files:
   "/etc/security/limits.conf" -> { "GEN003500" }
      comment => "CAT III UNIX STIG: 3.20.1 Restrict/Disable Core Dumps",
       handle => "stig_files_redhat_etc_security_limits_conf",
      edit_line => append_if_no_line("* - core 0");

####################
(GEN003520: CAT III)
####################

The SA will ensure the owner and group owner of the core dump data directory is root with permissions of 700, or more restrictive.

 files:
   "/var/crash" -> { "GEN003520" }
      comment => "CAT III UNIX STIG: 3.20.1 Restrict/Disable Core Dumps",
       handle => "stig_files_redhat_var_crash",
        perms => mog("700","root","root");

########################################
(GEN003860: CAT III) (Previously – V046)
########################################

The SA will ensure finger is not enabled.

 files:
   "/usr/bin/finger" -> { "GEN003860" }
      comment => "CAT II (Previously - V046) UNIX STIG: 4.3 Finger",
       handle => "stig_files_redhat_user_bin_finger",
       rename => disable;

-> Also see (GEN003860: CAT III) (Previously – V046)

########################################
(GEN005760: CAT III) (Previously – G179)
########################################

The SA will ensure the export configuration file has permissions of 644, or more restrictive.

-> See (GEN005740: CAT II) (Previously – G178)

#########################################################################################
#                                                                                       #
# CAT IV:                                                                               #
#   Vulnerabilities, when resolved, will prevent the possibility of degraded security.  #
#                                                                                       #
#########################################################################################

#######################################
(GEN001440: CAT IV) (Previously – G051)
#######################################

The SA will assign every user a home directory in the /etc/passwd file.

-> See (GEN001480: CAT II) (Previously – G053)

#######################################
(GEN001460: CAT IV) (Previously – G052)
#######################################

The SA will ensure all home directories defined in the /etc/passwd file exist.

-> See (GEN001480: CAT II) (Previously – G053)

#######################################
(GEN004440: CAT IV) (Previously – G133)
#######################################

The SA will ensure the sendmail logging level (the detail level of e-mail tracing and debugging information) in the sendmail.cf file is set to a value no lower than nine (9)

-> See (GEN004540: CAT II)
