from pathlib import Path
from unittest import TestCase, main

from la_xpath import Finder


class TestTemplate(TestCase):
    def test_finder(self):
        finder = Finder(Path("tests/res/template.html").read_text())
        paths = finder.find("test")

        assert len(paths) == 2

        assert "test" in paths[0][-1].text
        assert "body" == paths[0][-1].tag

        assert "test" in paths[0][-1][1].tail
        assert "meta" == paths[0][-1][1].tag


if __name__ == "__main__":
    main()
