---
layout: index
title: Home
published: true
sorting: 1
categories: ["index"]
alias: index.html
---
<div class="home">
   <div class="home-top">
      <h1>Welcome to CFEngine Documentation</h1>
      <div>
         This site contains information on how to manage and automate the infrastructure with CFEngine. 
         It includes the reference for the following version of CFEngine: 
      </div>
      <ul class="home-top_versions">
         <li>CFEngine {{site.cfengine.core_branch}}</li>
      </ul>
   </div>
   <div class="home-links">
      <ul>
         <li>Getting started</li>
         <li>
            <a href="/docs/{{site.cfengine.branch}}/guide-installation-and-configuration-pre-installation-checklist.html">Pre-installation Checklist</a>
            <div>Download package and check the system requirements for installation.</div>
         </li>
         <li>
            <a href="/docs/{{site.cfengine.branch}}/guide-installation-and-configuration-general-installation.html">General Installation</a>
            <div>The Steps to bring up a CFEngine installation within an organization.</div>
         </li>
         <li>
            <a href="/docs/{{site.cfengine.branch}}/guide-writing-and-serving-policy.html">Writing and serving policy</a>
            <div>Create promises which defines how some part of an overall system should behave.</div>
         </li>
         <li>
            <a href="/docs/{{site.cfengine.branch}}/guide-reporting.html">Reporting</a>
            <div>Configure different reports for various stakeholders within organization.</div>
         </li>
         <li>
            <a href="/docs/{{site.cfengine.branch}}/guide-introduction-directory-structure.html">CFEngine Directory Structure</a>
            <div>Understand the directory structure and some of the files and functions associated with each subdirectory.</div>
         </li>
         <li>
            <a href="/docs/{{site.cfengine.branch}}/guide-introduction-networking.html">Client Server Communication</a>
            <div>Sets up a line of communication between hosts.</div>
         </li>
      </ul>
      <ul>
         <li>Popular</li>
         <li>
            <a href="/docs/{{site.cfengine.branch}}/reference-promise-types.html">Promise type</a>
            <div>Learn about processes, packages, users, files, storage, services, etc.</div>
         </li>
         <li>
            <a href="/docs/{{site.cfengine.branch}}/reference-enterprise-api-ref.html">API reference</a>
            <div>The API is a conventional REST API which supports one or more GET, PUT, POST, or DELETE operations.</div>
         </li>
         <li>
            <a href="/docs/{{site.cfengine.branch}}/reference-language-concepts.html">Language concepts</a>
            <div>Learn Bundles, Bodies, Promises, Classes and Decisions, Variables, etc.</div>
         </li>
         <li>
            <a href="/docs/{{site.cfengine.branch}}/examples-tutorials-manage-packages.html">Manage packages</a>
            <div>Learn how to install, manage and remove packages using CFEngine.</div>
         </li>
         <li class="cfe-build">
            <span><b>CFEngine Build</b></span>
            <div>
               CFEngine Build is a catalogue of policy and modules created by CFEngine, our partner and community that 
               helps you to simplify the automation process. 
            </div>
            <a target="_blank" class="btn btn-transparent" href="https://build.cfengine.com">Go to the page <img src="/media/images/arrow-right.svg" /></a>
         </li>
      </ul>
   </div>
</div>
