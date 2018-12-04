---
layout: default
title: edit_xml
published: true
tags: [reference, bundle agent, edit_xml, xml, files promises, file editing]
---

The use of XML documents in systems configuration is widespread. XML
documents represent data that is complex and can be structured in
various ways. The XML based editing offers a powerful environment for
editing hierarchical and structured XML datasets.

XML editing promises are made in a `edit_xml`, which is then
used in the `edit_xml` attribute of a `files` promise. The promiser of
the `files` promise needs to be the XML document that is being edited.
Within an `edit_xml` bundle, various promise types are available to create
new or manipulate existing XML documents.

***

<!-- Use any suitable promise type for lookups in promise_attribute
# build_xpath
-->

## Common Attributes

The following attributes are available in all `edit_xml` promise types.

### build_xpath

**Description:** Builds an XPath within the XML file

Please note that when `build_xpath` is defined as an attribute within
an `edit_xml` promise body, the tree described by the specified XPath
will be verified and built BEFORE other `edit_xml` promises within same
promise body. Therefore, the file will not be empty during the execution
of such promises.

[%CFEngine_promise_attribute()%]

### select_xpath

**Description:** Select the XPath node in the XML file to edit

Edits to the XML document take place within the selected node. This
attribute is not used when inserting XML content into an empty file.

[%CFEngine_promise_attribute()%]

