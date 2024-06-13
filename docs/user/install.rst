.. _install:

Installation of ohmslaw
========================

This guide assumes you already have python and pip installed.

To install ohmslaw, run the following command in your terminal::

    $ pip install ohmslaw

Get the Source Code
-------------------

ohmslaw is actively developed on GitHub, where the source is `available <https://github.com/JuanBindez/ohmslaw>`_.

You can either clone the public repository::

    $ git clone git://github.com/JuanBindez/ohmslaw.git

Or, download the `tarball <https://github.com/JuanBindez/ohmslaw/tarball/master>`_::

    $ curl -OL https://github.com/JuanBindez/ohmslaw/tarball/master
    # optionally, zipball is also available (for Windows users).

Once you have a copy of the source, you can embed it in your Python package, or install it into your site-packages by running::

    $ cd ohmslaw
    $ python -m pip install .
