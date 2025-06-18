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
      <h1>Welcome to the CFEngine Documentation</h1>
      <div>
         This site contains information on how to manage and automate infrastructure with CFEngine.
         It includes the reference for the following versions of CFEngine:
      </div>
      <ul class="home-top_versions">
         {{< includehtml file="static/lts_versions_list.html" >}}
      </ul>
   </div>
   <div class="home-links">
      <ul>
         <li>Getting started</li>
         <li>
            <a href="/getting-started/installation">Installation</a>
            <div>Download and install CFEngine for the first time.</div>
         </li>
         <li>
            <a href="/getting-started/modules-from-cfengine-build">Modules</a>
            <div>Use modules to easily add reports or get things done without writing any code.</div>
         </li>
         <li>
            <a href="/getting-started/reporting-and-web-ui">Reporting and web UI</a>
            <div>Know more about your infrastructure and hosts, their data, compliance and make changes from within the Web UI.</div>
         </li>
         <li>
            <a href="/getting-started/writing-policy">Writing policy</a>
            <div>Write and deploy your first policy files to make changes to systems.</div>
         </li>
         <li>
            <a href="/getting-started/developing-modules">Developing modules</a>
            <div>Turn your policy, reports, or python code into CFEngine Build modules for others to use.</div>
         </li>
         <li>
            <a href="/examples/tutorials/writing-and-serving-policy">Tutorial series on policy language</a>
            <div>In-depth tutorials on how to work with CFEngine policy.</div>
         </li>
      </ul>
      <ul>
         <li>Popular</li>
         <li>
            <a href="/reference/promise-types">Promise types</a>
            <div>Learn about processes, packages, users, files, storage, services, etc.</div>
         </li>
         <li>
            <a href="/api/enterprise-api-ref">API reference</a>
            <div>The API is a conventional REST API which supports HTTP GET, PUT, POST, and DELETE operations.</div>
         </li>
         <li>
            <a href="/reference/language-concepts">Language concepts</a>
            <div>Learn about bundles, bodies, promises, variables, classes and decisions.</div>
         </li>
         <li>
            <a href="/examples/tutorials/manage-packages">Package management</a>
            <div>Learn how to install, manage, and remove packages using CFEngine.</div>
         </li>
         <li class="cfe-build">
            <span><b>CFEngine Build</b></span>
            <div>
               CFEngine Build is a catalog of policy and modules created by CFEngine, our partners and community which
               helps you simplify the automation process.
            </div>
            <a target="_blank" class="btn btn-transparent" href="https://build.cfengine.com">Go to the page <img src="/arrow-right.svg" /></a>
         </li>
      </ul>
   </div>
</div>
