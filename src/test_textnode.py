import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a link node", TextType.LINK_TEXT, 'boot.dev')
        ans = 'TextNode(This is a link node, link, boot.dev)'
        self.assertEqual(node.__repr__(), ans)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a link node", TextType.LINK_TEXT, 'boot.dev')
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
