import sys
from typing import Optional
from collections import defaultdict


def monte_carlo_pi(sample_size: Optional[str] = None) -> float:
    import random

    if not sample_size:
        return "Must provide sample size"

    sample_size = int(sample_size)
    inside_circle = lambda coord: coord[0] ** 2 + coord[1] ** 2 < 1
    ratio = (
        len(
            list(
                filter(
                    bool,
                    map(
                        inside_circle,
                        [
                            (random.random(), random.random())
                            for _ in range(sample_size)
                        ],
                    ),
                )
            )
        )
        / sample_size
    )

    return 4 * ratio


if __name__ == "__main__":
    methods = defaultdict(lambda: False, {"monte_carlo_pi": monte_carlo_pi})

    if len(sys.argv) > 1:
        method = methods[sys.argv[1]]
        if method:
            result = method(*[arg for arg in sys.argv[2:]])

            print(result)
