================
Getting Started
================

パッケージのインストール
============================

.. code-block:: bat

   pip install sphinxbootstrap4theme


conf.pyの設定
===================

.. code-block:: python

   import sphinxbootstrap4theme

   html_theme = 'sphinxbootstrap4theme'
   html_theme_path = [sphinxbootstrap4theme.get_path()]


オプション設定
=================

conf.pyのhtml_theme_optionsに指定できるオプションの説明です。

.. code-block:: python

   html_theme_options = {
       # navbarのスタイルを指定します。
       # 設定値：'fixed-top', 'full' (Default: 'fixed-top')
       'navbar_style' : 'fixed-top',

       # navbarの文字色のクラスを指定します。
       # dark, light
       'navbar_color_class' : 'dark',

       # navbarの背景色のクラスを指定します。
       # inverse, primary, faded, success, info, warning, danger
       'navbar_bg_class' : 'inverse',

       # navbarにドキュメントのtoctreeを表示するかどうか指定します。
       # Trueにした場合、ドロップダウンで4階層目まで表示します。
       'navbar_show_pages' : True,

       # navbarに表示するtoctreeのメニュー名を指定します。
       # (Default: 'Pages')
       navbar_pages_title : 'Pages',

       # navbarに表示されるリンクメニューを設定します。
       # 第一引数：メニュー名
       # 第二引数：URL
       # 第三引数；外部リンクの場合True、ドキュメントのURLの場合False
       'navbar_links' : [
            ('Home', 'index', False),
            ("Link", "http://example.com", True)
       ],
       # sidebarを表示するかどうか指定します。
       'show_sidebar' : True,

       # sidebarを右に表示します。
       # Falseの場合、左に表示します。
       # 設定値：True, False (Default: False)
       'sidebar_right': False,

       # sidebarを固定します。
       # 設定値：True, False (Default: True)
       'sidebar_fixed': True,

       # navbarの文字色のクラスを指定します。
       # 設定値：'dark', 'light' (Default: 'light')
       'sidebar_color_class': 'light',

       # sidebarの背景色のクラスを指定します。
       # 設定値：'inverse', 'primary', 'faded', 'success', 'info', 'warning', 'danger' (Default: 'faded')
       'sidebar_bg_class' : 'faded',

       # テーブルのヘッダーのスタイルのクラスを指定します。
       # 'inverse', 'light', ''
       'table_thead_class' : 'inverse',

       # フッターにショートカットキーの一覧表示用のボタンを表示するかどうか指定します。
       # 設定値：True, False (Default: False)
       'show_shortcut_list_btn' : False
   }