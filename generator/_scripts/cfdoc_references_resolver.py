import re
import os
import sys


def load_references(references_file):
    """Parse the _references.md file and return a dictionary of references."""
    references = {}
    content = ""

    refs_path = os.path.join(os.environ.get("WRKDIR"), references_file)
    try:
        if os.path.exists(refs_path):
            with open(refs_path, "r", encoding="utf-8") as file:
                content = file.read()
        else:
            sys.stderr.write(
                f"Warning: References file {refs_path} not found. No references will be added."
            )
            return ""
    except Exception as e:
        sys.stderr.write(f"Error reading references file {refs_path}: {str(e)}")
        return ""

    # Pattern to match reference definitions: [ref]: url "title"
    pattern = r'\[(.*?)\]:\s+(.*?)(?:\s+"(.*?)")?\s*$'

    for match in re.finditer(pattern, content, re.MULTILINE):
        ref, url, title = match.groups()
        if title is None:
            title = ""
        # store with lowercase key for case-insensitive matching
        references[ref.lower()] = (url, title)

    return references


def load_no_links(no_links_file):
    """Parse the _no_links.md file and return a set of function names that
    should NOT be autolinked.

    Each non-empty, non-comment line is a name like ``foo()`` or ``foo``; the
    trailing ``()`` is optional. HTML comment blocks (``<!-- ... -->``, possibly
    spanning multiple lines) are ignored. Names are stored lowercased for
    case-insensitive matching against autolink candidates.
    """
    no_links = set()

    path = os.path.join(os.environ.get("WRKDIR"), no_links_file)
    if not os.path.exists(path):
        sys.stderr.write(
            f"Warning: No-links file {path} not found. All function names will be autolinked.\n"
        )
        return no_links

    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
    except Exception as e:
        sys.stderr.write(f"Error reading no-links file {path}: {str(e)}\n")
        return no_links

    # Drop HTML comment blocks (including multi-line ones) before parsing names.
    content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)
    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue
        no_links.add(line.removesuffix("()").lower())

    return no_links


def process(file_path, references, no_links, missing):
    """Process a markdown file and replace reference links with direct links.

    Any reference that cannot be resolved is appended to `missing` as a
    (file_path, ref) tuple so the caller can fail the build.

    Code content is skipped so that things that look like reference links but
    aren't (CFEngine array notation `a[b][c]`, sample output `[1][0]`, etc.)
    don't get treated as broken `[text][ref]` links:
      * Triple-backtick fenced code blocks — common when snippets are pulled
        in from the core repo via macros.
      * Inline single-backtick code spans on a single line.

    Function-name autolinking (``foo()``) is the inverse: it deliberately
    targets backtick-quoted text, so it runs on every non-fenced line.
    """

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Pattern to match reference links: [`text`][reference]
    pattern = re.compile(r"\[(.*?)\]\[(.*?)\]")
    # finds functions except ones already processed inside []
    functions_pattern = re.compile(r"(?<!\[)\`([^\s]*?)\(\)\`(?!\])")

    def is_inside_inline_code(line, pos):
        # odd number of single backticks before `pos` means we're inside a span
        return line.count("`", 0, pos) % 2 == 1

    def replace_link(match):
        if is_inside_inline_code(match.string, match.start()):
            return match.group(0)

        text, ref = match.groups()
        ref = (
            ref or text
        )  # if ref is empty use text as ref to support cases like [ref][]

        ref_lower = ref.lower()
        if ref_lower in references:
            url, title = references[ref_lower]
            if title:
                escaped_title = title.replace('"', '\\"')
                return f'[{text}]({url} "{escaped_title}")'
            else:
                return f"[{text}]({url})"
        else:
            missing.append((file_path, ref))
            return match.group(0)

    def replace_function_link(match):
        ref = match.group(1)
        text = f"{ref}()"
        ref_lower = ref.lower()
        if ref_lower in no_links:
            # Explicitly opted out of autolinking; leave as plain text.
            return match.group(0)
        if ref_lower in references:
            url, title = references[ref_lower]
            if title:
                escaped_title = title.replace('"', '\\"')
                return f'[{text}]({url} "{escaped_title}")'
            else:
                return f"[{text}]({url})"
        else:
            missing.append((file_path, f"{ref}()"))
            return match.group(0)

    new_lines = []
    in_pre = False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_pre = not in_pre
            new_lines.append(line)
            continue
        if in_pre:
            new_lines.append(line)
            continue
        line = pattern.sub(replace_link, line)
        line = functions_pattern.sub(replace_function_link, line)
        new_lines.append(line)

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


def run(config):
    """Replaces [text][reference] with markdown links retrieved from _references.md.

    Exits non-zero if any reference cannot be resolved, so broken autolinks
    fail the build loudly instead of silently shipping unresolved markdown.
    """
    markdown_files = config["markdown_files"]
    references = load_references("documentation/generator/_references.md")
    no_links = load_no_links("documentation/generator/_no_links.md")

    missing = []
    for file in markdown_files:
        # cfdoc_log.markdown is the QA log written by cfdoc_qa.py, not real
        # documentation. Its entries quote link warnings using literal
        # [foo#foo][foo#foo] markdown, so linting it produces hundreds of bogus
        # "unresolved reference" errors. Never treat it as a source file.
        if os.path.basename(file) == "cfdoc_log.markdown":
            continue
        process(file, references, no_links, missing)

    if missing:
        sys.stderr.write(
            "ERROR: %d unresolved reference link(s) found in _references.md:\n"
            % len(missing)
        )
        for file_path, ref in missing:
            sys.stderr.write(f"  [{ref}] in {file_path}\n")
        sys.stderr.write(
            "Add the missing entries to documentation/generator/_references.md "
            "or fix the links in the listed files.\n"
        )
        sys.exit(1)
