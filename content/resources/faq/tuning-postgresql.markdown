---
layout: default
title: Tuning PostgreSQL
---

During install the CFEngine Enterprise Hub Package pre-configures PostgreSQL with a configuration for low (<3GB), medium (>3GB <64GB) or high (>64GB) memory which adjusts the values of `effective_cache_size`, `shared_buffers`, and `maintenance_work_mem`.

Depending on various factors your `postgresql.conf` may benefit from further tuning.

Parameters commonly tuned:

- `max_connections`

- `shared_buffers`

- `effective_cache_size`

- `maintenance_work_mem`

- `checkpoint_completion_target`

- `wal_buffers`

- `default_statistics_target`

- `random_page_cost`

- `effective_io_concurrency`

- `work_mem`

- `min_wal_size`

- `max_wal_size`

Tuning tools like [pgtune](https://github.com/kofemann/pgtune) and [pgconfigurator](https://www.cybertec-postgresql.com/en/products/pgconfigurator/) can be helpful in adjusting your settings.

**See also:**

- [Debugging slow queries][debugging slow queries].
- [Policy server requirements][Installing enterprise for production#Policy server requirements].
