A collection of utilities.

Used the following guide to create the package:
https://python-packaging.readthedocs.io/en/latest/minimal.html

Had some trouble registering, apparently you don't need to pre-register anymore.

Created a .pypirc file in my user base directory and added the follow:

[pypi]
username:Nambarc
password:********

The used the following command to upload to PyPi:
py setup.py register sdist upload -r https://www.python.org/pypi