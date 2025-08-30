from .d_03 import get_mul_expr, mul_tuple


def test_get_mul_expression_whole_word():
    assert get_mul_expr("mul(1,2)") == [("1", "2")]


def test_get_mul_expression_partial():
    assert get_mul_expr("my_mul(1,2), my_mul(3,4)") == [("1", "2"), ("3", "4")]


def test_mul_tuple():
    assert mul_tuple(("1", "2")) == 2
    assert mul_tuple(("3", "4")) == 12
