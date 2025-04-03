from textnode import TextNode, TextType


def main():
    node = TextNode("some text", TextType.NORMAL, "http://example.com")
    print(node)


main()
