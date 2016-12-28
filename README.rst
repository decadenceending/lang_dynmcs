===============================
Langevin Dynamics
===============================


.. image:: https://img.shields.io/pypi/v/lang_dynmcs.svg.
        :target: https://pypi.python.org/pypi/lang_dynmcs

.. image:: https://img.shields.io/travis/spectrumtouch/lang_dynmcs.svg
        :target: https://travis-ci.org/spectrumtouch/lang_dynmcs

.. image:: https://readthedocs.org/projects/lang-dynmcs/badge/?version=latest
        :target: https://lang-dynmcs.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/spectrumtouch/lang_dynmcs/shield.svg
     :target: https://pyup.io/repos/github/spectrumtouch/lang_dynmcs/
     :alt: Updates
     
.. image:: https://codecov.io/gh/spectrumtouch/lang_dynmcs/branch/master/graph/badge.svg
     :target: https://codecov.io/gh/spectrumtouch/lang_dynmcs


Langevin Dynamics program for computing dynamic properties of a particle.

* Free software: MIT license
* Documentation: https://lang-dynmcs.readthedocs.io.

About Langevin Dynamics
Langevin Dynamics is used in mathematical modeling of molecular systems and
their dynamics. Langevin Dynamics model is the first project in CHE 477.
In this project we will attempt to model dynamics of a simple system.

Features
--------

Features:
Calculate net Force for each time step, by considering: solvent force,
solvent drag force and potential energy.
Calculate acceleration using the obtained net Force
Use obtained acceleration to calculate new velocity for the current time
Calculate current position using the velocity for the current time step,
from the previous step.

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
