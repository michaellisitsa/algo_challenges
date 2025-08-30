from .d_03 import get_mul_expr


def test_get_mul_expression_whole_word():
    assert get_mul_expr("mul(1,2)") == ["mul(1,2)"]


def test_get_mul_expression_partial():
    assert get_mul_expr("my_mul(1,2), my_mul(3,4)") == ["mul(1,2)", "mul(3,4)"]
