from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        children: list | None,
        props: dict[str, str] | None = None
    ):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")

        if self.children is None:
            raise ValueError("ParentNode must have children")

        result = ""

        for child in self.children:
            result += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"
