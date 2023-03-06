# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import os

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "LINCC Frameworks Python Project Template"
copyright = "2023, LINCC Frameworks"
author = "LINCC Frameworks"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

master_doc = "index"  # This assumes that sphinx-build is called from the root directory
html_show_sourcelink = (
    False  # Remove 'view source code' from top of page (for html, not python)
)
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_sidebars = {
    "**": ["globaltoc.html","searchbox.html"],
}
html_css_files = ["readthedocs-custom.css"]  # Override some CSS settings