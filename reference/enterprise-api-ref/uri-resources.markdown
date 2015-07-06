---
layout: default
title:  URI Resources
published: true
tags: [reference, enterprise, REST, API, reporting, sql, URI, ldap]
---

### /api

**Supported Operations**: `GET`

**Fields**:

-   `apiName` *(string)* Human-friendly API name.
-   `apiVersion` *(string)* API version string.
-   `enterpriseVersion` *(string)* Version of the CFEngine Enterprise
    build.
-   `uiVersion` *(string)* The internal build number of the Enterprise UI
    (since 3.6)
-   `coreVersion` *(string)* The version of CFEngine Core (Community)
    the Enterprise version was built against.
-   `databaseHostname` *(string)* Hostname (or IP) of the database the
    API is connected to.
-   `databasePort` *(integer)* Port number of the database the API is
    connected to.
-   `authenticated` *("internal", "external")*, Whether the request
    was authenticated using the internal users table or an external
    source.
-   `license.expires` *(integer)* Time when the license expires.
-   `license.installTime` *(integer)* Time when the license was
    installed.
-   `license.owner` *(string)* The name of the license owner.
-   `license.granted` *(integer)* Host number capacity granted by the
    license.
-   `license.licenseUsage.lastMeasured` *(integer)* Time when license
    usage was last updated.
-   `license.licenseUsage.samples` *(integer)* Number of samples
    collected for license usage.
-   `license.licenseUsage.minObservedLevel` *(integer)* Minimum number
    of observed host licenses in use.
-   `license.licenseUsage.minObservedLevel` *(integer)* Maximum number
    of observed host licenses in use.
-   `license.licenseUsage.meanUsage` *(integer)* Average number of
    observed host licenses in use.
-   `license.licenseUsage.meanCumulativeUtilization` *(integer)* (not
    sure)
-   `license.licenseUsage.usedToday` *(integer)* Total number of host
    licenses observed used today.


### /api/settings

**Supported Operations**: `GET`, `POST`

**Fields**:

-   `rbacEnabled` *(boolean)* Whether RBAC is applied to requests.
-   `hostIdentifier` *(string)* The identfying string for hosts, such as name or IP.
-   `ldapEnabled` *(boolean)* Whether external authentication is
    activated.
-   `ldapBaseDN` *(string)* LDAP BaseDN to use for external LDAP
    requests.
-   `ldapFilter` *(string)* Filter for LDAP objects.
-   `ldapEncryption` *("plain", "ssl", "tls")* Type of LDAP binding to
    establish to external LDAP server. (Default: "plain").
-   `ldapHost` *(string)* Hostname of external LDAP server.
-   `ldapLoginAttribute` *(string)* LDAP attribute to use for
    usernames. (default: "uid").
-   `ldapUsername` *(string)* LDAP username.
-   `ldapPassword` *(string)* LDAP password.
-   `ldapUsersDirectory` *(string)* Attribute and value to qualify the
    directory in which to look up users, e.g. "ou=people".
-   `ldapPort` *(integer)* Port for external LDAP connections not
    using SSL. (default 389).
-   `ldapPortSSL` *(integer)* Port for external LDAP connections using
    SSL. (default 636).
-   `blueHostHorizon` *(integer)* Time interval (seconds) for when to
    consider a host unreachable. (default 900).
-   `logLevel` *("emergency", "alert", "critical", "error", "warning",
    "notice", "info", "debug")* Syslog filter specifying the severity
    level at which messages produced by the API should be emitted to
    syslog and apache.log. (default: error).
-   `sketchActivationAlertTimeout` *(integer)* Global timeout in
    minutes for sketch activation alerts.


### /api/user

**Supported Operations**: `GET`  

**Query Parameters**:

-   `id` *(regex string)* Regular expression for filtering usernames.
-   `external` *("true", "false")* Returns only internal users (false)
    or only external (true), or all if not specified.

### /api/user/:id

**Supported Operations**: `GET`, `PUT`, `POST`, `DELETE`

**Fields**:

-   `id` *(string)* ID of a user.
-   `password` *(string)* Password of a user. (Never returned from
    API).
-   `email` *(string)* Email address associated with user.
-   `roles` *(array of strings)* Set of IDs of roles a user is in.
    (Default: empty)
-   `external` *(boolean)* Whether or not the user was found
    externally (LDAP).


### /api/role

**Supported Operations**: `GET`


### /api/role/:id

**Supported Operations**: `GET`, `PUT`, `POST`, `DELETE`

**Fields**:

-   `id` *(string)* ID of a role.
-   `description` *(string)* Arbitrary text describing the role
-   `includeContext` *(comma delimited string of regular expression
    strings)* Includes hosts visible to the users in the role.
-   `excludeContext` *(comma delimited string of regular expression
    strings)* Excludes bundles visible to the users in the role.
-   `includeBundles` *(comma delimited string of regular expression
    strings)* Includes bundles visible to the users in the role.
-   `excludeBundles` *(comma delimited string of regular expression
    strings)* Excludes bundles visible to the users in the role.


### /api/host

**Supported Operations**: `GET` ,`DELETE`

*Query Parameters*:

-   `include-context` *(comma delimited string of regular expression
    strings)* Includes hosts having context matching the expression.
-   `exclude-context` *(comma delimited string of regular expression
    strings)* Excludes hosts having context matching the expression.


### /api/host/:host-id

-   `id` *(string)* ID of a host.
-   `hostname` *(string)* Hostname of a host.
-   `ip` *(string)* IP address of a host.

#### /api/host/:host-id/vital/:vital-id

**Supported Operations**: `GET`

*Query Parameters*:

-   `from` *(integer)* Timestamp marking the start of the interval for
    which to fetch data. Data is only available going back one week.
-   `to` *(integer)* End of data interval to be fetched.

**Fields**:

-   `id` *(string)* ID of vital sign.
-   `description` *(string)* Description of vital sign.
-   `units` *(string)* Measurement unit of vital sign.
-   `timestamp` *(integer)* Timestamp of the last received data point.
-   `values` *(array of [ t, y ], where t is the sample timestamp)*
    Vital sign data.

### /api/query

**Supported Operations**:  
`POST`

**Fields**:

-   `query` *(string)* SQL query string.
-   `sortColumn` *(string)* Column on which to sort results. This is
    applied to the result of the SQL query and can be considered post
    processing. The Mission Portal uses this to sort cached reports.
-   `sortDescending` *(boolean)* Apply post-sorting in descending order.
-   `skip` *(integer)* Number of results to skip for the processed
    query. The Mission Portal uses this for pagination on cached
    results.
-   `limit` *(integer)* Limit the number of results in the processed
    query.
-   `disableCache` *(boolean)* Don't use cached data


### /api/query/async

**Supported Operations**: `POST`

**Fields**:

-   `query` *(string)* SQL query string.
-   `id` *(string)* ID of the query job.
-   `error` *(string)* Error if anything went wrong.


### /api/query/async/:async-query-id

**Supported Operations**: `GET`, `DELETE`

**Fields**:

-   `id` *(string)* ID of the query job.
-   `percentageComplete` *(integer)* Processing status for the query.
-   `href` *(string)* Download link for the finished report.
-   `error` *(string)* Error if anything went wrong.

### Enterprise Design Center API

Please see [The Design Center API][] for the Design Center API
commands that are wrapped by the following Enterprise API commands.

#### /api/dc/sketch
* **GET**: List of sketches 

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

#### /api/dc/sketch/:name

* **GET**: info about specific sketch 

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
#### /api/dc/sketch/:sketchName
* **PUT**: install sketch in the system

#### /api/dc/definition
* **GET**: List of available definitions

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



#### /api/dc/definition/:definitionName
* *definitionName*: name of the definition 	
* **PUT**: Create new definition
* Request Body:

```json
	{
	"sketchName":"test",
	"params": {
		"hey":"ho"
		}
	}
```

#### /api/dc/environment
* **GET**: List of available environments

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

#### /api/dc/environment/:environmentName
* *environmentName*: name of the environment
* **PUT**: Create new environment
* Request Body:

```json
{
	"environment": ["cfengine3"]
}
```

#### /api/dc/activation?sketch=<sketchname>&details=1
*GET*: List of available activations

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

#### /api/dc/activation/:id/:sketchName?details+	
* *id*: (identifier of activation)
* *sketchName*: name of the sketch
* *Params details*: 1 or 0 for host and other details

* **GET**: Info about specific activations

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

* **PUT**: Create new activation

```json
	Request body:
	{
             
	     "environmentName":"092b04a40fdd4cb8bfdb685f2c4a0328",
	     "paramName":"c53db12b79d5b2b74f319b91caf7e88f",
 	     "bundleName": "installed"
	}
```

* **DELETE**: Delete the activation

#### /api/dc/validation
* **GET**: Get list of validations
	
#### /api/dc/validation/:id
* **GET**: Get specific validations

#### /api/dc/validate/:validationType
* *validationType*: specific validation type
* **POST**: validate the data 
* Request Body:

```json
	{
	"validationData":["asdasd"]
	}
```

#### /api/dc/workspace
* **GET**: checks for the workspace and returns the path

#### /api/dc/workspace/commit
* **POST**: Post the commits

```json
	Request Body:
	{
	'message': "some message",
    	'userEmail': 'email.com'
	}
```

#### /api/dc/workspace/reset
* **POST**: Resets the user workspace

#### /api/dc/workspace/settings
* **GET**: Returns the settings of the workspace (VCS settings), 404 if not found
* **POST**: Create the settings. Content-Type header should be multipart/form-data
* **DELETE**: Delete settings

```json
		Request Body:
		{
		 'gitServer':"serverurl",
		 'gitEmail': "email.com" ,
		 'gitBranch':"gitbranch name",
		 'gitAuthor': "author name",
		 'gitPrivateKey': "@filepath"
		}
		eg: curl -F "gitServer=servername" -F "gitEmail=mail" -F "gitPrivateKey=@/home/user1/Desktop/id_rsa" http://server
		
```
