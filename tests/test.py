from la_xpath import Finder
from la_xpath.build import build_xpath
from la_xpath.tag import simple_path

with open("tests/text.html") as f:
    finder = Finder(f)

paths = finder.find("LEGO")

for xpath in [build_xpath(p, finder._root) for p in paths]:
    print(xpath)

paths = [simple_path(p) for p in paths]

for xpath in [build_xpath(p, finder._root) for p in paths]:
    print(xpath)
