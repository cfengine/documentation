---
layout: default
title: set_005ftext-in-edit_005fxml-promises
categories: [Bundles-for-agent,set_005ftext-in-edit_005fxml-promises]
published: true
alias: Bundles-for-agent-set_005ftext-in-edit_005fxml-promises.html
tags: [Bundles-for-agent,set_005ftext-in-edit_005fxml-promises]
---

### `set_text` promises in edit\_xml

\

This promise is part of the XML-editing model. It assures that a
matching value string will be present in the specified node within the
XML file. If the existing value string does not exactly match, the
default promise is to replace the existing value string, within the
specified node. The specified node is determined by body-attributes. The
promise object referred to is a literal string of text.

\

~~~~ {.verbatim}
bundle edit_xml example
  {
  set_text:
    "text content to replace existing text, including whitespace, within selected node"

    select_xpath => "/Server/Service/Engine/Host/Alias";
  }
~~~~

\

Note that typically only a single value string, within a single selected
node, is set in each `set_text` promise. You may of course have multiple
promises that each set a value string.
