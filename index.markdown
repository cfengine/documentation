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
         {% include lts_versions_list.html %}
      </ul>
   </div>
   <div class="home-links">
      <ul>
         <li>Getting started</li>
         <li>
            <a href="getting-started-installation.html">Installation</a>
            <div>Download and install CFEngine for the first time.</div>
         </li>
         <li>
            <a href="getting-started-modules-from-cfengine-build.html">Modules</a>
            <div>Use modules to easily add reports or get things done without writing any code.</div>
         </li>
         <li>
            <a href="getting-started-writing-and-serving-policy.html">Reporting and Web UI</a>
            <div>Know more about your infrastructure and hosts, their data, compliance and make changes from within the Web UI.</div>
         </li>
         <li>
            <a href="getting-started-writing-policy.html">Writing policy</a>
            <div>Write and deploy your first policy files to make changes to systems.</div>
         </li>
         <li>
            <a href="getting-started-developing-modules.html">Developing modules</a>
            <div>Turn your policy, reoprts, or python code into CFEngine Build modules for others to use.</div>
         </li>
         <li>
            <a href="examples-tutorials-writing-and-serving-policy.html">Tutorial series on policy language</a>
            <div>In-depth tutorials on how to work with CFEngine policy.</div>
         </li>
      </ul>
      <ul>
         <li>Popular</li>
         <li>
            <a href="reference-promise-types.html">Promise types</a>
            <div>Learn about processes, packages, users, files, storage, services, etc.</div>
         </li>
         <li>
            <a href="api-enterprise-api-ref.html">API reference</a>
            <div>The API is a conventional REST API which supports one or more GET, PUT, POST, or DELETE operations.</div>
         </li>
         <li>
            <a href="reference-language-concepts.html">Language concepts</a>
            <div>Learn Bundles, Bodies, Promises, Classes and Decisions, Variables, etc.</div>
         </li>
         <li>
            <a href="examples-tutorials-manage-packages.html">Manage packages</a>
            <div>Learn how to install, manage and remove packages using CFEngine.</div>
         </li>
         <li class="cfe-build">
            <span><b>CFEngine Build</b></span>
            <div>
               CFEngine Build is a catalogue of policy and modules created by CFEngine, our partner and community that
               helps you to simplify the automation process.
            </div>
            <a target="_blank" class="btn btn-transparent" href="https://build.cfengine.com">Go to the page <img src="./media/images/arrow-right.svg" /></a>
         </li>
      </ul>
   </div>
</div>
