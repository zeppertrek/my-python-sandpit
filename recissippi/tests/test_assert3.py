# content of test_assert_3.py
# return_the_day ( daynum )
from utils import assortment
import pytest 
def test_function():
    assert assortment.return_the_day (1) == "tuesday"
	

def test_function2():
    assert assortment.return_the_day (2) == "tuesday"
	
def test_function3():
    assert assortment.return_the_day (2) == "tuesday"

@pytest.mark.parametrize("test_input,expected", [
    (0, "monday"),
    (1, "tuesday"),
    (2, "wednesday"),
])
def test_function44(test_input, expected):
    assert assortment.return_the_day (test_input) == expected

@pytest.mark.skip(reason="This test is being skipped because there some issues with the logic")
def test_functionskip2():
    assert assortment.return_the_day (2) in ( "tuesday", "wednesday")
