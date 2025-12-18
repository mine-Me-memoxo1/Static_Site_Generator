def markdown_to_blocks(text):
    lines = text.split('\n\n')
    lines = [if line: line.strip() for line in lines]
    return lines
