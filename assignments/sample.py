def add(a, b):
    """
    Returns the sum of a and b.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0
    """
    # ========== TODO ==========
    # Add a and b and return the result
    # Hint: use the + operator
    return a + b
    # ==========================


def multiply(a, b):
    """
    Returns the product of a and b.

    >>> multiply(2, 3)
    6
    >>> multiply(-1, 5)
    -5
    >>> multiply(0, 100)
    0
    """
    # ========== TODO ==========
    # Multiply a and b and return the result
    # Hint: use the * operator
    return a * b
    # ==========================


if __name__ == "__main__":
    # Try your own test cases here — this block is ignored during grading
    print(add(10, 20))
    print(multiply(3, 4))

    assert add(1, 1) == 2
    assert multiply(2, 5) == 10