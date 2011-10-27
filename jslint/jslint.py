#!/usr/bin/env python

# Copyright (C) 2011  Alejandro Blanco <ablanco@yaco.es>

"""
wrapper for JSLint
"""

from optparse import OptionParser
import os
import urllib2
import re
import sys
import subprocess
from tempfile import NamedTemporaryFile


pattern = r"Lint at line (\d+) character (\d+): (.*)"
default_jslint_options = r"""
strict: true,
white: true,
onevar: true,
undef: true,
newcap: true,
nomem: true,
regexp: true,
plusplus: true,
bitwise: true,
maxerr: 100,
indent: 4,
predef: ['document', 'window']
"""
node_script = r"""
var JSLINT = require("%s").JSLINT,
    print = require("sys").print,
    readFileSync = require("fs").readFileSync,
    error = null, i = 0, j = 0, src = null;

for (i = 2; i < process.argv.length; i++) {
    print("Analyzing file " + process.argv[i] + "\n");
    src = readFileSync(process.argv[i], "utf8");
    JSLINT(src, {%s});

    for (j = 0; j < JSLINT.errors.length; j++ ) {
        error = JSLINT.errors[j];
        if (error !== null) {
            if (typeof error.evidence !== "undefined") {
                print("\n" + error.evidence + "\n");
            } else {
                print("\n");
            }
            print("Lint at line " + error.line + " character " +
                  error.character + ": " + error.reason);
        }
    }

    if (JSLINT.errors.length > 0) {
        print("\n" + JSLINT.errors.length + " Error(s) found.\n");
        break;
    }
}
"""
usage = "Usage: %prog [options] jsfile"
parser = OptionParser(usage)
parser.add_option('-u', '--upgrade', dest='force', help='Upgrade JSLint',
                  action='store_true', default=False)
parser.add_option('-j', '--jslint', dest='jslint', help='JSLint location',
                  default=os.path.join('~', '.jslint', 'jslint.js'))
parser.add_option('-o', '--options', dest='jsoptions',
                  help='JSLint options', default=default_jslint_options)
parser.add_option('-n', '--node', dest='node',
                  help='Node location', default='node')


def execute_command(proc):
    p = subprocess.Popen(proc, stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out


def get_lint(options):
    jslint = os.path.expanduser(options.jslint)

    if not os.path.exists(jslint) or options.force:
        # download jslint from github
        response = urllib2.urlopen('https://raw.github.com/douglascrockford/'
                                   'JSLint/master/jslint.js')
        if not os.path.exists(os.path.dirname(jslint)):
            os.makedirs(os.path.dirname(jslint))
        f = open(jslint, 'w')
        f.write(response.read())
        response.close()
        f.write('\n\nexports.JSLINT = JSLINT;')  # add node support
        f.close()

    # write node script
    lint = NamedTemporaryFile()
    lint.write(node_script % (jslint[:-3], options.jsoptions))
    lint.file.flush()
    return lint


def process(jsfile, options):
    lint = get_lint(options)
    command = [options.node, lint.name, jsfile.name]
    output = execute_command(command)
    jsfile.close()
    lint.close()
    return [line for line in output.split("\n") if line]


def reformat(lines, pattern, filename):
    results = []
    regex = re.compile(pattern)
    for line in lines:
        matches = regex.search(line)
        if matches:
            line = int(matches.groups()[0])
            char = int(matches.groups()[1])
            msg = matches.groups()[2]
            results.append("%s - %d:%d - %s" % (filename, line, char, msg))
    return results


# Hooks entry point
def check_JSLint(code_string):
    tmpfile = NamedTemporaryFile()
    tmpfile.write(code_string)
    tmpfile.file.flush()
    return process(tmpfile, parser.get_default_values())


def main():
    (options, args) = parser.parse_args()
    if len(args) < 1:
        sys.stderr.write('One JavaScript file must be specified\n')
        sys.stderr.write(usage.replace('%prog', os.path.split(sys.argv[0])[1])
                         + '\n')
        sys.exit(False)
    filename = args[0]
    errors = process(open(filename, "r"), options)
    if len(errors) > 0:
        print "\n".join(reformat(errors, pattern, filename))
        sys.exit(False)
    sys.exit(True)


if __name__ == "__main__":
    main()
