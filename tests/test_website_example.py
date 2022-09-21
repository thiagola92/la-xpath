from pathlib import Path
from unittest import TestCase, main

from la_xpath import Finder


class TestWebsiteExample(TestCase):
    def test_finder(self):
        finder = Finder(Path("tests/res/website_example.html").read_text())
        paths = finder.find("domain")

        assert len(paths) == 3

        assert "Example Domain" in paths[0][-1].text
        assert "title" == paths[0][-1].tag

        assert "Example Domain" in paths[1][-1].text
        assert "h1" == paths[1][-1].tag

        assert "This domain is" in paths[2][-1].text
        assert "p" == paths[2][-1].tag


if __name__ == "__main__":
    main()
