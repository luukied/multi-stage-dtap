"""
Calculator program
"""

def divide(a_i: int, b_i: int) -> float:
    """Divides two integers
     Arguments:
        a_i, b_i
    
    Doctest:
    >>> divide(3, 3)
    1.0
    >>> divide(6, 3)
    2.0
    """
    return a_i / b_i


def multiply(a_i: int, b_i: int) -> int:
    """Multiplies two integers
    Arguments:
        a_i, b_i
    
    Doctest:
    >>> multiply(2, 3)
    6
    >>> multiply(6, 3)
    18
    """
    return a_i * b_i


def subtract(a_i: int, b_i: int) -> int:
    """Subtracts two integers
    Arguments:
        a_i, b_i

    Doctest:
    >>> subtract(5, 3)
    2
    >>> subtract(6, 3)
    3
    """
    return a_i - b_i


def add(a_i: int, b_i: int) -> int:
    """Adds two integers
    Arguments:
        a_i, b_i

    Doctest:
    >>> add(2, 3)
    5
    >>> add(6, 3)
    9
    """
    return a_i + b_i


def main() -> None:
    """main function"""
    expensive_computation = divide(add(15, 6), multiply(10, subtract(9, 2)))
    print(expensive_computation)


if __name__ == "__main__":
    main()
