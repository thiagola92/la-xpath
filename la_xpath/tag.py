from xml.etree.ElementTree import Element


def tag_occurrences(element: Element, tag: str) -> int:
    """Count how many occurrences of the tag happened in element."""
    return len([e for e in element if e.tag == tag])


def can_remove_parent(
    grandparent: Element | None, parent: Element, child: Element
) -> bool:
    """
    This can happen whenever the grandparent don't have anyone with the tag X
    and the parent only have one element with the tag X.

    In other words, returns whenever you can reduce something like:
        html/body/div
    To a simple version like:
        html//div
    """

    tag = child.tag

    if not grandparent and tag_occurrences(parent, tag) == 1:
        return True
    elif tag_occurrences(grandparent, tag) == 0 and tag_occurrences(parent, tag) == 1:
        return True
    return False


def simplify_path(path: list[Element]) -> list[Element]:
    """Return the path simplified by removing any element where '//' could be used instead."""

    to_ignore = []
    grandparent = None
    parent = path[0]

    for child in path[1:]:
        if can_remove_parent(grandparent, parent, child):
            to_ignore.append(parent)
        grandparent = parent
        parent = child

    return [e for e in path if e not in to_ignore]


def simplify_paths(paths: list[list[Element]]) -> list[list[Element]]:
    return [simplify_path(p) for p in paths]
