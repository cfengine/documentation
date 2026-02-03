---
layout: default
title: Limits
categories: [Reference, Limits]
---

There are various limits enforced in CFEngine, for names and values in both policy, web UI, and other places.
It can sometimes be relevant for both developers and users to know what limits are in place.
The term limits is used broadly, referring to different kinds of limits (character limits, rate limits, allowed / blocked characters, etc.).

## Limits in policy language and evaluation

**Variable names:** Maximum 1024 characters.

**Variable values (strings):** No explicit maximum, we've tested strings of several megabytes, however this is not recommended for several reasons:

- When strings get excessively long, everything you do with them takes a long time.
  To test this and give some kind of idea: parsing and storing a ~3MB string in a variable took 25 seconds on the author's laptop.
- If you want to include these variables in reporting data, they will be truncated.
  (See below for details).
- Any time you print such a variable, there will be a lot of output.
  (And printing this data to file or console is also slow).
- `cf-agent` will exit if you create variables so large that you run out of memory.
- Historically, some built-in functions in policy language have truncated strings (usually to around 4K bytes).
  This is not intended / desirable, we are fixing those, but it might be relevant for you, especially if you use older versions of CFEngine.

For these reasons, we recommend keeping both variable names and values (strings) to less than 1000 bytes.
If you need more, and you're okay with them being truncated in the reporting data, larger strings should also work well.
You can, for example, try to stay within 16K, it should not be particularly slow.

## Limits in reporting data

Each entity reported (such as a variable or class), including metadata about it, needs to fit within a 4096 byte network "transaction".

**Variables:** Maximum 4078 bytes combined for namespace, bundle name, variable name, variable value, and tags.
The last 18 bytes up to 4096 are a timestamp, and the separators added between the fields.

**Classes:** Maximum 4080 bytes combined for class name and tags.
The last 16 bytes are used for a timestamp and the separators.

## Limits in Web UI and Rest API

**URLs:** The URLs used in settings for LLMs and CFEngine Build projects are limited to 2048 characters.

**Group names:** Maximum 100 characters.

**Passwords:** Maximum 20 characters.

### CMDB / group data / host specific data

**Names:** Maximum 255 characters.

**Values:** Maximum 16 000 characters (16k).

## Limits in CFEngine Build

**Module names:** Maximum 64 characters.
Lowercase ASCII alphanumericals, starting with a letter, and possible singular dashes in the middle.
Uppercase letters and other symbols are not permitted.

**Build steps:** Maximum 256 characters.

**Filenames:** Maximum 128 characters.
Lowercase and uppercase ASCII letters, dots, dashes, and underscores.
Spaces and other symbols (like slashes, quotes, and semicolons) are not permitted.

<!--

Todos:

Password attempt limits.
2FA attempt limits.

Namespace name length.
Bundle name length.
Qualified name length (namespace:bundle.name).
-->
