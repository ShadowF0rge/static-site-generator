import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    # Test 1: Initialisierung mit Standardwerten
    def test_init_defaults(self):
        node = HTMLNode()

        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    # Test 2: Initialisierung mit Werten
    def test_init_with_values(self):
        node = HTMLNode(
            "p",
            "Hello World",
            [],
            {"class": "text"}
        )

        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "text"})

    # Test 3: props_to_html mit mehreren Properties
    def test_props_to_html(self):
        node = HTMLNode(
            "div",
            props={"class": "container", "id": "main"}
        )

        self.assertEqual(
            node.props_to_html(),
            ' class="container" id="main"'
        )

    # Test 4: props_to_html ohne Properties
    def test_props_to_html_none(self):
        node = HTMLNode("div")

        self.assertEqual(node.props_to_html(), '')

    # Test 5: __repr__
    def test_repr(self):
        node = HTMLNode("p", "Hello", [], {"class": "text"})

        self.assertEqual(
            repr(node),
            "p, Hello, [], {'class': 'text'}"
        )


if __name__ == "__main__":
    unittest.main()