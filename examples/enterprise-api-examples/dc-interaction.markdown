---
layout: default
title:  Enterprise API interaction with Design Center
published: true
sorting: 30
tags: [examples, enterprise, rest, api, design, center, sketches]
---

This is a simple walkthrough of a System::motd sketch activation
against CFEngine Enterprise Hub 192.168.33.2. There are several steps.
The most important step is where we define the sketch parameters.
Those are exactly what the Mission Portal **Design Center App**
generates through the GUI.

## Sample API call to Install sketch
* **Action**: `PUT`
* **URL**: http://192.168.33.2/api/dc/sketch/System::motd
* **HTTP return code**: 200
* **RESULT**:

```
{
    "System::motd":
    {
        "params\/debian_squeeze.json":"sketches\/system\/motd\/params\/debian_squeeze.json",
        "README.md":"sketches\/system\/motd\/README.md",
        "params\/example.json":"sketches\/system\/motd\/params\/example.json",
        "sketch.json":"sketches\/system\/motd\/sketch.json",
        "params\/debian_wheezy.json":"sketches\/system\/motd\/params\/debian_wheezy.json",
        "main.cf":"sketches\/system\/motd\/main.cf",
        "params\/simple.json":"sketches\/system\/motd\/params\/simple.json"
    },
    "sketches":{"System::motd":1}
}
```

## Sample API call to Define sketch parameters
* **Action**: `PUT`
* **URL**: http://192.168.33.2/api/dc/definition/myfirstsketchdefinition
* **HTTP return code**: 200
* **POST data**:

```
{
    'params': {'prepend_command': '/bin/uname -snrvm', 'motd_path': '/etc/motd', 'motd': 'hello dude2'},
    'sketchName': 'System::motd'
}
```

* **RESULT**: ```{"myfirstsketchdefinition":1}```

## Sample API call to Define environment
* **Action**: `PUT`
* **URL**: http://192.168.33.2/api/dc/environment/mymotdenvironment
* **HTTP return code**: 200
* **POST data**: ```{'environment': ['linux']}```
* **RESULT**: ```{"mymotdenvironment":1}```

## Sample API call to Activate sketch
* **Action**: `PUT`
* **URL**: http://192.168.33.2/api/dc/activation/myfirstsketchActivation/System::motd
* **HTTP return code**: 200

* **POST data**:

```
{
  'environmentName': 'mymotdenvironment',
  'bundleName': 'entry',
  'paramName': 'myfirstsketchdefinition',
  'sketchName': 'System::motd'
}
```
* **RESULT**:

```
{
  "System::motd":
  {
    "hash":"6cefdfedd0de3933c2ecac420b8d2aad",
    "params":["myfirstsketchdefinition"],
    "environment":"mymotdenvironment",
    "identifier":"myfirstsketchActivation",
    "target":"sketches",
    "bundle":"entry",
    "metadata":{"identifier":"myfirstsketchActivation","timestamp":1402657585}
  }
}
```

## Sample API call to Commit changes
* **Action**: `POST`
* **URL**: http://192.168.33.2/api/dc/workspace/commit
* **HTTP return code**: 200
* **POST data**: ```{'message': 'First-dc-api-commit', 'userEmail': 'test@test.com'}```
* **RESULT**: ```null```
