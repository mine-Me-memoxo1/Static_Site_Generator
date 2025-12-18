from src_to_dest import src_to_dest, extract_title
from unittest import TestCase

class TestExtractTitle(TestCase):

    def test_one(self):
        markdown = '# Hello'
        ans = 'Hello'
        self.assertEqual(extract_title(markdown), ans)

    def test_two(self):
        markdown = '# Title\n Hello'
        ans = 'Title\n Hello'
        self.assertEqual(extract_title(markdown), ans)

