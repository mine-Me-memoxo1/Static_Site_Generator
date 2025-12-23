from textnode import *
from src_to_dest import src_to_dest, generate_pages_recursive
import sys
def main(basepath='/'):
    #test = TextNode('This is some anchor text', TextType.LINK_TEXT, 'https://www.boot.dev')
    #print(test.__repr__())
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    src_to_dest()
    generate_pages_recursive('./content', './template.html', './docs', basepath)



main()
