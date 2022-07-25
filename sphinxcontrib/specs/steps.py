"""sphinxcontrib.specs.steps"""

from typing import TYPE_CHECKING, Dict, Any, List

from docutils import nodes
from docutils.nodes import Node
from sphinx.util.docutils import SphinxDirective

if TYPE_CHECKING:
    from sphinx.application import Sphinx


class steps_list(nodes.General, nodes.Element):
    pass


def visit_steps_list(self, _) -> None:
    pass


def depart_steps_list(self, _) -> None:
    pass


class step(nodes.Part, nodes.Element):
    pass


def visit_step(self, node: step) -> None:
    self.body.append(self.starttag(node, "details", classes=node["classes"]))


def depart_step(self, _) -> None:
    self.body.append("</details>\n")


class step_title(nodes.Part, nodes.TextElement):
    pass


def visit_step_title(self, node: step_title) -> None:
    self.body.append("<summary>")
    self.body.append(self.starttag(node, "span", classes=node["classes"]))


def depart_step_title(self, _) -> None:
    self.body.append("</span>\n")
    self.body.append("</summary>\n")


class StepsList(SphinxDirective):
    has_content = True

    def run(self) -> List[Node]:
        node = steps_list()
        wrapper = nodes.container(
            "\n".join(self.content), classes=["specssteps"]
        )
        wrapper.document = self.state.document
        self.state.nested_parse(self.content, self.content_offset, wrapper)

        node += [wrapper]

        return [node]


class Step(SphinxDirective):
    has_content = True
    final_argument_whitespace = True
    required_arguments = 1

    def run(self) -> List[Node]:
        node = step("")

        title_text = self.arguments[0]
        text_nodes, messages = self.state.inline_text(title_text, self.lineno)
        title_node = step_title(
            title_text, "", *text_nodes, classes=["specssteps-title"]
        )
        (
            title_node.source,
            title_node.line,
        ) = self.state_machine.get_source_and_line(self.lineno)
        node += [title_node]

        body_node = nodes.container(
            "\n".join(self.content), classes=["specssteps-body"]
        )
        body_node.document = self.state.document
        self.state.nested_parse(self.content, self.content_offset, body_node)

        node += [body_node]

        return [node]


def setup(app: "Sphinx") -> Dict[str, Any]:
    app.add_node(steps_list, html=(visit_steps_list, depart_steps_list))
    app.add_node(step, html=(visit_step, depart_step))
    app.add_node(step_title, html=(visit_step_title, depart_step_title))

    app.add_directive("stepslist", StepsList)
    app.add_directive("step", Step)
