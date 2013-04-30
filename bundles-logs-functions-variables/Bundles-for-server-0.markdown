---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Bundles-for-server-0.markdown.html
tags: [xx]
---

Bundles of `server`
-------------------

\

         
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
         
         

\

Bundles in the server describe access promises on specific file and
class objects supplied by the server to clients.

-   classes in common promises:
-   defaults in common promises:
-   meta in common promises:
-   reports in common promises:
-   vars in common promises:
-   \* in common promises:
-   commands in agent promises:
-   databases in agent promises:
-   guest\_environments in agent promises:
-   files in agent promises:
-   \* in edit\_line promises:
-   delete\_lines in edit\_line promises:
-   insert\_lines in edit\_line promises:
-   field\_edits in edit\_line promises:
-   replace\_patterns in edit\_line promises:
-   \* in edit\_xml promises:
-   build\_xpath in edit\_xml promises:
-   delete\_tree in edit\_xml promises:
-   insert\_tree in edit\_xml promises:
-   delete\_attribute in edit\_xml promises:
-   set\_attribute in edit\_xml promises:
-   delete\_text in edit\_xml promises:
-   set\_text in edit\_xml promises:
-   insert\_text in edit\_xml promises:
-   interfaces in agent promises:
-   methods in agent promises:
-   outputs in agent promises:
-   packages in agent promises:
-   processes in agent promises:
-   services in agent promises:
-   storage in agent promises:
-   access in server promises:
-   roles in server promises:
-   inferences in knowledge promises:
-   things in knowledge promises:
-   topics in knowledge promises:
-   occurrences in knowledge promises:
-   measurements in monitor promises:
