# SPDX-License-Identifier: ISC

import _1_not_quite_lisp as one
import _2_i_was_told_there_would_be_no_math as two


def test_floor():
    assert one.parse("(())")[0] == 0
    assert one.parse("()()")[0] == 0

    assert one.parse("(((")[0] == 3
    assert one.parse("(()(()(")[0] == 3
    assert one.parse("))(((((")[0] == 3

    assert one.parse("())")[0] == -1
    assert one.parse("))(")[0] == -1

    assert one.parse(")))")[0] == -3
    assert one.parse(")())())")[0] == -3


def test_basement():
    assert one.parse(")")[1] == 1
    assert one.parse("()())")[1] == 5


def test_two():
    result = two._parse(["2x3x4", "1x1x10"])
    assert result[0]["area"] == 58
    assert result[1]["area"] == 43
