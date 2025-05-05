from .d_02 import check


def test_pt2_valid_removing_third_error_on_fourth():
    # Fails on 3, remove 5 (1 before)
    assert check([1, 2, 5, 3, 4, 5])


def test_pt2_valid_removing_current_error_on_current():
    # Fails on 6, Remove 6
    assert check([1, 2, 6, 3, 4, 5])


def test_pt2_valid_removing_first_error_on_second():
    assert check([10, 4, 5, 6])


def test_pt2_valid_first_pair_duplicated():
    assert check([10, 10, 12, 15])


def test_pt2_valid_removing_second_error_on_second():
    assert check([4, 9, 5, 7, 9])


def test_pt2_valid_removing_second_error_on_third():
    assert check([4, 6, 5, 7, 9])


def test_pt2_valid_removing_last_duplicate_on_last():
    assert check([1, 2, 3, 4, 5, 5])


def test_pt2_valid_removing_last_direction_change_on_last():
    assert check([1, 2, 3, 4, 5, 4])


def test_pt2_valid_removing_penultimate_error_on_last():
    assert check([1, 2, 3, 4, 7, 5])


def test_pt2_valid_duplicate_third_and_fourth():
    assert check([1, 2, 3, 3, 5, 6])


def test_pt2_valid_last_error_on_last():
    assert check([1, 4, 7, 10, 20])


def test_pt2_valid_removing_first_error_on_third():
    # Failed at index 2 (70), but needed to remove index 0 (71)
    # https://www.reddit.com/r/adventofcode/comments/1h4rhtl/comment/m0183kl/
    assert check([71, 69, 70, 71, 72, 75]) == 1


# INVALID


def test_pt2_invalid_gt_3_gap():
    assert check([1, 6, 7, 12]) == 0


def test_pt2_invalid_duplicates():
    assert check([1, 1, 1, 2, 3, 4]) == 0


def test_pt2_invalid_direction_change():
    assert check([1, 2, 3, 4, 3, 2, 1]) == 0


def test_pt2_invalid_2_values():
    # Not part of inputs
    # Completed grep serach 'vim /\v^[0-9]+\s[0-9]+$/g %' with no matches
    # assert check([1, 6]) == 0
    pass


def test_pt2_invalid_first_2_values():
    assert check([1, 6, 17, 18, 19]) == 0


def test_pt2_invalid_characters():
    # No characters in the data set
    # vim /\v.*[a-zA-Z]+.*/g %
    pass


def test_pt2_invalid_last_2_values():
    assert check([1, 2, 3, 7, 12]) == 0


def test_pt2_invalid_error_on_last():
    assert check([1, 8, 4, 2, 5]) == 0


def test_pt2_invalid_error_on_first_and_last():
    assert check([1, 8, 4, 2, 5]) == 0


def test_pt2_invalid_first_and_third_duplicate():
    assert check([10, 6, 10, 3, 4]) == 0
