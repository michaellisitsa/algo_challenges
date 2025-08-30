from .d_03 import get_mul_expr, mul_tuple, slice_out_dos


def test_get_mul_expression_whole_word():
    assert get_mul_expr("mul(1,2)") == [("1", "2")]


def test_get_mul_expression_partial():
    assert get_mul_expr("my_mul(1,2), my_mul(3,4)") == [("1", "2"), ("3", "4")]


def test_mul_tuple():
    assert mul_tuple(("1", "2")) == 2
    assert mul_tuple(("3", "4")) == 12


def test_slice_out_dos():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert slice_out_dos(input) == ["xmul(2,4)&mul[3,7]!^", "do()?mul(8,5))"]


def test_slice_out_dos_2():
    input = "somethingdo()other thingdon't()don't()do()third thingdon't()"
    assert slice_out_dos(input) == ["somethingdo()other thing", "do()third thing"]
