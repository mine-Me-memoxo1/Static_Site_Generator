class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ''
        string = ''
        for key,value in self.props.items():
            string += f' {key}="{value}"'
        return string

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'


class LeafNode(HTMLNode):
    def __init__(self, tag, val, props=None):
        super().__init__(tag, val, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError('Leaf node has no value)')
        if self.tag is None:
            return self.value
        return f'<{self.tag}' + self.props_to_html() + f'>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError('Tag not present. It cannot be None')
        if self.children is None:
            raise ValueError('Children arguement cannot be None')
        tag = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            tag += child.to_html()
        tag += f'</{self.tag}>'
        return tag

    def __repr__(self):
        return f'ParentNode({self.tag}, {self.children}, {self.props}'

