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


def process(file_path, references, missing):
    """Process a markdown file and replace reference links with direct links.

    Any reference that cannot be resolved is appended to `missing` as a
    (file_path, ref) tuple so the caller can fail the build.
    """

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern to match reference links: [`text`][reference]
    pattern = r"\[(.*?)\]\[(.*?)\]"

    def replace_link(match):
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

    new_content = re.sub(pattern, replace_link, content)

    # finds functions except ones already processed inside []
    functions_pattern = r"(?<!\[)\`([^\s]*?)\(\)\`(?!\])"

    def replace_function_link(match):
        ref = match.group(1)
        text = f"{ref}()"
        ref_lower = ref.lower()
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

    new_content = re.sub(functions_pattern, replace_function_link, new_content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)


def run(config):
    """Replaces [text][reference] with markdown links retrieved from _references.md.

    Exits non-zero if any reference cannot be resolved, so broken autolinks
    fail the build loudly instead of silently shipping unresolved markdown.
    """
    markdown_files = config["markdown_files"]
    references = load_references("documentation/generator/_references.md")

    missing = []
    for file in markdown_files:
        process(file, references, missing)

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
