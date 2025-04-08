from textnode import TextType, TextNode
from htmlnode import HTMLNode
import re


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
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.NORMAL))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    splitted = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            splitted.append(node)
            continue
            
        extracted = extract_markdown_images(node.text)
        if not extracted:
            splitted.append(node)
            continue
            
        remaining_text = node.text
        for alt_text, url in extracted:
            image_markdown = f"![{alt_text}]({url})"
            if image_markdown in remaining_text:
                # Split at the first occurrence
                parts = remaining_text.split(image_markdown, 1)
                
                # Add text before the image if not empty
                if parts[0]:
                    splitted.append(TextNode(parts[0], TextType.NORMAL))
                
                # Add the image node
                splitted.append(TextNode(alt_text, TextType.IMAGE, url))
                
                # Update remaining text
                remaining_text = parts[1] if len(parts) > 1 else ""
        
        # Add any remaining text after processing all images
        if remaining_text:
            splitted.append(TextNode(remaining_text, TextType.NORMAL))
    return splitted

def split_nodes_link(old_nodes):
    splitted = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            splitted.append(node)
            continue
            
        extracted = extract_markdown_links(node.text)
        if not extracted:
            splitted.append(node)
            continue
            
        remaining_text = node.text
        for alt_text, url in extracted:
            link_markdown = f"[{alt_text}]({url})"
            if link_markdown in remaining_text:
                # Split at the first occurrence
                parts = remaining_text.split(link_markdown, 1)
                
                # Add text before the link if not empty
                if parts[0]:
                    splitted.append(TextNode(parts[0], TextType.NORMAL))
                
                # Add the link node
                splitted.append(TextNode(alt_text, TextType.LINK, url))
                
                # Update remaining text
                remaining_text = parts[1] if len(parts) > 1 else ""
        
        # Add any remaining text after processing all links
        if remaining_text:
            splitted.append(TextNode(remaining_text, TextType.NORMAL))
    return splitted