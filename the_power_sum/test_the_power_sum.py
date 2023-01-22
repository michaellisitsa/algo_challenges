from the_power_sum.the_power_sum import powerSum


class TestPowerSum:
    def test_sqrt_100_has_more_than_one_solution(self):
        # At least one solution has been found
        # sqrt(100) == 10
        assert powerSum(100, 2) > 0

    def test_sqrt_13_has_exactly_1_solution(self):
        # 2^2 + 3^2 == 13
        assert powerSum(13, 2) == 1
