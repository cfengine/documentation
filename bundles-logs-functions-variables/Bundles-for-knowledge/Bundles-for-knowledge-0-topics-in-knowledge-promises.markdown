---
layout: default
title: topics-in-knowledge-promises
categories: [Bundles-for-knowledge,topics-in-knowledge-promises]
published: true
alias: Bundles-for-knowledge-topics-in-knowledge-promises.html
tags: [Bundles-for-knowledge,topics-in-knowledge-promises]
---

### `topics` promises in knowledge

\

Topic promises are part of the knowledge management engine. A topic is
any string that refers to a concept or subject that we wish to include
in a knowledge base. If a topic has a very long name, it is best to made
the promiser object a short name and use the `comment` field to add the
long explanation (e.g. unique acronym and full text).

~~~~ {.smallexample}
     
      topics:
     
       "topic string"
     
        comment = "long name..",
        ...;
     
~~~~

Topics form associative structures based entirely on an abstract space
of natural language. Actually, this is only slightly more abstract than
files, processes and commands etc. The main difference in knowledge
management is that there are no corrective or maintenance operations
associated with knowledge promises.

Class membership in knowledge management is subtly different from other
parts of CFEngine. If a topic lies in a certain class context, the topic
uses it as a type-label. This is used for disambiguation of subject-area
in searches rather than for disambiguation of rules between physical
environments.

\

~~~~ {.verbatim}
bundle knowledge example
{
topics:

   "Distro"
      comment     => "Distribution of linux",              
      association => a("is a packaging of","Linux","is packaged as a");
}
~~~~

\

Topics are basically identifiers, where the comment field here is a long
form of the subject string. Associations form semantic links between
topics. Topics can appear multiple times in order to form multiple
associations.

-   [association in topics](#association-in-topics)
-   [synonyms in topics](#synonyms-in-topics)
-   [generalizations in topics](#generalizations-in-topics)

#### `association` (body template)

**Type**: (ext body)

`forward_relationship`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Name of forward association between promiser topic and
associates

**Example**:\
 \

~~~~ {.verbatim}
     
     body association example
     {
     forward_relation => "is bigger than";
     }
     
~~~~

**Notes**:\
 \
 \

`backward_relationship`

**Type**: string

**Allowed input range**: (arbitrary string)

**Synopsis**: Name of backward/inverse association from associates to
promiser topic

**Example**:\
 \

~~~~ {.verbatim}
     body association example
     {
     # ..
     backward_relationship => "is less than";
     }
     
~~~~

**Notes**:\
 \

Denotes the inverse name which is used for \`moralizing' the association
graph. \

`associates`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: List of associated topics by this forward relationship

**Example**:\
 \

~~~~ {.verbatim}
     
     body association example(literal,scalar,list)
     
     {
     #...
     associates => { "literal", $(scalar),  @(list)};
     }
     
~~~~

**Notes**:\
 \

An element of an association that is a list of topics to which the
current topic is associated.

#### `synonyms`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: A list of words to be treated as equivalents in the
defined context

**Example**:\
 \

~~~~ {.verbatim}
 mathematics::

   "tree" synonyms => { "DAG", "directed acyclic graph" };
~~~~

**Notes**:\
 \

*History*: Was introduced in version 3.1.3a1,Nova 2.0.2a1 (2010)

This may be used to simplify the identification of synonyms during topic
searches.

#### `generalizations`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: A list of words to be treated as super-sets for the
current topic, used when reasoning

**Example**:\
 \

~~~~ {.verbatim}
 topics:

  persons::

     "mark"  generalizations => { "person", "staff", "human being" };

  any::

     "10.10.10.10/24" generalizations => { "network", "CIDR format" };
~~~~

**Notes**:\
 \

*History*: Was introduced in version 3.2, Nova 2.1 (2011)

Generalizations are ways of thinking about topics in more general terms.
They are somewhat like container \`types' or \`classes' in hierarchical
modeling, but they need not be mutually exclusive categories.

Generalizations may be used in topic-lifting, a kind of brain-storming
about issues, when searching for diagnostic explanations.
