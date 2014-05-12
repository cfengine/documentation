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
<code class="cf3" style="background: #f5f9fb; border: 1px solid #e8eff1; display: block; font-weight: normal; margin: 2em 0; overflow: auto; padding: 2% 2% 2% 1%; width: 96%;">
<span class="k">body common control<span class="k"> <br/>   
<span class="p">{</span><br/>    
<span class="kr">bundlesequence <span class="o">=&gt;</span> <span class="p">{</span> <span class="s">"cfengine_documentation"</span> }<span class="p">;</span><br/>    
<span class="p">}</span><br/>  
<br/>    
<span class="k">bundle agent<span class="k"> <span class="nf">cfengine_documentation</span><br/>     
<span class="p">{</span><br/>     
<span class="kr">vars: </span><br/>   
<br/>  
  <span class="s">"links[1]"</span>   <span class="kr">string</span> <span class="o">=&gt;</span> <span class="s">"Get an [Introduction to CFEngine][Introduction], an [Overview of CFEngine][Overview] and a [Guide to How CFEngine Works][Guide].";</span> <br/>  
  <span class="s">"links[2]"</span>   <span class="kr">string</span> <span class="o">=&gt;</span> <span class="s">"[Get started][Get Started] with CFEngine."; </span> <br/>  
  <span class="s">"links[3]"</span>   <span class="kr">string</span> <span class="o">=&gt;</span> <span class="s">"Read about [Policy Language][Writing Policy and Promises] and see some [Examples of Policy Language][Examples].";</span> <br/>   
  <span class="s">"links[4]"</span>   <span class="kr">string</span> <span class="o">=&gt;</span> <span class="s">"Search the [Reference Documentation][Reference].";</span> <br/>  
  <span class="s">"links[5]"</span>   <span class="kr">string</span> <span class="o">=&gt;</span> <span class="s">"Discover [CFEngine Enterprise Edition][CFEngine Enterprise Guide].";</span> <br/>  
  <span class="s">"links[6]"</span>   <span class="kr">string</span> <span class="o">=&gt;</span> <span class="s">"Learn about [Reporting in the CFEngine Misssion Portal][Reporting in Mission Portal]."; </span> <br/>  
  <span class="s">"links[7]"</span>   <span class="kr">string</span> <span class="o">=&gt;</span> <span class="s">"Check release information";</span><br/>   
<span class="p">}</span> <br/>    
</code>
</p>
</div>


















