import unittest
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "text",
            props={"class": "text", "id": "1234"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="text" id="1234" '
        )
