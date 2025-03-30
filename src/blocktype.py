from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "CODE"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown_block):
    pass



# TODO
"""

Headings start with 1-6 # characters, followed by a space and then the heading text.
Code blocks must start with 3 backticks and end with 3 backticks.
Every line in a quote block must start with a > character.
Every line in an unordered list block must start with a - character, followed by a space.
Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
If none of the above conditions are met, the block is a normal paragraph.

"""