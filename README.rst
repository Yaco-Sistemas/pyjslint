==============
JSLint Wrapper
==============

JSLint wrapper for Python. Can be invoked from the command line and any Python
code.

It is built on the power of NodeJS.

Dependencies
============

It only depends on `nodejs <http://nodejs.org>`_. You must have node on your
system for running this wrapper.

It runs just fine with the `0.4.12 version
<http://nodejs.org/dist/node-v0.4.12.tar.gz>`_, but it may work too with other
versions.

There is no need to download JSLint, it will be fetched for your convinience.
But, if you want to use your own JSLint file you can specify it with an option,
just make it sure it is prepared to be executed on nodejs.

Installation
============

It is `uploaded to PyPI <http://pypi.python.org/pypi/pyjslint/>`_ so this will
do the trick::

    easy_install pyjslint

Or you can install it from the source code running::

    python setup.py install

In both cases you must have installed in your system setuptools or distribute.

Use it from the command line
============================

If you call the wrapper without arguments this will be the output::

    $ pyjslint
    One JavaScript file must be specified
    Usage: pyjslint [options] jsfile

So at least one JavaScript file must be specified.

Let's look at the possible options::

    $ pyjslint --help
    Usage: pyjslint [options] jsfile

    Options:
        -h, --help              show this help message and exit
        -u, --upgrade           Upgrade JSLint
        -j JSLINT, --jslint=JSLINT
                                JSLint location
        -o JSOPTIONS, --options=JSOPTIONS
                                JSLint options
        -n NODE, --node=NODE  Node location

With this options you can specify the JSLint file to use, where to find the
node executable or just make it sure it downloads the newest JSLint available.

Use it from Python
==================

If you want to use in your Python code, maybe in a control version system hook
or something, just make it sure it is in the Python path and do something like
this::

    import jslint

    # The method requires the text content of the file to check
    jslint.check_JSLint(file.read())

It will return a list with the errors found by JSLint.

There is no options yet if you invoke it this way. Maybe someday, contributions
are welcome ;)

Acknowledges
============

Based on `code from FND
<https://github.com/FND/misc/blob/ddcd0495d40f0c0203bfb063e30d4a110ef45666/JSLint/wrapper.py>`_.

Notes
=====

If no JSLint file is specified (the default behaviour), it will download the
newest one from `Douglas GitHub <https://github.com/douglascrockford/JSLint>`_
into ~/.jslint/jslint.js
