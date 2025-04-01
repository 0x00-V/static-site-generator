from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown_block):
    l = markdown_block.split('\n')

    if markdown_block.startswith('#'):
        c = 0
        for char in markdown_block:
            if char == '#':
                c += 1
            else:
                break
        if c <= 6 and len(markdown_block) > c and markdown_block[c] == ' ':
            return BlockType.HEADING
        else:
            return BlockType.PARAGRAPH
    elif markdown_block.startswith('```') and markdown_block.endswith('```'):
        return BlockType.CODE
    elif all(line.startswith('>') for line in l):
        return BlockType.QUOTE
    elif all(line.startswith('- ') for line in l):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list(l):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def is_ordered_list(l):
    if not l:
        return False
    for i, line in enumerate(l):
        num = i + 1
        prefix = f"{num}. "
        if not line.startswith(prefix):
            return False
    return True

