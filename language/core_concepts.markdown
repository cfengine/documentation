### 1.2 Core concepts

Unlike previous versions of CFEngine, which had no consistent model
for its features, you can recognize *everything* in CFEngine 3 from
just a few concepts.

*Promise*
  ~ A declaration about the *state* we desire to maintain (*e.g.,*
    the permissions or contents of a file, the availability or absence
    of a service, the (de)installation of a package).
*Promise bundles*
  ~ A collection of promises.
*Promise bodies*
  ~ A part of a promise which details and constrains its nature.
*Data types*
  ~ An interpretation of a scalar value: string, integer or real
    number.
*Variables*
  ~ An association of the form "LVALUE *represents* RVALUE", where
    rval may be a scalar value or a list of scalar values.
*Functions*
  ~ Built-in parameterized rvalues.
*Classes*
  ~ CFEngine's boolean classifiers that describe context.

If you have used CFEngine before then the most visible part of
CFEngine 3 will be its new language interface. Although it has been
clear for a long time that the organically grown language used in
CFEngine 1 and 2 developed many problems, it was not immediately clear
exactly what would be better. It has taken years of research to
simplify the successful features of CFEngine to a single overarching
model. To understand the new CFEngine, it is best to set aside any
preconceptions about what CFEngine is today. CFEngine 3 is a genuine
"next generation" effort, which is a springboard into the future of
system management.

