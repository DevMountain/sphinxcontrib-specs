"""sphinxcontrib.specs.content"""

from lib2to3.pytree import Base
from typing import TYPE_CHECKING, Dict, Any, List

from docutils.nodes import Node
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

if TYPE_CHECKING:
    from sphinx.application import Sphinx


class BaseContentDirective(SphinxDirective):
    contenttype_name = ""

    has_content = True
    first_argument_whitespace = True
    options = {"link": directives.unchanged}

    def run(self) -> List[Node]:
        return []


class Download(BaseContentDirective):
    contenttype_name = "download"


class Video(BaseContentDirective):
    contenttype_name = "video"


class Webpage(BaseContentDirective):
    contenttype_name = "webpage"


def setup(app: "Sphinx") -> Dict[str, Any]:
    for directive in [Download, Video, Webpage]:
        app.add_directive(directive.contenttype_name, directive)
