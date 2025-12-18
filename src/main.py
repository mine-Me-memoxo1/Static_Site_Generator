from textnode import *
from src_to_dest import src_to_dest, generate_page
def main():
    #test = TextNode('This is some anchor text', TextType.LINK_TEXT, 'https://www.boot.dev')
    #print(test.__repr__())
    src_to_dest()
    generate_page('./content/index.md', './template.html', './public/index.html')



main()
