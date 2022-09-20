from xml.etree.ElementTree import Element

from html5lib.html5parser import parse

from la_xpath.text import is_on_element


class Finder:
    def __init__(self, html: str) -> None:
        self._root: Element = parse(
            html, treebuilder="etree", namespaceHTMLElements=False
        )

    def find(self, text: str, lowercase: bool = False, attributes: bool = True):
        """Find paths which takes you to the text"""
        return self._find_paths(
            text, path=[self._root], lowercase=lowercase, attributes=attributes
        )

    def _find_paths(
        self, text: str, path: list[Element], lowercase: bool, attributes: bool
    ) -> list[list[Element]]:
        # Always work with the last element of the path
        element = path[-1]
        paths = []

        if is_on_element(text, element, lowercase, attributes):
            paths.extend([path])

        for child in element:
            paths.extend(self._find_paths(text, path + [child], lowercase, attributes))

        return paths
