---
layout: default
title: Functions
categories: [Reference, Functions]
published: true
alias: reference-functions.html
tags: [Reference, Functions]
---

There are a large number of functions built into CFEngine, and finding
the right one to use can be a daunting task. The following tables are
designed to make it easier for you to find the function you need, based
on the value or type that the function returns or processes as inputs.

## Functions listed by return value

### Functions That Return Class

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-accessedbefore">accessedbefore</a></td>
<td align="left"><a href="#Function-and">and</a></td>
<td align="left"><a href="#Function-changedbefore">changedbefore</a></td>
<td align="left"><a href="#Function-classify">classify</a></td>
<td align="left"><a href="#Function-classmatch">classmatch</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-concat">concat</a></td>
<td align="left"><a href="#Function-fileexists">fileexists</a></td>
<td align="left"><a href="#Function-filesexist">filesexist</a></td>
<td align="left"><a href="#Function-groupexists">groupexists</a></td>
<td align="left"><a href="#Function-hashmatch">hashmatch</a> <br /></td>
</tr>
<tr class="odd">
<td align="left"><a href="#Function-hostinnetgroup">hostinnetgroup</a></td>
<td align="left"><a href="#Function-hostrange">hostrange</a></td>
<td align="left"><a href="#Function-iprange">iprange</a></td>
<td align="left"><a href="#Function-isdir">isdir</a></td>
<td align="left"><a href="#Function-isexecutable">isexecutable</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-isgreaterthan">isgreaterthan</a></td>
<td align="left"><a href="#Function-islessthan">islessthan</a></td>
<td align="left"><a href="#Function-islink">islink</a></td>
<td align="left"><a href="#Function-isnewerthan">isnewerthan</a></td>
<td align="left"><a href="#Function-isplain">isplain</a> <br /></td>
</tr>
<tr class="odd">
<td align="left"><a href="#Function-isvariable">isvariable</a></td>
<td align="left"><a href="#Function-ldaparray">ldaparray</a></td>
<td align="left"><a href="#Function-or">or</a></td>
<td align="left"><a href="#Function-not">not</a></td>
<td align="left"><a href="#Function-regarray">regarray</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-regcmp">regcmp</a></td>
<td align="left"><a href="#Function-regextract">regextract</a></td>
<td align="left"><a href="#Function-regldap">regldap</a></td>
<td align="left"><a href="#Function-regline">regline</a></td>
<td align="left"><a href="#Function-reglist">reglist</a> <br /></td>
</tr>
<tr class="odd">
<td align="left"><a href="#Function-remoteclassesmatching">remoteclassesmatching</a></td>
<td align="left"><a href="#Function-returnszero">returnszero</a></td>
<td align="left"><a href="#Function-splayclass">splayclass</a></td>
<td align="left"><a href="#Function-strcmp">strcmp</a></td>
<td align="left"><a href="#Function-usemodule">usemodule</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-userexists">userexists</a> <br /></td>
</tr>
</tbody>
</table>

### Functions That Return (i,r,s)List

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-getindices">getindices</a></td>
<td align="left"><a href="#Function-getusers">getusers</a></td>
<td align="left"><a href="#Function-grep">grep</a></td>
<td align="left"><a href="#Function-ldaplist">ldaplist</a></td>
<td align="left"><a href="#Function-maplist">maplist</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-peerleaders">peerleaders</a></td>
<td align="left"><a href="#Function-peers">peers</a></td>
<td align="left"><a href="#Function-readintlist">readintlist</a></td>
<td align="left"><a href="#Function-readreallist">readreallist</a></td>
<td align="left"><a href="#Function-readstringlist">readstringlist</a> <br /></td>
</tr>
<tr class="odd">
<td align="left"><a href="#Function-splitstring">splitstring</a> <br /></td>
</tr>
</tbody>
</table>

### Functions That Return Int

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-accumulated">accumulated</a></td>
<td align="left"><a href="#Function-ago">ago</a></td>
<td align="left"><a href="#Function-countlinesmatching">countlinesmatching</a></td>
<td align="left"><a href="#Function-diskfree">diskfree</a></td>
<td align="left"><a href="#Function-getfields">getfields</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-getgid">getgid</a></td>
<td align="left"><a href="#Function-getuid">getuid</a></td>
<td align="left"><a href="#Function-now">now</a></td>
<td align="left"><a href="#Function-on">on</a></td>
<td align="left"><a href="#Function-randomint">randomint</a> <br /></td>
</tr>
<tr class="odd">
<td align="left"><a href="#Function-readintarray">readintarray</a></td>
<td align="left"><a href="#Function-readrealarray">readrealarray</a></td>
<td align="left"><a href="#Function-readstringarray">readstringarray</a></td>
<td align="left"><a href="#Function-readstringarrayidx">readstringarrayidx</a></td>
<td align="left"><a href="#Function-selectservers">selectservers</a> <br /></td>
</tr>
</tbody>
</table>

### Functions That Return (i,r)Range

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-irange">irange</a></td>
<td align="left"><a href="#Function-rrange">rrange</a> <br /></td>
</tr>
</tbody>
</table>

### Functions That Return Real

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-product">product</a></td>
<td align="left"><a href="#Function-sum">sum</a> <br /></td>
</tr>
</tbody>
</table>

### Functions That Return String

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-canonify">canonify</a></td>
<td align="left"><a href="#Function-escape">escape</a></td>
<td align="left"><a href="#Function-execresult">execresult</a></td>
<td align="left"><a href="#Function-getenv">getenv</a></td>
<td align="left"><a href="#Function-hash">hash</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-host2ip">host2ip</a></td>
<td align="left"><a href="#Function-hostsseen">hostsseen</a></td>
<td align="left"><a href="#Function-join">join</a></td>
<td align="left"><a href="#Function-lastnode">lastnode</a></td>
<td align="left"><a href="#Function-ldapvalue">ldapvalue</a> <br /></td>
</tr>
<tr class="odd">
<td align="left"><a href="#Function-peerleader">peerleader</a></td>
<td align="left"><a href="#Function-readfile">readfile</a></td>
<td align="left"><a href="#Function-readtcp">readtcp</a></td>
<td align="left"><a href="#Function-registryvalue">registryvalue</a></td>
<td align="left"><a href="#Function-remotescalar">remotescalar</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-translatepath">translatepath</a> <br /></td>
</tr>
</tbody>
</table>

## Functions That Fill Arrays

The following functions all fill arrays, although they return values
that depend on the number of items processed.

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-getfields">getfields</a></td>
<td align="left"><a href="#Function-readintarray">readintarray</a></td>
<td align="left"><a href="#Function-readrealarray">readrealarray</a></td>
<td align="left"><a href="#Function-readstringarray">readstringarray</a></td>
<td align="left"><a href="#Function-readstringarrayidx">readstringarrayidx</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-regextract">regextract</a> <br /></td>
</tr>
</tbody>
</table>

## Functions That Read Large Data

The following functions read data from inside CFEngine (from classes,
lists, strings, etc.) and outside of CFEngine (from files, databases,
arrays, etc.).

### Functions That Read Arrays

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-getindices">getindices</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-getvalues">getvalues</a></td>
<td align="left"><a href="#Function-regarray">regarray</a> <br /></td>
</tr>
</tbody>
</table>

### Functions That Read Disk Data

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-diskfree">diskfree</a> <br /></td>
</tr>
</tbody>
</table>

### Functions That Read From a Remote-CFEngine

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-remoteclassesmatching">remoteclassesmatching</a></td>
<td align="left"><a href="#Function-remotescalar">remotescalar</a> <br /></td>
</tr>
</tbody>
</table>

### Functions That Read Classes

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-and">and</a></td>
<td align="left"><a href="#Function-classify">classify</a></td>
<td align="left"><a href="#Function-classmatch">classmatch</a></td>
<td align="left"><a href="#Function-concat">concat</a></td>
<td align="left"><a href="#Function-not">not</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-or">or</a> <br /></td>
</tr>
</tbody>
</table>

### Functions That Read Command Output

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-execresult">execresult</a></td>
<td align="left"><a href="#Function-returnszero">returnszero</a></td>
<td align="left"><a href="#Function-usemodule">usemodule</a> <br /></td>
</tr>
</tbody>
</table>

### Functions That Read the Environment

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-getenv">getenv</a> <br /></td>
</tr>
</tbody>
</table>

### Functions That Read Files

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-countlinesmatching">countlinesmatching</a></td>
<td align="left"><a href="#Function-getfields">getfields</a></td>
<td align="left"><a href="#Function-getusers">getusers</a></td>
<td align="left"><a href="#Function-hashmatch">hashmatch</a></td>
<td align="left"><a href="#Function-peerleader">peerleader</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-peerleaders">peerleaders</a></td>
<td align="left"><a href="#Function-peers">peers</a></td>
<td align="left"><a href="#Function-readfile">readfile</a></td>
<td align="left"><a href="#Function-readintarray">readintarray</a></td>
<td align="left"><a href="#Function-readintlist">readintlist</a> <br /></td>
</tr>
<tr class="odd">
<td align="left"><a href="#Function-readrealarray">readrealarray</a></td>
<td align="left"><a href="#Function-readreallist">readreallist</a></td>
<td align="left"><a href="#Function-readstringarray">readstringarray</a></td>
<td align="left"><a href="#Function-readstringarrayidx">readstringarrayidx</a></td>
<td align="left"><a href="#Function-readstringlist">readstringlist</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-regline">regline</a> <br /></td>
</tr>
</tbody>
</table>

### Functions That Read LDAP Data

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-ldaparray">ldaparray</a></td>
<td align="left"><a href="#Function-ldaplist">ldaplist</a></td>
<td align="left"><a href="#Function-ldapvalue">ldapvalue</a></td>
<td align="left"><a href="#Function-regldap">regldap</a> <br /></td>
</tr>
</tbody>
</table>

### Functions That Read From the Network

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-readtcp">readtcp</a></td>
<td align="left"><a href="#Function-selectservers">selectservers</a> <br /></td>
</tr>
</tbody>
</table>

### Functions That Read the Windows Registry

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-registryvalue">registryvalue</a> <br /></td>
</tr>
</tbody>
</table>

### Functions That Read (i,r,s)Lists

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-grep">grep</a></td>
<td align="left"><a href="#Function-join">join</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-product">product</a> <br /></td>
</tr>
<tr class="odd">
<td align="left"><a href="#Function-reglist">reglist</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-sum">sum</a> <br /></td>
</tr>
</tbody>
</table>

### Functions That Read Strings

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-hash">hash</a></td>
<td align="left"><a href="#Function-lastnode">lastnode</a></td>
<td align="left"><a href="#Function-regcmp">regcmp</a></td>
<td align="left"><a href="#Function-regextract">regextract</a></td>
<td align="left"><a href="#Function-splitstring">splitstring</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-strcmp">strcmp</a></td>
<td align="left"><a href="#Function-translatepath">translatepath</a> <br /></td>
</tr>
</tbody>
</table>

## Functions That Look at File Metadata

The following functions examine file metadata, but don't use the
contents of the file.

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-accessedbefore">accessedbefore</a></td>
<td align="left"><a href="#Function-changedbefore">changedbefore</a></td>
<td align="left"><a href="#Function-fileexists">fileexists</a></td>
<td align="left"><a href="#Function-filesexist">filesexist</a></td>
<td align="left"><a href="#Function-isdir">isdir</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-islink">islink</a></td>
<td align="left"><a href="#Function-isnewerthan">isnewerthan</a></td>
<td align="left"><a href="#Function-isplain">isplain</a> <br /></td>
</tr>
</tbody>
</table>

## Functions That Look at Variables

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-isgreaterthan">isgreaterthan</a></td>
<td align="left"><a href="#Function-islessthan">islessthan</a></td>
<td align="left"><a href="#Function-isvariable">isvariable</a> <br /></td>
</tr>
</tbody>
</table>

## Functions Involving Date or Time

The following functions all do date or time computation

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-accessedbefore">accessedbefore</a></td>
<td align="left"><a href="#Function-accumulated">accumulated</a></td>
<td align="left"><a href="#Function-ago">ago</a></td>
<td align="left"><a href="#Function-changedbefore">changedbefore</a></td>
<td align="left"><a href="#Function-isnewerthan">isnewerthan</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-now">now</a></td>
<td align="left"><a href="#Function-on">on</a></td>
<td align="left"><a href="#Function-splayclass">splayclass</a> <br /></td>
</tr>
</tbody>
</table>

## Functions That Work With or On Regular Expressions

<table>
<tbody>
<tr class="odd">
<td align="left"><a href="#Function-classmatch">classmatch</a></td>
<td align="left"><a href="#Function-countlinesmatching">countlinesmatching</a></td>
<td align="left"><a href="#Function-escape">escape</a></td>
<td align="left"><a href="#Function-getfields">getfields</a></td>
<td align="left"><a href="#Function-grep">grep</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-readintarray">readintarray</a></td>
<td align="left"><a href="#Function-readintlist">readintlist</a></td>
<td align="left"><a href="#Function-readrealarray">readrealarray</a></td>
<td align="left"><a href="#Function-readreallist">readreallist</a></td>
<td align="left"><a href="#Function-readstringarray">readstringarray</a> <br /></td>
</tr>
<tr class="odd">
<td align="left"><a href="#Function-readstringarrayidx">readstringarrayidx</a></td>
<td align="left"><a href="#Function-readstringlist">readstringlist</a></td>
<td align="left"><a href="#Function-regarray">regarray</a></td>
<td align="left"><a href="#Function-regcmp">regcmp</a></td>
<td align="left"><a href="#Function-regextract">regextract</a> <br /></td>
</tr>
<tr class="even">
<td align="left"><a href="#Function-regldap">regldap</a></td>
<td align="left"><a href="#Function-regline">regline</a></td>
<td align="left"><a href="#Function-reglist">reglist</a></td>
<td align="left"><a href="#Function-splitstring">splitstring</a> <br /></td>
</tr>
</tbody>
</table>



-   [Function accessedbefore](#Function-accessedbefore)
-   [Function accumulated](#Function-accumulated)
-   [Function ago](#Function-ago)
-   [Function and](#Function-and)
-   [Function canonify](#Function-canonify)
-   [Function concat](#Function-concat)
-   [Function changedbefore](#Function-changedbefore)
-   [Function classify](#Function-classify)
-   [Function classmatch](#Function-classmatch)
-   [Function countclassesmatching](#Function-countclassesmatching)
-   [Function countlinesmatching](#Function-countlinesmatching)
-   [Function dirname](#Function-dirname)
-   [Function diskfree](#Function-diskfree)
-   [Function escape](#Function-escape)
-   [Function execresult](#Function-execresult)
-   [Function fileexists](#Function-fileexists)
-   [Function filesexist](#Function-filesexist)
-   [Function filesize](#Function-filesize)
-   [Function getenv](#Function-getenv)
-   [Function getfields](#Function-getfields)
-   [Function getgid](#Function-getgid)
-   [Function getindices](#Function-getindices)
-   [Function getuid](#Function-getuid)
-   [Function getusers](#Function-getusers)
-   [Function getvalues](#Function-getvalues)
-   [Function grep](#Function-grep)
-   [Function groupexists](#Function-groupexists)
-   [Function hash](#Function-hash)
-   [Function hashmatch](#Function-hashmatch)
-   [Function host2ip](#Function-host2ip)
-   [Function ip2host](#Function-ip2host)
-   [Function hostinnetgroup](#Function-hostinnetgroup)
-   [Function hostrange](#Function-hostrange)
-   [Function hostsseen](#Function-hostsseen)
-   [Function hostswithclass](#Function-hostswithclass)
-   [Function hubknowledge](#Function-hubknowledge)
-   [Function iprange](#Function-iprange)
-   [Function irange](#Function-irange)
-   [Function isdir](#Function-isdir)
-   [Function isexecutable](#Function-isexecutable)
-   [Function isgreaterthan](#Function-isgreaterthan)
-   [Function islessthan](#Function-islessthan)
-   [Function islink](#Function-islink)
-   [Function isnewerthan](#Function-isnewerthan)
-   [Function isplain](#Function-isplain)
-   [Function isvariable](#Function-isvariable)
-   [Function join](#Function-join)
-   [Function lastnode](#Function-lastnode)
-   [Function laterthan](#Function-laterthan)
-   [Function ldaparray](#Function-ldaparray)
-   [Function ldaplist](#Function-ldaplist)
-   [Function ldapvalue](#Function-ldapvalue)
-   [Function lsdir](#Function-lsdir)
-   [Function maplist](#Function-maplist)
-   [Function not](#Function-not)
-   [Function now](#Function-now)
-   [Function on](#Function-on)
-   [Function or](#Function-or)
-   [Function parseintarray](#Function-parseintarray)
-   [Function parserealarray](#Function-parserealarray)
-   [Function parsestringarray](#Function-parsestringarray)
-   [Function parsestringarrayidx](#Function-parsestringarrayidx)
-   [Function peers](#Function-peers)
-   [Function peerleader](#Function-peerleader)
-   [Function peerleaders](#Function-peerleaders)
-   [Function product](#Function-product)
-   [Function randomint](#Function-randomint)
-   [Function readfile](#Function-readfile)
-   [Function readintarray](#Function-readintarray)
-   [Function readintlist](#Function-readintlist)
-   [Function readrealarray](#Function-readrealarray)
-   [Function readreallist](#Function-readreallist)
-   [Function readstringarray](#Function-readstringarray)
-   [Function readstringarrayidx](#Function-readstringarrayidx)
-   [Function readstringlist](#Function-readstringlist)
-   [Function readtcp](#Function-readtcp)
-   [Function regarray](#Function-regarray)
-   [Function regcmp](#Function-regcmp)
-   [Function regextract](#Function-regextract)
-   [Function registryvalue](#Function-registryvalue)
-   [Function regline](#Function-regline)
-   [Function reglist](#Function-reglist)
-   [Function regldap](#Function-regldap)
-   [Function remotescalar](#Function-remotescalar)
-   [Function remoteclassesmatching](#Function-remoteclassesmatching)
-   [Function returnszero](#Function-returnszero)
-   [Function rrange](#Function-rrange)
-   [Function selectservers](#Function-selectservers)
-   [Function splayclass](#Function-splayclass)
-   [Function splitstring](#Function-splitstring)
-   [Function strcmp](#Function-strcmp)
-   [Function sum](#Function-sum)
-   [Function translatepath](#Function-translatepath)
-   [Function usemodule](#Function-usemodule)
-   [Function userexists](#Function-userexists)
