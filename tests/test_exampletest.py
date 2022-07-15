"""Example test."""

import pytest
from .testutil import flat_dict, tail_check, check_xpath

etree_cache = {}

@pytest.fixture(scope="module")
def cached_etree_parse():
    # Copied from https://github.com/sphinx-doc/sphinx/blob/9e1b4a8f1678e26670d34765e74edf3a3be3c62c/tests/test_build_html.py
    def parse(fname):
        if fname in etree_cache:
            return etree_cache[fname]
        with (fname).open("rb") as fp:
            etree = HTMLParser(namespaceHTMLElements=False).parse(fp)
            etree_cache.clear()
            etree_cache[fname] = etree
            return etree

    yield parse
    etree_cache.clear()

@pytest.mark.sphinx(buildername="html", testroot="builder-example")
def test_example_test_build(app):
    app.build()

    assert (app.outdir / "index.html").exists()

