import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_default(self):
        defaultNode = HTMLNode(props=None)
        self.assertEqual(defaultNode.props_to_html(), "")

        defaultNode = HTMLNode(props={})
        self.assertEqual(defaultNode.props_to_html(), "")

    def test_props_to_html_single_prop(self):
        node = HTMLNode(props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')
        
    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertIn(' href="https://example.com"', result)
        self.assertIn(' target="_blank"', result)
        self.assertEqual(len(result), len(' href="https://example.com" target="_blank"'))


if __name__ == "__main__":
    unittest.main()