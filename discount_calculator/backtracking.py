# DISCOUNTS_PER_ITEM = [[1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 0, 1]]

DISCOUNT_MAP: list[dict] = [
    {"price": 10, "applies": lambda idx: idx == 0},
    {"price": 20, "applies": lambda idx: idx == 1},
    {"price": 30, "applies": lambda idx: idx in [0, 1]},
    {"price": 20, "applies": lambda idx: idx in [1, 2]},
]
ITEM_QUANTITIES = [2, 3, 2]

# GLOBALS
# {(Disc1, qty), (Disc2, qty2)}
best_plan: frozenset[tuple[int, int]] = frozenset()

best_benefit: float = 0


def max_discounts(quantities) -> int:
    return min(qty for qty in quantities)


def backtrack(
    discounts: list[dict],
    discount_idx: int,
    quantities: list[int],
    current_plan: frozenset[tuple[int, int]],
) -> bool:
    # Get max qty for discount
    if discount_idx >= len(discounts):
        return False
    current_discount = discounts[discount_idx]
    discount_applies: list[bool] = [
        current_discount["applies"](idx) for idx in range(len(quantities))
    ]
    current_max_qty = max_discounts(
        [qty for idx, qty in enumerate(quantities) if current_discount["applies"](idx)]
    )
    for consumed_qty in range(current_max_qty + 1):
        remaining_quantities = [
            item_qty - consumed_qty if discount_applies[idx] else item_qty
            for idx, item_qty in enumerate(quantities)
        ]
        if not sum(remaining_quantities):
            return False
        new_plan = current_plan | frozenset[tuple[int, int]](
            [(discount_idx, consumed_qty)]
        )
        if not backtrack(
            discounts,
            discount_idx + 1,
            remaining_quantities,
            new_plan,
        ):
            # Calculate total benefit based on current_plan
            total_benefit = sum(
                discounts[discount_idx]["price"] * quantity
                for discount_idx, quantity in new_plan
            )
            global best_benefit
            global best_plan
            if total_benefit > best_benefit:
                best_plan = new_plan
                best_benefit = total_benefit
            print(f"{new_plan=},{total_benefit=}")
            print(f"{remaining_quantities=}")

    return True


def run(discounts: list[dict], quantities: list[int]):
    # Get first discount and start the backtracking
    backtrack(discounts, 0, quantities, frozenset[tuple[int, int]]())
    print(f"{best_plan=}, {best_benefit=}")


if __name__ == "__main__":
    print("start")
    ys = run(DISCOUNT_MAP, ITEM_QUANTITIES)
    # for xs in ys:
    #     print(" ".join(map(str, xs)))
