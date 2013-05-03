---
layout: default
title: things-in-knowledge-promises
categories: [Bundles-for-knowledge,things-in-knowledge-promises]
published: true
alias: Bundles-for-knowledge-things-in-knowledge-promises.html
tags: [Bundles-for-knowledge,things-in-knowledge-promises]
---

### `things` promises in knowledge

\

*History*: Was introduced in version 3.2, Nova 2.1 (2011)

Things are a special subset of topics that behave like objects in the
world. We have separated out things from more abstract topics to make it
easier to talk about the.

Things are typically objects we make inventories of, that influence one
another and might be connected. We interact with things in IT management
much more concretely than we do with abstract topics.

To make it simpler to talk about things, `things` promises were
introduced.

\

~~~~ {.verbatim}
body knowledge TheRealWorld
{
things:

  networks::

     "10.20.30.40"  is_connected_to => { "router 46", "computers::computer 23" };

  computers::

     "computer 23" belongs_to => { "Phileas Phogg", "ACME punchcard agency" };

}
~~~~

\

Things promises are in every way equivalent to the more general topics
promises. Things can be extended as topics. The contexts are
interchangeable between things and topics. The only purpose of things is
to make plainer a description of the \`physical' configurations of
regular worldly things.

-   [synonyms in things](#synonyms-in-things)
-   [affects in things](#affects-in-things)
-   [belongs\_to in things](#belongs_005fto-in-things)
-   [causes in things](#causes-in-things)
-   [certainty in things](#certainty-in-things)
-   [determines in things](#determines-in-things)
-   [generalizations in things](#generalizations-in-things)
-   [implements in things](#implements-in-things)
-   [involves in things](#involves-in-things)
-   [is\_caused\_by in things](#is_005fcaused_005fby-in-things)
-   [is\_connected\_to in things](#is_005fconnected_005fto-in-things)
-   [is\_determined\_by in things](#is_005fdetermined_005fby-in-things)
-   [is\_followed\_by in things](#is_005ffollowed_005fby-in-things)
-   [is\_implemented\_by in
    things](#is_005fimplemented_005fby-in-things)
-   [is\_located\_in in things](#is_005flocated_005fin-in-things)
-   [is\_measured\_by in things](#is_005fmeasured_005fby-in-things)
-   [is\_part\_of in things](#is_005fpart_005fof-in-things)
-   [is\_preceded\_by in things](#is_005fpreceded_005fby-in-things)
-   [measures in things](#measures-in-things)
-   [needs in things](#needs-in-things)
-   [provides in things](#provides-in-things)
-   [uses in things](#uses-in-things)

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

#### `affects`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Special fixed relation for describing topics that are
things

**Example**:\
 \

~~~~ {.verbatim}
things:

   "The Moon"   affects => {  "surf", "tides" };
~~~~

**Notes**:\
 \
 *History*: Was introduced in version 3.2, Nova 2.1 (2011)

#### `belongs_to`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Special fixed relation for describing topics that are
things

**Example**:\
 \

~~~~ {.verbatim}
things:

  "router-123" 

           comment => "Located at 23 Marlborough Street",
        belongs_to => { "company::cfengine" };
~~~~

**Notes**:\
 \

*History*: Was introduced in version 3.2, Nova 2.1 (2011)

#### `causes`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Special fixed relation for describing topics that are
things

**Example**:\
 \

~~~~ {.verbatim}
bundle knowledge test
{
things:

  "program crash" causes => { "rootprocs_low_anomaly" },
                     certainty => "possible";

}
~~~~

**Notes**:\
 \

*History*: Was introduced in version 3.2.0, Nova 2.1.0 (2011)

The complement of \`is\_caused\_by' for convenience.

#### `certainty`

**Type**: (menu option)

**Allowed input range**: \

~~~~ {.example}
               certain
               uncertain
               possible
~~~~

**Synopsis**: Selects the level of certainty for the proposed knowledge,
for use in inferential reasoning

**Example**:\
 \

~~~~ {.verbatim}
bundle knowledge test
{
things:

  "router one" is_connected_to => { "computer one" },
                     certainty => "uncertain";

  "router"             affects => { "network services" },
                     certainty => "possible";
}
~~~~

**Notes**:\
 \

*History*: Was introduced in version 3.1.5, Nova 2.1 (2011)

Certainty is used in automated reasoning about knowledge. It modifies
the relationships between things. For example, the certain relationship
\`is affected by' would become \`can be affected by' (possible) or
\`might be affected by' (uncertain).

#### `determines`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Special fixed relation for describing topics that are
things

**Example**:\
 \

~~~~ {.verbatim}
things:

  "router one" determines => { "network connectivity" },
                certainty => "uncertain";
~~~~

**Notes**:\
 \

*History*: Was introduced in version 3.1.5, Nova 2.1 (2011)

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

#### `implements`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Special fixed relation for describing topics that are
things

**Example**:\
 \

~~~~ {.verbatim}
things:

   "my promise"  
              implements => { "my goal" };
~~~~

**Notes**:\
 \

*History*: Was introduced in 3.4.0

#### `involves`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Special fixed relation for describing topics that are
things

**Example**:\
 \

~~~~ {.verbatim}
things:

   "desired state"

      involves => { 
                  "business goals", 
                  "knowing what state to configure", 
                  "knowing what objects to maintain" 
                  };
~~~~

**Notes**:\
 \

*History*: Was introduced in 3.3.0, Nova 2.2.0 (2012)

#### `is_caused_by`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Special fixed relation for describing topics that are
things

**Example**:\
 \

~~~~ {.verbatim}
bundle knowledge test
{
things:

  "core dump" is_caused_by => { "memory fault" },
                     certainty => "certain";

}
~~~~

**Notes**:\
 \

*History*: Was introduced in version 3.2.0, Nova 2.1.0 (2011)

The complement of \`causes' for convenience of expression.

#### `is_connected_to`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Special fixed relation for describing topics that are
things

**Example**:\
 \

~~~~ {.verbatim}
things:

 networks::

  "192.23.45.0/24"         comment => "Secure network, zone 0. Single octet for corporate offices",
                   is_connected_to => { "oslo-hub-123" };

  "192.12.74.0/23"         comment => "Zone 1, double octet for the London office developer network",
                   is_connected_to => { "oslo-hub-123" };

  "192.12.74.0/23"         comment => "Secure, single octet for the NYC office",
                   is_connected_to => { "nyc-hub-456" };

~~~~

**Notes**:\
 \

*History*: Was introduced in version 3.1.5, Nova 2.1.0 (2011)

#### `is_determined_by`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Special fixed relation for describing topics that are
things

**Example**:\
 \

~~~~ {.verbatim}
things:

  "why" is_determined_by => { "bodyparts::comment", "Semantic commentary" };
~~~~

**Notes**:\
 \

*History*: Was introduced in 3.3.0, Nova 2.2.0 (2012)

This is the inverse of `determines`.

#### `is_followed_by`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Special fixed relation for describing topics that are
things

**Example**:\
 \

~~~~ {.verbatim}
things:

  "Installing CFEngine"

    is_followed_by => { "bootstrapping", "policy editing" };
~~~~

**Notes**:\
 \

*History*: Was introduced in 3.3.0, Nova 2.2.0 (2012)

#### `is_implemented_by`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Special fixed relation for describing topics that are
things

**Example**:\
 \

~~~~ {.verbatim}
things:

   "my goal"  
              is_implemented_by => { "my promise" };
~~~~

**Notes**:\
 \

*History*: Was introduced in 3.4.0

#### `is_located_in`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Special fixed relation for describing topics that are
things

**Example**:\
 \

~~~~ {.verbatim}
things:

 countries::

   "UK"                 synonyms => { "Great Britain" },
                   is_located_in => { "EMEA", "Europe" };

   "Singapore"     is_located_in => { "APAC", "Asia" };

~~~~

**Notes**:\
 \

*History*: Was introduced in version 3.2, Nova 2.1 (2011)

#### `is_measured_by`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Special fixed relation for describing topics that are
things

**Example**:\
 \

~~~~ {.verbatim}
things:

 service_measurements::

  "login services" is_measured_by => { "ssh_in" };
~~~~

**Notes**:\
 \
 *History*: Was introduced in 3.4.0, Enterprise 3.0

#### `is_part_of`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Special fixed relation for describing topics that are
things

**Example**:\
 \

~~~~ {.verbatim}
things:

  "host 1" is_part_of => { "123.456.789.0/24" };
~~~~

**Notes**:\
 \

*History*: Was introduced in version 3.1.5, Nova 2.1 (2011)

#### `is_preceded_by`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Special fixed relation for describing topics that are
things

**Example**:\
 \

~~~~ {.verbatim}
things:

  "disk failure"

    is_preceded_by => { "write errors", "read errors" },
         certainty => "possible";
~~~~

**Notes**:\
 \

*History*: Was introduced in 3.3.0, Nova 2.2.0 (2012)

#### `measures`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Special fixed relation for describing topics that are
things

**Example**:\
 \

~~~~ {.verbatim}
things:

 service_measurements::

  "ssh_in"     measures => { "services::login services" },
               measures => { "ssh" };
~~~~

**Notes**:\
 \

*History*: Was introduced in 3.4.0, Enterprise 3.0

#### `needs`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Special fixed relation for describing topics that are
things

**Example**:\
 \

~~~~ {.verbatim}
things:

  "rack 123"     needs => { "power", "cooling" };

  "computer"     needs => { "cleaning", "monitoring" },
             certainty => "possible";
~~~~

**Notes**:\
 \

*History*: Was introduced in version 3.1.5, Nova 2.1 (2011)

#### `provides`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Special fixed relation for describing topics that are
things

**Example**:\
 \

~~~~ {.verbatim}
things:

   "host 23" provides => { "www", "email" };
~~~~

**Notes**:\
 \

*History*: Was introduced in version 3.2, Nova 2.1 (2011)

#### `uses`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: Special fixed relation for describing topics that are
things

**Example**:\
 \

~~~~ {.verbatim}
things:

  "apache 2.3" uses => { "mysql 4.5" };
~~~~

**Notes**:\
 \

*History*: Was introduced in version 3.2, Nova 2.1 (2011)
