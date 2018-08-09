#!/usr/bin/env python3
# -*- coding: utf-8 -*-\

source_suffix = '.rst'
master_doc = 'index'

version = "0.5.2"

project = 'Bootstrap4 theme'
copyright = '2016, Masahiko Yasuda'
author = 'Masahiko Yasuda'

language = 'en'

# templates_path = ['_templates']

# html_sidebars = {'**' : ['globaltoc.html', 'relations.html', 'searchbox.html', 'sourcelink.html']}

html_theme = 'sphinxbootstrap4theme'

html_theme_path = ['../themes']

html_theme_options = {
    'navbar_links' : [
        ('Home', 'index', False),
        ("Link", "http://example.com", True),
        ("GitHub", "https://github.com/myyasuda/sphinxbootstrap4theme", True)
    ],
    'sidebar_right': False,
    'sidebar_fixed': True,
    'navbar_style': 'fixed-top'
}

rst_prolog= u"""
    .. |project| replace:: sphinxbootstrap4
"""