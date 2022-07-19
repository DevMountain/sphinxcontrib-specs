"""Example test."""

import pytest
from html5lib import HTMLParser

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


@pytest.mark.sphinx(buildername="specs", testroot="builder-example")
def test_build_specs(app):
    """The Specs builder runs without error."""

    app.build()

    assert (app.outdir / "index.html").exists()


@pytest.mark.parametrize(
    "fname,expect",
    flat_dict(
        {
            "index.html": [
                (
                    './/div[@class="objectives"]//li[1]/p',
                    "student can create a variable",
                ),
                (
                    './/div[@class="objectives"]//li[2]/p',
                    "student can write a function",
                ),
                (
                    './/div[@class="objectives"]//li[3]/p',
                    "student can use print statement",
                ),
            ]
        }
    ),
)
@pytest.mark.sphinx(buildername="specs", testroot="builder-example")
def test_objectives(app, cached_etree_parse, fname, expect):
    """Test the `.. objectives::` directive."""

    app.build()

    check_xpath(cached_etree_parse(app.outdir / fname), fname, *expect)


@pytest.mark.parametrize(
    "fname,expect",
    flat_dict(
        {
            "index.html": [
                ('.//dl[@class="objectivesindex"]/dt', ""),
                ('.//dl[@class="objectivesindex"]/dd', ""),
                # has link to section associated with <dt>
                (
                    './/dl[@class="objectivesindex"]/dt/a[@href="#python-basics"]',
                    "Python Basics",
                ),
                (
                    './/dl[@class="objectivesindex"]/dt/a[@href="#loops-in-python"]',
                    "Loops in Python",
                ),
            ]
        }
    ),
)
@pytest.mark.sphinx(buildername="specs", testroot="builder-example")
def test_objectivesindex(app, cached_etree_parse, fname, expect):
    """Test the `.. objectivesindex::` directive."""

    app.build()

    check_xpath(cached_etree_parse(app.outdir / fname), fname, *expect)
