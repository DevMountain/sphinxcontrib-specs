"""sphinxcontrib.specs.content"""

from cgitb import html
from typing import TYPE_CHECKING, Dict, Any, List

from docutils import nodes
from docutils.nodes import Node
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

if TYPE_CHECKING:
    from sphinx.application import Sphinx


class specscontent(nodes.General, nodes.Element):
    pass


def visit_specscontent(self, node: specscontent) -> None:
    self.body.append(
        self.starttag(node, "div", classes=["specscontent"] + node["classes"])
    )


def depart_specscontent(self, _) -> None:
    self.body.append("</div>\n")


class specscontent_title(nodes.General, nodes.Element):
    pass


def visit_specscontent_title(self, node: specscontent_title) -> None:
    self.body.append(self.starttag(node, "div", classes=node["classes"]))


def depart_specscontent_title(self, _) -> None:
    self.body.append("</div>\n")


class BaseContentDirective(SphinxDirective):
    contenttype_name = ""
    contenttype_icon_markup = ""

    optional_arguments = 1
    final_argument_whitespace = True
    options_spec = {"link": directives.unchanged}
    has_content = True

    def run(self) -> List[Node]:
        node = specscontent()

        node["contenttype"] = self.contenttype_name
        node["link"] = self.options.get("link", "")

        icon_overrides = self.env.config.specs_contenttype_icons
        default_markup = self.contenttype_icon_markup
        node["icon_markup"] = (
            icon_overrides[self.contenttype_name]
            if self.contenttype_name in icon_overrides
            else default_markup
        )

        body_node = nodes.container(
            "", classes=["specscontent-body", self.contenttype_name]
        )

        title_node = specscontent_title(
            "", classes=["specscontent-body-title"]
        )
        if self.arguments and self.arguments[0]:
            title_node.document = self.state.document
            self.state.nested_parse(self.arguments[0], 0, title_node)
        else:
            title_node.append(
                nodes.TextElement("", self.contenttype_name.title())
            )

        body_node += [title_node]

        if self.content:
            desc_node = nodes.container("", classes=["specscontent-body-desc"])
            desc_node.document = self.state.document
            self.state.nested_parse(
                self.content, self.content_offset, desc_node
            )

            body_node += [desc_node]

        node += [body_node]

        return [node]


class Download(BaseContentDirective):
    contenttype_name = "download"


class Video(BaseContentDirective):
    contenttype_name = "video"


class Webpage(BaseContentDirective):
    contenttype_name = "webpage"


def setup(app: "Sphinx") -> Dict[str, Any]:
    app.add_config_value("specs_contenttype_icons", {}, "env")

    app.add_node(specscontent, html=(visit_specscontent, depart_specscontent))
    app.add_node(
        specscontent_title,
        html=(visit_specscontent_title, depart_specscontent_title),
    )

    for directive in [Download, Video, Webpage]:
        app.add_directive(directive.contenttype_name, directive)
