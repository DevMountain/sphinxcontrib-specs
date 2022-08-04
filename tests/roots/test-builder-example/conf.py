extensions = ["sphinxcontrib.specs", "sphinxlectern"]
html_theme = "specs"
html_use_index = False
html_sidebars = {"**": []}
html_permalinks_icon = "#"
smartquotes = True
pygments_style = "default"

lectern_substitutions = {
    # Python executable & version
    "pyname": "Python 3",
    "py": "python3",
    "pyi": "`python3`",
    "pycmd": "`python3`:cmd:",
    # iPython
    "ipyname": "IPython",
    "ipy": "ipython3",
    "ipyi": "`ipython3`",
    "ipycmd": "`ipython3`:cmd:",
    # PIP
    "pipname": "Pip 3",
    "pip": "pip3",
    "pipi": "`pip3`",
    "pipcmd": "`pip3`:cmd:",
    # Virtualenv manager
    "venvname": "Virtualenv",
    "venv": "virtualenv",
    "venvi": "`virtualenv`",
    "venvcmd": "`virtualenv`:cmd:",
    # Text editor
    "editorname": "VS Code",
    "editor": "code",
    "editori": "`code`",
    "editcmd": "`code`:cmd:",
}
