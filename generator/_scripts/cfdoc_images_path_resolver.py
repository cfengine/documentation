import re
import os


def run(config):
    """Fixes images paths
    The markdown files other than _index.markdown need img tag src values adjusted if they are relative.
    They need to reference the parent directory with ../ prefixed to the relative location of the image file.
    """
    markdown_files = config["markdown_files"]

    for file in markdown_files:
        process(file)


def load_references(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def process(file_path):
    """Process a markdown file to fix image paths"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        is_index_file = os.path.basename(file_path) == "_index.markdown"

        if is_index_file:
            # For _index.markdown files, leave image paths as is. As they are on the same level
            return

        # Pattern to match img src with relative paths that need fixing
        # skips ../, /, or http
        img_pattern = r'<img\s+([^>]*?)src="(?!\.\.\/|\/|https?:\/\/)([^"]+?)"([^>]*?)>'

        # Replace with ../ added to the path
        modified_content = re.sub(
            img_pattern, r'<img \1src="../\2"\3>', content, flags=re.IGNORECASE
        )
        if modified_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(modified_content)

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
