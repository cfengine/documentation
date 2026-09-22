import html.parser
import os
import re
import sys
import urllib.parse

# Tags/attributes that carry a URL we should be able to resolve to a file.
LINK_ATTRS = {
    "a": "href",
    "img": "src",
    "link": "href",
    "script": "src",
}

# Schemes that never point at a file in the built site.
SKIPPED_SCHEMES = ("mailto:", "tel:", "javascript:", "data:")

# The version switcher (lts_versions_list.html / versions_list.html) links to
# sibling docs builds for other branches/versions, e.g. "../../docs/3.27/",
# "../../docs/lts/" or "../../docs/archive/index.html". Each version/archive
# is built and deployed separately, so those paths never exist in this
# build's own _site and aren't broken links.
VERSION_LINK_RE = re.compile(
    r"(?:^|/)docs/(?:master|lts|archive|\d+(?:\.\d+){1,2})(?:/|$)"
)


class _LinkExtractor(html.parser.HTMLParser):
    """Collects (url, line) for every href/src found in one HTML page."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []

    def handle_starttag(self, tag, attrs):
        attr_name = LINK_ATTRS.get(tag)
        if attr_name is None:
            return
        url = dict(attrs).get(attr_name)
        if url:
            line, _col = self.getpos()
            self.links.append((url, line))


def _is_checkable(url):
    """Only internal links/assets are worth resolving against the filesystem."""
    url = url.strip()
    if not url or url.startswith("#"):
        return False
    if url.startswith(SKIPPED_SCHEMES):
        return False
    if VERSION_LINK_RE.search(url):
        return False
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme or parsed.netloc:
        return False  # external, e.g. http://, https://, //host/...
    return True


def _resolve(site_root, html_file, url):
    """Map an internal href/src to the file it should point at on disk.

    Returns None for links that don't reference a separate file (e.g. a bare
    "?query" link on the current page).
    """
    path = url.split("#", 1)[0].split("?", 1)[0]
    if not path:
        return None

    if path.startswith("/"):
        target = os.path.join(site_root, path.lstrip("/"))
    else:
        target = os.path.normpath(os.path.join(os.path.dirname(html_file), path))

    # Hugo renders pretty URLs as a directory containing index.html; a link
    # is valid whether or not it has the trailing slash the directory implies.
    if os.path.isdir(target):
        target = os.path.join(target, "index.html")

    return target


def _find_html_files(site_root):
    for dirpath, _dirnames, filenames in os.walk(site_root):
        for filename in filenames:
            if filename.endswith(".html"):
                yield os.path.join(dirpath, filename)


def run(config):
    """Checks every internal link/image/script src in the built site and
    exits non-zero, listing what's broken and where, if any target is
    missing.

    Runs against the generated HTML in CFE_DIR (after the Hugo build) rather
    than the markdown source, so it validates Hugo's actual routing (pretty
    URLs, aliases, page bundles) instead of a reimplementation of it.
    """
    site_root = os.path.join(config["project_directory"], config["CFE_DIR"])
    if not os.path.isdir(site_root):
        sys.stderr.write("ERROR: built site not found at %s\n" % site_root)
        sys.exit(1)

    broken = []
    for html_file in _find_html_files(site_root):
        parser = _LinkExtractor()
        with open(html_file, "r", encoding="utf-8", errors="replace") as f:
            parser.feed(f.read())

        for url, line in parser.links:
            if not _is_checkable(url):
                continue
            target = _resolve(site_root, html_file, url)
            if target is None:
                continue
            if not os.path.exists(target):
                broken.append((os.path.relpath(html_file, site_root), line, url))

    if broken:
        sys.stderr.write(
            "ERROR: %d broken internal link(s)/asset reference(s) found in the built site:\n"
            % len(broken)
        )
        for page, line, url in broken:
            sys.stderr.write("  %s:%d: %s\n" % (page, line, url))
        sys.exit(1)
