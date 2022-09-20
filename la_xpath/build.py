from xml.etree.ElementTree import Element

from la_xpath.tag import get_tag_index


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
