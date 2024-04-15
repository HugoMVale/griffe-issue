def foo(x: float) -> float:
    """Foo function.

    !!! note

        This works.

    Parameters
    ----------
    x : float
        Number

    Returns
    -------
    float
        Square of number.

    !!! note

        This fails when it used to work.

    """
    return x**2
