---
layout: default
title: Import & Export API
published: true
tags: [reference, enterprise, API, import, export]
---

Import & Export API provides users the ability to transfer Mission Portal data between hubs.

**See also:** [Export/Import Settings UI][Settings#Export/Import]

## Get available items to export

This API call provides a list of items available for export. Please note that the role of the user that authenticates to this API will affect what items are available. For example: the API user must have admin role in order to export settings.

**URI:** https://hub.example/data_transfer/api/exportItems

**Method:** GET

**Example request (curl):**

```
curl -k --user <username>:<password> \
  -X GET \
  https://hub.example/data_transfer/api/exportItems
```

**Example response:**

```
HTTP 200 Ok
[
    {
        "id": "categorizations",
        "name": "Host categorizations"
    },
    {
        "id": "dashboards",
        "name": "Dashboards"
    },
    {
        "id": "reports",
        "name": "Reports"
    },
    {
        "id": "settingsScripts",
        "name": "Custom notification scripts"
    },
    {
        "id": "users",
        "name": "Users"
    },
    {
        "id": "settingsRoles",
        "name": "Roles"
    },
    {
        "id": "settingsPreferences",
        "name": "Preferences"
    },
    {
        "id": "settingsAuthentication",
        "name": "LDAP authentication settings"
    },
    {
        "id": "settingsMail",
        "name": "Mail settings"
    },
    {
        "id": "settingsVCS",
        "name": "Version control repository"
    }
]
```

**Output:**

* **id**
    Item id. Use this id in export API call.
* **name**
    Name of export item.
    
    
## Export

**URI:** https://hub.example/data_transfer/api/export

**Method:** GET

**Parameters:**

* **item_id** *(array)*
    Item id to be exported.
    List of item ids you can obtain through [List of items to export][Import & Export API#Get available items to export]
        call described below. 
        
* **encryptionKey** *(string)*
    Encryption key to encrypt sensitive data. Please save this key to be able to import the data.
* **exportOnlyUserItems** *(string)*
    `true` - export only user items. `false` - export whole system data

**Example request (curl):**

```
curl -k -g --user <username>:<password> \
  -X GET \
  'https://hub.example/index.php/data_transfer/api/export?encryptionKey=key&exportOnlyUserItems=true&items[]=categorizations&items[]=dashboards&items[]=settingsAuthentication&items[]=settingsMail'

```

**Example response:**

```
HTTP 200 Ok
{
    "name": "export_12-14-2018_15:19:40.381400.phar",
}
```

**Output:**

* **name**
    Name of export file.
* **url**
    Url of export file.
    
## Download export file

**URI:** https://hub.example/data_transfer/api/download/:file_name:

**Method:** GET

**Parameters:**

* **file_name** *(string)*
  File name to be downloaded.
            

**Example request (curl):**

```
curl -k -g --user <username>:<password> \
  -X GET \
  --output /save/file/here/export_12-14-2018_15:19:40.381400.phar \
  'https://hub.example/index.php/data_transfer/api/download/export_12-14-2018_15:19:40.381400.phar'

```

**Example response:**

```
HTTP 200 Ok

Raw file contetnt
```

**Output headers:**

* Cache-Control: must-revalidate, post-check=0, pre-check=0
* Pragma: public
* Content-Description: File Transfer
* Content-Disposition: attachment; filename="export_12-14-2018_16:04:46.093500.phar"
* Content-Length: 337801
* Content-Type: application/octet-stream

 
## Analyze import file

This API call allows you to see short summary of file content.

**URI:** https://hub.example/data_transfer/api/analyzeImportFile

**Method:** POST

**Parameters:**

* **file** *(form data file)*
    File to be analyzed.

**Example request (curl):**

```
curl -k --user <username>:<password> \
-X POST \
-F file=@/path/to/file.phar  \
'https://hub.example/index.php/data_transfer/api/analyzeImportFile' 
```

**Example response:**

```
HTTP 200 Ok
{
    "categorizations": 3,
    "dashboards": "4, Widgets: 21 , Alerts: 31, Rules: 7",
    "settingsAuthentication": "yes",
    "settingsMail": "yes"
}
```

## Import

**URI:** https://hub.example/data_transfer/api/import

**Method:** POST

**Parameters:**

* **file** *(form data file)*
    File to be analyzed.
* **encryptionKey** *(string)*
    Encryption key that was set while export.
* **skipDuplicates** *(number)*
    Merge conflict strategy:
    `1` - skip duplicate items.
    `0` - overwrite duplicate items. 

**Example request (curl):**

```
curl -k --user <username>:<password> \
-X POST \
-F file=@/path/to/file.phar  \
-F encryptionKey=key \
-F skipDuplicates=1 \
'https://hub.example/index.php/data_transfer/api/analyzeImportFile' 
```

**Example response:**

```
HTTP 200 Ok
```

