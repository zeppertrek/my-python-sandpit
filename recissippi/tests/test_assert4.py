# content of test_assert_3.py
# return_the_day ( daynum )
#
# pytest -q -s --day_of_the_week=1  --expected_value="wednesday"  tests\test_assert4.py


from utils import assortment
import pytest 


def test_func_args_from_cmd_line(day_of_the_week, expected_value):
    assert assortment.return_the_day (day_of_the_week) == expected_value

