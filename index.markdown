---
layout: default
title: CFEngine 3.7 Manual
published: true
sorting: 1
---

CFEngine is a configuration management system that provides a framework for automated management of IT infrastructure.

CFEngine is decentralized and highly scalable. It is powered by autonomous agents that can continuously monitor, self-repair, and update or restore an entire IT system every five minutes, with negligible impact on system resources or performance.

<div class="highlight" style="font-weight: normal;">
<div class="cf3" style="background: #f5f9fb; border: 1px solid #e8eff1; display: block; font-weight: normal; margin: 2em 0; overflow: auto; padding: 2% 2% 2% 1%; width: 96%;font-family: Liberation Mono,Consolas,monospace;font-size: small;">
<span style="font-weight: normal;" class="k">body common control<span style="font-weight: normal;" class="k"> <br/>
<span style="font-weight: normal;" class="p">{</span><br/>
<span style="font-weight: normal;" class="kr">bundlesequence <span style="font-weight: normal;" class="o">=&gt;</span> <span style="font-weight: normal;" class="p">{</span> <span style="font-weight: normal;" class="s">"cfengine_documentation"</span> }<span style="font-weight: normal;" class="p">;</span><br/>
<span style="font-weight: normal;" class="p">}</span><br/>
<br/>
<span style="font-weight: normal;" class="k">bundle agent<span style="font-weight: normal;" class="k"> <span style="font-weight: normal;" class="nf">cfengine_documentation</span><br/>
<span style="font-weight: normal;" class="p">{</span><br/>
<span style="font-weight: normal;" class="kr">vars: </span><br/>
<br/>
   <span style="font-weight: normal;" class="p">"</span>
 <span style="font-weight: normal;" class="nv">links[1]</span>
 <span style="font-weight: normal;" class="p">"</span>   <span style="font-weight: normal;" class="kt">string </span>
 <span style="font-weight: normal;" class="o">=&gt; </span>
 <span style="font-weight: normal;" class="s" style="font-weight: normal;">"<a style="font-weight:bolder; color: #156a90; text-decoration:underline;font-size: 1.1em;line-height: 1.8; padding-left: 0.5em;" href="guide-introduction.html">Introduction to CFEngine</a>";</span> <br/>



  <span style="font-weight: normal;" class="p">"</span>
 <span style="font-weight: normal;" class="nv">links[2]</span>
 <span style="font-weight: normal;" class="p">"</span>   <span style="font-weight: normal;" class="kt">string </span>
 <span style="font-weight: normal;" class="o">=&gt; </span>
 <span style="font-weight: normal;" class="s" style="font-weight: normal;">"<a style="font-weight:bolder; color: #156a90; text-decoration:underline;font-size: 1.1em;line-height: 1.8; padding-left: 0.5em;" href="guide.html">Guide to How CFEngine Works</a>";</span> <br/>

  <span style="font-weight: normal;" class="p">"</span>
 <span style="font-weight: normal;" class="nv">links[3]</span>
 <span style="font-weight: normal;" class="p">"</span>   <span style="font-weight: normal;" class="kt">string </span>
 <span style="font-weight: normal;" class="o">=&gt; </span>
 <span style="font-weight: normal;" class="s" style="font-weight: normal;">"<a style="font-weight:bolder; color: #156a90; text-decoration:underline;font-size: 1.1em;line-height: 1.8; padding-left: 0.5em;" href="guide-installation-and-configuration.html">Installing and Configuring CFEngine</a>";</span> <br/>

  <span style="font-weight: normal;" class="p">"</span>
 <span style="font-weight: normal;" class="nv">links[4]</span>
 <span style="font-weight: normal;" class="p">"</span>   <span style="font-weight: normal;" class="kt">string </span>
 <span style="font-weight: normal;" class="o">=&gt; </span>
 <span style="font-weight: normal;" class="s" style="font-weight: normal;">"<a style="font-weight:bolder; color: #156a90; text-decoration:underline;font-size: 1.1em;line-height: 1.8; padding-left: 0.5em;" href="guide-writing-and-serving-policy.html">Read about Policy Language</a>";</span> <br/>

  <span style="font-weight: normal;" class="p">"</span>
 <span style="font-weight: normal;" class="nv">links[5]</span>
 <span style="font-weight: normal;" class="p">"</span>   <span style="font-weight: normal;" class="kt">string </span>
 <span style="font-weight: normal;" class="o">=&gt; </span>
 <span style="font-weight: normal;" class="s" style="font-weight: normal;">"<a style="font-weight:bolder; color: #156a90; text-decoration:underline;font-size: 1.1em;line-height: 1.8; padding-left: 0.5em;" href="examples.html">Policy Language Examples & Tutorials</a>";</span> <br/>

  <span style="font-weight: normal;" class="p">"</span>
 <span style="font-weight: normal;" class="nv">links[6]</span>
 <span style="font-weight: normal;" class="p">"</span>   <span style="font-weight: normal;" class="kt">string </span>
 <span style="font-weight: normal;" class="o">=&gt; </span>
 <span style="font-weight: normal;" class="s" style="font-weight: normal;">"<a style="font-weight:bolder; color: #156a90; text-decoration:underline;font-size: 1.1em;line-height: 1.8; padding-left: 0.5em;" href="reference.html">Search the Reference Documentation</a>";</span> <br/>

  <span style="font-weight: normal;" class="p">"</span>
 <span style="font-weight: normal;" class="nv">links[7]</span>
 <span style="font-weight: normal;" class="p">"</span>   <span style="font-weight: normal;" class="kt">string </span>
 <span style="font-weight: normal;" class="o">=&gt; </span>
 <span style="font-weight: normal;" class="s" style="font-weight: normal;">"<a style="font-weight:bolder; color: #156a90; text-decoration:underline;font-size: 1.1em;line-height: 1.8; padding-left: 0.5em;" href="enterprise-cfengine-guide.html">Discover CFEngine Enterprise Edition</a>";</span> <br/>

 <span style="font-weight: normal;" class="p">"</span>
 <span style="font-weight: normal;" class="nv">links[8]</span>
 <span style="font-weight: normal;" class="p">"</span>   <span style="font-weight: normal;" class="kt">string </span>
 <span style="font-weight: normal;" class="o">=&gt; </span>
 <span style="font-weight: normal;" class="s" style="font-weight: normal;">"<a style="font-weight:bolder; color: #156a90; text-decoration:underline;font-size: 1.1em;line-height: 1.8; padding-left: 0.5em;" href="enterprise-cfengine-guide-reporting.html">Learn about Enterprise Reporting</a>";</span> <br/>

 <span style="font-weight: normal;" class="p">"</span>
 <span style="font-weight: normal;" class="nv">links[9]</span>
 <span style="font-weight: normal;" class="p">"</span>   <span style="font-weight: normal;" class="kt">string </span>
 <span style="font-weight: normal;" class="o">=&gt; </span>
 <span style="font-weight: normal;" class="s" style="font-weight: normal;">"<a style="font-weight:bolder; color: #156a90; text-decoration:underline;font-size: 1.1em;line-height: 1.8; padding-left: 0.5em;" href="guide-latest-release-whatsnew.html">What's New in 3.7</a>";</span> <br/>

<span style="font-weight: normal;" class="p">}</span> <br/>
</div>
</div>
