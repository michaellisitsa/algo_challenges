# DISCOUNTS_PER_ITEM = [[1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 0, 1]]
DISCOUNT_MAP = [
    {"price": 10, "applies": lambda idx: idx == 0, "bundle": 0},
    {"price": 10, "applies": lambda idx: idx == 1, "bundle": 0},
    {"price": 10, "applies": lambda idx: idx in [0, 1], "bundle": 1},
    {"price": 10, "applies": lambda idx: idx in [1, 2], "bundle": 1},
]
ITEMS = [{"qty": 1}, {"qty": 2}, {"qty": 2}]


def run(discounts: list[dict], items: list[dict[str, int]]):
    """
    Pick the highest of the discounts for bundled items.
    This will iteratively pick the best discount out of all bundles.

    Returns:
        Matrix with overlapping bundle discounts removed
    """
    matrix: list[list[int]] = []
    for disc in discounts:
        matrix.append([1 if disc["applies"](idx) else 0 for idx in range(len(items))])
    matrix = [list(x) for x in zip(*matrix)]

    def next_conflict(new_matrix) -> list[int]:
        """
        Get next row of matrix with the sum of columns whose index has a bundle discount
        """
        for row_idx, row in enumerate(new_matrix):
            overlapping_indices = []
            for col_idx, cell in enumerate(row):
                if cell == 1 and discounts[col_idx]["bundle"] == 1:
                    overlapping_indices.append(col_idx)
            if len(overlapping_indices) > 1:
                return overlapping_indices
        return []

    while next_overlapping_indices := next_conflict(matrix):
        best_total = 0
        best_total_index = None
        for idx in next_overlapping_indices:
            column = [val[idx] for val in matrix]
            min_qty = min(
                item["qty"]
                for row_idx, item in enumerate(items)
                if column[row_idx] == 1
            )
            if (new_best_total := discounts[idx]["price"] * min_qty) > best_total:
                best_total_index = idx
                best_total = new_best_total

        # Now we remove all column values for the losing indices
        if best_total_index is not None:
            next_overlapping_indices.remove(best_total_index)
            for col_idx in next_overlapping_indices:
                for row_idx in range(len(matrix)):
                    matrix[row_idx][col_idx] = 0

    return matrix


# DISCOUNTS_PER_ITEM = [[1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 0, 1]]
DISCOUNT_MAP = [
    {"price": 10, "applies": lambda idx: idx in [0, 1]},
    {"price": 10, "applies": lambda idx: idx in [1, 2]},
]
ITEMS = [{"qty": 1}, {"qty": 2}, {"qty": 2}]


# Do we need to evaluate the non bundle discounts? We just have to loop over the discounts to find non-bundled
def run_only_bundled(discounts: list[dict], items: list[dict[str, int]]):
    """
    Pick the highest of the discounts for bundled items.
    This will iteratively pick the best discount out of all bundles.

    Returns:
        Matrix with overlapping bundle discounts removed
    """
    matrix: list[list[int]] = []
    for disc in discounts:
        matrix.append([1 if disc["applies"](idx) else 0 for idx in range(len(items))])
    matrix = [list(x) for x in zip(*matrix)]

    def next_conflict(new_matrix) -> list[int]:
        """
        Get next row of matrix with the sum of columns whose index has a bundle discount
        """
        for row_idx, row in enumerate(new_matrix):
            overlapping_indices = []
            for col_idx, cell in enumerate(row):
                if cell == 1:
                    overlapping_indices.append(col_idx)
            if len(overlapping_indices) > 1:
                return overlapping_indices
        return []

    while next_overlapping_indices := next_conflict(matrix):
        best_total = 0
        best_total_index = None
        for idx in next_overlapping_indices:
            column = [val[idx] for val in matrix]
            min_qty = min(
                item["qty"]
                for row_idx, item in enumerate(items)
                if column[row_idx] == 1
            )
            if (new_best_total := discounts[idx]["price"] * min_qty) > best_total:
                best_total_index = idx
                best_total = new_best_total

        # Now we remove all column values for the losing indices
        if best_total_index is not None:
            next_overlapping_indices.remove(best_total_index)
            for col_idx in next_overlapping_indices:
                for row_idx in range(len(matrix)):
                    matrix[row_idx][col_idx] = 0

    return matrix


if __name__ == "__main__":
    ys = run(DISCOUNT_MAP, ITEMS)
    for xs in ys:
        print(" ".join(map(str, xs)))
