import unittest
from textnode import TextNode, TextType
from functions import text_node_to_html_node, split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("blah blah", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode(
            "This is a text node",
            TextType.BOLD,
            "http://example.com"
        )
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_split_nodes_delimiter_simple(self):
        node = TextNode("One two three", TextType.NORMAL)
        nodes = split_nodes_delimiter([node], " ", TextType.NORMAL)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "One")
        self.assertEqual(nodes[1].text, "two")
        self.assertEqual(nodes[2].text, "three")
        self.assertTrue(all(n.text_type == TextType.NORMAL for n in nodes))

    def test_split_nodes_delimiter_no_delimiter(self):
        node = TextNode("No delimiters here", TextType.NORMAL)
        nodes = split_nodes_delimiter([node], ";", TextType.NORMAL)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "No delimiters here")
        self.assertEqual(nodes[0].text_type, TextType.NORMAL)

    def test_split_nodes_delimiter_multiple_spaces(self):
        node = TextNode("Lots   of   spaces", TextType.NORMAL)
        nodes = split_nodes_delimiter([node], " ", TextType.NORMAL)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Lots")
        self.assertEqual(nodes[1].text, "of")
        self.assertEqual(nodes[2].text, "spaces")
