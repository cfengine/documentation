---
layout: default
title:  Design Center REST API
published: true
tags: [reference, enterprise, REST, API, DC, sketch, URI, design center]
---

Please see [The Design Center API][The Design Center API] for the Design Center API
commands that are wrapped by the following Enterprise API commands.

## List of sketches

**URI:** https://hub.cfengine.com/api/dc/sketch

**Method:** GET

**Example response:**

```
{
  "meta": {
    "page": 1,
    "count": 69,
    "total": 69,
    "timestamp": 1383829723
  },
  "data": [
    {
      "Utilities::Staging": {
        "metadata": {
          "authors": [
            "Ted Zlatanov <tzz@lifelogs.com>"
          ],
          "version": 1,
          "name": "Utilities::Staging",
          "license": "MIT",
          "description": "Stage a directory of content to a target directory.",
          "tags": [
            "cfdc",
            "stage",
            "directory",
            "rsync"
          ],
          "depends": {
            "cfengine": {
              "version": "3.5.0"
            },
            "CFEngine::dclib::3.5.0": [],
            "CFEngine::dclib": [],
            "CFEngine::stdlib": {
              "version": 109
            }
          }
        }
      }
    }
  ]
}
```

## Information about specific sketch

**URI:** https://hub.cfengine.com/api/dc/sketch/:sketchName

**Method:** GET

**Example response:**

```
{
  "meta": {
    "page": 1,
    "count": 1,
    "total": 1,
    "timestamp": 1383831531
  },
  "data": [
    {
      "namespace": "cfdc_staging",
      "manifest": {
        "test.cf": {
          "comment": "Test Policy"
        },
        "params/demo.json": {
          "comment": "Demo parameters."
        },
        "README.md": {
          "documentation": true
        },
        "test.pl": {
          "test": true
        },
        "main.cf": {
          "desc": "main file"
        }
      },
      "interface": [
        "main.cf"
      ],
      "metadata": {
        "authors": [
          "Ted Zlatanov <tzz@lifelogs.com>"
        ],
        "version": 1,
        "name": "Utilities::Staging",
        "license": "MIT",
        "description": "Stage a directory of content to a target directory.",
        "tags": [
          "cfdc",
          "stage",
          "directory",
          "rsync"
        ],
        "depends": {
          "cfengine": {
            "version": "3.5.0"
          },
          "CFEngine::dclib::3.5.0": [],
          "CFEngine::dclib": [],
          "CFEngine::stdlib": {
            "version": 109
          }
        }
      },
      "entry_point": null,
      "api": {
        "stage": [
          {
            "name": "runenv",
            "type": "environment"
          },
          {
            "name": "metadata",
            "type": "metadata"
          },
          {
            "name": "source_dir",
            "validation": "PATH_ABSOLUTE_UNIX_OR_WINDOWS",
            "type": "string",
            "description": "Directory where the content can be found."
          },
          {
            "name": "dest_dir",
            "validation": "PATH_ABSOLUTE_UNIX_OR_WINDOWS",
            "type": "string",
            "description": "Directory where the content will be installed."
          },
          {
            "name": "owner",
            "validation": "USERNAME_UNIX",
            "type": "string",
            "description": "Owner of the dest_dir after staging."
          },
          {
            "name": "group",
            "validation": "USERNAME_UNIX",
            "type": "string",
            "description": "Owner of the dest_dir after staging."
          },
          {
            "name": "dirmode",
            "validation": "DIGITS",
            "type": "string",
            "description": "Directory mode to install."
          },
          {
            "name": "filemode",
            "validation": "DIGITS",
            "type": "string",
            "description": "File mode to install."
          },
          {
            "name": "options",
            "type": "array",
            "default": {
              "precommand": "/bin/echo precommand",
              "postcommand": "/bin/echo postcommand",
              "excluded": [
                ".cvs",
                ".svn",
                ".subversion",
                ".git",
                ".bzr"
              ]
            },
            "description": "Staging options."
          },
          {
            "name": "staged",
            "type": "return"
          },
          {
            "name": "directory",
            "type": "return"
          }
        ]
      }
    }
  ]
}
```

## Install sketch in the system

**URI:** https://hub.cfengine.com/api/dc/sketch/:sketchName

**Method:** PUT

**Example usage:** `Sample API call to Install sketch`

## List of available definitions

**URI:** https://hub.cfengine.com/api/dc/definition

**Method:** GET

**Example response:**

```
{
  "meta": {
    "page": 1,
    "count": 1,
    "total": 28,
    "timestamp": 1383831645
  },
  "data": [
    {
      "e180fc753487e749056f422f89420d06": {
        "Data::Classes": {
          "url_retriever": "/usr/bin/curl -s",
          "CF_MP_ENTRY_POINT": "bynet",
          "regex": "daas",
          "url": "http://asw.as",
          "classname": "as"
        }
      },
      "efce8022c7a53d3755ded38aa6b64730": {
        "Utilities::abortclasses": {
          "alert_only": "1",
          "trigger_file": "/COWBOY",
          "timeout": {
            "hours": 24,
            "years": 0,
            "minutes": 0,
            "action": "abortclasses_timeout_action_noop",
            "months": 0,
            "enabled": false,
            "days": "144"
          },
          "trigger_context": "any",
          "abortclass": "class"
        }
      }
    }
  ]
}
```

## Create new definition

**URI:** https://hub.cfengine.com/api/dc/definition/:definitionName

**Method:** PUT

**Example Request Body:**

```
{
  "sketchName": "test",
  "params": {
    "param_1": "value"
  }
}
```

**Example usage:** `Sample API call to Define sketch parameters`

## List of available environments

**URI:** https://hub.cfengine.com/api/dc/environment

**Method:** GET

**Example response:**

```
{
  "meta": {
    "page": 1,
    "count": 1,
    "total": 6,
    "timestamp": 1383831817
  },
  "data": [
    {
      "092b04a40fdd4cb8bfdb685f2c4a0328": {
        "verbose": "",
        "test": "",
        "activated": {
          "include": [
            "cfengine_3"
          ],
          "class_function": [
            {
              "function": "classmatch",
              "args": [
                "cfengine_3"
              ]
            }
          ],
          "exclude": []
        }
      }
    }
  ]
}
```

## Create new environment

**URI:** https://hub.cfengine.com/api/dc/environment/:name

**Method:** PUT

**Example Request Body:**

```
{
  "environment": [
    "cfengine3"
  ]
}
```

**Example usage:** `Sample API call to Define environment`

## List of available activations

**URI:** https://hub.cfengine.com/api/dc/activation

**Method:** GET

**Parameters:**

* **sketch** 
    Name of the sketch
* **details** 
    1 or 0 for extended details

**Example response:**

```
{
  "meta": {
    "page": 1,
    "count": 1,
    "total": 9,
    "timestamp": 1383831923
  },
  "data": [
    {
      "Data::Classes": [
        {
          "params": [
            "3603e753b8cb8ecc4d440dc91cd74742"
          ],
          "environment": "092b04a40fdd4cb8bfdb685f2c4a0328",
          "target": "sketches",
          "identifier": "cc",
          "bundle": "byfile",
          "metadata": {
            "identifier": "cc",
            "timestamp": 1379939700
          }
        },
        {
          "params": [
            "e180fc753487e749056f422f89420d06"
          ],
          "environment": "092b04a40fdd4cb8bfdb685f2c4a0328",
          "target": "sketches",
          "identifier": "aaa",
          "bundle": "bynet",
          "metadata": {
            "identifier": "aaa",
            "timestamp": 1380011681
          }
        }
      ],
      "Packages::removed": [
        {
          "params": [
            "8f068e0b3d7c2edc2d113a48b2485f94"
          ],
          "environment": "092b04a40fdd4cb8bfdb685f2c4a0328",
          "target": "sketches",
          "identifier": "12",
          "bundle": "removed",
          "metadata": {
            "identifier": "12",
            "timestamp": 1382366628
          }
        },
        {
          "params": [
            "e3134847d954d98d7419137b437cfd3c"
          ],
          "environment": "092b04a40fdd4cb8bfdb685f2c4a0328",
          "target": "sketches",
          "identifier": "xz",
          "bundle": "removed",
          "metadata": {
            "identifier": "xz",
            "timestamp": 1382367291
          }
        }
      ]
    }
  ]
}
```

## Activation details

**URI:** https://hub.cfengine.com/api/dc/activation/:activation_id/:sketchName

**Method:** GET

**Parameters:**

* **sketchName** 
    Name of the sketch
* **details**
    1 or 0 for host and other details

**Example response:**

```
{
  "meta": {
    "page": 1,
    "count": 1,
    "total": 1,
    "timestamp": 1383832020
  },
  "data": [
    [
      {
        "params": [
          "087b875ad637c6392acc3b78b66910cb"
        ],
        "environment": "092b04a40fdd4cb8bfdb685f2c4a0328",
        "target": "sketches",
        "identifier": "pokemon",
        "bundle": "installed",
        "metadata": {
          "identifier": "pokemon",
          "timestamp": 1383306456
        },
        "details": {
          "params": {
            "CF_MP_ENTRY_POINT": "installed",
            "pkgs_add": [
              "po"
            ]
          },
          "environments": {
            "verbose": "",
            "test": "",
            "activated": {
              "include": [
                "cfengine_3"
              ],
              "class_function": [
                {
                  "function": "classmatch",
                  "args": [
                    "cfengine_3"
                  ]
                }
              ],
              "exclude": []
            }
          },
          "hosts": []
        }
      }
    ]
  ]
}
```

## Create new activation

**URI:** https://hub.cfengine.com/api/dc/activation/:id

**Method:** PUT

**Example Request Body:**

```
{
  "environmentName": "092b04a40fdd4cb8bfdb685f2c4a0328",
  "paramName": "c53db12b79d5b2b74f319b91caf7e88f",
  "bundleName": "installed"
}
```

**Example usage:** `Sample API call to Activate sketch`

## Delete the activation

**URI:** https://hub.cfengine.com/api/dc/activation/:id

**Method:** DELETE

## List of validations

**URI:** https://hub.cfengine.com/api/dc/validation

**Method:** GET

## Get validation details

**URI:** https://hub.cfengine.com/api/dc/validation/:id

**Method:** GET

## Set validation type

**URI:** https://hub.cfengine.com/api/dc/validate/:validationType

**Method:** POST

**Example Request Body:**

```
{
  "validationData": [
    "asdasd"
  ]
}
```

## Get workspace

**URI:** https://hub.cfengine.com/api/dc/workspace

**Method:** GET

Checks for the workspace and returns the path.

## Post the commits

**URI:** https://hub.cfengine.com/api/dc/workspace/commit

**Method:** POST

**Example Request Body:**

```
{
  "message": "some message",
  "userEmail": "email.com"
}
```

**Example usage:** `Sample API call to Commit changes`

## Reset the user workspace

**URI:** https://hub.cfengine.com/api/dc/workspace/reset

**Method:** POST

## List workspace settings 

**URI:** https://hub.cfengine.com/api/dc/workspace/settings

**Method:** GET

Returns the settings of the workspace (VCS settings), 404 if not found.

## Create settings

**URI:** https://hub.cfengine.com/api/dc/workspace/settings

**Method:** POST

Content-Type header should be multipart/form-data.

**Example Request Body:**

```
{
  "gitServer": "serverurl",
  "gitEmail": "email.com",
  "gitBranch": "gitbranch name",
  "gitAuthor": "author name",
  "gitPrivateKey": "@filepath"
}
```

```bash
curl -F "gitServer=servername" -F "gitEmail=mail" -F "gitPrivateKey=@/home/user1/Desktop/id_rsa" http://server
```

## Delete settings

**URI:** https://hub.cfengine.com/api/dc/workspace/settings

**Method:** DELETE
