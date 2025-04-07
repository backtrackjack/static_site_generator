import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_simple(self):
        node = HTMLNode("text", props={"class": "text", "id": "1234"})
        self.assertEqual(node.props_to_html(), ' class="text" id="1234"')

    def test_props_to_html_empty(self):
        node = HTMLNode("text", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_complex(self):
        node = HTMLNode(
            "text",
            props={
                "class": "text",
                "id": "1234",
                "style": "color: red; font-size: 12px;",
            },
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="text" id="1234" style="color: red; font-size: 12px;"',
        )
