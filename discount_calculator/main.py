DISCOUNT_MAP = [
    {"price": 10, "applies": lambda idx: idx == 0, "bundle": 0},
    {"price": 10, "applies": lambda idx: idx == 1, "bundle": 0},
    {"price": 10, "applies": lambda idx: idx in [0, 1], "bundle": 1},
    {"price": 10, "applies": lambda idx: idx in [1, 2], "bundle": 1},
]
ITEMS = [{"qty": 1}, {"qty": 2}, {"qty": 2}]


def run(discounts: list[dict], items: list[dict[str, int]]) -> list[list[int]]:
    """
    Pick the highest of the discounts for bundled items.
    This will iteratively pick the best discount out of all bundles.

    Returns:
        Matrix with overlapping bundle discounts removed
    """
    if not items:
        return []

    matrix = [
        [int(d["applies"](i)) for d in discounts]
        for i in range(len(items))
    ]

    def bundle_cols(row):
        return [col for col, val in enumerate(row) if val and discounts[col]["bundle"]]

    def discount_total(col):
        return discounts[col]["price"] * min(
            items[row]["qty"] for row in range(len(items)) if matrix[row][col]
        )

    while conflict := next((bundle_cols(row) for row in matrix if len(bundle_cols(row)) > 1), None):
        best = max(conflict, key=discount_total)
        for col in conflict:
            if col != best:
                for row in matrix:
                    row[col] = 0

    return matrix


if __name__ == "__main__":
    ys = run(DISCOUNT_MAP, ITEMS)
    for xs in ys:
        print(" ".join(map(str, xs)))
