=======================
インストール方法
=======================


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