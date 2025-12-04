from pathlib import Path
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
        data = "".join(line.rstrip() for line in f)
        for data_idx, row in enumerate(grid_adj(139**2).tolist()):
            if data[data_idx] == "@":
                edges = 0
                i = 0
                while edges < 4 and i < len(row):
                    edges += 1 if row[i] is True and data[i] == "@" else 0
                    i += 1
                pt1 += 1 if edges < 4 else 0
        return pt1


if __name__ == "__main__":
    print(f"{run()=} ")
