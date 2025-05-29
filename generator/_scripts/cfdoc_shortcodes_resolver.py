import re

def process(file):
    try:
        # Read the file content
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the pattern {{%anything}} with {{% print `{{%$1}}` %}}
        # The .*? ensures a non-greedy match for the content between the braces
        updated_content = re.sub(r'\{\{%([^%]*?)\}\}', r'{{% print `{{%\1}}` %}}', content)
        
        # Write the updated content back to the file
        with open(file, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
    except Exception as e:
        print(f"Error processing {file}: {e}")

def run(config):
    markdown_files = config["markdown_files"]
    for file in markdown_files:
        process(file)
