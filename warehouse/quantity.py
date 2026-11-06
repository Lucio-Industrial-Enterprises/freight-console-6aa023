"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Return the integer quantity parsed from *value*.

    Raises ValueError for negative quantities.
    """
    result = int(value.strip())
    if result < 0:
        raise ValueError(f"Quantity must be non-negative, got {result}")
    return result
