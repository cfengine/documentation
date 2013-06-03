---
layout: default
title: edit_xml
categories: [Reference, Promise Types, files, edit_xml]
published: true
alias: reference-promise-types-edit-xml-promises.html
tags: [reference, bundles, agent, edit_xml, xml, edit_xml promises, files promises]
---

The use of XML documents in systems configuration is widespread. XML
documents represent data that is complex and can be structured in
various ways. The XML based editing offers a powerful environment for
editing hierarchical and structured XML datasets.

## Attributes

The following attributes are available in all `edit_xml` promise types.

### build_xpath

**Description**: Builds an XPath within the XML file

Please note that when `build_xpath` is defined as an attribute within
an `edit_xml` promise body, the tree described by the specified XPath
will be verified and built BEFORE other `edit_xml` promises within same
promise body. Therefore, the file will not be empty during the execution
of such promises.

**Type**: `string`

**Allowed input range**: (arbitrary string)

### select_xpath

**Description**: Select the XPath node in the XML file to edit

Edits to the XML document take place within the selected node. This
attribute is not used when inserting XML content into an empty file.

**Type**: `string`

**Allowed input range**: (arbitrary string)
