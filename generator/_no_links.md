<!--
  Names that look like CFEngine functions (`foo()`) but should NOT be
  autolinked. Autolinking normally turns `foo()` in backticks into a link to
  the documentation for that function, and fails the build if no target is
  found (see cfdoc_references_resolver.py). List one name per line here to opt
  it out of autolinking entirely — it is left as plain backtick text and does
  not count as a broken link. Lines starting with `<!--`/blank lines are
  ignored. The trailing `()` is optional.
-->

validate_promise()
evaluate_promise()
