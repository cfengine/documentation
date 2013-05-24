---
layout: default
title: set_text in edit_xml promises
categories: [Reference, Bundles for agent,set_text in edit_xml promises]
published: true
alias: reference-bundles-for-agent-set-text-in-edit-xml-promises.html
tags: [reference, bundles, agent, set_text, edit_xml, edit_xml promises, files promises]
---

This promise is part of the XML-editing model. It assures that a
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
