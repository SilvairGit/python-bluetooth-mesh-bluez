======================
bluetooth-mesh-bluez
======================

.. image:: https://img.shields.io/pypi/v/bluetooth-mesh-bluez.svg
   :target: https://pypi.org/project/bluetooth-mesh-bluez
   :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/bluetooth-mesh-bluez.svg
   :target: https://pypi.org/project/bluetooth-mesh-bluez
   :alt: Python versions

----

Bluetooth mesh SDK for Python allows developing applications communicating with
Bluetooth mesh network using BlueZ's bluetooth-meshd.

What is this thing?
--------------------

This library provides a high-level async API for interacting with BlueZ mesh stack via D-Bus interface.

https://www.bluetooth.com/specifications/mesh-specifications

https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/doc/mesh-api.txt

Supported features include:

- **Application framework**: high-level API for creating mesh applications, elements, and models
- **D-Bus integration**: async communication with ``bluetooth-meshd`` via ``dbus-next``
- **Model support**: configuration, generic, light, sensor, scene, time, and Silvair-specific models
- **Provisioning**: provisioner and provision agent interfaces

Installation
------------

This project requires Python 3.14.

You can install "bluetooth-mesh-bluez" via `pip`_ from `PyPI`_::

    $ pip install bluetooth-mesh-bluez

You can also add it to a Poetry-managed project::

    $ poetry add bluetooth-mesh-bluez

If you want to work on this repository locally, install the project and development dependencies
with Poetry::

    $ poetry install

Contributing
------------

Contributions are very welcome. Tests can be run with `pytest`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `GPL-2.0`_ license, "bluetooth-mesh-bluez" is
free and open source software.

Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`GPL-2.0`: http://opensource.org/licenses/GPL-2.0
.. _`file an issue`: https://github.com/SilvairGit/python-bluetooth-mesh-bluez/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
