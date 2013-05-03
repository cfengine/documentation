---
layout: default
title: Variable-context-const
categories: [Special-Variables,Variable-context-const]
published: true
alias: Special-Variables-Variable-context-const.html
tags: [Special-Variables,Variable-context-const]
---

### Variable context `const`

\

CFEngine defines a number of variables for embedding unprintable values
or values with special meanings in strings.

-   [Variable const.dollar](#Variable-const_002edollar)
-   [Variable const.endl](#Variable-const_002eendl)
-   [Variable const.n](#Variable-const_002en)
-   [Variable const.r](#Variable-const_002er)
-   [Variable const.t](#Variable-const_002et)

#### Variable const.dollar

\

~~~~ {.verbatim}
reports:

  some::

   # This will report: The value of $(const.dollar) is $
   "The value of $(const.dollar)(const.dollar) is $(const.dollar)";

   # This will report: But the value of \$(dollar) is \$(dollar)
   "But the value of \$(dollar) is \$(dollar)";
~~~~

#### Variable const.endl

\

~~~~ {.verbatim}
reports:

 cfengine_3::

  "A newline with either $(const.n) or with $(const.endl) is ok";
  "But a string with \n in it does not have a newline!";
~~~~

#### Variable const.n

\

~~~~ {.verbatim}
reports:

 cfengine_3::

  "A newline with either $(const.n) or with $(const.endl) is ok";
  "But a string with \n in it does not have a newline!";
~~~~

#### Variable const.r

\

~~~~ {.verbatim}
reports:

 cfengine_3::

  "A carriage return character is $(const.r)";
~~~~

#### Variable const.t

\

~~~~ {.verbatim}
reports:

 cfengine_3::

  "A report with a$(const.t)tab in it";
~~~~
