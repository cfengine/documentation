---
layout: default
title: build_xpath
published: true
tags: [reference, bundle agent, edit_xml, xml, files promises, file editing]
---

This promise type assures that a balanced XML tree, described by the given
XPath, will be present within the XML file. If the document is empty, the
default promise is to build the XML tree within the document. If the document is
not empty, the default promise is to verify the given XPath, and if necessary,
locate an insertion node and build the necessary portion of XML tree within
selected node. The insertion node is selected as the last unique node that is
described by the XPath and also found within the document. The promise object
referred to is a literal string representation of an XPath.

```cf3
    bundle edit_xml example
    {
    build_xpath:
       "/Server/Service/Engine/Host";
    }
```

Note that typically, only a single XPath is built in each `build_xpath`
promise. You may of course have multiple promises that each build an
XPath. The supported syntax used in building an XPath is currently
limited to a simple and compact format, as shown in the above example.
The XPath must begin with '/', as it is verified and built using an
absolute path, from the root node of the document.

The resulting document can then be further modified using `insert_tree`,
`set_text`, `set_attribute` etc promises. Using predicate statements to set
attributes or text values directly via build_xpath can lead to non-convergent
behavior, and is discouraged.


