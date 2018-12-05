---
layout: default
title: Debugging Slow Queries
published: true
sorting: 90
tags: [ FAQ, Enterprise, debug, Mission Portal ]
---

If Mission Portal seems to take too much time to generate pages or reports or if API calls seem 
to be taking too long. You can enable logging and analyzing slow queries in postgresql with the
following changes:

1. Edit `/var/cfengine/state/pg/data/postgresql.conf`. Add the following lines at the end of the file

   ```sh
   session_preload_libraries = 'auto_explain'
   auto_explain.log_analyze = 'on'
   auto_explain.log_min_duration = 1000
   ```

   The `log_min_duration` is in milliseconds so adjust as needed.

   See https://www.postgresql.org/docs/current/auto-explain.html for more details.

2. Observe the postgresql log at `/var/log/postgresql.log`. Send the log with any
   bug report you wish to send.
