from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent.resolve()

project = "React Native"
root_doc = "index"
extensions = ["sphinxcontrib.specs"]
html_theme = "specs"

pygments_style = "default"
