from pathlib import Path
import heapq
from itertools import combinations
from math import sqrt


def pt1():
    result = None
    coords = []
    pq = []
    disjoint_sets = []
    coord_to_set = {}
    with open(f"{Path(__file__).parent}/data/08.txt", "r") as f:
        result = 0
        # for each  pair of  points On^2  we  calculate their distance from each other in 3d space.
        for line in f:
            coords.append(
                tuple([int(coord) for coord in line.rstrip().split(",")])
            )  # Tuple so its hashable
        for pt1, pt2 in combinations(coords, 2):
            distance = sqrt(
                (pt2[2] - pt1[2]) ** 2 + (pt2[1] - pt1[1]) ** 2 + (pt2[0] - pt1[0]) ** 2
            )
            # heapq will be ordered element-wise by tuple values a
            # https://stackoverflow.com/questions/45137002/define-heap-key-for-an-array-of-tuples#45137076
            heapq.heappush(pq, (distance, pt1, pt2))
        i = 0
        while i < len(pq) - 1 and i < 1000 and len(coord_to_set) <= len(coords):
            distance, pt1, pt2 = heapq.heappop(pq)
            if pt1 in coord_to_set and pt2 in coord_to_set:
                # Join 2 disjoint sets
                if coord_to_set[pt1] != coord_to_set[pt2]:
                    set_1 = disjoint_sets[coord_to_set[pt1]]
                    set_2 = disjoint_sets[coord_to_set[pt2]]
                    union_set = set_1 | set_2
                    disjoint_sets.append(union_set)
                    # sentinel value for deleted records so we don't have to renumber all other records
                    disjoint_sets[coord_to_set[pt1]] = set()
                    disjoint_sets[coord_to_set[pt2]] = set()
                    for item in union_set:
                        coord_to_set[item] = (
                            len(disjoint_sets) - 1
                        )  # Update the cache with the latest
            elif pt1 in coord_to_set:
                set_idx = coord_to_set[pt1]
                disjoint_sets[set_idx].add(pt2)
                coord_to_set[pt2] = set_idx
            elif pt2 in coord_to_set:
                set_idx = coord_to_set[pt2]
                disjoint_sets[set_idx].add(pt1)
                coord_to_set[pt1] = set_idx
            else:
                disjoint_sets.append({pt1, pt2})
                coord_to_set[pt1] = len(disjoint_sets) - 1
                coord_to_set[pt2] = len(disjoint_sets) - 1
            i += 1
        disjoint_sets = sorted(disjoint_sets, key=lambda val: len(val), reverse=True)
        for disjoint_set in disjoint_sets[:3]:
            result = len(disjoint_set) * result if result else len(disjoint_set)

        return result


if __name__ == "__main__":
    print(f"{pt1()=}")
