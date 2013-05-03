---
layout: default
title: inferences-in-knowledge-promises
categories: [Bundles-for-knowledge,inferences-in-knowledge-promises]
published: true
alias: Bundles-for-knowledge-inferences-in-knowledge-promises.html
tags: [Bundles-for-knowledge,inferences-in-knowledge-promises]
---

### `inferences` promises in knowledge

\

\

~~~~ {.verbatim}
inferences:

  "is close to" 
           comment => "Cluster property",
         precedent => { "is close to" },
         qualifier => { "is close to" };

  "is far from" 
           comment => "Remote cluster property",
         precedent => { "is far from" },
         qualifier => { "is close to" };
~~~~

\

*History*: Was introduced in version 3.1.0

Inference promises are used to perform simple contextual reasoning in
the knowledge map. This feature is currently only supported in
commercial versions of CFEngine as it is developed.

The promiser of an inference promise is the *result* of the inference,
i.e. the conclusion to be drawn from combining two knowledge assertions.
The body specifies what existing associations must be in place between
topics in order to draw the conclusion between the start and the end.

~~~~ {.smallexample}
     
                 precedent                 qualifier
       TOPIC 1 -------------- TOPIC 2 --------------- TOPIC 3
     
                         promised inference
       TOPIC 1 --------------------------------------- TOPIC 3
     
~~~~

For example,

~~~~ {.smallexample}
     
              is mother to          is married to
       ALICE -------------- BOB ----------------- CAROL
     
                     is mother in law to
       ALICE --------------------------------------- CAROL
     
~~~~

Note that, like all promises, they are expected to be unique. Multiple
promisers promising different bodies is potentially inconsistent.
However, inference is inherently ambiguous, and we need to accommodate
multiple patterns. To this end, lists of regular expressions may be used
to match multiple instances.

-   [precedents in inferences](#precedents-in-inferences)
-   [qualifiers in inferences](#qualifiers-in-inferences)

#### `precedents`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: The foundational vector for a trinary inference

**Example**:\
 \

~~~~ {.verbatim}
inferences:

  "is far from" 
           comment => "Remote cluster property",
         precedent => { "is far from"},
         qualifier => { "is close to", "is far from" };
~~~~

**Notes**:\
 \

*History*: Was introduced in version 3.1.0b3,Nova 2.0.0b1 (2010)

A general regular expression may be used to match suitable alternatives,
so as to make the promise unique.

#### `qualifiers`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: The second vector in a trinary inference

**Example**:\
 \

~~~~ {.verbatim}
inferences:

  "is far from" 
           comment => "Remote cluster property",
         precedent => { "is far from" },
         qualifier => { "is close to|is far from" };
~~~~

**Notes**:\
 \

*History*: Was introduced in version 3.1.0 (2010)

A general regular expression may be used to match suitable alternatives,
so as to make the promise unique.
