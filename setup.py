# Copyright (C) 2011  Alejandro Blanco <ablanco@yaco.es>

import os
from setuptools import setup


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name="pyjslint",
    version='0.3.1',
    author="Alejandro Blanco",
    author_email="ablanco@yaco.es",
    description="JSLint wrapper",
    long_description=read('README.rst'),
    license="BSD-3",
    classifiers = ["Development Status :: 4 - Beta",
                   "Environment :: Console",
                   "Intended Audience :: Developers",
                   "Intended Audience :: System Administrators",
                   "License :: OSI Approved :: BSD License",
                   "Natural Language :: English",
                   "Programming Language :: JavaScript",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Quality Assurance"],
    keywords="jslint javascript lint hook qa",
    modules=['pyjslint'],
    url='https://github.com/Yaco-Sistemas/pyjslint/',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'pyjslint = jslint:main',
            ]},
)
