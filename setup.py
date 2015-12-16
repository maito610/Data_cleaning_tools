# -*- coding: utf-8 -*-
"""Setup file for the Data_cleaning_tools project.
"""


import codecs
import os.path
import re
import sys
from setuptools import setup, find_packages

# avoid a from get_zipcode_from_gmap import __version__ as version (that compiles get_zipcode_from_gmap.__init__ and is not compatible with bdist_deb)
version = None
for line in codecs.open(os.path.join('get_zipcode_from_gmap', '__init__.py'), 'r', encoding='utf-8'):
    matcher = re.match(r"""^__version__\s*=\s*['"](.*)['"]\s*$""", line)
    version = version or matcher and matcher.group(1)

# get README content from README.md file
with codecs.open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as fd:
    long_description = fd.read()


setup(
    name='get_zipcode_from_gmap',
    version=version,
    description='No description yet.',
    long_description=long_description,
    author='maito',
    author_email='maito.tauchi@en-japan.io',
    license='GPL-3',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='get_zipcode_from_gmap.tests',
    install_requires=[],
    setup_requires=[],
    classifiers=[],
)
