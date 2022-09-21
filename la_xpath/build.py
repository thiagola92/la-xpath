from xml.etree.ElementTree import Element


def get_tag_index(parent: Element, child: Element) -> int:
    """
    Get the tag index from the element.

    If one element have 5 'div' tags and you pass the third,
    the function will return 3 (xpath index start on 1).
    """

    count = 0

    for e in parent:
        if e.tag == child.tag:
            count += 1

            if e is child:
                return count

    raise ValueError("Child not present in parent")


def build_xpath(path: list[Element], root: Element) -> str:
    string = ""
    parent = path[0]

    for element in path:
        if element is parent:
            string += f"/{element.tag}"
        elif element not in parent:
            if not string.endswith("/"):
                string += "/"
        else:
            index = get_tag_index(parent, element)
            string += f"/{element.tag}[{index}]"

        parent = element

    return string
