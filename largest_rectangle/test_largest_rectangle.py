from largest_rectangle.largest_rectangle import ascending_array_of_value


class TestAscendingArrayOfValue:
    def test_only_ascending_returns_array(self):
        assert ascending_array_of_value(10, 15, 0) == [0, 0, 0, 0, 0]

    def test_only_descending_returns_empty_array(self):
        assert ascending_array_of_value(10, 5, 0) == []

    def test_equal_returns_empty_array(self):
        assert ascending_array_of_value(10, 10, 0) == []


class TestLargestRectangle:
    pass
