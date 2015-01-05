---
layout: default
title: bundle edit_xml
published: true
tags: [reference, bundle agent, bundle edit_xml, xml, files promises, file editing]
---

The use of XML documents in systems configuration is widespread. XML
documents represent data that is complex and can be structured in
various ways. The XML based editing offers a powerful environment for
editing hierarchical and structured XML datasets.

XML editing promises are made in a `bundle edit_xml`, which is then
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

# build_xpath

This promise type assures that a
balanced XML tree, described by the given XPath, will be present within
the XML file. If the document is empty, the default promise is to build
the XML tree within the document. If the document is not empty, the
default promise is to verify the given XPath, and if necessary, locate
an insertion node and build the necessary portion of XML tree within
selected node. The insertion node is selected as the last unique node
that is described by the XPath and also found within the document. The
promise object referred to is a literal string representation of an
XPath.

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

# insert_tree

This promise type assures that a
balanced XML tree, containing the matching subtree, will be present in
the specified node within the XML file. If the subtree is not found, the
default promise is to insert the tree into the specified node. The
specified node is determined by body-attributes. The promise object
referred to is a literal string representation of a balanced XML tree.

```cf3
    bundle edit_xml example
    {
    insert_tree:

      "<Host name=\"cfe_host\"><Alias>cfe_alias</Alias></Host>"
        select_xpath => "/Server/Service/Engine";
    }
```

Note that typically, only a single tree, within a single specified node,
is inserted in each `insert_tree` promise. You may of course have
multiple promises that each insert a tree.

# delete_tree

This promise type assures that a
balanced XML tree, containing the matching subtree, will not be present
in the specified node within the XML file. If the subtree is found, the
default promise is to remove the containing tree from within the
specified node. The specified node is determined by body-attributes. The
promise object referred to is a literal string representation of a
balanced XML subtree.

```cf3
    bundle edit_xml example
    {
    delete_tree:

      "<Host name=\"cfe_host\"></Host>"
        select_xpath => "/Server/Service/Engine";
    }
```

Note that typically, only a single tree, within a single specified node,
is deleted in each `delete_tree` promise. You may of course have
multiple promises that each delete a tree.

# insert_text

This proimse type assures that a value
string, containing the matching substring, will be present in the
specified node within the XML file. If the substring is not found, the
default promise is to append the substring to the end of the existing
value string, within the specified node. The specified node is
determined by body-attributes. The promise object referred to is a
literal string of text.

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

# set_text

This promise type assures that a
matching value string will be present in the specified node within the
XML file. If the existing value string does not exactly match, the
default promise is to replace the existing value string, within the
specified node. The specified node is determined by body-attributes. The
promise object referred to is a literal string of text.

```cf3
    bundle edit_xml example
    {
    set_text:
      "text content to replace existing text, including whitespace, within selected node"

        select_xpath => "/Server/Service/Engine/Host/Alias";
    }
```

Note that typically only a single value string, within a single selected
node, is set in each `set_text` promise. You may of course have multiple
promises that each set a value string.


# delete_text

This promise type assures that a value
string, containing the matching substring, will not be present in the
specified node within the XML file. If the substring is found, the
default promise is to remove the existing value string, from within the
specified node. The specified node is determined by body-attributes. The
promise object referred to is a literal string of text.

```cf3
    bundle edit_xml example
    {
    delete_text:

      "text content to match, as a substring, of text to be deleted from specified node"
        select_xpath => "/Server/Service/Engine/Host/Alias";
    }
```

Note that typically, only a single value string, within a single
specified node, is deleted in each `delete_text` promise. You may of
course have multiple promises that each delete a value string.


# set_attribute

This promise type assures that an
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

## Attributes ##

### attribute_value

**Description:** Value of the attribute to be inserted into the XPath node
of the XML file

**Type:** `string`

**Allowed input range:** (arbitrary string)


# delete_attribute

This promise type assures that an
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
      "attribute name"
        select_xpath => "/Server/Service/Engine/Host";
    }
```

Note that typically, only a single attribute, within a single specified
node, is deleted in each `delete_attribute` promise. You may of course
have multiple promises that each delete an attribute.
