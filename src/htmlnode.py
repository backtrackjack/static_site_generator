from functools import reduce


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        return reduce(
            lambda x,
            k: x + f"{k}=\"{self.props[k]}\" ",
            self.props,
            " "
        )
