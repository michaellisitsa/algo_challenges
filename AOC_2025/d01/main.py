from pathlib import Path


def run():
    with open(f"{Path(__file__).parent}/data/01.txt", "r") as f:
        dial = 50
        pt1 = 0
        pt2 = 0
        for line in f:
            count = int(line[1:-1])
            count = count if line[0] == "R" else -count
            sum = dial + count
            rotations, remainder = divmod(abs(sum), 100)
            passes = rotations
            prev_dial = dial
            if sum > 0:
                # 0 -> 0 (rotations 0) = minus 0
                # 150 -> 50 (1 rotation) = minus 100
                # 100 -> 0 (1 rotation) = minus 100
                # 250 -> 50 (2 rotations) = minus 200
                # 50 -> 0 (0 rotations) = leave
                dial = sum - (rotations * 100)
            elif sum < 0:
                # -20 -> 80 (1 rotations) = plus 100
                # -99 -> 1 (1 rotations) = plus 100
                # -100 -> 0 (1 rotations) = plus 100
                # -101 -> 99 (2 rotations) = plus 200
                # -230 -> 70 (3 rotations) = plus 300
                # -20 -> 0 (0 rotation) = none
                rotations = rotations if remainder == 0 else rotations + 1
                dial = sum + (rotations * 100)
            else:
                dial = 0

            if dial == 0:
                # If landing on zero, rotations will take into account passing 0.
                # We don't also need to count landing on zero.
                # e.g. 45 + R55 = 100 -> dial=0
                # (1 pass only)
                if count < 0:
                    pt2 += 1
                pt1 += 1
            if prev_dial == 0 and count < 0:
                # This should render as only 0 rotation, but we've had to wind clock forward 100
                # 0 + L14 = -14 -> dial=86
                pt2 += rotations - 1
            else:
                pt2 += rotations

        return pt1, pt2


if __name__ == "__main__":
    print(run())
