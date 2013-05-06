## Knowledge Management

A unique aspect of CFEngine, that is fully developed in the commercial
editions of the software, its ability to enable integrated knowledge
management as part of an automation process, and to use its
configuration technology as a `semantic' documentation engine.


Knowledge management is the challenge of our times. Organizations
frequently waste significant effort re-learning old lessons because
they have not been documented and entered into posterity. Now you can
alleviate this problem with some simple rules of thumb and even build
sophisticated index-databases of documents.

### Promises and Knowledge

The learning curve for configuration management systems has been the
brunt of frequent criticism over the years. Users are expected to
either confront the informational complexity of systems at a detailed
level, or abandon the idea of fine control altogether. This has led
either to information overload or over-simplification. The ability to
cope with information complexity is therefore fundamental to IT
management

CFEngine introduced the promise model for configuration in order to
flatten out this learning curve. It can lead to simplifications in
use, because a lot of the thinking has been done already and is
encapsulated into the model. One of its special properties is that it
is both a model for system behaviour and a model for knowledge
representation (this is what declarative languages seek to be, of
course). More specifically, it incorporated a subset of the ISO
standard for `Topic Maps', an open technology for semantic indexing of
information resources. By bringing together these two technologies
(which are highly compatible), we end up with a seamless front-end for
sewing together and browsing system information.

Knowledge management is a field of research in its own right, and it
covers a multitude of issues both human and technological. Most would
agree that knowledge is composed of facts and relationships and that
there is a need both for clear definitions and semantic context to
interpret knowledge properly; but how do we attach meaning to raw
information without ambiguity?

Knowledge has quite a lot in common with configuration: what after all
is knowledge but a configuration of ideas in our minds, or on some
representation medium (paper, silicon etc). It is a coded pattern,
preferably one that we can agree on and share with others. Both
knowledge and configuration management are about describing patterns.
A simple knowledge model can be used to represent a policy or
configuration; conversely, a simple model of policy configuration can
manufacture a knowledge structure just as it might manufacture a
filesystem or a set of services.

### The basics of knowledge

Knowledge only truly begins when we write things down:

* The act of formulating something in writing brings a discipline of
thought than often lends clarity to an idea.

* You never confront an idea fully until you try to put it into language.

* Any written record that is kept allows others to read it and pass on
the knowledge.

The trouble is that writing is something people don't like to do, and
few are very good at. To an engineer, it can feel like a waste of
time, especially during a busy day, to break off from the doing to
write about the doing. Also, writing requires a spurt of creative
thinking and engineers are often more comfortable with manipulating
technical patterns and notations than writing fluent linguistic
formulations that seem overtly long-winded.

CFEngine tries to bridge this gap by making documentation simple and
part of the technical configuration. CFEngine's knowledge agent then
uses AI and network science algorithms to construct a readable
documentation from these technical annotations. It can do this because
a lot of thought has already gone into the meaning of the promise
model.

### Annotating promises

The beginning of knowledge is to annotate the technical
specifications. Remember that the point of a promise is to convey an
intention. When writing promises, get into the habit of giving every
promise a comment that explains its intention. Also, expect to give
special promises handles, or helpful labels that can be used to refer
to them in other promise statements. A handle could be something dumb
like `xyz', but you should try to use more meaningful titles to help
make references clear.


    files:

    "/var/cfengine/inputs"
        handle => "update_policy",
        comment => "Update the CFEngine input files from the policy server",
        perms => system("600"),
        copy_from => rcp("$(master_location)","$(policy_server)"),
        depth_search => recurse("inf"),
        file_select => input_files,
        action => immediate;

If a promise affects another promise in some way, you can make the
affected one promise one of the promisees, like this: access:

    "/master/CFEngine/inputs" -> { "update_policy", "other_promisee" },

    handle  => "serve_updates",
      admit   => { "217.77.34.*" };

Conversely, if a promise might depend on another in some (even indirect) way, document this too.

    files:

    "/var/cfengine/inputs"

      handle => "update_policy",
     comment => "Update the CFEngine input files from the policy  server",
     depends_on => { "serve_updates" },
     perms => system("600"),
     copy_from => rcp("$(master_location)","$(policy_server)"),
     depth_search => recurse("inf"),
     file_select => input_files,
     action => immediate;

This use of annotation is the first level of documentation in
CFEngine. The annotations are used internally by CFEngine to provide
meaningful error messages with context and to compute dependencies
that reveal the existence of process chains. These can be turned into
a topic map for browsing the policy relationships in a web browser,
using cf-know.

The CFEngine Knowledge Map is only available in commercial editions of
the software, where the necessary support to set up and maintain this
technology can be provided.

### A promise model of topic maps

CFEngine's model of promises can also be used to promise information
and its relevance in different contexts. The Knowledge agent cf-know
understands three kinds of promise.

* topics - A topic is merely a string that can be associated with
    another string. It represents a `subject to be talked about'. Like other
    promise types, you can use contexts, which are formed from other
    topics expressions to limit the scope of the current topic promise.

* things - Things are a simplified interface to topics, that were introduced
    to make it easier for users to contribute knowledge about more
    concrete `things', or less abstract ideas. A challenge with
    knowledge management is the abstract and technical nature of the
    models one must use to represent it. Things attempt to make that task
    easier.

* occurrences - An occurrence is a reference to a document or a piece of text that
    actually represents knowledge content about the topic concerned.
    Occurrences are generally URLs or strings explaining things or topics.

### What topic maps offer

CFEngine is capable of automating the documentation of a policy, using
basic annotations provided above, as a knowledge map. They require
very little effort from the user. If you are using the Community
Edition of CFEngine, you can develop a topic map, but we do not
support the backend technology without a commercial license. In either
case, once you become familiar with the use of Topic Maps, you will
want to extend your knowledge manually to incorporate things like:

* Local (high level) policy documents
* Related databases, such as CMDBs

So let us spend a while showing how to encode knowledge in topic maps using cf-know.

The kind of result you can expect is shown in the pictures below. The
example figures show typical pages generated by the knowledge agent
cf-know. The first of these shows how we use the technology to power
the web knowledge base in the commercial CFEngine product.

In this use, all of the data are based on documentation for the
CFEngine software, and most of the relationships are manually entered.

For a second example, consider how CFEngine can generate such a
knowledge map analysis of its own configuration (self-analysis). The
data in the images below describe the CFEngine configuration promises.
One such page is generated, for instance, for each policy promise, and
pages are generated for reports from different computers etc. You can
also create you own `topic pages' for any local (enterprise)
information that you have.

In this example, the promise has been given the promise-handle
update_policy, and the associations and the lower graph shows how this
promise relates to other promises through its documented dependencies
(these are documented from the promisees and depends_on attributes of
other promises.).

The example page shows two figures, one above the other. The upper
figure shows the thirty nearest topics (of any kind) that are related
to this one. Here the relationships are unspecific. This diagram can
reveal pathways to related information that are often unexpected, and
illustrates relationships that broaden one's understanding of the
place the current promise occupies within the whole.

Although the graphical illustrations are just renderings of semantic
associations shown more fully in text, they are useful for visualizing
several levels of depth in the associative network. This can be
surprisingly useful for brainstorming and reasoning alike. In
particular, one can see the other promises that could be affected if
we were to make a change to the current promise. Such impact analyses
can be crucial to planning change and release management of policy.

A knowledge base is a slightly improved implementation of a Topic Map
which is an ISO standard technology. A topic map works like an index
that can point to many different kinds of external resources, and may
contain simple text and images internally. So you use it to bind
together documents of any kind. A CFEngine knowledge base is not a new
document format, it is an overlay map that joins ideas and resources
together, and displays relationships.

### The nuts and bolts of topic maps

Topic maps are really electronic indices, but they form and work like
webs. A topic is the technical representation of a `subject', i.e.
anything you might want to discuss, abstract or physical e.g. an item
of `abstract knowledge', which probably has a number of concrete
exemplars. It might be a person, a machine, a quality, etc.

Topics can be classified into boxes called topic-types so that related
things can be collated and unrelated things can be separated, e.g.
types allow us to distinguish between rmdir the Unix utility and rmdir
the Unix system-call.

Each typed topic can further point to a number of references or
exemplars called occurrences. For instance, an occurrence of the topic
`computer' might include books, web documents, database entries,
physical manifestations, or any other information. An occurrence is a
reference that exemplifies the abstract topic. Occurrence references
are like the page numbers in an index.

A book index typically has `see also' references which point from one
topic to another. Topic Maps allow one to define any kind of
association between topics. Unlike an ordinary index, a topic map has
a rich (potentially infinite) variety of cross reference types. For
instance,

     topic_1 ``is a kind of'' topic_2
     topic_1 ``is improved by'' topic 2
     topic_1 ``solves the problem of'' topic_2

The topic map model thus has three levels of containers:

* Contexts - The box into which we classify a topic to disambiguate
  different topics with the same name (`in the context of')2.

* Topics/Things - The representation of a subject (an index term). 

* Occurrence Types - A term that explains how an actual document
    occurrence relates to the topic is claims to say something about. e.g. (tutorial,
    manual, or example,  definition, photo-album etc). 

* Occurrences - Specific information resources: these are pointers to
  the actual documents that we want to read (like page numbers in an index).

Contexts map conveniently into CFEngine classes. Topics map
conveniently into promisers. Occurrences also map to promisers of a
different type. These three label different levels of granularity of
meaning. Contexts represent a set of topics that might be relevant,
which in turn encompass a set of occurrences of resources that contain
actual information about the topics in that context. The primacy of
topics in this stems from their ability to form networks by
association.

The classic approach to information modeling is to build a
hierarchical decomposition of non-overlapping objects. Data are
manipulated into non-overlapping containers which often prove to be
overly restrictive. Topic maps allow us to avoid the kinds of mistakes
that have led to monstrosities like the Common Information Model (CIM)
with its thousands of strictly non-overlapping type categories.

Each topic allows us to effectively `shine a light' onto the
occurrences of information that highlight the concepts pertinent to
the topic somehow.

### Example of topics promises

You can use cf-know to render a topic map either as text (for command
line use) or as HTML (for web rendering). We begin with the text
rendering as it requires less infrastructure. You will just need a
database.

Try typing in the following knowledge promises:

     body common control
     {
     bundlesequence  => { "tm" };
     }
     
     ###################################################
     
     bundle knowledge tm
     {
     topics:
     
     
     "server" comment => "Common name for a computer in a desktop";
     "desktop" comment => "Common name for a computer for end users";
     
     programs:: # context of programs
     
     "httpd" comment => "A web service process";
     "named" comment => "A name service process";
     
     services::
     
     "WWW" comment => "World Wide Web service",
           association => a("is implemented by",
                            "programs::httpd",
                            "implements");
     
      # if we don't specify a context, it is "any"
     
     "WWW" association => a("looks up addresses with",
                            "named",
                            "serves addresses to");
     
     occurrences:
     
     httpd::
        "http://www.apache.org"
          represents => { "website" };
     
     }
     
     ###################################################
     
     body association a(f,name,b)
     
     {
     forward_relationship => "$(f)";
     backward_relationship => "$(b)";
     associates => { $(name) };
     }

The simplified things interface is similar, but uses fixed relations:

    bundle knowledge company_knowledge
    {
    things:
     regions::

       "EMEA"     comment => "Europe, The Middle-East and Africa";
       "APAC"     comment => "Asia and the Pacific countries";

     countries::
       "UK"            synonyms => { "Great Britain" },
              is_located_in => { "EMEA", "Europe" };

       "Netherlands"   synonyms => { "Holland" },
              is_located_in => { "EMEA", "Europe" };

       "Singapore"     is_located_in => { "APAC", "Asia" };

     locations::
       "London_1"    is_located_in => { "London", "UK" };
       "New_Jersey"  is_located_in => { "USA" };

     networks::

      "192.23.45.0/24"         comment => "Secure network, zone 0. Single octet for corporate offices",
                   is_connected_to => { "oslo-hub-123" };

#### Analyzing and indexing the policy

CFEngine can analyze the promises you have made, index and cross reference them using the command:

    # cf-promises -r

Normally, the default policy in Nova or Constellation will perform this command each time the policy is changed.
Previous: Analyzing and indexing the policy, Up: Example of topics promises

#### cf-know

CFEngine's knowledge agent cf-know allows you to make promises about
knowledge and its inter-relationships. It is not specifically a
generic topic map language: rather it provides a powerful
configuration language for managing a knowledge base that can be
compiled into a topic map.

To build a topic map from a set of knowledge promises in knowledge.cf, you would write:

    # cf-know -b -f ./knowledge.cf

The syntax of this file is hinted at below. The full ISO standard
topic map model is too rich to be a useful tool for system knowledge
management. However, this is where powerful configuration management
can help to simplify the process: encoding a topic map is a complex
problem in configuration, which is exactly what CFEngine is for.
CFEngine's topic map promises have the following form:

     bundle knowledge example
     {
     topics:
     
     topic_type_context::                          # canonical container
     
     "Topic name"                                # short topic name
     
           comment => "Use this for a longer description",
       association => a("forward assoc to","Other topic","backward assoc");
     
       "Other topic";
     
     occurrences:
     
     Topic_name::                                   # Topic
     
       "http://www.example.org/document.xyz"        # URI to instance
     
         represents => { "Definition", "Tutorial"}; # sub-types
     }

The association body templates look like this:

    body association a(f,name,b)
    {
    forward_relationship => "$(f)"; 
    backward_relationship => "$(b)";
    associates => { $(name) };
    }

Promise theory adds a clear structure to the topic map ontology, which
is highly beneficial as experience shows that weak conceptual models
lead to poor knowledge maps.

### Modeling configuration promises as topic maps

We can model topic maps as promises within CFEngine; the question then
remains as to how to use topic maps to model configurations so that
CFEngine users can navigate the documented promises using a web
browser and be able to see all of the relationships between otherwise
isolated and fragmentary rules. This will form the basis of a semantic
Configuration Management Database (sCMDB) for the CFEngine software.
The key to making these ends meet is to see the configuration of the
topic map as a number Ã¶f promises made in the abstract space of
topics and the turning each promise into a meta-promise that models
the configuration as a topic with attendant associations. Consider the
following CFEngine promise.

    bundle agent update
    {
    files:

    any::

    "/var/cfengine/inputs'' -> { "policy_team'', ''dependent'' },

        comment => ``Check policy updates from source'',
        perms => true,
        mode => 600,
        copy_from => true,
        copy_source => /policy/masterfiles,
        compare => digest,
        depth_search => true,
        depth => inf,
        ifelapsed => 1;

}

This system configuration promise can be mapped by CFEngine into a
number of other promise proposals intended for the cf-know agent.
Suppressing some of the details, we have:

    type_files::

    "/var/cfengine/inputs"
        association => a("promise made in bundle","update","bundle contains promise");
    "/var/cfengine/inputs"
        association => a("specifies body type","perms","is specified in");
    "/var/cfengine/inputs"
        association => a("specifies body type","mode","is specified in");
    "/var/cfengine/inputs"
        association => a("specifies body type","copy_from","is specified  in");

    # etc ...
    occurrences:

        _var_CFEngine_inputs::

        "promise_output_common.html#promise__var_CFEngine_inputs_update_cf_13"
             represents => { "promise definition" };

Note that in this mapping, the actual promise (viewed as a real world
entity) is an occurrence of the topic 'promise'; at the same time each
promise could be discussed as a different topic allowing meta-modeling
of the entity-relation model in the real-world data. Conversely the
topics themselves become configuration items or 'promisers' in the
promise model. The effect is to create a navigable semantic web for
traversing the policy; this documents the structure and intention of
the policy using a small ontology of standard concepts and can be
extended indefinitely by human domain experts.
