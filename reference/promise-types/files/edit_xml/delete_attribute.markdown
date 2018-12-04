---
layout: default
title: delete_attribute
published: true
tags: [reference, bundle agent, edit_xml, xml, files promises, file editing]
---

This promise type assures that an attribute, with the given name, will not be
present in the specified node within the XML file. If the attribute is found,
the default promise is to remove the attribute, from within the specified node.
The specified node is determined by body-attributes. The promise object referred
to is a literal string representation of the name of the attribute to be
deleted.

```cf3
    bundle edit_xml example
    {
    delete_attribute:
      "attribute name"
        select_xpath => "/Server/Service/Engine/Host";
    }
```

Note that typically, only a single attribute, within a single specified
node, is deleted in each `delete_attribute` promise. You may of course
have multiple promises that each delete an attribute.

*See Also:* [Common `edit_xml` attributes][edit_xml#common edit_xml attributes]
