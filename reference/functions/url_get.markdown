---
layout: default
title: url_get
published: true
tags: [reference, communication functions, functions, url, www, file, ftp, http, https, url_get, inline_json]
---

[%CFEngine_function_prototype(url, options_container)%]

**Description:** Retrieves the contents of a `url` using options from
  a data container. The data is returned in a
  data container.

**NOTE** that the `options_container` can be specified as inline JSON

[This function can accept many types of data parameters.][Functions#collecting functions]

Currently only `file`, `http`, and `ftp` URLs are supported.
Internally, `libcurl` is used.

`url_get()` caches its results. To invalidate the cache, use a
different set of options, e.g. by modifying an unused key with the
system time.

If the `libcurl` integration is not available, the function will exit
with an error and the variable will remain undefined. If the `libcurl`
initialization fails, the function will also exit with an error. In
every other normal case, the function will return a valid data
container. In official CFEngine packages, `libcurl` integration is
always provided.

The available options currently are:

* `url.max_content`: if present, specifies the maximum number of content bytes to retrieve (**default 4096**).
* `url.max_headers`: if present, specifies the maximum number of response headers to retrieve (**default 4096**).
* `url.verbose`: if 1, `libcurl` will be more verbose while retrieving the content (**default 0**).
* `url.timeout`: if present, `libcurl` will time out the request after that many seconds (**default 3**).
* `url.referer`: if present, `libcurl` will set the Referer to this (**default unset**).
* `url.user-agent`: if present, `libcurl` will set the User-Agent to this (**default unset**).
* `url.headers`: an array of strings in the format `Foo: bar` specifying headers for the request (**default `[Host: host , Accept: \*/\*]`**).

The returned data container will have the following keys:

* `returncode`: the HTTP response code, e.g. `200`.
* `rc`: the `libcurl` integer result code, either `0` for success or something else for failure
* `error_message`: when present, indicates the request was unsuccessful and explains why
* `success`: a boolean.  When `success` is `false`, the result code was not `0` and the request was unsuccessful.
* `content`: the response content as a string
* `headers`: the response headers as a string

[%CFEngine_function_attributes(url, options_container)%]

**Example:**

This example retrieves two URLs using one set of options. The options
are specified in JSON and parsed into a data container `options`. That
data container is then passed to each invocation of `url_get`.

```
bundle agent main
{
  vars:
      "options_str" string => '
{
  "url.max_content": 512,
  "url.verbose": 0,
  "url.headers": [ "Foo: bar" ]
}';
      "options" data => parsejson($(options_str));
      "url" string => "http://cfengine.com";
      "res" data => url_get($(url), options);
      "out" string => format("%S", res);

      "url2" string => "http://nosuchcfenginehost.com";
      "res2" data => url_get($(url2), options);
      "out2" string => format("%S", res2);

  reports:
      "$(this.bundle): from $(url) with options $(options_str) we got $(out)";
      "$(this.bundle): from $(url2) with options $(options_str) we got $(out2)";
}
```

Output:

```
R: main: from http://cfengine.com with options
{
  "cfengine.max_content": 512,
  "curl.verbose": 0,
  "curl.headers": [ "Foo: bar" ]
} we got {"returncode":200,"rc":0,"success":true,"content":"\n<!DOCTYPE html>\n<!--[if lt IE 7]>\n<html class=\"no-js lt-ie9 lt-ie8 lt-ie7\" lang=\"en-US\" prefix=\"og: http://ogp.me/ns#\"> <![endif]-->\n<!--[if IE 7]>\n<html class=\"no-js lt-ie9 lt-ie8\" lang=\"en-US\" prefix=\"og: http://ogp.me/ns#\"> <![endif]-->\n<!--[if IE 8]>\n<html class=\"no-js lt-ie9\" lang=\"en-US\" prefix=\"og: http://ogp.me/ns#\"> <![endif]-->\n<!--[if gt IE 8]><!-->\n<html class=\"no-js\" lang=\"en-US\" prefix=\"og: http://ogp.me/ns#\"> <!--<![endif]-->\n<head>\n\n    \n    <meta charset=\"utf-8\">\n\n    <title>\n        CFEng","headers":"HTTP/1.1 200 OK\r\nDate: Fri, 27 Mar 2015 18:13:01 GMT\r\nServer: Apache\r\nX-Powered-By: PHP/5.3.3\r\nX-Pingback: http://cfengine.com/xmlrpc.php\r\nConnection: close\r\nTransfer-Encoding: chunked\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"}

R: main: from http://nosuchcfenginehost.com with options
{
  "cfengine.max_content": 512,
  "curl.verbose": 0,
  "curl.headers": [ "Foo: bar" ]
} we got {"returncode":0,"rc":6,"success":false,"content":"","headers":""}
```

**History:** Introduced in CFEngine 3.8. The [collecting function][Functions#collecting functions] behavior was added in 3.9.

**See also:** `readtcp()`, `mergedata()`, `parsejson()`, [about collecting functions][Functions#collecting functions], and `data` documentation.
