import re

def run(config):
    markdown_files = config["markdown_files"]
    for file in markdown_files:
        process(file)

def process(file_path):
    """
    Reads a markdown file, searches for code block headers that include specific flags
    (file=..., noindent, noparse, noeval), and moves file=... finding to a new line inside 
    square brackets and ignores the rest flags as we don't use them in the markdown rendering.
    """
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Find and replace codeblocks
        transformed_content = transform_codeblocks(content)
        
        # Write file if content was changed
        if transformed_content != content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(transformed_content)
            
    except Exception as e:
        print(f"Error processing file {file_path}: {str(e)}")
        raise

def transform_codeblocks(content):
    """
    Find code block headers that include file=... and optional flags (noindent, noparse, noeval),
    remove all flags except file=... because we don't process them in docs,
    and move file=... to a new line inside square brackets.
    """

    pattern = re.compile(
        r'^```([a-zA-Z0-9_-]+)' # language
        r'((?:\s+(file=[^\s]+|noindent|noparse|noeval))+)\s*$',  # flags
        re.MULTILINE
    )

    def replacer(match):
        language = match.group(1)
        all_flags = match.group(2)

        # Extract the file=... part
        file_flag_match = re.search(r'file=[^\s]+', all_flags)
        if file_flag_match:
            file_flag = file_flag_match.group()
            return f"```{language}\n[{file_flag}]"
        else:
            return f"```{language}"

    return pattern.sub(replacer, content)
