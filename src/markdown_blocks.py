def markdown_to_blocks(markdown):
    return [
        "\n".join(line.strip() for line in block.strip().split("\n"))
        for block in markdown.split("\n\n")
        if block.strip()
    ]
