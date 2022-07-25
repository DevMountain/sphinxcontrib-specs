"""sphinxcontrib.specs.builder

The Specializations builder.
"""

from typing import Dict, Any

from docutils import nodes
from sphinx.builders.html import StandaloneHTMLBuilder


class SpecsBuilder(StandaloneHTMLBuilder):
    name = "specs"
    search = False

    # def get_doc_context(
    #     self, docname: str, body: str, metatags: str
    # ) -> Dict[str, Any]:
    #     return super().get_doc_context(docname, body, metatags)
