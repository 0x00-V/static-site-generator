import re

from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, other):
        return(self.text == other.text and self.text_type == other.text_type and self.url == other.url)
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError("Invalid TextType!")
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_node = node.text.split(delimiter)
            for i, content in enumerate(split_node):
                if content: 
                    if i % 2 == 0:
                        new_nodes.append(TextNode(content, TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(content, text_type))
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        imgs = extract_markdown_images(node.text)
        if not imgs:
            new_nodes.append(node)
            continue
        
        curr_txt = node.text

        for alt, url in imgs:
            img_markdown = f"![{alt}]({url})"
            split = curr_txt.split(img_markdown, 1)
            if split[0]:
                new_nodes.append(TextNode(split[0], TextType.TEXT))
            
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

            if len(split) > 1:
                curr_txt = split[1]
            else:
                curr_txt = ""
        if curr_txt:
            new_nodes.append(TextNode(curr_txt, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        
        curr_txt = node.text

        for text, url in links:
            link_markdown = f"[{text}]({url})"
            split = curr_txt.split(link_markdown, 1)
            if split[0]:
                new_nodes.append(TextNode(split[0], TextType.TEXT))
            
            new_nodes.append(TextNode(text, TextType.LINK, url))

            if len(split) > 1:
                curr_txt = split[1]
            else:
                curr_txt = ""
        
        if curr_txt:
            new_nodes.append(TextNode(curr_txt, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes
    
def markdown_to_blocks(markdown):
    res = []

    for block in markdown.split("\n\n"):
        if not block.strip():
            continue
            
        clean = ""
        for l in block.strip().split("\n"):
            clean += l.strip() + "\n"
    
        res.append(clean.strip())
    return res