from pathlib import Path


def check(line):
    vals = line.split()
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
                valid = False
                break
            direction = 1 if current - previous > 0 else -1
        difference = (current - previous) * direction

        if difference > 3 or difference <= 0:
            # Should I call recursively? so that the logic works without the next entry?
            # Check skip_previous matches

            # Early return as the sequence is invalid
            valid = False
            break
        idx += 1
    # We have reached the end and have not marked the sequence as invalid.
    if valid:
        return 1
    else:
        return 0


def pt_1():
    with open(f"{Path(__file__).parent}/data/02.txt", "r") as f:
        sum = 0
        for line in f:
            sum += check(line)
    return sum


if __name__ == "__main__":
    print("pt_1", pt_1())
