.. _cli:

Command-line interface (CLI)
============================


Volts:

.. code:: bash

    $ ohmslaw volts -I 2 -R 4

Current:

.. code:: bash

    $ ohmslaw current -V 10 -R 5

Resistance:

.. code:: bash

    $ ohmslaw resistance -V 5 -I 2

Watts:

.. code:: bash

    $ ohmslaw watts R 15 I 20

Find resistor:

.. code:: bash

    $ ohmslaw find_resistor --source 10 --component_voltage 2


To list all command line options, simply type

.. code:: bash

    $ ohmslaw -h


Finally, if you're filing a bug report, the cli contains a switch called
``--build-playback-report``, which bundles up the state, allowing others
to easily replay your issue.