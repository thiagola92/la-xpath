from xml.etree.ElementTree import Element

from html5lib.html5parser import parse

from la_xpath.tag import simplify_paths
from la_xpath.text import is_on_element


class Finder:
    def __init__(self, html: str) -> None:
        self._root: Element = parse(
            html, treebuilder="etree", namespaceHTMLElements=False
        )

    def find(
        self,
        text: str,
        sensitive: bool = False,
        attributes: bool = False,
        simplify: bool = False,
    ):
        """
        Find paths which takes you to the text.

        text - the document as string or file-like object into a tree
        sensitive - whenever case sensitive matter in search
        attributes - whenever should search in attributes the text
        simplify - whenever should remove elements where '//' is possible
        """
        paths = self._find_paths(
            text,
            path=[self._root],
            sensitive=sensitive,
            attributes=attributes,
        )

        if simplify:
            paths = simplify_paths(paths)

        return paths

    def _find_paths(
        self, text: str, path: list[Element], sensitive: bool, attributes: bool
    ) -> list[list[Element]]:
        # Always work with the last element of the path
        element = path[-1]
        paths = []

        if is_on_element(text, element, sensitive, attributes):
            paths.extend([path])

        for child in element:
            paths.extend(self._find_paths(text, path + [child], sensitive, attributes))

        return paths
