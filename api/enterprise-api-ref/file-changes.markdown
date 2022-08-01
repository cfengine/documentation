---
layout: default
title: File Changes API
published: true
tags: [reference, enterprise, API, reporting, file changes]
---


## File changes statistics

**URI:** https://hub.cfengine.com/api/file-changes/statistics?fromTime=:fromTime&toTime=:toTime

**Method:** GET

Get file changes statistics by period.

* **fromTime** *(timestamp)*
    Include changes performed within interval. Format: `YYYY-mm-dd HH:MM:SS`
* **toTime** *(timestamp)*
    Include changes performed within interval. Format: `YYYY-mm-dd HH:MM:SS`

**Example request (curl):**

```
curl -k --user <username>:<password> \
  -X GET \
  "https://hub.cfengine.com/api/file-changes/statistics?fromTime=2019-07-01%2008:56&toTime=2019-07-08%2023:56"
'
```

**Example response:**

```
{
    "data": {
        "DIFF": {
            "20 Sep 2019": 0,
            "21 Sep 2019": 0,
            "22 Sep 2019": 0,
            "23 Sep 2019": 0,
            "24 Sep 2019": 0,
            "25 Sep 2019": 0,
            "26 Sep 2019": 0,
            "27 Sep 2019": 23
        },
        "C": {
            "20 Sep 2019": 0,
            "21 Sep 2019": 0,
            "22 Sep 2019": 0,
            "23 Sep 2019": 0,
            "24 Sep 2019": 0,
            "25 Sep 2019": 0,
            "26 Sep 2019": 0,
            "27 Sep 2019": 33
        },
        "S": {
            "20 Sep 2019": 0,
            "21 Sep 2019": 0,
            "22 Sep 2019": 0,
            "23 Sep 2019": 0,
            "24 Sep 2019": 0,
            "25 Sep 2019": 0,
            "26 Sep 2019": 0,
            "27 Sep 2019": 225
        }
    },
    "labels": {
        "DIFF": "Change in content (with file diff)",
        "C": "Change in content (based on file hash)",
        "S": "Change in file stats"
    },
    "dates": [
        "20 Sep 2019",
        "21 Sep 2019",
        "22 Sep 2019",
        "23 Sep 2019",
        "24 Sep 2019",
        "25 Sep 2019",
        "26 Sep 2019",
        "27 Sep 2019"
    ]
}
```

**Output:**

* **DIFF**
    Contains object with statistics of a change in content (with file diff), the object's key is change date and object's value is a number of changed files.
* **C**
    Contains object with statistics of a change in content (based on file hash), the object's key is change date and object's value is a number of changed files.
* **S**
    Contains object with statistics of a change in file stats, the object's key is change date and object's value is a number of changed files.
* **labels**
    Labels of `DIFF, C, S ` change types.
* **dates**
    The array of selected dates.
