```console
root@hub:~# curl -k \
--user <admin>:<password> \
-X POST \
https://hub.localdomain/api/inventory  \
-H 'content-type: application/json' \
-d '{
      "sort":"Host name",
      "filter":{
         "CFEngine version":{
            "not_match":"{{site.cfengine.branch}}.0"
         }
      },
      "select":[
         "Host name",
         "CFEngine version"
       ]
    }'
```
