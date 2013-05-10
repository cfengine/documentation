---
layout: default
title: 
categories: [Bundles-for-agent]
published: true
alias: Bundles-for-agent.html
tags: [Bundles-for-agent]
---

Bundles of `agent`
------------------

  

```
     
     bundle agent main(parameter)
     
     {
     vars:
     
       "sys_files"    slist        = {
                                      "/etc/passwd",
                                      "/etc/services"
                                      };
     files:
     
       "$(sys_files)" perms        = p("root","0644"),
                      changes      = trip_wire;
     
       "/etc/shadow"  perms        = p("root","0600"),
                      changes      = trip_wire;
     
       "/usr"         changes      = trip_wire,
                      depth_search = recurse("inf");
     
       "/tmp"         delete       = tidy,
                      file_select  = days("2"),
                      depth_search = recurse("inf");
     
     }
     
```

  

Agent bundles contain user-defined promises for `cf-agent`. The types of
promises and their corresponding bodies are detailed below.

-   [classes in common promises](#classes-in-common-promises):
-   [defaults in common promises](#defaults-in-common-promises):
-   [meta in common promises](#meta-in-common-promises):
-   [reports in common promises](#reports-in-common-promises):
-   [vars in common promises](#vars-in-common-promises):
-   [\* in common promises](#Miscellaneous-in-common-promises):
-   [commands in agent promises](#commands-in-agent-promises):
-   [databases in agent promises](#databases-in-agent-promises):
-   [guest\_environments in agent
    promises](#guest_005fenvironments-in-agent-promises):
-   [files in agent promises](#files-in-agent-promises):
-   [\* in edit\_line
    promises](#Miscellaneous-in-edit_005fline-promises):
-   [delete\_lines in edit\_line
    promises](#delete_005flines-in-edit_005fline-promises):
-   [insert\_lines in edit\_line
    promises](#insert_005flines-in-edit_005fline-promises):
-   [field\_edits in edit\_line
    promises](#field_005fedits-in-edit_005fline-promises):
-   [replace\_patterns in edit\_line
    promises](#replace_005fpatterns-in-edit_005fline-promises):
-   [\* in edit\_xml promises](#Miscellaneous-in-edit_005fxml-promises):
-   [build\_xpath in edit\_xml
    promises](#build_005fxpath-in-edit_005fxml-promises):
-   [delete\_tree in edit\_xml
    promises](#delete_005ftree-in-edit_005fxml-promises):
-   [insert\_tree in edit\_xml
    promises](#insert_005ftree-in-edit_005fxml-promises):
-   [delete\_attribute in edit\_xml
    promises](#delete_005fattribute-in-edit_005fxml-promises):
-   [set\_attribute in edit\_xml
    promises](#set_005fattribute-in-edit_005fxml-promises):
-   [delete\_text in edit\_xml
    promises](#delete_005ftext-in-edit_005fxml-promises):
-   [set\_text in edit\_xml
    promises](#set_005ftext-in-edit_005fxml-promises):
-   [insert\_text in edit\_xml
    promises](#insert_005ftext-in-edit_005fxml-promises):
-   [interfaces in agent promises](#interfaces-in-agent-promises):
-   [methods in agent promises](#methods-in-agent-promises):
-   [outputs in agent promises](#outputs-in-agent-promises):
-   [packages in agent promises](#packages-in-agent-promises):
-   [processes in agent promises](#processes-in-agent-promises):
-   [services in agent promises](#services-in-agent-promises):
-   [storage in agent promises](#storage-in-agent-promises):
-   [access in server promises](#access-in-server-promises):
-   [roles in server promises](#roles-in-server-promises):
-   [measurements in monitor
    promises](#measurements-in-monitor-promises):
