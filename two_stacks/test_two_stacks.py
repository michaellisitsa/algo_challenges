from two_stacks.two_stacks import stack_depth_not_exceeding_sum


class TestTwoStacks:
    def test_list_maxSum_matches_currentSum_exactly(self):
        # At least one solution has been found
        # sqrt(100) == 10
        depth, currentSum = stack_depth_not_exceeding_sum([1, 3, 2, 4, 6, 7], 10)
        assert depth == 4
        assert currentSum == 10

    def test_list_with_maxSum_less_than_first_item_returns_zero_depth(self):
        depth, currentSum = stack_depth_not_exceeding_sum([11, 3], 10)
        assert depth == 0
        assert currentSum == 0

    def test_list_maxSum_does_not_match_currentSum(self):
        # At least one solution has been found
        # sqrt(100) == 10
        depth, currentSum = stack_depth_not_exceeding_sum([1, 3], 2)
        assert depth == 1
        assert currentSum == 1  # which is different to maxSum=2
