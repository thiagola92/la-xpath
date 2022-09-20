from xml.etree.ElementTree import Element


def tag_occurrences(element: Element, tag: str) -> int:
    """Count how many occurrences of the tag happened in element"""
    return len([e for e in element if e.tag == tag])


def can_remove_parent(
    grandparent: Element | None, parent: Element, child: Element
) -> bool:
    """
    Analyse tags to know whenever you can reduce something like:
        html/body/div
    To a simple version like:
        html//div
    """

    tag = child.tag

    if not grandparent and tag_occurrences(parent, tag) == 1:
        return True
    elif tag_occurrences(parent, tag) == 1 and tag_occurrences(grandparent, tag) == 0:
        return True
    return False


def simple_path(path: list[Element]) -> list[Element]:
    """Return the path simplified by removing any element where '//' could be used"""

    to_ignore = []
    grandparent = None
    parent = path[0]

    for child in path[1:]:
        if can_remove_parent(grandparent, parent, child):
            to_ignore.append(parent)
        grandparent = parent
        parent = child

    return [e for e in path if e not in to_ignore]


def get_tag_index(parent: Element, child: Element) -> int:
    """
    Get the tag index from the element

    If one element have 5 'div' tags and you pass the third,
    the function will return 3 (xpath index start on 1)
    """

    count = 0

    for e in parent:
        if e.tag == child.tag:
            count += 1

            if e is child:
                return count

    raise ValueError("Child not present in parent")
