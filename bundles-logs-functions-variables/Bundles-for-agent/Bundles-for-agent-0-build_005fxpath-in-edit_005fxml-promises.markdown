---
layout: default
title: build_005fxpath-in-edit_005fxml-promises
categories: [Bundles-for-agent,build_005fxpath-in-edit_005fxml-promises]
published: true
alias: Bundles-for-agent-build_005fxpath-in-edit_005fxml-promises.html
tags: [Bundles-for-agent,build_005fxpath-in-edit_005fxml-promises]
---

### `build_xpath` promises in edit\_xml

\

This promise is part of the XML-editing model. It assures that a
balanced XML tree, described by the given XPath, will be present within
the XML file. If the document is empty, the default promise is to build
the XML tree within the document. If the document is not empty, the
default promise is to verify the given XPath, and if necessary, locate
an insertion node and build the necessary portion of XML tree within
selected node. The insertion node is selected as the last unique node
that is described by the XPath and also found within the document. The
promise object referred to is a literal string representation of an
XPath.

\

~~~~ {.verbatim}
bundle edit_xml example
  {
  build_xpath:
    "/Server/Service/Engine/Host[ @name=\"cfe_host\" | Alias = cfe_alias ]";
  }
~~~~

\

Note that typically, only a single XPath is built in each `build_xpath`
promise. You may of course have multiple promises that each build an
XPath. The supported syntax used in building an XPath is currently
limited to a simple and compact format, as shown in the above example.
The XPath must begin with '/', as it is verified and built using an
absolute path, from the root node of the document.
