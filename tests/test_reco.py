import pytest


@pytest.mark.parametrize("x", [0, 1, 2])
def test_exception(x):

    param = 10
    try:
        div = param / x
    except ZeroDivisionError:
        pytest.warns()
        pytest.fail("Cannot divide")

    if div == param:
        pytest.xfail("Same value")
