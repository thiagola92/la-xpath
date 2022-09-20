from xml.etree.ElementTree import Element


def is_on_element(
    text: str, element: Element, lowercase: bool, attributes: bool
) -> bool:
    """Check whenever the text is inside the element"""
    if is_on_text(text, element, lowercase):
        return True

    if attributes and is_on_attrib(text, element, lowercase):
        return True

    return False


def is_on_text(text: str, element: Element, lowercase: bool) -> bool:
    """Check whenever the text is inside the element text"""

    return (
        (element.text and lowercase and text.lower() in element.text.lower())
        or (element.text and text in element.text)
        or (element.tail and lowercase and text.lower() in element.tail.lower())
        or (element.tail and text in element.tail)
    )


def is_on_attrib(text: str, element: Element, lowercase: bool) -> bool:
    """Check whenever the text is inside the element attributes"""

    for v in element.attrib.values():
        if lowercase and text.lower() in v.lower():
            return True
        elif text in v:
            return True

    return False
