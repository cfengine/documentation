import re


def run(config):
    markdown_files = config["markdown_files"]
    for file in markdown_files:
        process(file)


def process(file_path):
    """
    Reads a markdown file, searches for code block that have one-word flags
    and replace with flag=value. Otherwise Hugo will fail to parse markdown
    with error `failed to parse Markdown attributes; you may need to quote the values`
    """
    try:
        # Read the file
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Find and replace codeblocks
        transformed_content = transform_codeblocks(content)

        # Write file if content was changed
        if transformed_content != content:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(transformed_content)

    except Exception as e:
        print(f"Error processing file {file_path}: {str(e)}")
        raise


def transform_codeblocks(content):
    pattern = re.compile(
        r"^\s*```([a-zA-Z0-9_-]+)"  # language
        r"[ \t]+\{([^}]*)\}\s*$",  # flags
        re.MULTILINE,
    )

    def replacer(match):
        language = match.group(1)
        all_flags = match.group(2).strip()

        if not all_flags:
            return f"```{language}"

        flag_parts = all_flags.split()
        transformed_flags = []

        for flag in flag_parts:
            if "=" in flag:
                # Already in key=value format, keep as is
                transformed_flags.append(flag)
            else:
                # One-word flag, transform to flag=""
                transformed_flags.append(f'{flag}=""')

        flags_str = " ".join(transformed_flags)
        return f"```{language} {{{flags_str}}}"

    return pattern.sub(replacer, content)
