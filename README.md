# sphinxcontrib.specs

A Sphinx extension for building Devmountain's Specs v3.0 curriculum!

## Installation

##### Install with your favorite package manager

```bash
poetry add sphinxcontrib-specs

# ...or just use pip
pip install sphinxcontrib-specs
```


##### Add the extension to your Sphinx configuration file

```python
# conf.py

extensions = [
  # ...
  'sphinxcontrib.specs',
]
```

##### Set your `html_theme` to `"specs"`

```python
# conf.py

html_theme = "specs"
```

##### Build using the `specs` builder

```bash
sphinx-build -b specs . _build/specs
```

## Features

Uhh... look for the docs in Notion.

Or just look at the example in [`tests/roots/test-builder-example`](tests/roots/test-builder-example/index.rst).
