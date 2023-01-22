
from the_power_sum.the_power_sum import powerSum

class TestPowerSum:
    def test_nth_root_is_integer_returns_gt_1(self):
        # At least one solution has been found
        # sqrt(100) == 10
       assert powerSum(100,2) > 0

    def test_nth_root_2nd_level_is_integer_returns_gt_1(self):
        # 2^2 + 3^2 == 13
        assert powerSum(13,2) > 0