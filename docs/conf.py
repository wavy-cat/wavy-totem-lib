#                  Copyright WavyCat 2024.
#  Distributed under the Boost Software License, Version 1.0.
#         (See accompanying file LICENSE or copy at
#           https://www.boost.org/LICENSE_1_0.txt)

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'wavy-totem-lib'
copyright = '2024, WavyCat'
author = 'WavyCat'
release = '2.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_immaterial'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_immaterial'
html_static_path = ['_static']

html_title = "%s v%s Documentation" % (project, release)
html_short_title = "%s %s Documentation" % (project, release)

html_theme_options = {
    "repo_url": "https://github.com/wavy-cat/wavy-totem-lib",
    "icon": {
        "repo": "fontawesome/brands/github",
    },
    "features": [
        "navigation.expand",
        # "navigation.tabs",
        # "toc.integrate",
        "navigation.sections",
        # "navigation.instant",
        # "header.autohide",
        "navigation.top",
        # "navigation.tracking",
        # "search.highlight",
        "search.share",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "announce.dismiss",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "green",
            "accent": "light-green",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "green",
            "accent": "light-green",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to light mode",
            },
        },
    ],
    # "version_dropdown": True,
    # "version_info": [
    #     {
    #         "version": "https://sphinx-immaterial.rtfd.io",
    #         "title": "ReadTheDocs",
    #         "aliases": [],
    #     },
    #     {
    #         "version": "https://jbms.github.io/sphinx-immaterial",
    #         "title": "Github Pages",
    #         "aliases": [],
    #     },
    # ],
    "toc_title_is_page_title": True,
    "social": [
        {
            "icon": "fontawesome/brands/github",
            "link": "https://github.com/wavy-cat/wavy-totem-lib",
            "name": "Source on github.com",
        },
        {
            "icon": "fontawesome/brands/python",
            "link": "https://pypi.org/project/wavy-totem-lib/",
        }
    ]
}
