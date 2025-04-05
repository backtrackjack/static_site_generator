from textnode import TextType
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
