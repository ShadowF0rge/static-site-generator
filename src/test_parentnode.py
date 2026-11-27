
import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):

    # 1. Einfacher ParentNode
    def test_simple_parent(self):
        node = ParentNode(
            "p",
            [LeafNode(None, "Hello")]
        )

        self.assertEqual(node.to_html(), "<p>Hello</p>")

    # 2. Mehrere Kinder
    def test_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold"),
                LeafNode(None, " Normal "),
                LeafNode("i", "Italic"),
            ]
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold</b> Normal <i>Italic</i></p>"
        )

    # 3. Verschachtelte ParentNodes
    def test_nested_parent(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [LeafNode(None, "Hello")]
                )
            ]
        )

        self.assertEqual(
            node.to_html(),
            "<div><p>Hello</p></div>"
        )

    # 4. Mehrere Verschachtelungsebenen
    def test_deeply_nested_parent(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [
                        ParentNode(
                            "p",
                            [LeafNode(None, "Deep text")]
                        )
                    ]
                )
            ]
        )

        self.assertEqual(
            node.to_html(),
            "<div><section><p>Deep text</p></section></div>"
        )

    # 5. Verschachtelte ParentNodes mit mehreren Kindern
    def test_nested_multiple_children(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold"),
                        LeafNode(None, " Normal")
                    ]
                ),
                ParentNode(
                    "p",
                    [LeafNode("i", "Italic")]
                )
            ]
        )

        self.assertEqual(
            node.to_html(),
            "<div><p><b>Bold</b> Normal</p><p><i>Italic</i></p></div>"
        )

    # 6. ParentNode mit Properties
    def test_parent_with_props(self):
        node = ParentNode(
            "div",
            [LeafNode(None, "Hello")],
            {"class": "container", "id": "main"}
        )

        self.assertEqual(
            node.to_html(),
            '<div class="container" id="main">Hello</div>'
        )

    # 7. ParentNode ohne Properties
    def test_parent_without_props(self):
        node = ParentNode(
            "div",
            [LeafNode(None, "Hello")]
        )

        self.assertEqual(
            node.to_html(),
            "<div>Hello</div>"
        )

    # 8. ParentNode ohne Tag
    def test_parent_without_tag(self):
        node = ParentNode(
            None,
            [LeafNode(None, "Hello")]
        )

        with self.assertRaises(ValueError):
            node.to_html()

    # 9. ParentNode ohne Kinder (leere Liste)
    def test_parent_with_empty_children(self):
        node = ParentNode("div", [])

        self.assertEqual(node.to_html(), "<div></div>")

    # 10. ParentNode mit None als Children
    def test_parent_with_none_children(self):
        node = ParentNode("div", None)

        with self.assertRaises(ValueError):
            node.to_html()

    # 11. ParentNode mit None als Kind
    def test_parent_with_none_child(self):
        node = ParentNode("div", [None])

        with self.assertRaises(AttributeError):
            node.to_html()

    # 12. ParentNode mit ungültigem Kind
    def test_parent_with_invalid_child(self):
        node = ParentNode("div", ["Hello"])

        with self.assertRaises(AttributeError):
            node.to_html()

    # 13. ParentNode mit mehreren verschiedenen HTML-Tags
    def test_different_html_tags(self):
        node = ParentNode(
            "ul",
            [
                ParentNode("li", [LeafNode(None, "First")]),
                ParentNode("li", [LeafNode(None, "Second")]),
                ParentNode("li", [LeafNode(None, "Third")]),
            ]
        )

        self.assertEqual(
            node.to_html(),
            "<ul><li>First</li><li>Second</li><li>Third</li></ul>"
        )

    # 14. ParentNode mit verschachtelten Properties
    def test_nested_props(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [LeafNode(None, "Hello")],
                    {"class": "paragraph"}
                )
            ],
            {"id": "main"}
        )

        self.assertEqual(
            node.to_html(),
            '<div id="main"><p class="paragraph">Hello</p></div>'
        )


if __name__ == "__main__":
    unittest.main()
