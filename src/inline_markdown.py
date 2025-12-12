from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_list.append(old_node)
            continue
        split_nodes = []
        split_list = old_node.text.split(delimiter)
        if len(split_list) % 2 == 0:
            raise ValueError('Invalid Markdown syntax! Closing delimter not found.')
        for i in range(len(split_list)):
            if split_list[i] == '':
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split_list[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(split_list[i], text_type))
        new_list.extend(split_nodes)
    return new_list


def extract_markdown_images(text):
    matches = re.findall(r'!\[([^\[\]]*)\]\(([^\(\)]*)\)', text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r'(?<!1)\[([^\[\]]*)\]\(([^\[\]]*)\)', text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        for group in images:
            img_alt, img_link = group
            split_text = original_text.split(f'![{img_alt}]({img_link})', 1)
            if len(split_text) != 2:
                raise ValueError('invalid markdown, image section not closed')
            if split_text[0] != '':
                split_nodes.append(TextNode(split_text[0], TextType.TEXT))
            split_nodes.append(TextNode(img_alt, TextType.IMAGE, url = img_link))
            original_text = split_text[-1]
        if original_text != '':
            split_nodes.append(TextNode(original_text, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes 



def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

