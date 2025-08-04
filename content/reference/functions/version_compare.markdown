---
layout: default
title: version_compare
---

{{< CFEngine_function_prototype(version1, comparison, version2) >}}

**Description:** Returns `true` if the specified version comparison expression is true.

{{< CFEngine_function_attributes(version1, comparison, version2) >}}

The `version_compare()` function can be used to compare 2 arbitrary semver version numbers.
This can be useful if you have 2 versions of a package and you want to know if they are the same version, if one is newer than the other etc.

**Example:**

{{< CFEngine_include_snippet(version_compare.cf, #\+begin_src cfengine3, .*end_src) >}}

Output:

{{< CFEngine_include_snippet(version_compare.cf, #\+begin_src\s+example_output\s*, .*end_src) >}}

**Notes:**

Internally, `version_compare` uses the same version comparison logic as other version functions (`cf_version_minimum`, etc.).
This means that only the **`major.minor.patch`** parts of the version string are compared, everything after patch is ignored so `1.2.3`, `1.2.3-1`, `1.2.3-2`, `1.2.3+git1234`, `1.2.3a` are all considered the same version.

In policy you can combine `version_compare()` and `strcmp()` to get more info if desirable:

```cfengine3
bundle agent main
{
  reports:
    "Same patch version, but not exactly the same version string"
      if => and(
        version_compare("$(a)", "=", "$(b)"),
        not(strcmp("$(a)", "$(b)"))
      );
}
```

CFEngine's version comparison functions also support partial version numbers, so if you supply only a major version, or a major and minor version, but no patch version, only the provided parts are compared:

```cfengine3
bundle agent main
{
  vars:
    "patch_a"
      string => "3.21.1";
    "patch_b"
      string => "4.0.1";

  reports:
    "patch_a is a part of the 3.21 series: 3.21 == $(patch_a)"
      if => version_compare("3.21", "==", "$(patch_a)");
    "patch_b is in major version 4: 4 == $(patch_b)"
      if => version_compare("4", "==", "$(patch_b)");
}
```

Beware that using partial version numbers can lead to situations with surprising results, the `>`, `<`, `=`, `!=` operators may not behave exactly as the policy writer expects:

```cfengine3
bundle agent main
{
  reports:
    "3.22.1 > 3.22" # No, won't be printed
      if => version_compare("3.22.1", ">", "3.22");
    "3.22.1 >= 3.22" # Yes, will be printed
      if => version_compare("3.22.1", ">=", "3.22");
}
```

Since `3.22` is less specific than `3.22.1` they are considered equal - all of the parts which can be compared are the same.
For the version comparison logic, if you are asking if something is greater than `3.22`, it must be at least `3.23`, `3.22.1` is not enough.
Thus, it is often more intuitive to use the `>=` operator to mean all versions at or after the specified version (regardless of how specific the version numbers are).

**See also:** `cf_version_minimum()`, `cf_version_maximum()`, `cf_version_after()`, `cf_version_before()`, `cf_version_at()`, `cf_version_between()`.

**History:**

- Introduced in 3.23.0
