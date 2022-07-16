from os import path
from pathlib import Path

from sphinx.application import Sphinx

from . import builder

package_dir = Path(path.abspath(path.dirname(__file__)))


def setup(app: Sphinx) -> None:
    # Theme
    app.add_html_theme("specs", (package_dir / "theme").resolve())

    # Builder
    app.add_builder(builder.SpecsBuilder)
