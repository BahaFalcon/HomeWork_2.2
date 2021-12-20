import pytest

from velocity import calculate_average_velocity

def test_one_arg():
    assert(1.0, calculate_average_velocity(1))

def test_simple_average():
    assert(15.0, calculate_average_velocity(10, 20))

def test_raises_when_no_args():
    with pytest.raises(ZeroDivisionError):
        calculate_average_velocity()

def test_works_with_str_args():
    assert(10.0, calculate_average_velocity(10, 20, 'A'))

def test_only_non_int_args():
    assert(0.0, calculate_average_velocity(None, b'd', 'A'))

def test_negative_average():
    assert(-15.0, calculate_average_velocity(-10, -20))

def test_sum_is_zero():
    assert(0.0, calculate_average_velocity(-10, 10))


if __name__ == '__main__':
    pytest.main()