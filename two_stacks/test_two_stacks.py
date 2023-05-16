from two_stacks.two_stacks import stack_depth_not_exceeding_sum, sum_stack, twoStacks


class Test_stack_depth_not_exceeding_sum:
    def test_empty_stack_returns_zero(self):
        depth, currentSum = stack_depth_not_exceeding_sum([], 1)
        assert depth == 0
        assert currentSum == 0

    def test_depth_matches_stack_length(self):
        depth, currentSum = stack_depth_not_exceeding_sum([1, 2, 3], 6)
        assert depth == 3
        assert currentSum == 6

    def test_maxSum_greater_than_stack_sum(self):
        depth, currentSum = stack_depth_not_exceeding_sum([1, 2, 3], 10)
        assert depth == 3
        assert currentSum == 6

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

    def test_original_stack_length_not_modified(self):
        original_stack = [1, 3]
        stack_depth_not_exceeding_sum(original_stack, 2)
        assert len(original_stack) == 2


class Test_sum_stack:
    def test_empty_stack_returns_zero(self):
        assert sum_stack([]) == 0

    def test_stack_returns_correct_value(self):
        assert sum_stack([1, 2]) == 3

    def test_original_stack_length_not_modified(self):
        original_stack = [1, 3]
        sum_stack(original_stack)
        assert len(original_stack) == 2


class Test_twoStacks:
    def test_high_score_only_taking_from_b_stack(self):
        assert twoStacks(10, [7, 3], [8, 1, 1]) == 3
