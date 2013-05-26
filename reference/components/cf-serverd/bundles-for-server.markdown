---
layout: default
title: Bundles for server
categories: [Reference, Components, cf-serverd, Bundles for server]
published: true
alias: reference-components-bundles-for-server.html
tags: [reference, components, cf-serverd, bundles, server]
---

Bundles in the server describe access promises on specific file and
class objects supplied by the server to clients.


```cf3
     
     bundle server access_rules()
     
     {
     access:
     
       "/home/mark/PrivateFiles"
     
         admit   = { ".*\.example\.org" };
     
       "/home/mark/\.cfagent/bin/cf-agent"
     
         admit   = { ".*\.example\.org" };
     
     roles:
     
       ".*"  authorize = { "mark" };
     }
     
     
```
