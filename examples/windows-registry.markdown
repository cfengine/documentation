---
layout: default
title: Windows Registry Examples 
published: true
sorting: 14
tags: [Examples,Windows Registry]
---

* [Windows registry][Windows Registry Examples#Windows registry]
* [unit_registry_cache.cf][Windows Registry Examples#unit_registry_cache.cf]
* [unit_registry.cf][Windows Registry Examples#unit_registry.cf]

## Windows registry

```cf3
body common control
{
bundlesequence => { "reg" };
}

bundle agent reg
{
vars:

  "value" string => registryvalue("HKEY_LOCAL_MACHINE\SOFTWARE\Cfengine AS\Cfengine","value3");

reports:

  windows::

   "Value extracted: $(value)";

}
```

## unit_registry_cache.cf

```cf3
body common control
{
 bundlesequence => {
#                   "registry_cache"

#                   "registry_restore"

                   };
}

#########################################


bundle agent registry_cache
{
 databases:
  windows::

     "HKEY_LOCAL_MACHINE\SOFTWARE\Adobe"
        database_operation => "cache",
        database_type      => "ms_registry",
        comment => "Save correct registry settings for Adobe products";
}

#########################################


bundle agent registry_restore
{
 databases:
  windows::

     "HKEY_LOCAL_MACHINE\SOFTWARE\Adobe"
        database_operation => "restore",
        database_type      => "ms_registry",
        comment => "Make sure Adobe products have correct registry settings";
}
```

## unit_registry.cf

```cf3
body common control
{
 
bundlesequence => { "databases" };
}


bundle agent databases

{
databases:

 windows::

  # Regsitry has (value,data) pairs in "keys" which are directories


#  "HKEY_LOCAL_MACHINE\SOFTWARE\Cfengine AS"


#    database_operation => "create", 

#    database_type     => "ms_registry";


#  "HKEY_LOCAL_MACHINE\SOFTWARE\Cfengine AS\Cfengine"


#    database_operation => "create", 

#    database_rows => { "value1,REG_SZ,new value 1", "value2,REG_SZ,new val 2"} ,

#    database_type     => "ms_registry";



  "HKEY_LOCAL_MACHINE\SOFTWARE\Cfengine AS\Cfengine"

    database_operation => "delete", 
    database_columns => { "value1", "value2" } ,
    database_type => "ms_registry";


# "HKEY_LOCAL_MACHINE\SOFTWARE\Cfengine AS\Cfengine"


#    database_operation => "cache",   # cache,restore


#    registry_exclude => { ".*Windows.*CurrentVersion.*", ".*Touchpad.*", ".*Capabilities.FileAssociations.*", ".*Rfc1766.*" , ".*Synaptics.SynTP.*", ".*SupportedDevices.*8086", ".*Microsoft.*ErrorThresholds" },


#    database_type     => "ms_registry";


"HKEY_LOCAL_MACHINE\SOFTWARE\Cfengine AS"

   database_operation => "restore",
   database_type      => "ms_registry";

}
```