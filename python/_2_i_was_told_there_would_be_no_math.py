# SPDX-License-Identifier: ISC

import io
from functools import reduce
from operator import add, mul


def _parse(input_stream):
    "Generate list of sqft of gift wrap and ft of ribbon needed for each gift"
    # input_string = (
    #     input_object.readline() if isinstance(input_object, io.IOBase) else input_object
    # )
    gifts = []
    for line in input_stream:
        edges = sorted([int(edge) for edge in line.split("x")])
        sides = [
            edges[0] * edges[1],
            edges[1] * edges[2],
            edges[2] * edges[0],
        ]
        area = 2 * sides[0] + 2 * sides[1] + 2 * sides[2]
        area_with_slack = area + min(sides)

        ribbon = 2 * edges[0] + 2 * edges[1] + reduce(mul, edges)

        gifts.append({"area": area_with_slack, "ribbon": ribbon})
    return gifts


def parse(input_stream):
    dimensions = _parse(input_stream)
    areas = [gift["area"] for gift in dimensions]
    ribbons = [gift["ribbon"] for gift in dimensions]
    return reduce(add, areas), reduce(add, ribbons)
