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
            return ""
        props_str = "".join([f' {t[0]}="{t[1]}"' for t in self.props.items()])
        return props_str
    
    def __repr__(self):
        return f"HTMLNode({self.tag=}, {self.value=}, {self.children=}, {self.props=})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Value cannot be None, all leafs must have a value")
        
        html = self.value

        if self.tag:
            html = f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"
        
        return html
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
       

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag cannot be None, all parents must have a tag")
        if not self.children:
            raise ValueError("Children cannot be None, all parents must have children")
        
        children_html = ""
        for child in self.children:          
            children_html += child.to_html()

        html = f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

        return html
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"