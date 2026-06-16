"""Wrap bare IPv4 URLs in angle brackets so Markdown renders them as links.

Markdown auto-links hostname URLs but not IP-based ones like
``http://192.0.2.1:8080/path``, so this rewrites them to ``<...>`` autolinks.

- Matches ``http(s)://`` URLs with a dotted IPv4 host, optional port and path,
  anywhere on a line (not just on their own line).
- Skips fenced code blocks, inline `code` spans, and URLs already inside an
  autolink, a `[text](link)`, or an `href="..."` attribute.
- Trailing sentence punctuation is left outside the link.

``run(config)`` is the entry point; it transforms each file in
``config["markdown_files"]`` and writes it back only if it changed.
"""

import re

IPV4_URL_RE = re.compile(
    r"""
    (?<![<(`/\w"'])            # skip if already inside <autolink>, [text](link),
                               # `code`, an href="..."/'...' attribute, or a longer
                               # token (word char / slash) that we'd be splitting
    (                          # capture group 1: the URL itself
      https?://                # scheme
      (?:\d{1,3}\.){3}\d{1,3}  # IPv4
      (?::\d+)?                # optional :port
      (?:/[^\s<>)\]`'"]*)?     # optional /path — stop at whitespace or chars
                               # that typically close/quote the URL
    )
    """,
    re.VERBOSE,
)

FENCE_RE = re.compile(
    r"""
    ^(\s*)              # leading indentation (captured but unused)
    (```+|~~~+)         # fence marker: 3+ backticks or 3+ tildes
    """,
    re.VERBOSE,
)


def run(config):
    for file in config["markdown_files"]:
        process(file)


def process(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        transformed = transform(content)

        if transformed != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(transformed)
    except Exception as e:
        print(f"cfdoc_ip_autolink: error processing {file_path}: {e}")
        raise


def transform(content):
    out_lines = []
    in_fence = False
    fence_marker = None

    for line in content.splitlines(keepends=True):
        if in_fence:
            out_lines.append(line)
            if fence_marker and line.lstrip().startswith(fence_marker):
                in_fence = False
                fence_marker = None
            continue

        m = FENCE_RE.match(line)
        if m:
            fence_marker = m.group(2)
            in_fence = True
            out_lines.append(line)
            continue

        out_lines.append(transform_line(line))

    return "".join(out_lines)


# Stripped from the end of a URL so sentence punctuation stays in the prose.
TRAILING_PUNCT = ".,;:!?"


def _wrap(match):
    url = match.group(1)
    trailing = ""
    while url and url[-1] in TRAILING_PUNCT:
        trailing = url[-1] + trailing
        url = url[:-1]
    return f"<{url}>{trailing}"


def transform_line(line):
    # Split on inline backtick spans so URLs inside `code` are untouched.
    parts = re.split(r"(`+[^`\n]*`+)", line)
    for i, chunk in enumerate(parts):
        if i % 2 == 1:
            continue
        parts[i] = IPV4_URL_RE.sub(_wrap, chunk)
    return "".join(parts)
