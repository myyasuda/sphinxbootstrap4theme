.. image:: https://travis-ci.org/myyasuda/sphinxbootstrap4theme.svg?branch=master
    :target: https://travis-ci.org/myyasuda/sphinxbootstrap4theme

==========================================
Bootstrap v4.0.0alpha.2のSphinx HTMLテーマ
==========================================

`デモ <http://myyasuda.github.io/sphinxbootstrap4theme>`_

利用方法
========

.. code-block:: bat

   pip install sphinxbootstrap4theme

conf.pyの設定の設定例
---------------------

.. code-block:: python

   import sphinxbootstrap4theme

   # htmlテーマの設定
   html_theme = 'sphinxbootstrap4theme'
   html_theme_path = [sphinxbootstrap4theme.get_path()]

   # htmlロゴの設定
   # ロゴはnavbarに表示されます。
   # height37pxで表示されます。
   html_logo = '_static/logo.jpg'

   html_theme_options = {

       # navbarのスタイルを指定します。
       # 設定値：'fixed-top', 'full' (Default: 'fixed-top')
       'navbar_style' : 'fixed-top',

       # navbarの文字色のクラスを指定します。
       # 設定値：'dark', 'light' (Default: 'dark')
       'navbar_color_class' : 'dark',

       # navbarの背景色のクラスを指定します。
       # 設定値：'inverse', 'primary', 'faded', 'success', 'info', 'warning', 'danger' (Default: 'inverse')
       'navbar_bg_class' : 'inverse',

       # navbarにドキュメントのtoctreeを表示するかどうか指定します。
       # Trueの場合、ドロップダウンで4階層目まで表示します。
       # Falseの場合、非表示になります。
       # 設定値： True, False (Default: True)
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
       # 設定値：True, Flase (Default: True)
       'show_sidebar' : True,

       # sidebarを右に表示します。
       # Falseの場合、左に表示します。
       # 設定値：True, False (Default: False)
       'sidebar_right': False,

       # sidebarを固定します。
       # 設定値：True, False (Default: True)
       'sidebar_fixed': True,

       # テーブルのヘッダーのスタイルのクラスを指定します。
       # 設定値：'inverse', 'light', '' (Default: 'inverse')
       'table_thead_class' : 'inverse',

       # フッターにショートカットキーの一覧表示用のボタンを表示するかどうか指定します。
       # 設定値：True, False (Default: False)
       'show_shortcut_list_btn' : False
   }


開発方法
========

環境準備
--------

以下のアプリケーションをインストールする必要があります。

- java 1.8
- python 3.5.1
- sphinx 1.4.1

テーマを配布用にパッケージング
------------------------------

.. code-block:: bat

   gradlew buildPackage

テーマをインストール
------------------------------

.. code-block:: bat

   gradlew installPackage

PyPIにテーマを登録
------------------

.. code-block:: bat

   gradlew uploadPackage

exampleのドキュメントのビルド
-----------------------------

「example/_build」にビルド後のドキュメントが生成されます。

.. code-block:: bat

   gradlew example

TODO
----

- サイドメニューのオンオフボタンの実装


ライセンス
==========

+--------------+---------------+-------------+-----------------------------------------------------+
|サードパーティ|バージョン     |ライセンス   |URL                                                  |
+==============+===============+=============+=====================================================+
| Bootstrap    |v4.0.0-alpha.2 | MIT license |https://github.com/twbs/bootstrap/blob/master/LICENSE|
+--------------+---------------+-------------+-----------------------------------------------------+

