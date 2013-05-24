---
layout: default
title: delete_tree in edit_xml promises
categories: [Reference, Bundles for agent, delete_tree in edit_xml promises]
published: true
alias: reference-bundles-for-agent-delete-tree-in-edit-xml-promises.html
tags: [reference, bundles for agent, delete_tree, edit_xml, xml, files promises, promises]
---

This promise is part of the XML-editing model. It assures that a
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
    "Host name=\"cfe_host\">/Host>"

    select_xpath => "/Server/Service/Engine";
  }
```

  

Note that typically, only a single tree, within a single specified node,
is deleted in each `delete_tree` promise. You may of course have
multiple promises that each delete a tree.
