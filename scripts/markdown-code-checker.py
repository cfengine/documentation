import marko as md
import os
import argparse
import sys


def extract_inline_code(file_path, languages):
    """extract inline code, language and filters from markdown"""

    with open(file_path, "r") as f:
        content = f.read()

    parser = md.parser.Parser()
    ast = parser.parse(content)

    for child in ast.children:

        if not isinstance(child, md.block.FencedCode):
            continue

        info_string = child.lang.split("|")
        language = info_string[0]
        flags = info_string[1:]

        if language in languages:
            yield language, child.children[0].children, flags


ignored_dirs = [".git"]


def get_markdown_files(start, languages):
    """locate all markdown files and call extract_inline_code on them"""

    if os.path.isfile(start):
        return {start: list(extract_inline_code(start, languages))}

    return_dict = {}
    for root, dirs, files in os.walk(start):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]

        for f in files:
            if f.endswith(".markdown") or f.endswith(".md"):
                path = os.path.join(root, f)
                return_dict[path] = list(extract_inline_code(path, languages))

    return return_dict


def extract(path, i, language, code_snippet):
    with open(f"{path}.snippet-{i}.{language}", "w") as f:
        f.write(code_snippet)


def check_syntax():
    pass


def check_output():
    pass


def replace():
    pass


def autoformat():
    pass


def parse_args():
    parser = argparse.ArgumentParser(
        prog="Markdown inline code checker",
        description="Tool for checking the syntax, the format and the output of markdown inline code",
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
    parser.add_argument(
        "--extract",
        help="extract the inline code into their own files",
        action="store_true",
        required=False,
    )
    parser.add_argument(
        "--autoformat",
        help="automatically format all inline code",
        action="store_true",
        required=False,
    )
    parser.add_argument(
        "--syntax-check",
        help="check syntax of all inline code",
        action="store_true",
        required=False,
    )
    parser.add_argument(
        "--replace",
        help="replace inline code",
        action="store_true",
        required=False,
    )
    parser.add_argument(
        "--output-check",
        help="check output of all inline code",
        action="store_true",
        required=False,
    )

    return parser.parse_args()


if __name__ == "__main__":
    supported_languages = {"cf3": "cf", "json": "json", "yaml": "yml"}
    args = parse_args()

    if not os.path.exists(args.path):
        print("[error] This path doesn't exist")
        sys.exit(-1)

    for language in args.languages:
        if language not in supported_languages:
            print(
                f"[error] Unsupported language '{language}'. The supported languages are: {", ".join(supported_languages.keys())}"
            )
            sys.exit(-1)

    parsed_markdown = get_markdown_files(args.path, args.languages)

    for path, inline_code_list in parsed_markdown.items():
        for i, (language, code_snippet, flags) in enumerate(inline_code_list):

            if args.extract and "noextract" not in flags:
                extract(path, i + 1, supported_languages[language], code_snippet)

            if args.syntax_check and "novalidate" not in flags:
                check_syntax()

            if args.autoformat and "noautoformat" not in flags:
                autoformat()

            if args.replace and "noreplace" not in flags:
                replace()

            if args.output_check and "noexecute" not in flags:
                check_output()
