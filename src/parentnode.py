from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Missing tag")
        if self.children == None:
            raise ValueError("Missing children")
        my_lovely_children = ""
        for node in self.children:
            my_lovely_children += node.to_html()
        return f"<{self.tag}>{my_lovely_children}</{self.tag}>"
    

    