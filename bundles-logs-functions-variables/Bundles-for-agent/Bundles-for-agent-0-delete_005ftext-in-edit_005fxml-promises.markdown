---
layout: default
title: delete_005ftext-in-edit_005fxml-promises
categories: [Bundles-for-agent,delete_005ftext-in-edit_005fxml-promises]
published: true
alias: Bundles-for-agent-delete_005ftext-in-edit_005fxml-promises.html
tags: [Bundles-for-agent,delete_005ftext-in-edit_005fxml-promises]
---

### `delete_text` promises in edit\_xml

\

This promise is part of the XML-editing model. It assures that a value
string, containing the matching substring, will not be present in the
specified node within the XML file. If the substring is found, the
default promise is to remove the existing value string, from within the
specified node. The specified node is determined by body-attributes. The
promise object referred to is a literal string of text.

\

~~~~ {.verbatim}
bundle edit_xml example
  {
  delete_text:
    "text content to match, as a substring, of text to be deleted from specified node"

    select_xpath => "/Server/Service/Engine/Host/Alias";
  }
~~~~

\

Note that typically, only a single value string, within a single
specified node, is deleted in each `delete_text` promise. You may of
course have multiple promises that each delete a value string.
