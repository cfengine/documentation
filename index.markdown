---
layout: default
title: CFEngine 3.6
published: true
sorting: 1
---

CFEngine is a configuration management system that provides a framework for automated management of IT infrastructure throughout its life cycle.

CFEngine is decentralized and highly scalable. It is powered by autonomous agents that can continuously monitor, self-repair, and update or restore an entire IT system every five minutes, with negligible impact on system resources or performance.

<div class="highlight">
<p>
<div class="cf3" style="background: #f5f9fb; border: 1px solid #e8eff1; display: block; font-weight: normal; margin: 2em 0; overflow: auto; padding: 2% 2% 2% 1%; width: 96%;font-family: Liberation Mono,Consolas,monospace;font-size: small;">
<span class="k">body common control<span class="k"> <br/>   
<span class="p">{</span><br/>    
<span class="kr">bundlesequence <span class="o">=&gt;</span> <span class="p">{</span> <span class="s">"cfengine_documentation"</span> }<span class="p">;</span><br/>    
<span class="p">}</span><br/>  
<br/>    
<span class="k">bundle agent<span class="k"> <span class="nf">cfengine_documentation</span><br/>     
<span class="p">{</span><br/>     
<span class="kr">vars: </span><br/>   
<br/>  
  <span class="p">"</span><span class="nv">links[1]</span><span class="p">"</span>   <span class="kt">string</span> <span class="o">=&gt;</span> <span class="s">"Get an <a href="overview-introduction.html">Introduction to CFEngine</a>, an <a href="overview.html">Overview of CFEngine</a> and a <a href="guide.html">Guide to How CFEngine Works</a>.";</span> <br/>  
  <span class="p">"</span><span class="nv">links[2]</span><span class="p">"</span><span class="kt">string</span> <span class="o">=&gt;</span> <span class="s">"<a href="getting-started.html">Get started</a> with CFEngine."; </span> <br/>  
  <span class="p">"</span><span class="nv">links[3]</span><span class="p">"</span><span class="kt">string</span> <span class="o">=&gt;</span> <span class="s">"Read about <a href="guide-writing-policy-and-promises.html">Policy Language</a> and see some <a href="examples.html">Examples of Policy Language</a>.";</span> <br/>   
  <span class="p">"</span><span class="nv">links[4]</span><span class="p">"</span><span class="kt">string</span> <span class="o">=&gt;</span> <span class="s">"Search the <a href="reference.html">Reference Documentation</a>.";</span> <br/>  
  <span class="p">"</span><span class="nv">links[5]</span><span class="p">"</span><span class="kt">string</span> <span class="o">=&gt;</span> <span class="s">"Discover <a href="overview-system-overview-enterprise-overview.html">CFEngine Enterprise Edition</a>.";</span> <br/>  
  <span class="p">"</span><span class="nv">links[6]</span><span class="p">"</span><span class="kt">string</span> <span class="o">=&gt;</span> <span class="s">"Learn about <a href="overview-system-overview-enterprise-overview-enterprise-mission-portal-overview-mission-portal-reports.html">Reporting in the CFEngine Misssion Portal</a>."; </span> <br/>  
  <span class="p">"</span><span class="nv">links[7]</span><span class="p">"</span><span class="kt">string</span> <span class="o">=&gt;</span> <span class="s">"<a href="overview-learning-resources-latest-release.html">Check release information</a>";</span><br/>   
<span class="p">}</span> <br/>    
</div>
</p>
</div>


















