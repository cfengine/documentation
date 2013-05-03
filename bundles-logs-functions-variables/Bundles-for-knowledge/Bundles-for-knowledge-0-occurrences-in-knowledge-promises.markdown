---
layout: default
title: occurrences-in-knowledge-promises
categories: [Bundles-for-knowledge,occurrences-in-knowledge-promises]
published: true
alias: Bundles-for-knowledge-occurrences-in-knowledge-promises.html
tags: [Bundles-for-knowledge,occurrences-in-knowledge-promises]
---

### `occurrences` promises in knowledge

\

Occurrences are documents or information resources that discuss topics.
An occurrence promise asserts that a particular document of text
resource in fact represents information about one or more topics. This
is used to construct references to actual information in a topic map.

~~~~ {.smallexample}
     
      occurrences:
     
        topic_name::
     
          "URL reference or literal string"
     
              represents = { "sub-topic disambiguator", ... },
              representation = "literal or url";
     
~~~~

\

~~~~ {.verbatim}
 Mark_Burgess::

     "http://www.iu.hio.no/~mark"
            represents => { "Home Page" };

 lvalue::

     "A variable identifier, i.e. the left hand side of an '=' association. The promiser in a variable promise."
            represents => { "Definitions" },
            representation => "literal";

 Editing_Files::

 "http://www.cfengine.org/confdir/customizepasswd.html" 
   represents => { "Setting up users" };

~~~~

\

Occurrences are pointers to information about topics. This might be a
literal text string or a URL reference to an external document.

-   [about\_topics in occurrences](#about_005ftopics-in-occurrences)
-   [represents in occurrences](#represents-in-occurrences)
-   [representation in occurrences](#representation-in-occurrences)

#### `about_topics`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of topics that the document or resource addresses

**Example**:\
 \

~~~~ {.verbatim}
 "/docs/SpecialTopic_RBAC.html#tag"

     represents => { "Text section" }, 
   about_topics => { "defining roles" };
~~~~

**Notes**:\
 \

*History*: Was introduced in 3.3.0, Nova 2.2.0 (2012)

As of CFEngine 3.3.0, this represents a list of topics on which the
named occurrence provides information.

History: Previously the context class had been used for this purpose,
but this led to confusion between usage or context and the subjects
covered by a document.

#### `represents`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of explanations for what relationship this document
has to the topics it is about

**Example**:\
 \

~~~~ {.verbatim}
occurrences:

  Promise_Theory::

    "A theory of autonomous actors that offer certainty through promises"

      represents     => { "Definitions" },
      representation => "literal";
~~~~

**Notes**:\
 \

The sub-topic or occurrence-type represented by the document reference
in a knowledge base. This string is intended as an annotation to the
reader about the nature of the information located in the occurrence
document. It should be used \`creatively'.

If the document type is an image and one of the items in this list is a
url, beginning with either / or http, then `cf-know` treats the
reference as a url to be reached when the image is clicked on.

#### `representation`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               literal
               url
               db
               file
               web
               image
               portal
~~~~

**Synopsis**: How to interpret the promiser string (e.g. actual data or
reference to data)

**Example**:\
 \

~~~~ {.verbatim}
occurrences:

  Promise_Theory::

    "A theory of autonomous actors that offer certainty through promises"

      represents     => { "Definitions" },
      representation => "literal";

~~~~

**Notes**:\
 \

This is a form of knowledge representation in a topic map occurrence
reference. If the type `portal` is used it assumes that a new website
should open in a new target window.
