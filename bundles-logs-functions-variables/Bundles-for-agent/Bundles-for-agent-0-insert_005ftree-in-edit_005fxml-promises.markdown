---
layout: default
title: insert_005ftree-in-edit_005fxml-promises
categories: [Bundles-for-agent,insert_005ftree-in-edit_005fxml-promises]
published: true
alias: Bundles-for-agent-insert_005ftree-in-edit_005fxml-promises.html
tags: [Bundles-for-agent,insert_005ftree-in-edit_005fxml-promises]
---

### `insert_tree` promises in edit\_xml

\

This promise is part of the XML-editing model. It assures that a
balanced XML tree, containing the matching subtree, will be present in
the specified node within the XML file. If the subtree is not found, the
default promise is to insert the tree into the specified node. The
specified node is determined by body-attributes. The promise object
referred to is a literal string representation of a balanced XML tree.

\

~~~~ {.verbatim}
bundle edit_xml example
  {
  insert_tree:
    "Host name=\"cfe_host\">Alias>cfe_alias/Alias>/Host>"

    select_xpath => "/Server/Service/Engine";
  }
~~~~

\

Note that typically, only a single tree, within a single specified node,
is inserted in each `insert_tree` promise. You may of course have
multiple promises that each insert a tree.
