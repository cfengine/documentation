---
layout: default
title: canonify
categories: [Reference, Functions, canonify]
published: true
alias: reference-functions-canonify.html
tags: [reference, data functions, functions, canonify]
---

**Prototype:** `canonify(text)`

**Return type:** `string`

**Description:** Convert an arbitrary string `text` into a legal class name.

This function turns arbitrary text into class data (See
[classify()][classify]).

**Arguments**:

* `text` : String containing non-identifier characters, in the range `.*`

**Example:**  


```cf3
    commands:

       "/var/cfengine/bin/$(component)"

           ifvarclass => canonify("start_$(component)");
```

