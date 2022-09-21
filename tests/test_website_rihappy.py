from pathlib import Path
from unittest import TestCase, main

from la_xpath import Finder


class TestWebsitRihappy(TestCase):
    def test_finder(self):
        finder = Finder(Path("tests/res/website_rihappy.html").read_text())
        paths = finder.find("LEGO")

        # assert "LEGO - Minecraft - A Emboscada do Creeper - 21177" in paths[0][-1].text
        # assert "title" == paths[0][-1].tag


if __name__ == "__main__":
    main()
