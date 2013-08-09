---
layout: printable
title: Knowledge Management
categories: [Manuals, Knowledge Management]
published: false 
alias: manuals-knowledge-management.html
tags: [manuals, knowledge]
---

[link](#why-does-knowledge-matter)

Above all, CFEngine promotes a human understanding of complex processes.
Its promises are easily documentable using comments that the system
remembers and reminds us about in error reporting. It hides irrelevant
and transitory details of implementation so that the intentions behind
the promises are highlighted for all to see. This means that the
knowledge of your organization can be encoded into a terse,
easy-to-understand CFEngine language based on promises.

### Why does Knowledge Matter?

It is this human understanding of large systems that often makes the
difference between a sustainable automation effort, and an effort that
fails to gain traction:

1.  Technical descriptions are hard to remember. You might understand
    your configuration decisions when you are writing them, but a few
    months later when something goes wrong, you will probably have
    forgotten what you were thinking. That costs you time and effort to
    diagnose.

2.  Organizations are fragile to the loss of those individuals who code
    policy. If they leave, often there is no one left who can understand
    or fix the system. Only with proper documentation is it possible to
    immunize against loss.

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
is both a model for system behavior and a model for knowledge
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
part of the technical configuration. 


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
          handle       => "update_policy",
          comment      => "Update the CFEngine input files from the policy server",
          perms        => system("600"),
          copy_from    => rcp("$(master_location)","$(policy_server)"),
          depth_search => recurse("inf"),
          file_select  => input_files,
          action       => immediate;

If a promise affects another promise in some way, you can make the
affected one promise one of the promisees, like this:

    access:

        "/master/CFEngine/inputs" -> { "update_policy", "other_promisee" },
          handle  => "serve_updates",
          admit   => { "217.77.34.*" };

This use of annotation is the first level of documentation in
CFEngine. The annotations are used internally by CFEngine to provide
meaningful error messages with context and to compute dependencies
that reveal the existence of process chains. 

#### Analyzing and indexing the policy

CFEngine can analyze the promises you have made, index and cross reference them using the command:

    $ cf-promises -r

Normally, the default policy in CFEngine Enterprise will perform this command 
each time the policy is changed.

