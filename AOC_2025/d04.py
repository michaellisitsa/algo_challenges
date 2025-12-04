from pathlib import Path
from copy import copy
import numpy as np


# Adjacency matrix generator was borrowed from https://stackoverflow.com/a/60342810
# Could have used a graph library too.
def grid_adj(N: int) -> np.ndarray:
    """Creates a 2D grid adjacency matrix."""
    sqN = np.sqrt(N).astype(int)
    adj = np.zeros((sqN, sqN, sqN, sqN), dtype=bool)
    for i in range(sqN):
        for j in range(sqN):
            # Connect x=i, y=j, to x-1 and x+1, y-1 and y+1
            adj[i, j, max((i - 1), 0) : (i + 2), max((j - 1), 0) : (j + 2)] = True
    adj = adj.reshape(N, N)
    # Remove self-connections
    adj ^= np.eye(N, dtype=bool)
    return adj


def run():
    with open(f"{Path(__file__).parent}/data/04.txt", "r") as f:
        pt1 = 0
        pt2 = 0
        data = list("".join(line.rstrip() for line in f))
        adj_matrix = grid_adj(139**2).tolist()
        pt1_complete = False
        while True:
            next_data = copy(data)
            for data_idx, row in enumerate(adj_matrix):
                if data[data_idx] == "@":
                    edges = 0
                    i = 0
                    while edges < 4 and i < len(row):
                        if row[i] is True and data[i] == "@":
                            edges += 1
                        i += 1
                    if edges < 4:
                        pt1 += 0 if pt1_complete else 1
                        pt2 += 1
                        next_data[data_idx] = "."
            if next_data == data:
                break
            data = next_data
            pt1_complete = True
        return pt1, pt2


if __name__ == "__main__":
    print(f"{run()=} ")
