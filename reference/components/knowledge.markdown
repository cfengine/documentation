---
layout: default
title: Bundles for knowledge 
categories: [Reference, Components, Bundles for knowledge]
published: false
alias: reference-components-bundles-for-knowledge.html
tags: [components, knowledge, bundles]
---


```cf3
     bundle knowledge system
     
     {
     topics:
     
      Troubleshooting::
     
       "Segmentation fault"
            association = a("is caused by","Bad memory reference","can cause");
     
       "Remote connection problem";
       "Web server not running";
       "Print server not running";
       "Bad memory reference";
     }
```

Knowledge bundles describe topic maps, i.e. Topics, Associations and
Occurrences (of topics in documents). This is for knowledge modeling and
has no functional effect on a system.
