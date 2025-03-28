

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        result = ""
        if self.props:
            for k, v in self.props.items():
                result += f" {k}=\"{v}\""
        return result
    
    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}"
