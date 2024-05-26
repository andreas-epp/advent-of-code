# SPDX-License-Identifier: ISC

import io
from functools import reduce
from operator import add


def _parse(input_stream):
    "Generate list of sqft of gift wrap needed for each gift"
    # input_string = (
    #     input_object.readline() if isinstance(input_object, io.IOBase) else input_object
    # )
    results = []
    for line in input_stream:
        edges = [int(edge) for edge in line.split("x")]
        sides = [
            edges[0] * edges[1],
            edges[1] * edges[2],
            edges[2] * edges[0],
        ]
        area = 2 * sides[0] + 2 * sides[1] + 2 * sides[2]
        area_with_slack = area + min(sides)

        results.append({"area": area_with_slack})
    return results


def parse(input_stream):
    areas = [area["area"] for area in _parse(input_stream)]
    return reduce(add, areas)

