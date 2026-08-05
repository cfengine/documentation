---
layout: default
title: validfiledata
aliases:
  - "/reference-functions-validfiledata.html"
---

{{< CFEngine_function_prototype(filename, filetype) >}}

**Description:** Parses CSV, JSON, or YAML data from file `filename`
and returns `true` if the content is valid and `false` otherwise.

When `filetype` is `auto`, the file type is inferred from the extension
(ignoring case): `.csv` means CSV; `.json` means JSON; `.yaml` or `.yml` means
YAML. If the file doesn't match any of those names, JSON is used.

{{< CFEngine_function_attributes(filename, filetype) >}}

**Example:**

```cf3
bundle agent main
{
  vars:
    "content"
      data => readdata("/tmp/a.json", "auto"),
      if => validfiledata("/tmp/a.json", "auto");
}
```

**See also:** [`data_expand()`][data_expand], `readdata()`, `readcsv()`, `readyaml()`, `readjson()`, `readenvfile()`, `validdata()`, `data` documentation.

**History:** Was introduced in 3.29.0.
