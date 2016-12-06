.. image:: https://travis-ci.org/myyasuda/sphinxbootstrap4theme.svg?branch=master
    :target: https://travis-ci.org/myyasuda/sphinxbootstrap4theme

=============================================
Bootstrap v4 HTML Theme for Sphinx
=============================================

`Demo <http://myyasuda.github.io/sphinxbootstrap4theme>`_

Instllation
===========

.. code-block:: bat

   pip install sphinxbootstrap4theme


Setting conf.py
===============

.. code-block:: python

   import sphinxbootstrap4theme

   html_theme = 'sphinxbootstrap4theme'
   html_theme_path = [sphinxbootstrap4theme.get_path()]

   # Html logo in navbar.
   # Fit in the navbar at the height of image is 37 px.
   html_logo = '_static/logo.jpg'


Html theme options
==================

The following is a description of the options that can be specified in **html_theme_options** in conf.py.

.. code-block:: python

   html_theme_options = {
       # Navbar style.
       # Values: 'fixed-top', 'full' (Default: 'fixed-top')
       'navbar_style' : 'fixed-top',

       # Navbar link color modifier class.
       # Values: 'dark', 'light' (Default: 'dark')
       'navbar_color_class' : 'dark',

       # Navbar background color class.
       # Values: 'inverse', 'primary', 'faded', 'success',
       #         'info', 'warning', 'danger' (Default: 'inverse')
       'navbar_bg_class' : 'inverse',

       # Show global TOC in navbar.
       # To display up to 4 tier in the drop-down menu.
       # Values: True, False (Default: True)
       'navbar_show_pages' : True,

       # Link name for global TOC in navbar.
       # (Default: 'Pages')
       'navbar_pages_title' : 'Pages',

       # Specify a list of menu in navbar.
       # Tuples forms:
       #  ('Name', 'external url or path of pages in the document', boolean)
       # Third argument:
       # True indicates an external link.
       # False indicates path of pages in the document.
       'navbar_links' : [
            ('Home', 'index', False),
            ("Link", "http://example.com", True)
       ],

       # Total width(%) of the document and the sidebar.
       # (Default: 80%)
       'main_width' : '80%',

       # Render sidebar.
       # Values: True, False (Default: True)
       'show_sidebar' : True,

       # Render sidebar in the right of the document.
       # Values：True, False (Default: False)
       'sidebar_right': False,

       # Fix sidebar.
       # Values: True, False (Default: True)
       'sidebar_fixed': True,

       # Html table header class.
       # Values: 'inverse', 'light' (Deafult: 'inverse')
       'table_thead_class' : 'inverse'
   }


開発方法
========

環境準備
--------

以下のアプリケーションをインストールする必要があります。

- python 3.5.2
- sphinx 1.5

テーマを配布用にパッケージング
------------------------------

.. code-block:: bat

   python setup.py sdist

テーマをインストール
------------------------------

.. code-block:: bat

   pip install dist/sphinxbootstrap4theme-${version}.zip

PyPIにテーマを登録
------------------

.. code-block:: bat

   python setup.py register sdist upload

exampleのドキュメントのビルド
-----------------------------

「example/_build」にビルド後のドキュメントが生成されます。

.. code-block:: bat

   sphinx-build -b html ./example ./example/_build -c ./example


ライセンス
==========

+--------------+---------------+-------------+-----------------------------------------------------+
|サードパーティ|バージョン     |ライセンス   |URL                                                  |
+==============+===============+=============+=====================================================+
| Bootstrap    |v4.0.0-alpha.5 | MIT license |https://github.com/twbs/bootstrap/blob/master/LICENSE|
+--------------+---------------+-------------+-----------------------------------------------------+

