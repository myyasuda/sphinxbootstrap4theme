==================
ビルド用のコマンド
==================

|project|\ 's build command list.

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

