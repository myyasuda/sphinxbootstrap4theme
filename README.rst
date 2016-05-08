==========================================
Bootstrap v4.0.0alpha.2のSphinx HTMLテーマ
==========================================

利用方法
========

sphinxbootstrap4フォルダをthemeフォルダにコピー

conf.pyの設定の設定例
---------------------

.. code-block:: python

   # htmlテーマの設定
   html_theme = 'sphinxbootstrap4'

   # htmlロゴの設定
   # ロゴはnavbarに表示されます。
   # height37pxで表示されます。
   html_logo = '_static/logo.jpg'

   html_theme_options = {

       # navbarの文字色のクラスを指定します。
       # 設定値：'dark', 'light' (Default: 'dark')
       'navbar_color_class' : 'dark',

       # navbarの背景色のクラスを指定します。
       # 設定値：'inverse', 'primary', 'secondary', 'success', 'info', 'warning', 'danger' (Default: 'inverse')
       'navbar_bg_class' : 'inverse',

       # navbarにドキュメントのtoctreeを表示するかどうか指定します。
       # Trueの場合、ドロップダウンで4階層目まで表示します。
       # Falseの場合、非表示になります。
       # 設定値： True, False (Default: True)
       'navbar_show_pages' : True,

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

       # navbarの文字色のクラスを指定します。
       # 設定値：'dark', 'light' (Default: 'dark')
       'sidebar_color_class': 'dark',

       # sidebarの背景色のクラスを指定します。
       # 設定値：'inverse', 'primary', 'secondary', 'success', 'info', 'warning', 'danger' (Default: 'inverse')
       'sidebar_bg_class' : 'inverse',

       # テーブルのヘッダーのスタイルのクラスを指定します。
       # 設定値：'inverse', 'light', '' (Default: 'inverse')
       'table_thead_class' : 'inverse'
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

