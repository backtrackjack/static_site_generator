from enum import Enum


def markdown_to_blocks(markdown):
    return [
        "\n".join(line.strip() for line in block.strip().split("\n"))
        for block in markdown.split("\n\n")
        if block.strip()
    ]


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def block_to_block_type(block):
    if block.startswith("#"):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        return BlockType.QUOTE
    if block.startswith("- "):
        return BlockType.ULIST
    if block[0].isdigit() and block[1:3] == ". ":
        return BlockType.OLIST
    return BlockType.PARAGRAPH
