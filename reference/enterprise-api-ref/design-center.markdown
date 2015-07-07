---
layout: default
title:  Design Center REST API
published: true
tags: [reference, enterprise, REST, API, DC, sketch, URI, design center]
---

Please see [The Design Center API][] for the Design Center API
commands that are wrapped by the following Enterprise API commands.

### /api/dc/sketch *GET*

List of sketches.

**Example response:**

```json
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
        }]
    }
```

### /api/dc/sketch/:sketchName *GET*

Information about specific sketch.

**Example response:**

```json
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

### /api/dc/sketch/:sketchName *PUT*

Install sketch in the system. 

**Example usage:** `Sample API call to Install sketch`

### /api/dc/definition *GET*

List of available definitions.

**Example response:**

```json
{
    "meta": {
        "page": 1,
        "count": 1,
        "total": 28,
        "timestamp": 1383831645
    },
    "data": [
        {
            ...
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

### /api/dc/definition/:definitionName *PUT*

Create new definition.

**Example Request Body:**

```json
{
    "sketchName":"test",
    "params": {
        "hey":"ho"
    }
}
```

**Example usage:** `Sample API call to Define sketch parameters`

### /api/dc/environment *GET*

List of available environments

**Example response:**

```json
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
    ]
}
```

### /api/dc/environment/:name *PUT*

Create new environment.

**Example Request Body:**

```json
{
    "environment": ["cfengine3"]
}
```

**Example usage:** `Sample API call to Define environment`

### /api/dc/activation *GET*

List of available activations

**Fields:**
* **sketch** - name of the sketch
* **details** - 1 or 0 for details

**Example response:**

```json
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

### /api/dc/activation/:id/:sketchName *GET*

Info about specific activations.

**Fields:**
* **sketchName**- name of the sketch
* **details** - 1 or 0 for host and other details

**Example response:**

```json
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

### /api/dc/activation/:id *PUT*

Create new activation.

**Example Request Body:**

```json
{
     "environmentName":"092b04a40fdd4cb8bfdb685f2c4a0328",
     "paramName":"c53db12b79d5b2b74f319b91caf7e88f",
     "bundleName": "installed"
}
```

**Example usage:** `Sample API call to Activate sketch`

### /api/dc/activation/:id *DELETE*

Delete the activation.

### /api/dc/validation *GET*

Get list of validations.
    
### /api/dc/validation/:id *GET*

Get specific validation.

### /api/dc/validate/:validationType *POST*

**Example Request Body:**

```json
{
    "validationData": ["asdasd"]
}
```

### /api/dc/workspace *GET*

Checks for the workspace and returns the path.

### /api/dc/workspace/commit *POST*

Post the commits.

**Example Request Body:**

```json
{
    'message': "some message",
    'userEmail': 'email.com'
}
```

**Example usage:** `Sample API call to Commit changes`

### /api/dc/workspace/reset *POST*

Resets the user workspace.

### /api/dc/workspace/settings *GET*

Returns the settings of the workspace (VCS settings), 404 if not found.

### /api/dc/workspace/settings *POST*

Create the settings. Content-Type header should be multipart/form-data.

**Example Request Body:**

```json
{
    'gitServer':"serverurl",
    'gitEmail': "email.com" ,
    'gitBranch':"gitbranch name",
    'gitAuthor': "author name",
    'gitPrivateKey': "@filepath"
}

eg: curl -F "gitServer=servername" -F "gitEmail=mail" -F "gitPrivateKey=@/home/user1/Desktop/id_rsa" http://server
```

### /api/dc/workspace/settings *DELETE*

Delete settings.
