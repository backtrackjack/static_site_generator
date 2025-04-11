from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
    markdown_to_html_node,
)
import os
import shutil
from pathlib import Path


def copy_to_directory(src, dest):
    print(f"Copying {src} to {dest}")
    if not os.path.exists(src):
        raise FileNotFoundError(f"Source {src} does not exist.")
    if not os.path.exists(dest) and not os.path.isfile(dest):
        os.mkdir(dest)

    for item in os.listdir(src):
        item_src = os.path.join(src, item)
        item_dest = os.path.join(dest, item)
        if os.path.isfile(item_src):
            print(f"Copying file {item_src} to {item_dest}")
            shutil.copy(item_src, item_dest)
        else:
            copy_to_directory(item_src, item_dest)


def extract_title(markdown):
    def h1_filter(block):
        return block_to_block_type(block) == BlockType.HEADING and block.startswith(
            "# "
        )

    h1_blocks = list(
        filter(
            h1_filter,
            markdown_to_blocks(markdown),
        )
    )

    if len(h1_blocks) == 0:
        raise Exception("No h1 found in markdown")

    return h1_blocks[0].replace("# ", "").strip()


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    f = open(from_path, "r")
    markdown = f.read()
    f.close()
    f = open(template_path, "r")
    template = f.read()
    f.close()
    md_to_html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", md_to_html)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    f = open(dest_path, "w")
    f.write(template)
    f.close()


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
