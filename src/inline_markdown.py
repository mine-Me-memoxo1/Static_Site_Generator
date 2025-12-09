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
    matches = re.findall(f'(?<!1)\[([^\[\]]*)\]\(([^\[\]]*)\)', text)
    return matches
    
