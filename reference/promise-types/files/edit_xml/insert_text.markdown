---
layout: default
title: insert_text
published: true
tags: [reference, bundle agent, edit_xml, xml, files promises, file editing]
---

This proimse type assures that a value string, containing the matching
substring, will be present in the specified node within the XML file. If the
substring is not found, the default promise is to append the substring to the
end of the existing value string, within the specified node. The specified node
is determined by body-attributes. The promise object referred to is a literal
string of text.

```cf3
    bundle edit_xml example
    {
    insert_text:

      "text content to be appended to existing text, including whitespace, within specified node"
        select_xpath => "/Server/Service/Engine/Host/Alias";
    }
```

Note that typically only a single value string, within a single
specified node, is inserted in each `insert_text` promise. You may of
course have multiple promises that each insert a value string.
