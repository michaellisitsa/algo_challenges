from pathlib import Path


def check(vals, with_shortened_list=False):
    idx = 0
    direction = 1
    valid = True
    while idx < len(vals):
        previous = int(vals[idx - 1])
        current = int(vals[idx])
        # Can only compare on the 2nd iteration
        if idx == 0:
            idx += 1
            continue

        if idx == 1:
            # Determine direction based on the first comparison
            if current - previous == 0:
                # If same value doesn't matter which is removed
                if not with_shortened_list and check(vals[1:], True) == 1:
                    break
                valid = False
                break
            direction = 1 if current - previous > 0 else -1
        difference = (current - previous) * direction

        if difference > 3 or difference <= 0:
            two_pre_shortened_list = vals[:]
            two_pre_shortened_list.pop(idx - 2)
            # We have to check either the current or last. Either could've caused the error
            # e.g. [ 10, 6, 10, 3, 4 ] - fails on 3rd item, but issue is 1st item
            if not with_shortened_list and check(two_pre_shortened_list, True) == 1:
                break

            pre_shortened_list = vals[:]
            pre_shortened_list.pop(idx - 1)
            # e.g. [1, 2, 5, 3, 4, 5] - fails on 4th item, but issue is with 3rd item
            if not with_shortened_list and check(pre_shortened_list, True) == 1:
                break

            shortened_list = vals[:]
            shortened_list.pop(idx)
            # e.g. [1, 6, 3, 4, 5] - fails on 2nd item AND issue is 2nd item
            if not with_shortened_list and check(shortened_list, True) == 1:
                break
            # Early return as the sequence is invalid
            valid = False
            break
        idx += 1
    if valid:
        # We have reached the end and have not marked the sequence as invalid.
        return 1
    else:
        return 0


def pt_1():
    with open(f"{Path(__file__).parent}/data/02.txt", "r") as f:
        sum = 0
        for idx, line in enumerate(f):
            sum += check(line.split(), True)
    return sum


def pt_2():
    with open(f"{Path(__file__).parent}/data/02.txt", "r") as f:
        sum = 0
        for idx, line in enumerate(f):
            sum += check(line.split(), False)
    return sum


if __name__ == "__main__":
    print("pt_1", pt_1())
    print("pt_2", pt_2())
