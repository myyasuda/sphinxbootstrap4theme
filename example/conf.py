#!/usr/bin/env python3
# -*- coding: utf-8 -*-\

source_suffix = '.rst'
master_doc = 'index'

version = "0.1.0"

project = 'Bootstrap4 theme'
copyright = '2016, Masahiko Yasuda'
author = 'Masahiko Yasuda'

language = 'ja'

templates_path = ['_templates']

# html_sidebars = {'**' : ['globaltoc.html']}

html_theme = 'sphinxbootstrap4theme'

html_theme_path = ['../themes']

html_theme_options = {
    'navbar_style' : 'fixed-top',
    'navbar_color_class': 'dark',
    'navbar_bg_class' : 'inverse',
    'navbar_show_pages' : True,
    'navbar_links' : [
        ('Home', 'index', False),
        ("Link", "http://example.com", True)
    ],
    'show_sidebar' : True,
    'sidebar_right': False,
    'sidebar_fixed': True,
    'sidebar_color_class': 'light',
    'sidebar_bg_class' : 'faded',
    'table_thead_class' : 'inverse',
    'show_shortcut_list_btn' : True
}

rst_prolog= u"""
    .. |project| replace:: sphinxbootstrap4
"""