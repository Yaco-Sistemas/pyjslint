# Copyright (C) 2011  Alejandro Blanco <ablanco@yaco.es>

import os
from setuptools import setup

from jslint import version


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name="pyjslint",
    version=version,
    author="Alejandro Blanco",
    author_email="ablanco@yaco.es",
    description="JSLint wrapper",
    long_description=read('README.rst'),
    license="BSD-3",
    keywords="jslint javascript lint hook qa",
    packages=['jslint'],
    url='https://github.com/Yaco-Sistemas/pyjslint/',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'pyjslint = jslint.jslint:main',
            ]},
)
