from pathlib import Path
from unittest import TestCase, main

from la_xpath import Finder


class TestWebsiteExample(TestCase):
    def test_finder(self):
        finder = Finder(Path("tests/res/example.html").read_text())
        paths = finder.find("domain")

        assert len(paths) == 2

        assert "This domain is for use in illustrative" in paths[0][-1].text
        assert "p" == paths[0][-1].tag

        assert "More information..." == paths[1][-1].text
        assert "a" == paths[1][-1].tag


if __name__ == "__main__":
    main()
