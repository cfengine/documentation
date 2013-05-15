---
layout: default
title: delete fattribute in edit fxml promises
categories: [Bundles-for-agent,delete-fattribute-in-edit-fxml-promises]
published: true
alias: Bundles-for-agent-delete-fattribute-in-edit-fxml-promises.html
tags: [Bundles for agent,delete fattribute in edit fxml promises]
---

### `delete_attribute` promises in edit\_xml

  

This promise is part of the XML-editing model. It assures that an
attribute, with the given name, will not be present in the specified
node within the XML file. If the attribute is found, the default promise
is to remove the attribute, from within the specified node. The
specified node is determined by body-attributes. The promise object
referred to is a literal string representation of the name of the
attribute to be deleted.

  

```cf3
bundle edit_xml example
  {
  delete_attribute:
    "name"

    select_xpath => "/Server/Service/Engine/Host";
  }
```

  

Note that typically, only a single attribute, within a single specified
node, is deleted in each `delete_attribute` promise. You may of course
have multiple promises that each delete an attribute.
