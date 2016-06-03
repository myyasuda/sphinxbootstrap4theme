#!/usr/bin/env python3
# -*- coding: utf-8 -*-\

source_suffix = '.rst'
master_doc = 'index'

version = "0.3.1"

project = 'Bootstrap4 theme'
copyright = '2016, Masahiko Yasuda'
author = 'Masahiko Yasuda'

language = 'en'

# templates_path = ['_templates']

# html_sidebars = {'**' : ['globaltoc.html']}

html_theme = 'sphinxbootstrap4theme'

html_theme_path = ['../themes']

html_theme_options = {
    'navbar_links' : [
        ('Home', 'index', False),
        ("Link", "http://example.com", True),
        ("GitHub", "https://github.com/myyasuda/sphinxbootstrap4theme", True)
    ],
    'show_shortcut_list_btn' : True
}

rst_prolog= u"""
    .. |project| replace:: sphinxbootstrap4
"""