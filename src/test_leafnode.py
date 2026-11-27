import unittest
from leafnode import *


class TestLeafNode(unittest.TestCase):

    # Test 1: Initialisierung
    def test_init(self):
        node = LeafNode("p", "Hello World")

        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello World")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)


    # Test 3: HTML mit Properties
    def test_to_html_with_props(self):
        node = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com"}
        )

        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )

    # Test 4: HTML ohne Tag
    def test_to_html_without_tag(self):
        node = LeafNode(None, "Just text")

        self.assertEqual(node.to_html(), "Just text")

    # Test 5: __repr__ ohne children
    def test_repr(self):
        node = LeafNode("p", "Hello World", {"class": "text"})

        self.assertEqual(
            repr(node),
            "p, Hello World, {'class': 'text'}"
        )


if __name__ == "__main__":
    unittest.main()