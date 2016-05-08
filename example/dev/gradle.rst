======================
Gradleのタスク
======================

|project|\ のタスクの一覧です。

テーマを配布用にパッケージング
===========================================

distディレクトリ配下にパッケージが出力されます。

.. code-block:: bat

   gradlew buildPackage

テーマのインストール
===========================================

distディレクトリはいかに出力されたパッケージをインストールします。

.. code-block:: bat

   gradlew installPackage

PyPIにテーマを登録
===========================================

.. code-block:: bat

   gradlew uploadPackage

exampleのドキュメントのビルド
==========================================

「example/_build」にビルド後のドキュメントが生成されます。

.. code-block:: bat

   gradlew example

