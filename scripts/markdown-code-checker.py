from cfbs.pretty import pretty_file
from shutil import which
import markdown_it
import os
import argparse
import sys
import subprocess


def extract_inline_code(file_path, languages):
    """extract inline code, language and filters from markdown"""

    with open(file_path, "r") as f:
        content = f.read()

    md = markdown_it.MarkdownIt("commonmark")
    ast = md.parse(content)

    for child in ast:

        if child.type != "fence":
            continue

        if not child.info:
            continue

        info_string = child.info.split()
        language = info_string[0]
        flags = info_string[1:]

        if language in languages:
            yield {
                "language": language,
                "flags": flags,
                "first_line": child.map[0],
                "last_line": child.map[1],
            }


ignored_dirs = [".git"]


def get_markdown_files(start, languages):
    """locate all markdown files and call extract_inline_code on them"""

    if os.path.isfile(start):
        return {
            "files": {
                start: {"code-blocks": list(extract_inline_code(start, languages))}
            }
        }

    return_dict = {"files": {}}
    for root, dirs, files in os.walk(start):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]

        for f in files:
            if f.endswith(".markdown") or f.endswith(".md"):
                path = os.path.join(root, f)
                return_dict["files"][path] = {
                    "code-blocks": list(extract_inline_code(path, languages))
                }

    return return_dict


def extract(path, i, language, first_line, last_line):

    with open(path, "r") as f:
        content = f.read()

    code_snippet = "\n".join(content.split("\n")[first_line + 1 : last_line - 1])

    with open(f"{path}.snippet-{i}.{language}", "w") as f:
        f.write(code_snippet)


def check_syntax(path, i, language, first_line, last_line):
    file_name = f"{path}.snippet-{i}.{language}"
    abs_file_name = os.path.abspath(file_name)

    if not os.path.exists(file_name):
        print(
            f"[error] Couldn't find the file '{file_name}'. Run --extract to extract the inline code."
        )
        return

    match language:
        case "cf":
            p = subprocess.run(
                ["/var/cfengine/bin/cf-promises", abs_file_name],
                capture_output=True,
                text=True,
            )
            err = p.stderr

            if err:
                err = err.replace(abs_file_name, f"{path}:{first_line}")
                print(err)


def check_output():
    pass


def replace(path, i, language, first_line, last_line):
    file_name = f"{path}.snippet-{i}.{language}"

    try:
        with open(file_name, "r") as f:
            pretty_content = f.read()
    except:
        print(
            f"[error] Couldn't find the file '{file_name}'. Run --extract to extract the inline code."
        )
        return

    with open(path, "r") as f:
        lines = f.read().split("\n")
        pretty_lines = pretty_content.split("\n")

        offset = len(pretty_lines) - len(lines[first_line + 1 : last_line - 1])

    lines[first_line + 1 : last_line - 1] = pretty_lines

    with open(path, "w") as f:
        f.write("\n".join(lines))

    return offset


def autoformat(path, i, language, first_line, last_line):
    file_name = f"{path}.snippet-{i}.{language}"

    match language:
        case "json":
            try:
                pretty_file(file_name)
            except:
                print(
                    f"[error] Couldn't find the file '{file_name}'. Run --extract to extract the inline code."
                )


def parse_args():
    parser = argparse.ArgumentParser(
        prog="Markdown inline code checker",
        description="Tool for checking the syntax, the format and the output of markdown inline code",
    )
    parser.add_argument(
        "path",
        help="path of file or directory to check syntax on",
        nargs="?",
        default=".",
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

    if (
        args.syntax_check
        and "cf3" in args.languages
        and not which("/var/cfengine/bin/cf-promises")
    ):
        print("[error] cf-promises is not installed")
        sys.exit(-1)

    for language in args.languages:
        if language not in supported_languages:
            print(
                f"[error] Unsupported language '{language}'. The supported languages are: {", ".join(supported_languages.keys())}"
            )
            sys.exit(-1)

    parsed_markdowns = get_markdown_files(args.path, args.languages)

    for path in parsed_markdowns["files"].keys():
        offset = 0
        for i, code_block in enumerate(parsed_markdowns["files"][path]["code-blocks"]):

            # adjust line numbers after replace
            for cb in parsed_markdowns["files"][path]["code-blocks"][i:]:
                cb["first_line"] += offset
                cb["last_line"] += offset

            if args.extract and "noextract" not in code_block["flags"]:
                extract(
                    path,
                    i + 1,
                    supported_languages[code_block["language"]],
                    code_block["first_line"],
                    code_block["last_line"],
                )

            if args.syntax_check and "novalidate" not in code_block["flags"]:
                check_syntax(
                    path,
                    i + 1,
                    supported_languages[code_block["language"]],
                    code_block["first_line"],
                    code_block["last_line"],
                )

            if args.autoformat and "noautoformat" not in code_block["flags"]:
                autoformat(
                    path,
                    i + 1,
                    supported_languages[code_block["language"]],
                    code_block["first_line"],
                    code_block["last_line"],
                )

            if args.output_check and "noexecute" not in code_block["flags"]:
                check_output()

            if args.replace and "noreplace" not in code_block["flags"]:
                offset = replace(
                    path,
                    i + 1,
                    supported_languages[code_block["language"]],
                    code_block["first_line"],
                    code_block["last_line"],
                )
