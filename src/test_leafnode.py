import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_span(self):
        node = LeafNode("span", "Hello, world!")
        self.assertEqual(node.to_html(), "<span>Hello, world!</span>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("p", "Hello, world!", props={"class": "text"})
        self.assertEqual(
            node.to_html(), '<p class="text">Hello, world!</p>'
        )
