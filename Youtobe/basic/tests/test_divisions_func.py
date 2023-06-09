from basic.my_funcs.utils import division
import pytest


@pytest.mark.parametrize('a, b, expected_result', [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)
                                                   ])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


# def test_zero_division():
#     with pytest.raises(ZeroDivisionError):
#         division(10, 0)
#
# def test_type_error():
#     with pytest.raises(TypeError):
#         division(10, '2')

@pytest.mark.parametrize('expected_exception, divider, divisionable', [(ZeroDivisionError, 0, 10),
                                                                        (TypeError, '2', 20)])
def test_division_with_error(expected_exception, divider, divisionable):
    with pytest.raises(expected_exception):
        division(divisionable, divider)
