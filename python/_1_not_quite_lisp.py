# SPDX-License-Identifier: ISC

import io


def parse(input_object):
    "find Santa's floor"

    input_string = (
        input_object.readline() if isinstance(input_object, io.IOBase) else input_object
    )

    counter = 0
    position = 0
    position_basement = None

    for character in input_string:
        position += 1

        if character == "(":
            counter += 1
        elif character == ")":
            counter -= 1

        if counter == -1 and not position_basement:
            position_basement = position
    return (counter, position_basement)
