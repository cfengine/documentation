---
layout: default
title: Introduction-to-functions
categories: [Special-functions,Introduction-to-functions]
published: true
alias: Special-functions-Introduction-to-functions.html
tags: [Special-functions,Introduction-to-functions]
---

### Introduction to Functions

\
 There are a large number of functions built into CFEngine, and finding
the right one to use can be a daunting task. The following tables are
designed to make it easier for you to find the function you need, based
on the value or type that the function returns or processes as inputs.

#### Functions listed by return value

##### Functions That Return Class

  ---------------------------------------------------------- -------------------------------------- ------------------------------------------ -------------------------------------- ------------------------------------------
  [accessedbefore](#Function-accessedbefore)                 [and](#Function-and)                   [changedbefore](#Function-changedbefore)   [classify](#Function-classify)         [classmatch](#Function-classmatch) \
                                                                                                                                                                                      

  [concat](#Function-concat)                                 [fileexists](#Function-fileexists)     [filesexist](#Function-filesexist)         [groupexists](#Function-groupexists)   [hashmatch](#Function-hashmatch) \
                                                                                                                                                                                      

  [hostinnetgroup](#Function-hostinnetgroup)                 [hostrange](#Function-hostrange)       [iprange](#Function-iprange)               [isdir](#Function-isdir)               [isexecutable](#Function-isexecutable) \
                                                                                                                                                                                      

  [isgreaterthan](#Function-isgreaterthan)                   [islessthan](#Function-islessthan)     [islink](#Function-islink)                 [isnewerthan](#Function-isnewerthan)   [isplain](#Function-isplain) \
                                                                                                                                                                                      

  [isvariable](#Function-isvariable)                         [ldaparray](#Function-ldaparray)       [or](#Function-or)                         [not](#Function-not)                   [regarray](#Function-regarray) \
                                                                                                                                                                                      

  [regcmp](#Function-regcmp)                                 [regextract](#Function-regextract)     [regldap](#Function-regldap)               [regline](#Function-regline)           [reglist](#Function-reglist) \
                                                                                                                                                                                      

  [remoteclassesmatching](#Function-remoteclassesmatching)   [returnszero](#Function-returnszero)   [splayclass](#Function-splayclass)         [strcmp](#Function-strcmp)             [usemodule](#Function-usemodule) \
                                                                                                                                                                                      

  [userexists](#Function-userexists) \
  ---------------------------------------------------------- -------------------------------------- ------------------------------------------ -------------------------------------- ------------------------------------------

##### Functions That Return (i,r,s)List

  ---------------------------------------- -------------------------------- -------------------------------------- ---------------------------------------- ----------------------------------------------
  [getindices](#Function-getindices)       [getusers](#Function-getusers)   [grep](#Function-grep)                 [ldaplist](#Function-ldaplist)           [maplist](#Function-maplist) \
                                                                                                                                                            

  [peerleaders](#Function-peerleaders)     [peers](#Function-peers)         [readintlist](#Function-readintlist)   [readreallist](#Function-readreallist)   [readstringlist](#Function-readstringlist) \
                                                                                                                                                            

  [splitstring](#Function-splitstring) \
  ---------------------------------------- -------------------------------- -------------------------------------- ---------------------------------------- ----------------------------------------------

##### Functions That Return Int

  ---------------------------------------- ------------------------------------------ ---------------------------------------------------- ---------------------------------------------------- --------------------------------------------
  [accumulated](#Function-accumulated)     [ago](#Function-ago)                       [countlinesmatching](#Function-countlinesmatching)   [diskfree](#Function-diskfree)                       [getfields](#Function-getfields) \
                                                                                                                                                                                                

  [getgid](#Function-getgid)               [getuid](#Function-getuid)                 [now](#Function-now)                                 [on](#Function-on)                                   [randomint](#Function-randomint) \
                                                                                                                                                                                                

  [readintarray](#Function-readintarray)   [readrealarray](#Function-readrealarray)   [readstringarray](#Function-readstringarray)         [readstringarrayidx](#Function-readstringarrayidx)   [selectservers](#Function-selectservers) \
                                                                                                                                                                                                
  ---------------------------------------- ------------------------------------------ ---------------------------------------------------- ---------------------------------------------------- --------------------------------------------

##### Functions That Return (i,r)Range

  ---------------------------- ------------------------------
  [irange](#Function-irange)   [rrange](#Function-rrange) \
                               
  ---------------------------- ------------------------------

##### Functions That Return Real

  ------------------------------ ------------------------
  [product](#Function-product)   [sum](#Function-sum) \
                                 
  ------------------------------ ------------------------

##### Functions That Return String

  -------------------------------------------- ---------------------------------- ------------------------------------ ------------------------------------------ ------------------------------------------
  [canonify](#Function-canonify)               [escape](#Function-escape)         [execresult](#Function-execresult)   [getenv](#Function-getenv)                 [hash](#Function-hash) \
                                                                                                                                                                  

  [host2ip](#Function-host2ip)                 [hostsseen](#Function-hostsseen)   [join](#Function-join)               [lastnode](#Function-lastnode)             [ldapvalue](#Function-ldapvalue) \
                                                                                                                                                                  

  [peerleader](#Function-peerleader)           [readfile](#Function-readfile)     [readtcp](#Function-readtcp)         [registryvalue](#Function-registryvalue)   [remotescalar](#Function-remotescalar) \
                                                                                                                                                                  

  [translatepath](#Function-translatepath) \
  -------------------------------------------- ---------------------------------- ------------------------------------ ------------------------------------------ ------------------------------------------

#### Functions That Fill Arrays

The following functions all fill arrays, although they return values
that depend on the number of items processed.

  -------------------------------------- ---------------------------------------- ------------------------------------------ ---------------------------------------------- ------------------------------------------------------
  [getfields](#Function-getfields)       [readintarray](#Function-readintarray)   [readrealarray](#Function-readrealarray)   [readstringarray](#Function-readstringarray)   [readstringarrayidx](#Function-readstringarrayidx) \
                                                                                                                                                                            

  [regextract](#Function-regextract) \
  -------------------------------------- ---------------------------------------- ------------------------------------------ ---------------------------------------------- ------------------------------------------------------

#### Functions That Read Large Data

The following functions read data from inside CFEngine (from classes,
lists, strings, etc.) and outside of CFEngine (from files, databases,
arrays, etc.).

##### Functions That Read Arrays

  -------------------------------------- ----------------------------------
  [getindices](#Function-getindices) \

  [getvalues](#Function-getvalues)       [regarray](#Function-regarray) \
                                         
  -------------------------------------- ----------------------------------

##### Functions That Read Disk Data

  ----------------------------------
  [diskfree](#Function-diskfree) \
  ----------------------------------

##### Functions That Read From a Remote-CFEngine

  ---------------------------------------------------------- ------------------------------------------
  [remoteclassesmatching](#Function-remoteclassesmatching)   [remotescalar](#Function-remotescalar) \
                                                             
  ---------------------------------------------------------- ------------------------------------------

##### Functions That Read Classes

  ---------------------- -------------------------------- ------------------------------------ ---------------------------- ------------------------
  [and](#Function-and)   [classify](#Function-classify)   [classmatch](#Function-classmatch)   [concat](#Function-concat)   [not](#Function-not) \
                                                                                                                            

  [or](#Function-or) \
  ---------------------- -------------------------------- ------------------------------------ ---------------------------- ------------------------

##### Functions That Read Command Output

  ------------------------------------ -------------------------------------- ------------------------------------
  [execresult](#Function-execresult)   [returnszero](#Function-returnszero)   [usemodule](#Function-usemodule) \
                                                                              
  ------------------------------------ -------------------------------------- ------------------------------------

##### Functions That Read the Environment

  ------------------------------
  [getenv](#Function-getenv) \
  ------------------------------

##### Functions That Read Files

  ---------------------------------------------------- ---------------------------------------- ---------------------------------------------- ---------------------------------------------------- ----------------------------------------------
  [countlinesmatching](#Function-countlinesmatching)   [getfields](#Function-getfields)         [getusers](#Function-getusers)                 [hashmatch](#Function-hashmatch)                     [peerleader](#Function-peerleader) \
                                                                                                                                                                                                    

  [peerleaders](#Function-peerleaders)                 [peers](#Function-peers)                 [readfile](#Function-readfile)                 [readintarray](#Function-readintarray)               [readintlist](#Function-readintlist) \
                                                                                                                                                                                                    

  [readrealarray](#Function-readrealarray)             [readreallist](#Function-readreallist)   [readstringarray](#Function-readstringarray)   [readstringarrayidx](#Function-readstringarrayidx)   [readstringlist](#Function-readstringlist) \
                                                                                                                                                                                                    

  [regline](#Function-regline) \
  ---------------------------------------------------- ---------------------------------------- ---------------------------------------------- ---------------------------------------------------- ----------------------------------------------

##### Functions That Read LDAP Data

  ---------------------------------- -------------------------------- ---------------------------------- --------------------------------
  [ldaparray](#Function-ldaparray)   [ldaplist](#Function-ldaplist)   [ldapvalue](#Function-ldapvalue)   [regldap](#Function-regldap) \
                                                                                                         
  ---------------------------------- -------------------------------- ---------------------------------- --------------------------------

##### Functions That Read From the Network

  ------------------------------ --------------------------------------------
  [readtcp](#Function-readtcp)   [selectservers](#Function-selectservers) \
                                 
  ------------------------------ --------------------------------------------

##### Functions That Read the Windows Registry

  --------------------------------------------
  [registryvalue](#Function-registryvalue) \
  --------------------------------------------

##### Functions That Read (i,r,s)Lists

  -------------------------------- --------------------------
  [grep](#Function-grep)           [join](#Function-join) \
                                   

  [product](#Function-product) \

  [reglist](#Function-reglist) \

  [sum](#Function-sum) \
  -------------------------------- --------------------------

##### Functions That Read Strings

  ---------------------------- -------------------------------------------- ---------------------------- ------------------------------------ ----------------------------------------
  [hash](#Function-hash)       [lastnode](#Function-lastnode)               [regcmp](#Function-regcmp)   [regextract](#Function-regextract)   [splitstring](#Function-splitstring) \
                                                                                                                                              

  [strcmp](#Function-strcmp)   [translatepath](#Function-translatepath) \
                               
  ---------------------------- -------------------------------------------- ---------------------------- ------------------------------------ ----------------------------------------

#### Functions That Look at File Metadata

The following functions examine file metadata, but don't use the
contents of the file.

  -------------------------------------------- ------------------------------------------ ------------------------------------ ------------------------------------ ----------------------------
  [accessedbefore](#Function-accessedbefore)   [changedbefore](#Function-changedbefore)   [fileexists](#Function-fileexists)   [filesexist](#Function-filesexist)   [isdir](#Function-isdir) \
                                                                                                                                                                    

  [islink](#Function-islink)                   [isnewerthan](#Function-isnewerthan)       [isplain](#Function-isplain) \
                                                                                          
  -------------------------------------------- ------------------------------------------ ------------------------------------ ------------------------------------ ----------------------------

#### Functions That Look at Variables

  ------------------------------------------ ------------------------------------ --------------------------------------
  [isgreaterthan](#Function-isgreaterthan)   [islessthan](#Function-islessthan)   [isvariable](#Function-isvariable) \
                                                                                  
  ------------------------------------------ ------------------------------------ --------------------------------------

#### Functions Involving Date or Time

The following functions all do date or time computation

  -------------------------------------------- -------------------------------------- -------------------------------------- ------------------------------------------ ----------------------------------------
  [accessedbefore](#Function-accessedbefore)   [accumulated](#Function-accumulated)   [ago](#Function-ago)                   [changedbefore](#Function-changedbefore)   [isnewerthan](#Function-isnewerthan) \
                                                                                                                                                                        

  [now](#Function-now)                         [on](#Function-on)                     [splayclass](#Function-splayclass) \
                                                                                      
  -------------------------------------------- -------------------------------------- -------------------------------------- ------------------------------------------ ----------------------------------------

#### Functions That Work With or On Regular Expressions

  ---------------------------------------------------- ---------------------------------------------------- ------------------------------------------ ---------------------------------------- ------------------------------------------------
  [classmatch](#Function-classmatch)                   [countlinesmatching](#Function-countlinesmatching)   [escape](#Function-escape)                 [getfields](#Function-getfields)         [grep](#Function-grep) \
                                                                                                                                                                                                

  [readintarray](#Function-readintarray)               [readintlist](#Function-readintlist)                 [readrealarray](#Function-readrealarray)   [readreallist](#Function-readreallist)   [readstringarray](#Function-readstringarray) \
                                                                                                                                                                                                

  [readstringarrayidx](#Function-readstringarrayidx)   [readstringlist](#Function-readstringlist)           [regarray](#Function-regarray)             [regcmp](#Function-regcmp)               [regextract](#Function-regextract) \
                                                                                                                                                                                                

  [regldap](#Function-regldap)                         [regline](#Function-regline)                         [reglist](#Function-reglist)               [splitstring](#Function-splitstring) \
                                                                                                                                                       
  ---------------------------------------------------- ---------------------------------------------------- ------------------------------------------ ---------------------------------------- ------------------------------------------------

