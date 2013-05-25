---
layout: default
title: Datatypes
categories: [Manuals, Language Concepts, Datatypes]
published: true
alias: manuals-language-concepts-datatypes.html
tags: [manuals, language, syntax, concepts, datatypes]
---

### Datatypes

CFEngine variables have two high-level types: scalars and lists. 

* A scalar is a single value, 
* a list is a collection of scalars. 

Each scalar may have one of three types: string, int or real.  Typing is dynamic, so these are interchangeable in many instances with a few exceptions, while CFEngine will try its best to coerce string values into int and real types, if it cannot it will report an error.    String scalars are sequences of characters, integers are whole numbers, and reals are float pointing numbers.  While CFEngine typing is mostly dynamic, arguments to special functions check the defined argument type for consistency. 

Integer constants may use suffixes to represent large numbers.  The following suffixes can be used to create integer values for common powers of 1000.

* 'k' = value times 1000.
* 'm' = value times 1000^2
* 'g' = value times 1000^3

Since computing systems such as storage and memory are based on binary values, CFEngine also provide the following uppercase suffixes to create integer values for common powers of 1024.

* 'K' = value times 1024.
* 'M' = value times 1024^2
* 'G' = value times 1024^3

There is a special suffix which is used to denote percentages.

* '%' meaning percent, used in limited contexts

Lastly, there is a reserved value which can be used to specific a parameter as having no limit at all.

* 'inf' = a constant representing an unlimited value.
