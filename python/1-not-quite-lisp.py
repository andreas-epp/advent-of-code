#!/bin/python
# SPDX-License-Identifier: ISC

import doctest


def parse(input):
    """find Santa's floor
    >>> process("(())")
    0
    >>> process("()()")
    0

    >>> process("(((")
    3
    >>> process("(()(()(")
    3
    >>> process("))(((((")
    3

    >>> process("())")
    -1
    >>> process("))(")
    -1

    >>> process(")))")
    -3
    >>> process(")())())")
    -3
    """

    counter = 0
    for character in input:
        if character == "(":
            counter += 1
        elif character == ")":
            counter -= 1
    return counter


print(parse(input()))
