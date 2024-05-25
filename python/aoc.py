#!/bin/python3
# SPDX-License-Identifier: ISC

"""
Run advent of code scripts.

Usage:
    aoc.py <num> [-|<file>]
"""

from docopt import docopt
import sys, os, importlib

opt = docopt(__doc__)

script_dir = os.path.dirname(sys.argv[0])


input_stream = None
if opt["<file>"]:
    input_stream = open(opt["<file>"])
else:
    input_stream = sys.stdin

files = os.listdir(script_dir)
for file in files:
    if file.startswith("_" + opt["<num>"] + "_"):
        parse = importlib.import_module(file.removesuffix(".py")).parse
        break
else:
    raise Exception("file number doesn't exist")

print(parse(input_stream))

if input_stream and input_stream is not sys.stdin:
    input_stream.close()
