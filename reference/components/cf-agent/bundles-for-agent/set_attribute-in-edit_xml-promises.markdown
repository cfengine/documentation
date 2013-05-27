---
layout: default
title: set_attribute
categories: [Reference, Promise Types, files, edit_xml, set_attribute]
published: true
alias: reference-promise-types-files-edit_xml-set_attribute.html
tags: [reference, bundles, agent, set_attribute, edit_xml, xml, files_promises, promises]
---

This promise is part of the XML-editing model. It assures that an
attribute, with the given name and value, will be present in the
specified node within the XML file. If the attribute is not found, the
default promise is to insert the attribute, into the specified node. If
the attribute is already present, the default promise is to insure that
the attribute value is set to the given value. The specified node and
attribute value are each determined by body-attributes. The promise
object referred to is a literal string representation of the name of the
attribute to be set.

  

```cf3
bundle edit_xml example
  {
  set_attribute:
    "name"

    attribute_value => "cfe_host",
    select_xpath => "/Server/Service/Engine/Host";
  }
```

  

Note that typically only a single attribute, within a single selected
node, is set in each `set_attribute` promise. You may of course have
multiple promises that each set an attribute.

-   [attribute\_value in
    set\_attribute](#attribute_005fvalue-in-set_005fattribute)

#### `attribute_value`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Value of the attribute to be inserted into the XPath node
of the XML file

**Example**:  
   

```cf3
body attribute_value example(s)
{
attribute_value => "$(s)";
}
```

**Notes**:  
   
