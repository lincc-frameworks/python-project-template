# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


from setuptools_scm import get_version

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "LINCC Frameworks Python Project Template"
copyright = "2025, LINCC Frameworks"
author = "LINCC Frameworks"
release = get_version(root="..")
# for example take major/minor
version = ".".join(release.split(".")[:2])

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

master_doc = "index"  # This assumes that sphinx-build is called from the root directory
html_favicon = "static/favicon.ico"
html_show_sourcelink = False  # Remove 'view source code' from top of page (for html, not python)

# Allow a custom CSS.
html_static_path = ["static"]
html_css_files = ["custom.css"]

extensions = ["sphinx_copybutton", "sphinx.ext.autosectionlabel"]

# -- sphinx-copybutton configuration ----------------------------------------
## sets up the expected prompt text from console blocks, and excludes it from
## the text that goes into the clipboard.
copybutton_exclude = ".linenos, .gp"
copybutton_prompt_text = ">> "

## lets us suppress the copy button on select code blocks.
copybutton_selector = "div:not(.no-copybutton) > div.highlight > pre"

# -- Options for autosectionlabel -------------------------------------------------

autosectionlabel_prefix_document = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
