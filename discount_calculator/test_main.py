from main import run


def test_resolves_overlapping_bundles_keeps_higher_total():
    """
    Given 3 items and 4 discounts (2 non-bundle, 2 bundle), where bundle
    discounts overlap on item 1, the algorithm should keep the bundle discount
    with the higher total value.

    Input matrix (items x discounts):

                  D0         D1         D2          D3
                  (no-bndl)  (no-bndl)  (bundle)    (bundle)
        Item 0    1          0          1           0
        Item 1    0          1          1           1
        Item 2    0          0          0           1

    Conflict: Item 1 has both D2 (bundle) and D3 (bundle).
      - D2 covers items 0,1 → min_qty = min(1,2) = 1 → total = 10*1 = 10
      - D3 covers items 1,2 → min_qty = min(2,2) = 2 → total = 10*2 = 20
    D3 wins, D2 is zeroed out.
    """
    discounts = [
        {"price": 10, "applies": lambda idx: idx == 0, "bundle": 0},
        {"price": 10, "applies": lambda idx: idx == 1, "bundle": 0},
        {"price": 10, "applies": lambda idx: idx in [0, 1], "bundle": 1},
        {"price": 10, "applies": lambda idx: idx in [1, 2], "bundle": 1},
    ]
    items = [{"qty": 1}, {"qty": 2}, {"qty": 2}]

    result = run(discounts, items)

    assert result == [
        [1, 0, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 0, 1],
    ]


def test_no_bundle_discounts_returns_matrix_unchanged():
    """
    When no discounts are bundles, there are no conflicts to resolve.
    The matrix should pass through unchanged.

    Input/output matrix (items x discounts):

                  D0         D1
                  (no-bndl)  (no-bndl)
        Item 0    1          0
        Item 1    0          1
    """
    discounts = [
        {"price": 5, "applies": lambda idx: idx == 0, "bundle": 0},
        {"price": 5, "applies": lambda idx: idx == 1, "bundle": 0},
    ]
    items = [{"qty": 3}, {"qty": 2}]

    result = run(discounts, items)

    assert result == [
        [1, 0],
        [0, 1],
    ]


def test_non_overlapping_bundles_returns_matrix_unchanged():
    """
    Two bundle discounts that don't share any items have no conflict.

    Input/output matrix (items x discounts):

                  D0          D1
                  (bundle)    (bundle)
        Item 0    1           0
        Item 1    0           1
    """
    discounts = [
        {"price": 10, "applies": lambda idx: idx == 0, "bundle": 1},
        {"price": 10, "applies": lambda idx: idx == 1, "bundle": 1},
    ]
    items = [{"qty": 1}, {"qty": 1}]

    result = run(discounts, items)

    assert result == [
        [1, 0],
        [0, 1],
    ]


def test_higher_price_bundle_wins_over_lower():
    """
    Two bundle discounts overlap on the same item. The one with the higher
    price * min_qty total wins.

    Input matrix (items x discounts):

                  D0          D1
                  (bundle)    (bundle)
        Item 0    1           1

    Both cover only item 0 (qty=5):
      - D0: price=20, total = 20*5 = 100
      - D1: price=10, total = 10*5 = 50
    D0 wins, D1 is zeroed out.
    """
    discounts = [
        {"price": 20, "applies": lambda idx: idx == 0, "bundle": 1},
        {"price": 10, "applies": lambda idx: idx == 0, "bundle": 1},
    ]
    items = [{"qty": 5}]

    result = run(discounts, items)

    assert result == [
        [1, 0],
    ]


def test_bundle_wins_by_min_qty_not_coverage():
    """
    A bundle covering fewer items can win if min_qty gives it a higher total.

    Input matrix (items x discounts):

                  D0          D1
                  (bundle)    (bundle)
        Item 0    1           1
        Item 1    1           0

    D0 covers items 0,1 → min_qty = min(1,10) = 1 → total = 10*1 = 10
    D1 covers item 0   → min_qty = 1            → total = 15*1 = 15
    D1 wins, D0 is zeroed out.

    Expected output matrix:

                  D0          D1
                  (bundle)    (bundle)
        Item 0    0           1
        Item 1    0           0
    """
    discounts = [
        {"price": 10, "applies": lambda idx: idx in [0, 1], "bundle": 1},
        {"price": 15, "applies": lambda idx: idx == 0, "bundle": 1},
    ]
    items = [{"qty": 1}, {"qty": 10}]

    result = run(discounts, items)

    assert result == [
        [0, 1],
        [0, 0],
    ]


def test_mixed_bundle_and_non_bundle_non_bundle_untouched():
    """
    Non-bundle discounts sharing items with bundle discounts are not
    affected by conflict resolution.

    Input matrix (items x discounts):

                  D0          D1          D2
                  (no-bndl)   (bundle)    (bundle)
        Item 0    1           1           1

    Conflict between D1 and D2 on item 0 (qty=3):
      - D1: price=10, total = 10*3 = 30
      - D2: price=5,  total = 5*3  = 15
    D1 wins, D2 is zeroed. D0 (non-bundle) is untouched.

    Expected output matrix:

                  D0          D1          D2
                  (no-bndl)   (bundle)    (bundle)
        Item 0    1           1           0
    """
    discounts = [
        {"price": 10, "applies": lambda idx: idx == 0, "bundle": 0},
        {"price": 10, "applies": lambda idx: idx == 0, "bundle": 1},
        {"price": 5, "applies": lambda idx: idx == 0, "bundle": 1},
    ]
    items = [{"qty": 3}]

    result = run(discounts, items)

    assert result == [
        [1, 1, 0],
    ]


def test_three_overlapping_bundles_resolved_iteratively():
    """
    Three bundle discounts all overlap on item 0. The algorithm resolves
    conflicts iteratively — first pass picks the best of the first pair
    found, second pass resolves any remaining conflict.

    Input matrix (items x discounts):

                  D0          D1          D2
                  (bundle)    (bundle)    (bundle)
        Item 0    1           1           1

    All cover item 0 (qty=2):
      - D0: price=5,  total = 10
      - D1: price=20, total = 40
      - D2: price=10, total = 20

    First conflict found: [0, 1, 2]. D1 wins (highest total).
    D0 and D2 are zeroed out.

    Expected output matrix:

                  D0          D1          D2
                  (bundle)    (bundle)    (bundle)
        Item 0    0           1           0
    """
    discounts = [
        {"price": 5, "applies": lambda idx: idx == 0, "bundle": 1},
        {"price": 20, "applies": lambda idx: idx == 0, "bundle": 1},
        {"price": 10, "applies": lambda idx: idx == 0, "bundle": 1},
    ]
    items = [{"qty": 2}]

    result = run(discounts, items)

    assert result == [
        [0, 1, 0],
    ]


def test_empty_items_returns_empty_matrix():
    """
    No items means no matrix rows.

    Input/output matrix: (empty)
    """
    discounts = [
        {"price": 10, "applies": lambda idx: False, "bundle": 1},
    ]
    items = []

    result = run(discounts, items)

    assert result == []
