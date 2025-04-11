import marko as md
import os
import argparse
import sys


def extract_inline_code(file_path, languages):
    """extract inline code, language from markdown"""

    with open(file_path, "r") as f:
        content = f.read()

    parser = md.parser.Parser()
    ast = parser.parse(content)

    code_snippet_count = 0
    for child in ast.children:
        # TODO: add a way to exclude a code snippet
        if isinstance(child, md.block.FencedCode) and child.lang in languages:
            code_snippet_count += 1
            yield (code_snippet_count, child.lang, child.children[0].children)


ignored_dirs = [".git"]


def get_markdown_files(start, languages):
    """locate all markdown files and call check_code_syntax on them"""

    if os.path.isfile(start):
        check_code_syntax(start, languages)

    for root, dirs, files in os.walk(start):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]

        for f in files:
            if f.endswith(".markdown") or f.endswith(".md"):
                path = os.path.join(root, f)
                check_code_syntax(path, languages)


def check_code_syntax(path, languages):
    """check syntax of every code snippet of one specific markdown file"""

    iter = extract_inline_code(path, languages)
    for i, language, code_snippet in iter:

        file_name = f"{path}.snippet-{i}"
        match language:
            case "cf3":
                write_file(file_name, "cf", code_snippet)
                # TODO: run cf-promises on the file
                # maybe also check run cf-agent and check if output is correct
                break
            case "json":
                write_file(file_name, "json", code_snippet)
                # TODO: check json syntax and run cfbs pretty
                break
            case "yaml":
                write_file(file_name, "yml", code_snippet)
                # TODO: check yaml syntax
                break


def write_file(file_name, extension, code_snippet):
    with open(f"{file_name}.{extension}", "w") as f:
        f.write(code_snippet)


def parse_args():
    parser = argparse.ArgumentParser(
        prog="Markdown inline code syntax checker",
        description="checks the syntax of documentation inline code",
    )
    parser.add_argument(
        "--path",
        "-p",
        help="path of file or directory to check syntax on",
        default=".",
        required=False,
    )
    parser.add_argument(
        "--languages",
        "-l",
        nargs="+",
        help="languages to check syntax of",
        default=["cf3", "json", "yaml"],
        required=False,
    )

    return parser.parse_args()


if __name__ == "__main__":
    supported_languages = ["cf3", "json", "yaml"]
    args = parse_args()

    if not os.path.exists(args.path):
        print("[error] This path doesn't exist")
        sys.exit(-1)

    for language in args.languages:
        if language not in supported_languages:
            print(
                f"[error] Unsupported language '{language}'. The supported languages are: {", ".join(supported_languages)}"
            )
            sys.exit(-1)

    get_markdown_files(args.path, args.languages)
