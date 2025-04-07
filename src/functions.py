from textnode import TextType, TextNode
from htmlnode import HTMLNode


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            return HTMLNode(None, text_node.text)
        case TextType.BOLD:
            return HTMLNode("b", text_node.text)
        case TextType.ITALIC:
            return HTMLNode("i", text_node.text)
        case TextType.CODE:
            return HTMLNode("code", text_node.text)
        case TextType.LINK:
            return HTMLNode("a", text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return HTMLNode("img", props={"src": text_node.url})
    raise ValueError(f"Unknown text type: {text_node.text_type}")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        if not node.text:
            continue

        parts = [part for part in node.text.split(delimiter) if part]

        if delimiter in ("**", "_", "`"):
            if len(parts) % 2 != 0:
                raise Exception(
                    f"Closing delimiter {delimiter} not found for {node.text}"
                )

        for i in range(len(parts)):
            if i % 2 == 0:
                new_nodes.append(TextNode(parts[i], TextType.NORMAL))
            else:
                new_nodes.append(TextNode(parts[i], text_type))

    return new_nodes
