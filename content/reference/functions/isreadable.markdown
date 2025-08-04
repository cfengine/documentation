---
layout: default
title: isreadable
---

{{< CFEngine_function_prototype(path, timeout) >}}

**Description:** Check if a file is readable.

This function checks if the file specified by the `path` parameter is readable
by trying to read 1 Byte from it. If the file is not ready for I/O, and the
`timeout` parameter is not set to 0, the read operation will block for at most
`timeout` number of seconds.

The `timeout` parameter is optional and defaults to 3 seconds, if it is not
specified. If the `timeout` parameter is set to 0, the read operation may block
indefinetly.

The function evaluates to false if the time limit expires or the read operation
fails for any other reason (e.g. permission denied).

**Notes:**

When the `timeout` parameter is set to 0, the agent will try to open and read
the file in the main thread, which can cause the agent to block indefinetly.

When the `timeout` parameter is not 0, the agent will spawn a separate thread
in a detached state, that will try to open and read the file. The agent will
wait for at most N number of seconds for the spawned thread to finish. If the
thread does not finish in time, the agent will consider the file unreadable.

If the file is of size 0, the function will return true, if it successfully
reads 0 bytes (reaches end-of-file).

Please *note* that the agent will evaluate this policy function multiple times,
meaning that the use of this function can cause a significant performance
penalty.

**Example:**

{{< CFEngine_include_snippet(isreadable.cf, #\+begin_src cfengine3, .*end_src) >}}

Output:

{{< CFEngine_include_snippet(isreadable.cf, #\+begin_src\s+example_output\s*, .*end_src) >}}

**History:** Introduced in 3.22.

**See also:** [`filestat()`][filestat], [`isexecutable()`][isexecutable], [`isdir()`][isdir], [`isplain()`][isplain].
