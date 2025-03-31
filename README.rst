.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/Asylum_Research_AFM.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/Asylum_Research_AFM
    .. image:: https://readthedocs.org/projects/Asylum_Research_AFM/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://Asylum_Research_AFM.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/Asylum_Research_AFM/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/Asylum_Research_AFM
    .. image:: https://img.shields.io/pypi/v/Asylum_Research_AFM.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/Asylum_Research_AFM/
    .. image:: https://img.shields.io/conda/vn/conda-forge/Asylum_Research_AFM.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/Asylum_Research_AFM
    .. image:: https://pepy.tech/badge/Asylum_Research_AFM/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/Asylum_Research_AFM
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/Asylum_Research_AFM

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

===================
Asylum_Research_AFM
===================

AFM to DataFed Utility
=====================================

Instructions
------------

1. If you do not have a Python instance, it is recommended to install `Anaconda <https://www.anaconda.com/>`_.
2. Download the GitHub repository.
3. Install the dependencies using ``pip install -r requirements.txt``.
4. Set up a `Globus <https://www.globus.org/globus-connect>`_ account.
5. You need to be running `Globus-Personal-Connect <https://www.globus.org/globus-connect-personal>`_ on the computer and set up an endpoint.
6. Set up an account on `DataFed <https://datafed.ornl.gov/>`_.
7. Setup DataFed:

   - In your terminal, run ``datafed setup``.
   - Enter your username and password.

8. Set up a Globus account.
9. You need to be running Globus on the computer and set up an endpoint. This can be done using Globus Personal Connect.
10. Find your Globus endpoint ID and type the following command: ``datafed ep default set <endpoint_name_here>``.
11. Done!

Running Script
--------------

Run in the command line ``python DataFedLogin.py`` and input your username and password when prompted. Once "Successfully logged in to Data as {your username}" is printed, you are free to upload as many files as you want. This can be done by running this in the command line ``python ibw_to_datafed.py "<full file path>" "<collection id on Datafed>"`` as many times for as many files as you would like. When you are done uploading your files, to maintain security, please run ``python DataFedLogout.py``. This is to ensure your account does not automatically sign in the next time someone tries to upload a file.

Using the Igor Panel
--------------------

.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.6. For details and usage
information on PyScaffold see https://pyscaffold.org/.
