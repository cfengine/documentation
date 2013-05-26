---
layout: default
title: insert_tree in edit_xml promises
categories: [Reference, Components, cf-agent, Bundles for agent,insert_tree in edit_xml promises]
published: true
alias: reference-components-bundles-for-agent-insert-tree-in-edit-xml-promises.html
tags: [reference, bundles, agent,insert_tree, edit_xml, xml, files promises]
---
  
This promise is part of the XML-editing model. It assures that a
balanced XML tree, containing the matching subtree, will be present in
the specified node within the XML file. If the subtree is not found, the
default promise is to insert the tree into the specified node. The
specified node is determined by body-attributes. The promise object
referred to is a literal string representation of a balanced XML tree.

  

```cf3
bundle edit_xml example
  {
  insert_tree:
    "Host name=\"cfe_host\">Alias>cfe_alias/Alias>/Host>"

    select_xpath => "/Server/Service/Engine";
  }
```

  

Note that typically, only a single tree, within a single specified node,
is inserted in each `insert_tree` promise. You may of course have
multiple promises that each insert a tree.
