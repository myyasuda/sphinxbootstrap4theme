========================================
Examples
========================================

.. _TOP:

Tables
======

+---------+-----------+------------+-------------------+
|         | 使用例    |  書き方    |  HTMLタグ         |
+=========+===========+============+===================+
|強調     |*文字列*   | \*で囲む   | <em>              |
+---------+-----------+------------+-------------------+
|強い強調 |**文字列** | \*\*で囲む | <strong>          |
+---------+-----------+------------+-------------------+
|コード   |``文字列`` |\`\`で囲む  |<span class="pre"> |
+---------+-----------+------------+-------------------+

Code Blocks
===========

::

    ふつうの文章::

        コードブロック

    ふつうの文章



.. code-block:: rst

  .. code-block:: python

        import sys

        print sys.path


Download Links
==============

**rst**

.. code-block:: rst

    :download:`this file <examples.rst>`

**Output Example**

:download:`this file <./examples.rst>`


Admonitions
===========

**Hint**

.. code-block:: rst

    .. hint::

        This is a hint directive!

.. hint::

    This is a **hint** directive!

**Note**

.. code-block:: rst

    .. note::

        This is a note directive!

.. note::

    This is a **note** directive!

**Warning**

.. code-block:: rst

    .. warning::

        This is a warning directive!

.. warning::

    This is a **warning** directive!

**Tip**

.. code-block:: rst

    .. tip::

        This is a tip directive!

.. tip::

    This is a **tip** directive!


**Important**

.. code-block:: rst

    .. important::

        This is a important directive!

.. important::

    This is a **important** directive!

**Error**

.. code-block:: rst

    .. error::

        This is a error directive!

.. error::

    This is a **error** directive!

**Caution**

.. code-block:: rst

    .. caution::

        This is a caution directive!

.. caution::

    This is a caution directive!

**Danger**

.. code-block:: rst

    .. danger::

        This is a danger directive!

.. danger::

    This is a **danger** directive!

