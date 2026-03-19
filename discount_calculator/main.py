import pandas as pd

# DISCOUNTS_PER_ITEM = [[1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 0, 1]]
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

    qtys = pd.Series([item["qty"] for item in items])
    prices = pd.Series([d["price"] for d in discounts], dtype=float)
    is_bundle = pd.Series([bool(d["bundle"]) for d in discounts])

    # Build matrix: rows=items, cols=discounts
    df = pd.DataFrame(
        {i: [int(d["applies"](j)) for j in range(len(items))] for i, d in enumerate(discounts)}
    )

    while True:
        bundle_df = df.loc[:, is_bundle]
        conflict_mask = bundle_df.sum(axis=1) > 1
        if not conflict_mask.any():
            break

        # First item with conflicting bundle discounts
        row_idx = conflict_mask.idxmax()
        conflict_cols = bundle_df.columns[bundle_df.loc[row_idx] == 1]

        # value = price * min_qty across items covered by the discount
        totals = pd.Series(
            {col: prices[col] * qtys[df[col] == 1].min() for col in conflict_cols}
        )
        best_col = totals.idxmax()

        df[conflict_cols.difference([best_col])] = 0

    return df.values.tolist()


if __name__ == "__main__":
    ys = run(DISCOUNT_MAP, ITEMS)
    for xs in ys:
        print(" ".join(map(str, xs)))
