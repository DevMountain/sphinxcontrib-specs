"""sphinxcontrib.specs.content"""

from typing import TYPE_CHECKING, Dict, Any, List

from docutils.nodes import Node
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

if TYPE_CHECKING:
    from sphinx.application import Sphinx


class ContentList(SphinxDirective):
    has_content = True

    def run(self) -> List[Node]:
        return []


class Video(SphinxDirective):
    has_content = True
    first_argument_whitespace = True
    options = {"link": directives.unchanged}

    def run(self) -> List[Node]:
        return []


def setup(app: "Sphinx") -> Dict[str, Any]:
    app.add_directive("contentlist", ContentList)
    app.add_directive("video", Video)
