from pathlib import Path
import operator


def pt1():
    with open(f"{Path(__file__).parent}/data/05.txt", "r") as f:
        result = 0
        ranges = []
        adding_ranges = True
        for line in f:
            if line == "\n":
                adding_ranges = False
                continue
            if adding_ranges is True:
                start, _, end = line.strip("\n").partition("-")
                ranges.append([int(start), int(end)])
            else:
                for rng in ranges:
                    if int(line.strip("\n")) <= rng[1] and int(line) >= rng[0]:
                        result += 1
                        break
        return result


def pt2():
    with open(f"{Path(__file__).parent}/data/05.txt", "r") as f:
        result = 0
        ranges = []
        adding_ranges = True
        for line in f:
            if line == "\n":
                adding_ranges = False
                break
            if adding_ranges is True:
                start, _, end = line.strip("\n").partition("-")
                ranges.append({"start": int(start), "end": int(end)})

        ranges = sorted(ranges, key=operator.itemgetter("start"))
        compacted_ranges = []
        for idx, rng in enumerate(ranges):
            if not compacted_ranges:
                compacted_ranges.append(ranges[0])
            else:
                last = compacted_ranges[-1]
                if rng["end"] >= last["start"] and rng["start"] <= last["end"]:
                    # Compact the last range
                    last["end"] = max(last["end"], rng["end"])
                else:
                    compacted_ranges.append(rng)

        return sum((rng["end"] - rng["start"]) + 1 for rng in compacted_ranges)


if __name__ == "__main__":
    print(f"{pt1()=} {pt2()=}")
