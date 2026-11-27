import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(node, node2)

        node = TextNode("Hi", TextType.CODE, None)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(
            "TextNode(This is a text node, `Code text`, None)", repr(node)
        )



if __name__ == "__main__":
    unittest.main()