#!/bin/python
# SPDX-License-Identifier: ISC

import doctest


def parse(input):
    """find Santa's floor
    >>> parse("(())")[0]
    0
    >>> parse("()()")[0]
    0

    >>> parse("(((")[0]
    3
    >>> parse("(()(()(")[0]
    3
    >>> parse("))(((((")[0]
    3

    >>> parse("())")[0]
    -1
    >>> parse("))(")[0]
    -1

    >>> parse(")))")[0]
    -3
    >>> parse(")())())")[0]
    -3

    >>> parse(")")[1]
    1
    >>> parse("()())")[1]
    5
    """

    counter = 0
    position = 0
    position_basement = None

    for character in input:
        position += 1

        if character == "(":
            counter += 1
        elif character == ")":
            counter -= 1

        if counter == -1 and not position_basement:
            position_basement = position
    return (counter, position_basement)


print(parse(input()))
