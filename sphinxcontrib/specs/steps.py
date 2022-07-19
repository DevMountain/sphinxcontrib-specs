"""sphinxcontrib.specs.steps"""

from typing import TYPE_CHECKING, Dict, Any, List

from docutils.nodes import Node
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

if TYPE_CHECKING:
    from sphinx.application import Sphinx


class StepsList(SphinxDirective):
    has_content = True

    def run(self) -> List[Node]:
        return []


class Step(SphinxDirective):
    has_content = True
    first_argument_whitespace = True

    def run(self) -> List[Node]:
        return []


def setup(app: "Sphinx") -> Dict[str, Any]:
    app.add_directive("stepslist", StepsList)
    app.add_directive("step", Step)
