# SPDX-License-Identifier: ISC

import _1_not_quite_lisp as one


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
